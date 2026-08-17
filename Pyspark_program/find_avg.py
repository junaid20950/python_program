"""
create dataframe in PySpark
find avg. stock value on daily basis for each stock
find max avg stock value of each stock"""

Data = [("2023-01-01","AAPL", 150.00),
("2023-01-02","AAPL", 155.00),
("2023-01-01","GOOG", 2500.00),
("2023-01-02","GOOG", 2550.00),
("2023-01-01","MSFT", 300.00),
("2023-01-02","MSFT", 310.00)]

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

Schema = ["date","stock","value"]

spark = SparkSession.builder.appName("stock").getOrCreate()

df = spark.createDataFrame(Data, schema = Schema)

# df1 = df.withColumn("date",to_date(col("date"),'yyyy-MM-dd'))
# df1.printSchema()

# df2 = df1.groupBy("stock","date").agg(avg("value").alias("avg_value"))
# df3 = df2.groupBy("stock").agg(max("avg_value").alias("max_stock_value"))
# df3.show()

df.createOrReplaceTempView("my_table")

result_sql = spark.sql("""WITH CTE AS(SELECT stock, CAST(date AS DATE) AS date,
                          AVG(value) AS avg_stock
                          FROM my_table
                          GROUP BY stock, date)
                          SELECT stock, MAX(avg_stock) AS max_stock
                          FROM CTE
                          GROUP BY stock """)

result_sql.show()