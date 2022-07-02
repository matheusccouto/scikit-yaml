"""Test get object from string"""

import sklearn.pipeline
import sklearn.linear_model

from skyaml import get_object


def test_pipeline():
    """Test get pipeline."""
    assert get_object("sklearn.pipeline.Pipeline") == sklearn.pipeline.Pipeline


def test_linear_model():
    """Test get pipeline."""
    assert get_object("sklearn.linear_model.Ridge") == sklearn.linear_model.Ridge
