import pickle
import pandas as pd
from math import exp


def make_prediction(input: dict) -> float:
    model_path = 'main_app/static/models/finalized_model.pkl'
    model = pickle.load(open(model_path, 'rb'))

    # Le champ est nommé First_Flr_SF dans models.py mais le modele attend une colonne 1st Flr SF
    input_df = pd.DataFrame(input, index=[0]).rename(columns={'First_Flr_SF':'1st Flr SF'})

    input_df.columns = input_df.columns.str.replace('_',' ' )

    try:
        # le modèle a été entraîné sur les log
        log_price = model.predict(input_df)
        pred = int(exp(log_price))
    except TypeError:
        pred = 0
    except ValueError:
        pred = 0
    return pred
