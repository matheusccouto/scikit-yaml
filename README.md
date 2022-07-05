# scikit-yaml
Define Scikit-Learn objects using YAML

[![PyPi Version](https://img.shields.io/pypi/v/scikit-yaml.svg)](https://pypi.python.org/pypi/scikit-yaml/)
[![MIT License](https://img.shields.io/github/license/matheusccouto/scikit-yaml)](https://github.com/matheusccouto/scikit-yaml/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/matheusccouto/scikit-yaml/branch/main/graph/badge.svg?token=jvukfL51k7)](https://app.codecov.io/gh/matheusccouto/scikit-yaml/branch/main)

## Getting Started
### Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Bluff.
```bash
pip install scikit-yaml
```
### Usage
#### Define a Scikit-Learn object from YAML file.
```python
import skyaml
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

obj = Pipeline([("scaler", StandardScaler()), ("svc", sklearn.svm.SVC())])
skyaml.py2yaml(obj, "pipeline.yml",)
```

#### Create a YAML file from a Scikit-Learn from YAML file.
```python
import skyaml

skyaml.yaml2py("pipeline.yml")
```

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Contact

[![Linkedin](https://img.shields.io/badge/-matheusccouto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/matheusccouto/)](https://www.linkedin.com/in/matheusccouto/)
[![Gmail](https://img.shields.io/badge/-matheusccouto@gmail.com-006bed?style=flat-square&logo=Gmail&logoColor=white&link=mailto:matheusccouto@gmail.com)](mailto:matheusccouto@gmail.com)
