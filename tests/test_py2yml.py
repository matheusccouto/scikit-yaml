"""Test creating YAML files from python objects."""

import os
import shutil

import deepdiff
import pytest
import sklearn.compose
import sklearn.ensemble
import sklearn.linear_model
import sklearn.pipeline
import sklearn.preprocessing
import sklearn.svm
import yaml

import skyaml

THIS_DIR = os.path.dirname(__file__)
DATA_DIR = os.path.join(THIS_DIR, "data")
TEMP_DIR = os.path.join(THIS_DIR, "temp")


def assert_yamls_equals(file1, file2):
    """Compare two YAMLs files"""
    # pylint: disable=invalid-name
    with open(file1, "r", encoding="utf-8") as f1:
        with open(file2, "r", encoding="utf-8") as f2:
            d1 = yaml.load(f1, Loader=yaml.SafeLoader)
            d2 = yaml.load(f2, Loader=yaml.SafeLoader)
            assert len(deepdiff.DeepDiff(d1, d2)) == 0


@pytest.fixture(scope="module", autouse=True)
def setup_and_teardown():
    """Setup and teardown."""
    os.makedirs(TEMP_DIR, exist_ok=True)
    yield
    shutil.rmtree(TEMP_DIR)


def test_linear_model():
    """Test get linear model."""
    out = os.path.join(TEMP_DIR, "linear_model.yml")
    ref = os.path.join(DATA_DIR, "linear_model.yml")
    skyaml.py2yaml(
        sklearn.linear_model.LinearRegression(),
        path=out,
    )
    assert_yamls_equals(out, ref)


def test_gradient_boosting():
    """Test export gradient boosting."""
    out = os.path.join(TEMP_DIR, "gradient_boosting.yml")
    ref = os.path.join(DATA_DIR, "gradient_boosting.yml")
    skyaml.py2yaml(
        sklearn.ensemble.HistGradientBoostingRegressor(
            loss="poisson",
            learning_rate=0.01,
            max_depth=8,
        ),
        path=out,
    )
    assert_yamls_equals(out, ref)


def test_pipeline():
    """Test export pipeline."""
    out = os.path.join(TEMP_DIR, "pipeline.yml")
    ref = os.path.join(DATA_DIR, "pipeline.yml")
    skyaml.py2yaml(
        sklearn.pipeline.Pipeline(
            [
                ["scaler", sklearn.preprocessing.StandardScaler()],
                ["svc", sklearn.svm.SVC()],
            ]
        ),
        path=out,
    )
    assert_yamls_equals(out, ref)


def test_deeper_pipeline():
    """Test export a deeper pipeline."""
    out = os.path.join(TEMP_DIR, "deeper_pipeline.yml")
    ref = os.path.join(DATA_DIR, "deeper_pipeline.yml")
    skyaml.py2yaml(
        sklearn.pipeline.Pipeline(
            [
                (
                    "ColumnTransformer",
                    sklearn.compose.ColumnTransformer(
                        transformers=[
                            "Encoder",
                            sklearn.preprocessing.OneHotEncoder(sparse=False),
                            (0,),
                        ],
                        remainder=sklearn.preprocessing.PowerTransformer(),
                    ),
                ),
                [
                    "Regressor",
                    sklearn.ensemble.HistGradientBoostingRegressor(
                        loss="poisson",
                        random_state=0,
                    ),
                ],
            ]
        ),
        path=out,
    )
    assert_yamls_equals(out, ref)
