#!py_env/bin/python3.7

# Libraries
from airflow import DAG
from datetime import datetime
from datetime import timedelta
from airflow.operators.bash import BashOperator

# Default arguments
default_args = {
    'owner': 'gerardo',
    'retries': 5,
    'retry_delay' : timedelta(minutes=2)
}

# DAG specifications. 
with DAG(
    dag_id = 'first_bash_dag',
    default_args = default_args,
    description = 'first print string dag example',
    start_date = datetime(2023, 3, 14, 23, 42),
    schedule_interval = '*/5 * * * *',
) as dag:
    
    # Task 1.
    first_task = BashOperator(
        task_id = 'first_task',
        bash_command= "echo Hello World!"
    )





