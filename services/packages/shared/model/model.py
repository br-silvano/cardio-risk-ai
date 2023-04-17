import pickle
from typing import List
from numpy import ndarray

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

from .interfaces import IModel, IModelSaver
from .no_op_model_saver import NoOpModelSaver

class Model(IModel):
    def __init__(self, model: DecisionTreeClassifier = None, saver: IModelSaver = NoOpModelSaver()):
        self.model = model if model is not None else DecisionTreeClassifier()
        self.saver = saver

    def fit(self, X_train: pd.DataFrame, y_train: pd.Series) -> None:
        self.model.fit(X_train, y_train)

    def predict(self, X_test: pd.DataFrame) -> ndarray:
        return self.model.predict(X_test)

    def save(self, file_path: str) -> None:
        with open(file_path, 'wb') as file:
            pickle.dump(self.model, file)

    def set_model_saver(self, saver: IModelSaver) -> None:
        self.saver = saver

    @classmethod
    def load(cls, file_path: str) -> 'Model':
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        return cls(model=model)
