import pickle
import numpy as np

def load_model():
    with open('saved_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

model = load_model()

#model
forestModelFood = model["model_food"]
forestModelDrink = model["model_drink"]

#encoder
age_LE = model["age_ENC"]
food_LE = model["food_ENC"]
drink_LE = model["drink_ENC"]

food_ohe = model["food_ohe"]
drink_ohe = model["drink_ohe"]