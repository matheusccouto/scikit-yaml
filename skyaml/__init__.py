"""Define Scikit-Learn objects using YAML"""

import json
import inspect
import pkgutil
import re

import sklearn
import yaml


def _get_submodules(module):
    """Get all submodules of a module."""
    if hasattr(module, "__path__"):
        return [name for _, name, _ in pkgutil.iter_modules(module.__path__)]
    return []


def _get_all_objects(module):
    """Get all objects from a module."""
    objs = {}
    submodules = _get_submodules(module)

    for name in dir(module):
        if not name.startswith("_"):
            obj = getattr(module, name)
            if name in submodules:
                objs.update(_get_all_objects(obj))
            elif inspect.isclass(obj) or inspect.isfunction(obj):
                objs[name] = obj

    return objs


def _dict2py(dic):
    """Create a python instance from dict structure."""
    objs = _get_all_objects(sklearn)

    if isinstance(dic, list):
        for i, item in enumerate(dic):
            dic[i] = _dict2py(item)
        return dic

    if isinstance(dic, dict):
        for key in dic.keys():
            dic[key] = _dict2py(dic[key])
            kwargs = dic[key] if dic[key] is not None else {}
            try:
                return objs[key](**kwargs)
            except KeyError:
                pass
        return dic

    return dic


def _py2dict(py):
    """Create a dict from a python object."""
    txt = str(py)

    # Transform tuples in lists.
    txt = re.sub(r"(?<=[\[\s])\(", "[", txt)
    txt = re.sub(r"(?<=\))\)(?=[\]\,])", "]", txt)

    # Transform kwargs in dicts.
    txt = re.sub(r"(?<=[\w\d])\(", ": {", txt)
    txt = re.sub(r"\)", "}", txt)

    # Envolve it in brackets:
    txt = "{" + txt + "}"
    txt = re.sub(r"(?<!\{)\b\w+\:\s*\{.*?\}", r"{\g<0>}", txt)

    # Add collons.
    txt = re.sub(r"=", ":", txt)

    # Add quotes.
    txt = re.sub(r"[\w]+(?=\:)", r"'\g<0>'", txt)

    # Transform single quotes into double
    txt = txt.replace("'", '"')

    # Replace some keywords:
    txt = txt.replace("True", "true")
    txt = txt.replace("False", "false")
    txt = txt.replace("None", "null")
    txt = txt.replace("{}", "null")

    return json.loads(txt)


def yaml2py(path):
    """Create a python object from a YAML file."""
    with open(path, mode="r", encoding="utf-8") as file:
        return _dict2py(yaml.load(file, Loader=yaml.SafeLoader))


def py2yaml(obj, path):
    """Create a YAML file from a python object."""
    with open(path, mode="w", encoding="utf-8") as file:
        yaml.dump(_py2dict(obj), file, Dumper=yaml.SafeDumper)
