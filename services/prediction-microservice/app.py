import pandas as pd
from flask import Flask, jsonify, request
from typing import List
from shared.data_preparation.data_preparation import DataPreparation
from shared.data_preparation.interfaces import IDataPreparation
from shared.model.interfaces import IModel
from shared.model.model import Model

app = Flask(__name__)

MODEL_FILE_PATH = 'model.pkl'


@app.route('/predict', methods=['POST'])
def predict() -> List[float]:
    # Prepare data
    data_preparation: IDataPreparation = DataPreparation()
    prepared_data = data_preparation.prepare_data(request.get_json(), False)
    prepared_dataframe = data_preparation.prepare_dataframe(prepared_data)

    # Load model
    model: IModel = Model()
    try:
        model = model.load(MODEL_FILE_PATH)
    except Exception as e:
        return jsonify({'message': f'Error loading model: {str(e)}'}), 500

    if model is None:
        return jsonify({'message': 'Model could not be loaded.'}), 500

    # Predictions results
    try:
        predictions = predict_data(model, prepared_dataframe)
    except Exception as e:
        return jsonify({'message': f'Error predicting data: {str(e)}'}), 500

    return jsonify(predictions.tolist())


def predict_data(model: IModel, prepared_data: pd.DataFrame) -> List[float]:
    return model.predict(prepared_data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
