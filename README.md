**Deprecated! Please use [scikit-dict](https://github.com/matheusccouto/scikit-dict) instead.**

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
## Usage
### Create a YAML file from a Scikit-Learn from YAML file.
```python
import skyaml
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

obj = Pipeline([("scaler", StandardScaler()), ("svc", sklearn.svm.SVC())])
skyaml.py2yaml(obj, "pipeline.yml",)
```
It will create a file with this content:
```yaml
Pipeline:
  steps:
    - - scaler
      - StandardScaler:
    - - svc
      - SVC:
```

### Define a Scikit-Learn object from YAML file.
Recreate the original pipeline.
```python
import skyaml

skyaml.yaml2py("pipeline.yml")
```

## Why should I use this?
This package aim to make experimentation with scikit-learn pipelines more convenient.

The goal is to decouple the pipeline from the executing code, so the user can focus only on the pipeline itself.

It also make it easier to quickly switching in between pipelines, and log it as artifacts on experiment tracking tools (e.g. MLFlow). It works better alongside CLI applications.

It is true that using an separated python file to define a pipeline may work as way. However, YAML is human-friendly and unambiguous. The user is not left trying to guess if the framework expects an class, or how to define the method that will be called in the experiment.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License.

## Contact

[![Linkedin](https://img.shields.io/badge/-matheusccouto-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/matheusccouto/)](https://www.linkedin.com/in/matheusccouto/)
[![Gmail](https://img.shields.io/badge/-matheusccouto@gmail.com-006bed?style=flat-square&logo=Gmail&logoColor=white&link=mailto:matheusccouto@gmail.com)](mailto:matheusccouto@gmail.com)
