import datetime
import logging

logger = logging.getLogger(__name__)

from airflow.sdk import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

import boto3
import psycopg2

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