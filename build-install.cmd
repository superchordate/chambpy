python -m pip install --user --upgrade setuptools wheel
python setup.py sdist bdist_wheel
pip install dist/chambpy-0.0.1.tar.gz