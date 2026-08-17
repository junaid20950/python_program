from databricks.connect import DatabricksSession

print("Connecting to Databricks...")

# Replace 'YOUR_CLUSTER_ID_HERE' with the ID you copied from your browser
config = {
    "cluster_id": "7474659456999788"
}

# Pass the configuration into the builder
spark = DatabricksSession.builder.config(conf=config).getOrCreate()

print("Connection successful! Running test query...")
df = spark.sql("SELECT 'Hello from Databricks!' AS status")
df.show()
