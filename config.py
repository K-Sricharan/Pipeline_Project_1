from zenml.steps import BaseParameters

class ModelNameConfig(BaseParameters):
    """Model_configs"""
    model_name: str = "LinearRegression"
               