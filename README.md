# 📊 Sales Data Analytics

A comprehensive data analytics project analyzing ~10,000 US sales records to identify patterns, fix data quality issues, and evaluate performance across customer segments and regions.

## 🎯 Project Objectives

- Clean and prepare raw sales data for analysis
- Identify sales patterns and trends
- Evaluate regional and segment performance
- Provide data-driven recommendations for business growth

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Excel** | Initial data exploration & duplicate removal |
| **Tableau Prep** | Data cleaning workflow |
| **Python** | Custom transformation scripts |
| **Power BI** | Interactive dashboard |

## 📁 Project Structure
```
sales-data-analytics/
├── data/
│   └── FinalSalesDataset.xlsx
├── scripts/
│   ├── generatePricePerProduct.py
│   └── handlingBlanks.py
├── tableau/
│   └── SalesDataCleaningFlow.tfl
├── powerbi/
│   └── SalesDataAnalyticsDashboard.pbix
└── docs/
    ├── Principles_Of_Business_Analytics_Report.pdf
    └── Sales_Data_Analysis_Presentation.pptx
```

## 🧹 Data Cleaning Process

### Issues Identified & Resolved

| Issue | Solution |
|-------|----------|
| 3 duplicate records | Removed in Excel |
| "Technologi" typo in Category | Corrected to "Technology" |
| Blank values in Sales & Quantity | Python script to calculate from Price Per Product |
| Incorrect Ship Mode | Calculated field based on date difference |
| Missing Profit values | Manually calculated for specific Product IDs |

### Python Scripts

**generatePricePerProduct.py**
- Calculates unique price for each Product ID
- Formula: `(Sales / Quantity) * 100 / (100 - Discount%)`
- Output merged with original dataset via Left Outer Join

**handlingBlanks.py**
- Handles blank Sales values using Price Per Product
- Fixes decimal values in Quantity
- Removes records with no reference values for calculation

### Ship Mode Correction Logic

| Date Difference | Ship Mode |
|-----------------|-----------|
| 0 days | Same Day |
| 1 day | First Class |
| 2 days | Second Class |
| ≥3 days | Standard Class |

## 📈 Key Insights

### Sales Performance
- **Technology** leads with 48.96% of total sales
- **West region** has the highest sales volume
- Sales peak in **October** ($0.31M) and **December**
- Lower sales in **January** and **February**

### Shipping Analysis
- Average shipping time: 3.7 - 4.2 days
- Most orders use **Standard Class** (3-day delivery)
- Faster shipping correlates with higher sales

### Recommendations
1. Focus marketing efforts on Technology products
2. Expand operations in West region
3. Optimize inventory for Q4 demand peaks
4. Consider promoting faster shipping options

## 📊 Dashboard Preview

The Power BI dashboard includes:
- Sales per Month over Years (2011-2014)
- Monthly Sales Trend
- Total Sales by Region
- Average Shipping Time by Month
- Orders by Shipping Class
- Profit & Sales by Segment
- Sales by Category breakdown

## 👥 Team Members

| Member | Lead Role | Supporting Role |
|--------|-----------|-----------------|
| Aswin Muthusamy | Data Cleaning, Scripting, Dashboard | Proof-reading |
| Ganga Hariharan | Report Writing, Insights | Proof-reading |
| Omkar Krishnapurkar | Report Writing, Meetings | Dashboard |
| Adhish Pillai | Presentation | Insights |
| Yashwanth Duddupuddi | Presentation | - |

## 🎓 Academic Context

This project was completed as part of the **Principles of Business Analytics** course at **Maynooth University School of Business**.

## 📝 License

MIT