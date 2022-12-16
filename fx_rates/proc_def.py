from pyspark.sql import SparkSession, DataFrame, SparkSession
from pyspark import SparkFiles
from datetime import datetime
import spark_sess
import log


spark = spark_sess.spark_sess()
logs = log.log_initialize()

def load_data(url: str, file_name: str) -> DataFrame:
    logs.info(f"Load_data from {url}")
    spark.sparkContext.addFile(url)
    return spark.read.json("file://" + SparkFiles.get(file_name))


def dataframe_merge(df1: DataFrame, df2: DataFrame) -> DataFrame:
    logs.info(f"Megre dataframes")
    return df1.union(df2)


def generate_filename() -> str:
    logs.info(f"Generate file name")
    now = datetime.now()
    return f"fx_rates_{now.year}_{now.month}_{now.day}_{now.hour}_{now.minute}_{now.second}.csv"
