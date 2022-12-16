# python -m pytest --import-mode=append tests/
import sys
sys.path.insert(0, './fx_rates')

import spark_sess
import proc_def
import process_fx_rates


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
    pass
