"""Define Scikit-Learn objects using YAML"""

import importlib
import pkgutil

import sklearn
import yaml


def _get_all_objects():  # TODO
    """Get all sklearn objects."""
    objs = []
    for _, name, _ in pkgutil.iter_modules(sklearn.__path__):
        if not name.startswith("_"):
            objs.append(name)
    return objs


def get_object(name):
    """Get a sklearn object from its name."""
    module_name = ".".join(name.split(".")[:-1])
    if not module_name.startswith("sklearn"):
        module_name = "sklearn." + module_name
    object_name = name.split(".")[-1]
    module = importlib.import_module(module_name)
    return getattr(module, object_name)


def _dict2py(dic):
    """Create a sklearn instance from dict structure."""
    if isinstance(dic, list):
        for i, item in enumerate(dic):
            dic[i] = _dict2py(item)
        return dic

    if isinstance(dic, dict):
        for key in dic.keys():
            dic[key] = _dict2py(dic[key])
            kwargs = dic[key] if dic[key] is not None else {}
            return get_object(key)(**kwargs)
        return dic

    return dic


def yaml2py(path):
    """Create a YAML string from a python object."""
    with open(path, mode="r", encoding="utf-8") as file:
        return _dict2py(yaml.load(file, Loader=yaml.SafeLoader))
