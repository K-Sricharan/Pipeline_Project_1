import loggging
from ABC import ABC, abstractmethod

import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

class Evaluation(ABC):
    @abstractmethod
    def calculate_scores(self, y_true: np.ndarray,y_pred: np.ndarray):

        pass

class MSE(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            loggging.info("Calculating MSE")
            mse = mean_squared_error(y_true,y_pred)
            loggging.info("MSE:{}".format(mse))
            return mse
        except Exception as e:
            loggging.error("Error in calculating MSE:{}".format(e))
            raise e
        
class R2(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            loggging.info("Calculating R2 Score")
            r2 = r2_score(y_true,y_pred)
            loggging.info("MSE:{}".format(mse))
            return r2
        except Exception as e:
            loggging.error("Error in calculating r2:{}".format(e))
            raise e
        
class RMSE(Evaluation):
    def calculate_scores(self, y_true: np.ndarray, y_pred: np.ndarray):
        try:
            loggging.info("Calculating RMSE")
            RMSE = mean_squared_error(y_true,y_pred, squared=False)
            loggging.info("MSE:{}".format(RMSE))
            return RMSE
        except Exception as e:
            loggging.error("Error in calculating RMSE:{}".format(e))
            raise e
    

