from flask import Flask, request, jsonify
from shared.data_preparation.data_preparation import DataPreparation
from shared.data_preparation.interfaces import IDataPreparation
from shared.model.interfaces import IModel, IModelSaver
from shared.model.model import Model
from shared.model.pickle_model_saver import PickleModelSaver
from modules.decision_tree_trainer import DecisionTreeTrainer
from modules.interfaces import IModelTrainer

app = Flask(__name__)

MODEL_FILE_PATH = 'model.pkl'
MINIMUM_QUALITY = {'accuracy': 0.8, 'precision': 0.8, 'recall': 0.8, 'f1': 0.8}


@app.route('/training', methods=['POST'])
def train_model() -> jsonify:
    # Prepare data
    data_preparation: IDataPreparation = DataPreparation()
    prepared_data = data_preparation.prepare_data(request.get_json(), True)
    prepared_dataframe = data_preparation.prepare_dataframe(prepared_data)

    # Train model
    model: IModel = Model()

    model_trainer: IModelTrainer = DecisionTreeTrainer()
    model_training = model_trainer.train(model, prepared_dataframe)
    training_result_model = model_training.get('model')
    training_result_metrics = model_training.get('metrics')

    # Evaluate model quality
    quality_check = all(
        training_result_metrics[k] >= MINIMUM_QUALITY[k] for k in MINIMUM_QUALITY)
    if not quality_check:
        return jsonify({
            'messages': "The model's quality is insufficient. It will be necessary to redo it.",
            **training_result_metrics
        }), 400

    # Save model
    try:
        model_saver: IModelSaver = PickleModelSaver()
        model: IModel = Model(model=training_result_model, saver=model_saver)
        model.save(MODEL_FILE_PATH)
    except Exception as e:
        return jsonify({'messages': f"Error saving model: {str(e)}"}), 500

    return jsonify({
        'messages': "The model meets the minimum quality requirements.",
        **training_result_metrics
    }), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
