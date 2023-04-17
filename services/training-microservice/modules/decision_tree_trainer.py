from typing import Any, Dict

import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split

from shared.model.model import Model
from .interfaces import IModelTrainer


class DecisionTreeTrainer(IModelTrainer):
    def train(self, model: Model, df: pd.DataFrame) -> Dict[str, Any]:
        X = df.drop(columns=['id', 'paciente_id', 'risco_cardiovascular'])
        y = df['risco_cardiovascular']

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        }
        return {
            'model': model.model,
            'metrics': metrics
        }
