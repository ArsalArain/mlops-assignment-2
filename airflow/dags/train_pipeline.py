from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def run_training():
    subprocess.check_call(["python", "-m", "src.train", "--output-dir", "models"])

with DAG(dag_id='train_pipeline', start_date=datetime(2025,12,1), schedule_interval='@daily', catchup=False) as dag:
    train = PythonOperator(
        task_id='train_model',
        python_callable=run_training
    )
