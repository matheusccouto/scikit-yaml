"""Define Scikit-Learn objects using YAML"""

import importlib
import pkgutil
from types import ModuleType

import sklearn
import yaml


def _get_submodules(module):
    """Get all submodules of a module."""
    if hasattr(module, "__path__"):
        return [name for _, name, ispkg in pkgutil.iter_modules(module.__path__)]
    return []


def _get_all_objects(module):
    """Get all objects from a module."""
    objs = []
    submodules = _get_submodules(module)

    for name in dir(module):
        if not name.startswith("_"):
            obj = getattr(module, name)
            if name in submodules:
                objs += _get_all_objects(obj)
            else:
                objs.append(f"{module.__name__}.{name}")
                
    return objs


def get_object(name):
    """Get a sklearn object from its name."""
    objs = _get_all_objects(sklearn)
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
