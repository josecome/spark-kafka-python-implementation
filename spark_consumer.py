from pyspark.sql import SparkSession
import time

spark = SparkSession \
    .builder \
    .appName("Streaming from Kafka") \
    .config("spark.streaming.stopGracefullyOnShutdown", True) \
    .config('spark.jars.packages', 'org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0') \
    .getOrCreate()

df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:9092") \
        .option("subscribe", "my_favorite_topic") \
        .option("startingOffsets", "earliest") \
        .load()

deserialized_df = df.selectExpr("CAST(value AS STRING)")

query = deserialized_df.writeStream.outputMode("append").format("console").start()

time.sleep(10)

query.stop()

# query.awaitTermination()