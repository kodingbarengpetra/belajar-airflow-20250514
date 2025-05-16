from airflow.dags.dag_helloworld import tambah_tambah


def test_tambah_tambah():
    # Test case 1: Tambah 1 + 2
    assert tambah_tambah(1, 2) == 3

    # Test case 2: Tambah 0 + 0
    assert tambah_tambah(0, 0) == 0

    # Test case 3: Tambah -1 + 1
    assert tambah_tambah(-1, 1) == 0

