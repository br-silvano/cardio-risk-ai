from abc import ABC, abstractmethod
from numpy import ndarray

import pandas as pd
from sklearn.tree import DecisionTreeClassifier


class IModel(ABC):
    @abstractmethod
    def fit(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        pass

    @abstractmethod
    def predict(self, X_test: pd.DataFrame) -> ndarray:
        pass

    @abstractmethod
    def save(self, file_path: str) -> None:
        pass


class IModelSaver:
    def save(self, model: DecisionTreeClassifier, file_path: str) -> None:
        pass
