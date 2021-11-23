from utils.csv_handler import CSVHandler
from utils.trainer import Trainer


if __name__ == "__main__":
    csv_handler = CSVHandler('gathered_data/consolidated_data.csv')
    csv_handler.read_with_pandas()
    trainer = Trainer('train-data', csv_handler.pandas_datasource)
    trainer.create_model()
    trainer.persist_model()