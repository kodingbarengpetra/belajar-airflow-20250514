import logging
import datetime
# pylint: disable=import-error,no-name-in-module
from airflow.models.dag import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

logger = logging.getLogger(__name__)

# pylint: disable=unexpected-keyword-arg
with DAG(
    dag_id="dag_helloworld",
    start_date=datetime.datetime(2021, 1, 1),
    schedule=None,
    catchup=False,
):
    logger.info("This is a log message")
    EmptyOperator(task_id="task")


def list_file_from_bucket():
    pass

def tambah_tambah(a, b):
    return a + b
