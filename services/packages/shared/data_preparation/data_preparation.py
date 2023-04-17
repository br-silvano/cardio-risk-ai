import pandas as pd

from .interfaces import IDataPreparation
from .prepare_data import prepare_data
from .prepare_dataframe import prepare_dataframe


class DataPreparation(IDataPreparation):
    def prepare_data(self, data, hasLabels: bool):
        return prepare_data(data, hasLabels)

    def prepare_dataframe(self, data) -> pd.DataFrame:
        return prepare_dataframe(data)
