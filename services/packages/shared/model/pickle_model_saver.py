import pickle
from sklearn.tree import DecisionTreeClassifier

from .interfaces import IModelSaver

class PickleModelSaver(IModelSaver):
    def save(self, model: DecisionTreeClassifier, file_path: str) -> None:
        with open(file_path, 'wb') as file:
            pickle.dump(model, file)