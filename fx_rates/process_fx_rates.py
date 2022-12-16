from pyspark.sql.functions import explode, col
import proc_def
import log


def process_files():
    url1 = "http://api.nbp.pl/api/exchangerates/tables/a?format=json"
    df1 = proc_def.load_data(url1, "a")

    url2 = "http://api.nbp.pl/api/exchangerates/tables/b?format=json"
    df2 = proc_def.load_data(url2, "b")

    df_merged = proc_def.dataframe_merge(df1, df2)

    output_file_name = proc_def.generate_filename()
    # df_merged.select(df_merged.effectiveDate, df_merged.no, explode(df_merged.rates)).select(col("effectiveDate"), col("no"), col("col.code"), col("col.currency"), col("col.mid")).coalesce(1).write.options(delimiter=';').mode('overwrite').csv(output_file_name)
    df_write = df_merged.select(df_merged.effectiveDate, df_merged.no, explode(df_merged.rates)).select(col("effectiveDate"), col("no"), col("col.code"), col("col.currency"), col("col.mid")).coalesce(1)
    proc_def.write_output(df_write, output_file_name, ";", "overwrite")


process_files()
