#!py_env/bin/python3.7

# Libraries
import sys
sys.path.append('path')
from airflow import DAG
from plugins.project_01.random_write import random_write
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

default_args = {
    'owner':'gerardo',
    'retries' : 5,
    'retry_delay':timedelta(minutes=5)
}

with DAG(
    default_args = default_args,
    dag_id = 'python_dag_random_write',
    description = 'random write dag python example',
    start_date = datetime(2023, 3, 15, 4, 30),
    schedule_interval = '*/3 * * * *',
) as dag:
    
    # Python Task N1
    task_1 = PythonOperator(
        task_id = 'random_numpy',
        python_callable = random_write,
        op_kwargs={'path': 'path'}
    )
