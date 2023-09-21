from zenml import pipeline

from clean_data import clean_df
from evaluation import evaluate_model
from ingest_data import ingest_df
from model_train import train_model

@pipeline
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_model(df)
    evaluate_model(df)
