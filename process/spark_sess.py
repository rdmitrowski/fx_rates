from pyspark.sql import SparkSession


def spark_sess() -> SparkSession:
    return SparkSession.builder.appName("Process fx rates").getOrCreate()
