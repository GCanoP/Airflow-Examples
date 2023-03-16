#!py_env/bin/python3.7

# Libraries
import sys
sys.path.append('/home/gerardo/Escritorio/airflow')
from airflow import DAG
from plugins.random_selection import random_numpy
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'gerardo',
    'retries' : 5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    default_args = default_args,
    dag_id = 'first_python_dag',
    description = 'first dag operation example',
    start_date = datetime(2023, 3, 14, 23, 50),
    schedule_interval = '*/5 * * * *',
) as dag:
    
    # Python Task N1
    task_1 = PythonOperator(
        task_id = 'random_numpy',
        python_callable = random_numpy
    )
