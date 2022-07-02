"""Test creating python objects from YAML files."""

import os

import sklearn.ensemble
import sklearn.linear_model

import skyaml

THIS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(THIS_DIR, "data")

# pylint: disable=invalid-name


def test_linear_model():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "linear_model.yaml"))
    py = sklearn.linear_model.LinearRegression()
    assert type(yml) is type(py)


def test_gradient_boosting():
    """Test get linear model."""
    yml = skyaml.yaml2py(os.path.join(DATA_DIR, "gradient_boosting.yaml"))
    py = sklearn.ensemble.HistGradientBoostingRegressor(
        loss="poisson",
        learning_rate=0.01,
        max_depth=None,
    )
    assert str(yml) is str(py)
