pytest -vs tests/test_login.py
pytest -vs -m smoke tests/test_login.py
pytest -vs --html=report.html tests/test_login.py
