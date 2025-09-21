# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Load the dataset from Lakehouse
df = pd.read_csv("sample_customer_data.csv")  # Replace with your Lakehouse path if needed

# Display basic info
print("Initial Data Overview:")
print(df.head())

# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=["Gender", "Region"], drop_first=True)

# Select features for clustering
features = ["Age", "Annual Income (k$)", "Spending Score (1-100)"] + \
           [col for col in df_encoded.columns if col.startswith("Gender_") or col.startswith("Region_")]
X = df_encoded[features]

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
df_encoded['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize clusters
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_encoded, x="Annual Income (k$)", y="Spending Score (1-100)", hue="Cluster", palette="Set2")
plt.title("Customer Segments by Income and Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Save clustered data to CSV for Power BI
df_encoded.to_csv("segmented_customers.csv", index=False)
