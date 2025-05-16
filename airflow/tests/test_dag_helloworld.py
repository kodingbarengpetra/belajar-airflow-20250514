import pytest
from airflow.models import DagBag
from airflow.models.dag import DAG
from airflow.providers.standard.operators.empty import EmptyOperator

def test_dag_helloworld_loaded():
    """Test that the DAG can be loaded properly"""
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    assert dag_bag.import_errors == {}
    assert 'dag_helloworld' in dag_bag.dags

def test_dag_helloworld_structure():
    """Test the structure of the DAG"""
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    dag = dag_bag.dags['dag_helloworld']
    
    # Test DAG configuration
    assert dag.dag_id == 'dag_helloworld'
    assert dag.schedule is None
    assert not dag.catchup
    
    # Test tasks
    tasks = dag.tasks
    assert len(tasks) == 1
    
    # Test task properties
    task = tasks[0]
    assert isinstance(task, EmptyOperator)
    assert task.task_id == 'task'

def test_dag_helloworld_dependencies():
    """Test that the DAG has no dependencies between tasks"""
    dag_bag = DagBag(dag_folder='dags', include_examples=False)
    dag = dag_bag.dags['dag_helloworld']
    
    # Since there's only one task, there should be no dependencies
    assert len(dag.edge_list) == 0 