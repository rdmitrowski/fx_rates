# python -m pytest --import-mode=append tests/
from pyspark.sql import DataFrame
from chispa import assert_df_equality
from pyspark.sql.types import StructType, StructField, FloatType, StringType, IntegerType

import sys
sys.path.insert(0, './fx_rates')

import spark_sess
import proc_def

def test_spark_sess():
    sess = spark_sess.spark_sess
    pass


def test_load_data():
    url1 = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    df1 = proc_def.load_data(url1, "a")
    pass


def test_generate_filename():
    file_name = proc_def.generate_filename()
    assert file_name.startswith("fx_rates") and file_name.endswith(".csv")

def test_dataframe_merge():
    spark = spark_sess.spark_sess()
    df1 = spark.createDataFrame(
        [("243/A/NBP/2022", "2022-12-16", "bat (Tajlandia)", "THB", 0.1265)],
        StructType([StructField("no", StringType(), True),
        StructField("effectiveDate", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("code", StringType(), True),
        StructField("mid", FloatType(), True)])
        )
    df2 = spark.createDataFrame(
        [("243/A/NBP/2022", "2022-12-16", "dolar amerykański", "USD", 4.4227)],
        #["no", "effectiveDate", "currency", "code", "mid"]
        StructType([StructField("no", StringType(), True),
        StructField("effectiveDate", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("code", StringType(), True),
        StructField("mid", FloatType(), True)])
        )
    df_expected =  spark.createDataFrame([
        ("243/A/NBP/2022", "2022-12-16", "bat (Tajlandia)", "THB", 0.1265),
        ("243/A/NBP/2022", "2022-12-16", "dolar amerykański", "USD", 4.4227)],     
        #["no", "effectiveDate", "currency", "code", "mid"]
        StructType([StructField("no", StringType(), True),
        StructField("effectiveDate", StringType(), True),
        StructField("currency", StringType(), True),
        StructField("code", StringType(), True),
        StructField("mid", FloatType(), True)])
        )
    df_result= proc_def.dataframe_merge(df1, df2)
    assert_df_equality(df_result, df_expected)
