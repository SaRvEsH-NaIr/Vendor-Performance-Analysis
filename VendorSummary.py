# Importing the libraries
# -------------------------------------------------------------------------------------------------------------

import pandas as pd
import sqlite3
import logging
from ingestion import ingest_data

# Creating Logging Service
# -------------------------------------------------------------------------------------------------------------

logging.basicConfig(
    filename = "logs/.log",
    level = logging.DEBUG,
    format ="%(asctime)s - %(levelname)s - %(message)s",
    filemode = "a"
)

# Creating a Function to create vendor summary table by combining parts of different tables
# -------------------------------------------------------------------------------------------------------------

def create_vendor_summary(conn):
    vendor_sales_summary = pd.read_sql('''
        WITH 

        FreightSummary AS (
            SELECT 
                VendorNumber, 
                SUM(Freight) AS FreightCost 
            FROM Vendor_Invoice 
            GROUP BY VendorNumber
        ),

        PurchaseSummary AS (
            SELECT
                p.VendorNumber, 
                p.VendorName, 
                p.Brand, 
                p.Description,
                p.PurchasePrice, 
                pp.Volume,
                pp.Price as ActualPrice,
                SUM(p.Quantity) as TotalQuantity,
                SUM(p.Dollars) as TotalPurchaseDollars
            FROM Purchases p
            JOIN Purchase_prices pp ON p.Brand = pp.Brand
            WHERE p.PurchasePrice > 0
            GROUP BY p.VendorNumber, p.VendorName, p.Brand, p.Description, p.PurchasePrice, pp.Price, pp.Volume
        ),

        SalesSummary AS (
            SELECT
                VendorNo,
                Brand,
                SUM(SalesDollars) AS TotalSalesDollars,
                SUM(SalesPrice) AS TotalSalesPrice,
                SUM(SalesQuantity) AS TotalSalesQuantity,
                SUM(ExciseTax) AS TotalExciseTax
            FROM Sales
            GROUP BY VendorNo, Brand
        )

        SELECT 
            ps.VendorNumber,
            ps.VendorName,
            ps.Brand,
            ps.Description,
            ps.PurchasePrice,
            ps.ActualPrice,
            ps.Volume,
            ps.TotalQuantity,
            ps.TotalPurchaseDollars,
            ss.TotalSalesQuantity,
            ss.TotalSalesDollars,
            ss.TotalSalesPrice,
            ss.TotalExciseTax,
            fs.FreightCost
        FROM PurchaseSummary as ps
        JOIN SalesSummary as ss
            ON ps.VendorNumber = ss.VendorNo
            AND ps.Brand = ss.Brand
        LEFT JOIN FreightSummary as fs
            ON ps.VendorNumber = fs.VendorNumber
        ORDER BY ps.TotalPurchaseDollars DESC
            ''', conn)
    
    return vendor_sales_summary

# Creating a Function to clean the dataset and create new features
# -------------------------------------------------------------------------------------------------------------

def clean_data(df):
    # Changing data type to float
    df['Volume'] = df['Volume'].astype('float64')
    
    # Removing extra spaces
    df['VendorName'] = df['VendorName'].str.strip()
    
    # Creating new feature columns
    df['GrossProfit'] = df['TotalSalesDollars'] - df['TotalPurchaseDollars']
    df['ProfitMargin'] = df['GrossProfit'] / df['TotalSalesDollars'] * 100
    df['StockTurnover'] = df['TotalSalesQuantity'] / df['TotalQuantity']
    df['SalestoPurchaseRatio'] = df['TotalSalesDollars'] / df['TotalPurchaseDollars']
    
    reutn df
    
# Calling all functions
# -------------------------------------------------------------------------------------------------------------

if __name__ = "__main__":
    logging.info('Creating Database Connection')
    conn = sqlite3.connect('inventory.db')
    
    logging.info('Creating Vendor Summary Table')
    summary_df = create_vendor_summary(conn)
    
    logging.info('Cleaning the Data')
    clean_df = clean_data(summary_df)
    logging.info(f'Cleaned Dataset: {clean_df.head}')
    
    logging.info('Ingesting Data into the database')
    ingest_db(clean_df, 'vendor_sales_summary', conn)
    logging.info('Process Completed')