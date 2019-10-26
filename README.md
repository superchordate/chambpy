# chambpy

My commonly-used code. I'm an R developer primarily, so I typically
use function names from R so I can remember them easily.

*Package init format sourced from https://github.com/pypa/sampleproject.*

# Installation

* Download and unzip these files.
* Run the code in build-install.cmd:

```
    python -m pip install --user --upgrade setuptools wheel
    python setup.py sdist bdist_wheel
    pip install dist/chambpy-0.0.1.tar.gz
```

# Usage

Import in python and use the functions. For example:

```python
from chambpy.saveload import save
X = 'X'
y = 'y'
save( 'sample.pkl', X, y )
```

# Functions

**saveload** module:

|Function|Description|
|---|---|
|save|Saves multiple objects in a pickle file (.pkl). First arg must be the path. Other arguments will be saved as a named dictionary.|
|load|Loads objects saved with save() into the global environment.|