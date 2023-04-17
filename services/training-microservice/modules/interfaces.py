from abc import ABC, abstractmethod
from typing import Any, Dict
import pandas as pd


class IModelTrainer(ABC):
    @abstractmethod
    def train(self, df: pd.DataFrame) -> Dict[str, Any]:
        pass
