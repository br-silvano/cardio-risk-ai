from typing import List
import pandas as pd
from abc import ABC, abstractmethod


class IDataPreparation(ABC):
    @abstractmethod
    def prepare_data(self, data, hasLabels: bool):
        pass

    @abstractmethod
    def prepare_dataframe(self, data) -> pd.DataFrame:
        pass
