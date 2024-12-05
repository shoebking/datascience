from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.model_training import ModelTrainer
from src.datascience import logger


STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_data_model_training()
        model_trainer_config = ModelTrainer(config=model_trainer_config)
        model_trainer_config.train()