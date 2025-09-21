
# Citizen Data Science in Action: Fabric Notebooks to Power BI in Minutes

## 📘 Project Overview
This project demonstrates how Microsoft Fabric empowers business users to perform data science tasks—such as customer segmentation—without writing complex code. Using Fabric Notebooks and Power BI, users can ingest data, build machine learning models, and visualize insights in minutes.

## 🎯 Objectives
- Enable citizen data scientists to build ML workflows with low-code tools.
- Perform customer segmentation using K-Means clustering.
- Visualize insights in Power BI using Direct Lake connectivity.

## 📊 Dataset Description
The dataset used is a synthetic customer dataset containing:
- `CustomerID`: Unique identifier
- `Age`: Customer age
- `Gender`: Male/Female
- `Annual Income (k$)`: Income in thousands
- `Spending Score (1–100)`: Synthetic score representing spending behavior
- `Region`: Geographic region (North, South, East, West)

## 🛠️ Tools Used
- **Microsoft Fabric**
  - Lakehouse
  - Python Notebooks
- **Power BI**
  - Direct Lake connectivity
- **Python Libraries**
  - pandas, matplotlib, seaborn, scikit-learn

## 🚀 Implementation Steps
1. Upload `sample_customer_data.csv` to Lakehouse.
2. Open a Python Notebook and run the clustering code:
   - Encode categorical variables
   - Scale numerical features
   - Apply K-Means clustering
   - Save results to `segmented_customers.csv`
3. Visualize clusters using matplotlib and seaborn.

## 📈 Power BI Dashboard Features
- Clustered bar chart: Number of customers per segment
- Scatter plot: Annual Income vs Spending Score by cluster
- Slicers: Region and Gender filters
- Cards: Average income and spending score per cluster
- Table: Customer details with cluster assignment

## 🔗 Connecting Power BI to Fabric (Direct Lake Mode)
1. Open Power BI Desktop or Power BI in Fabric.
2. Select **Lakehouse (Microsoft Fabric)** as the data source.
3. Choose your workspace and Lakehouse.
4. Load the `segmented_customers` table.
5. Build interactive visuals using real-time data.

---

© 2025 Microsoft Fabric Project. All rights reserved.
