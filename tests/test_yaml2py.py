"""Test creating python objects from YAML files."""

import os

import sklearn.compose
import sklearn.ensemble
import sklearn.linear_model
import sklearn.pipeline
import sklearn.preprocessing
import sklearn.svm

import skyaml

THIS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(THIS_DIR, "data")

# pylint: disable=invalid-name


def test_linear_model():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "linear_model.yml"))
    py = sklearn.linear_model.LinearRegression()
    assert type(yml) is type(py)


def test_gradient_boosting():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "gradient_boosting.yml"))
    py = sklearn.ensemble.HistGradientBoostingRegressor(
        loss="poisson",
        learning_rate=0.01,
        max_depth=8,
    )
    assert str(yml) == str(py)


def test_pipeline():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "pipeline.yml"))
    py = sklearn.pipeline.Pipeline(
        [
            ["scaler", sklearn.preprocessing.StandardScaler()],
            ["svc", sklearn.svm.SVC()],
        ]
    )
    assert str(yml) == str(py)


def test_deeper_pipeline():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "deeper_pipeline.yml"))
    py = sklearn.pipeline.Pipeline(
        [
            [
                "ColumnTransformer",
                sklearn.compose.ColumnTransformer(
                    transformers=[
                        "Encoder",
                        sklearn.preprocessing.OneHotEncoder(sparse=False),
                        [0],
                    ],
                    remainder=sklearn.preprocessing.PowerTransformer(),
                ),
            ],
            [
                "Regressor",
                sklearn.ensemble.HistGradientBoostingRegressor(
                    loss="poisson",
                    random_state=0,
                ),
            ],
        ]
    )
    assert str(yml) == str(py)
