# Vendor Performance Analytics

## Project Overview

**Vendor Performance Analytics** is a comprehensive data-driven solution designed to optimize profitability and operational efficiency in the retail and wholesale industry. This project leverages data engineering, exploratory data analysis, and statistical hypothesis testing to provide actionable insights into inventory management, vendor performance, and pricing strategies.

---

## Business Problem

Effective inventory and sales management are critical for optimizing profitability in the retail and wholesale industry. Companies face significant challenges including inefficient pricing, poor inventory turnover, and vendor dependency that directly impact their bottom line. Without data-driven insights, organizations risk incurring substantial losses and missing opportunities for cost optimization.

### Key Business Objectives

This analysis addresses the following critical business questions:

- **Identify Underperforming Brands**: Which brands require promotional or pricing adjustments to improve sales performance and market competitiveness?

- **Determine Top Vendors**: Which vendors are the primary contributors to sales and gross profit, and how dependent is the organization on these key suppliers?

- **Analyze Bulk Purchasing Impact**: What is the relationship between bulk purchasing volumes and unit costs, and how can we optimize procurement strategies?

- **Assess Inventory Turnover**: How efficiently is inventory being managed, and where can we reduce holding costs while improving operational efficiency?

- **Investigate Profitability Variance**: What are the significant differences in profitability metrics between high-performing and low-performing vendors, and what drives these variances?

---

## Data Pipeline Architecture

### 1. Data Ingestion & Preprocessing

**Technology Stack**: Python, Pandas

The project implements a robust data pipeline script that:

- **Ingests raw CSV files** from multiple sources
- **Performs data cleaning** including handling missing values, outliers, and inconsistent formats
- **Validates data quality** to ensure reliability for downstream analysis
- **Transforms raw data** into analysis-ready formats

**Key Processing Steps**:
- Data type validation and conversion
- Duplicate record identification and removal
- Missing value treatment using domain-specific logic
- Outlier detection and handling
- Feature normalization and standardization

### 2. Data Storage & Query

**Technology Stack**: SQLite, SQL

Data is stored in a relational database enabling:

- Efficient data retrieval through optimized SQL queries
- Consolidation of multiple data sources into a unified analytical schema
- Support for complex joins across vendor, brand, and sales dimensions
- Scalable storage for large-scale retail datasets

**Database Schema Highlights**:
- Vendor master table with performance metrics
- Brand portfolio with sales and profitability data
- Transaction-level inventory and sales records
- Aggregated metrics for quick analysis

### 3. Exploratory Data Analysis (EDA)

**Technology Stack**: Python (Pandas, NumPy, Matplotlib, Seaborn)

Comprehensive EDA performed to:

- Identify patterns and trends in vendor performance
- Visualize sales and profitability distributions
- Analyze correlation between variables
- Detect data anomalies and validate data quality
- Establish baseline metrics for hypothesis testing

### 4. Statistical Analysis & Hypothesis Testing

**Methodology**: Independent Samples T-Test

A rigorous hypothesis testing framework was employed to validate business assumptions and draw statistically significant conclusions.

---

## Analysis Findings

### Finding 1: Brands Requiring Promotional or Pricing Adjustments

**Business Question**: Which brands exhibit lower sales performance but higher profit margins?

**Visualization**: <img width="850" height="545" alt="image" src="https://github.com/user-attachments/assets/8f91cff5-541a-413e-a087-7ae4c0e67fd8" />

**Key Insights**:
- Identified a targeted segment of brands with paradoxical performance characteristics—high profit margins despite lower sales volumes
- These brands represent optimization opportunities where strategic pricing or promotional initiatives could unlock significant value
- The high profit margins suggest healthy unit economics; the challenge is driving market penetration and sales volume
- Brands in this category show potential for increased profitability through increased market share gains

**Recommendations**:
- Implement targeted promotional campaigns to boost sales visibility
- Consider strategic pricing reductions to increase volume and market share
- Invest in brand awareness and customer engagement initiatives
- Evaluate product positioning and marketing mix strategies

---

### Finding 2: Vendor Contribution Analysis

**Business Question**: Which vendors are the primary drivers of purchase volume and profitability?

**Visualization**: <img width="911" height="3090" alt="image" src="https://github.com/user-attachments/assets/6f675ad5-e016-4d89-851e-24d9887f618a" />

**Key Insights**:
- **Pareto Principle Validation**: The analysis confirms the 80/20 rule—approximately 66% of total purchases are concentrated in the top 10 vendors
- **Top Vendor**: DIAGEO NORTH AMERICA INC leads with 16% of total purchase dollars
- **Vendor Concentration**: The top 5 vendors account for a significant portion (>40%) of procurement
- **Long Tail Effect**: The remaining vendors (34% combined contribution) represent fragmentation in the supply chain

**Vendor Rankings** (Top 10 by Purchase Contribution):
1. DIAGEO NORTH AMERICA INC - 16.0%
2. MARTIGNETTI COMPANIES - 8.0%
3. PERNOD RICARD USA - 8.0%
4. JIM BEAM BRANDS COMPANY - 8.0%
5. BACARDI USA INC - 6.0%
6. CONSTELLATION BRANDS INC - 5.0%
7. BROWN-FORMAN CORP - 4.0%
8. E & J GALLO WINERY - 4.0%
9. ULTRA BEVERAGE COMPANY LLP - 4.0%
10. M S WALKER INC - 3.0%

**Recommendations**:
- Strengthen relationships with top 5 vendors through preferred partner agreements
- Negotiate volume-based discounts with key suppliers
- Develop contingency plans to mitigate supply chain risk from vendor concentration
- Consider strategic diversification to reduce dependency on single vendors
- Monitor vendor performance metrics continuously

---

### Finding 3: Sales Performance by Vendor and Brand

**Business Question**: What are the top performing vendors and brands in terms of sales revenue?

**Visualization**: <img width="1491" height="490" alt="image" src="https://github.com/user-attachments/assets/5fd9dc17-16d9-4df0-87de-5889596cf409" />

**Key Insights**:
- **Top Vendor by Sales**: DIAGEO NORTH AMERICA INC leads with approximately $69M in sales
- **Top Brand by Sales**: Jack Daniels No 7 Black achieves approximately $96M in sales
- **Brand-Vendor Relationship**: Leading brands are distributed by top-performing vendors
- **Revenue Concentration**: A significant portion of total revenue is generated by top performers, indicating market maturity

**Top Performance Metrics**:
- Top vendor average sales: ~$69M
- Top brand average sales: ~$96M
- Sales distribution shows 80/20 concentration pattern

**Recommendations**:
- Allocate marketing resources to top-performing brands for further growth
- Analyze product mix of top vendors for cross-selling opportunities
- Develop vendor exclusivity agreements for premium brands
- Study top performer characteristics for replication across portfolio

---

### Finding 4: Correlation Analysis

**Business Question**: What relationships exist between pricing, volume, profitability, and inventory metrics?

**Visualization**: <img width="1044" height="816" alt="image" src="https://github.com/user-attachments/assets/d55dfad4-bd1a-4dea-b2c4-50f3942629c3" />

**Key Insights**:
- **Strong Price Correlation**: Purchase Price and Actual Price show strong positive correlation (0.99), indicating consistent pricing strategies
- **Revenue Drivers**: Total Sales Dollars, Total Purchase Dollars, and Total Quantity show strong correlations (0.82-0.88), confirming volume drives revenue
- **Profitability Relationships**: Gross Profit shows strong correlation with sales metrics (0.69-0.82), validating profit dependency on volume
- **Stock Turnover**: Exhibits high correlation with Sales-to-Purchase ratio (1.00), indicating efficient inventory conversion
- **Weak Brand Relationships**: Brand variable shows low correlation with financial metrics, suggesting brand identity is less deterministic than operational factors

**Correlation Highlights**:
- Strong positive correlations (0.82-0.99): Revenue and quantity metrics
- Moderate correlations (0.55-0.70): Profitability and operational metrics
- Weak correlations (-0.21-0.14): Brand and vendor identifiers with numeric outcomes

**Recommendations**:
- Focus optimization efforts on quantity and volume drivers
- Volume strategies are more impactful than pricing adjustments alone
- Inventory turnover metrics are reliable KPIs for operational efficiency
- Consider non-financial factors (brand quality, reputation) for brand differentiation

---

### Finding 5: Hypothesis Testing - Vendor Profitability Variance

**Business Question**: Is there a statistically significant difference in profit margins between top-performing and low-performing vendors?

**Statistical Test**: Independent Samples T-Test

**Hypothesis Framework**:
- **Null Hypothesis (H₀)**: There is no significant difference in mean profit margins between top-performing and low-performing vendors
- **Alternative Hypothesis (H₁)**: Mean profit margins of top-performing and low-performing vendors are significantly different
- **Significance Level**: α = 0.05

**Test Methodology**:
```
Vendors classified by total sales quartiles:
- Top performers: Vendors in 75th percentile and above
- Low performers: Vendors in 25th percentile and below

T-test conducted using:
- Independent samples (unequal variance assumption)
- Two-tailed significance test
```

## Conclusion

This vendor performance analytics project provides a data-driven foundation for strategic decision-making in retail and wholesale operations. Through rigorous data analysis, correlation studies, and statistical hypothesis testing, we have validated key business assumptions and identified actionable optimization opportunities.

The insights gained from this analysis—particularly regarding vendor concentration, brand performance, and profitability variance—can drive significant value through improved vendor negotiations, targeted marketing initiatives, and optimized inventory management.
