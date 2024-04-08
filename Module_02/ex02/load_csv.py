import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    This fonction load a .csv, print the dimensions and print it.
    """
    try:
        if not os.path.exists(path):
            raise AssertionError("File doesn't exists.")
        if not path.lower().endswith('.csv'):
            raise AssertionError("File haven't the good format.")
        data = pd.read_csv(path)
        print("Loading dataset of dimensions : ", data.shape)
        return data
    except AssertionError as error:
        print(AssertionError.__name__ + ":", error)
        return None
