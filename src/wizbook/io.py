"""
Input & Output, for;
- local filesystem
...
"""

import io
import os
import json
import csv
import pickle
import functools
from typing import List, Dict, Any, Callable


# Safety first! ensure funcs are called correctly, break if not
def ensure_readargs(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(kwargs, "filepath"):
            filepath = kwargs["filepath"]
        else:
            filepath = args[0]
        assert filepath is not None, f"the 'filepath' must be specified! recieved: '{filepath}'"
        # that file exist wiz?
        if os.path.exists(filepath):
            return func(*args, **kwargs)
        else:
            raise FileNotFoundError(
                f"File: '{filepath}' does not exist. One cannot read a nonexistent file."
            )
    return wrapper


def ensure_writeargs(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if "data" not in kwargs and len(args) < 2:
            raise ValueError("Data to write must be specified!")
        if "filepath" not in kwargs and len(args) < 1:
            raise ValueError("The 'filepath' must be specified!")
        return func(*args, **kwargs)
    return wrapper


# JSON et al
@ensure_readargs
def read_json_data(filepath: str) -> Dict[Any, Any]:
    if os.path.exists(filepath):
        file = io.open(filepath, mode="r", encoding="utf-8")
        data = json.load(file)
        file.close()
        return data  # dictionary for parsing/uploading
    else:
        print(
            f"File: '{filepath}' doesn't seem to exist, returning empty dictionary")
        # base for creating any new data dicts (writer util can work with one entry)
        return {}


@ensure_writeargs
def write_json_data(filepath: str, data):
    with io.open(filepath, mode="w", encoding="utf-8") as f:
        file = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(file)
        f.close()


@ensure_readargs
def read_jsonl_data(filepath: str) -> List[Dict]:
    if os.path.exists(filepath):
        data = []
        file = io.open(filepath, mode="r", encoding="utf-8")
        for line in file:
            data.append(json.loads(line))
        file.close()
        return data  # list of dicts per line in JSON
    else:
        print(f"File: '{filepath}' doesn't seem to exist")
        return {}


@ensure_writeargs
def write_jsonl_data(filepath: str, data: List[Dict]):
    with open(filepath, mode="w", encoding="utf-8") as f:
        # Write out all provided lines
        for jeh_son in data:
            # json.dump(jeh_son, f, ensure_ascii=False)
            try:
                f.write(json.dumps(dict(jeh_son), separators=(',', ':')))
            except Exception as E:
                print(jeh_son)
                print("broken?")
                print(E)
            f.write("\n")  # newlines must be verbosely written in JSONL
        f.close()


def convert_jsons_to_jsonl(json_dir: str, jsonl_path: str):
    """ Given a Directory full of JSON Files, Convert it into a single JSONL File, handy for ad-hoc MongoDB Uploads """
    if os.path.exists(json_dir):
        data = []
        for filename in os.listdir(json_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(json_dir, filename)
                data.append(read_json_data(filepath))
        write_jsonl_data(jsonl_path, data)
    return


# Txt & Markdown
@ensure_writeargs
def write_txt_data(filepath: str, data):
    """ Dump a String to a text file, should refactor if ever using """
    with io.open(filepath, mode="w", encoding="utf-8") as f:
        f.write(data)
        f.close()


@ensure_readargs
def read_txt_data(filepath: str, lines: bool = False):
    """ Read in text from filepath as an array of strings """
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines


# Delimted
@ensure_writeargs
def write_delim_data(filepath: str, data: List[List[Any]], delim: str = ','):
    """ Write a list of lists to a delimited text file. """
    with open(filepath, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=delim)
        writer.writerows(data)


@ensure_readargs
def read_delim_data(filepath: str, delim: str = ',') -> List[List[Any]]:
    """ Read data from a delimited text file as a list of lists. """
    with open(filepath, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=delim)
        return list(reader)


# Pickle-mono
@ensure_readargs
def read_pickle_data(filepath: str) -> Any:
    """ grab some pickled data from disk, hopefully safe... """
    if os.path.exists(filepath):
        with open(filepath, mode="rb") as file:
            data = pickle.load(file)
        return data  # unpickled object


@ensure_writeargs
def write_pickle_data(filepath: str, data: Any):
    """ dump some pickled data to disk """
    with open(filepath, mode="wb") as f:
        pickle.dump(data, f)
