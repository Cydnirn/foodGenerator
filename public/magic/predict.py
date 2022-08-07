from os import path
import pickle
import numpy as np

filePath = path.abspath(__file__)
dirPath = path.dirname(filePath)
modelFilePath = path.join(dirPath, 'saved_model.pkl')

def load_model():
    with open(modelFilePath, 'rb') as file:
        model = pickle.load(file)
    return model

def inverse_ohe(label, arr):
    for i in arr:
        i = np.argmax(i)
        i = label.inverse_transform([i])
        return i

model = load_model()

#model
forestModelFood = model["model_food"]
forestModelDrink = model["model_drink"]

#encoder

#READ FOR AGE and MOOD
"""
They are case sensitive

Age: Balita, Remaja, Dewasa, Anak - anak, lansia
Mood: Marah, Sedih, Senang
"""
age_LE = model["age_ENC"]
food_LE = model["food_ENC"]
drink_LE = model["drink_ENC"]

#READ FOR FOOD AND DRINKS
"""
They are case sensitive

Food: Cokelat, Nasi goreng , Seblak, Mie pedas, Daging, 
    Sayur-sayuran, Ikan-ikanan, Telur, Makanan laut, Kacang-kacangan

Drink: Air mineral, Minuman bersoda, Es krim, 
    Teh, Kopi, Susu, Air kelapa, Jus
"""

#Abandoned OneHotEncoder
"""
c_ohe = OneHotEncoder()
d_ohe = OneHotEncoder()
food_ohe = model["food_ohe"]
drink_ohe = model["drink_ohe"]
"""

#Format for array is [[Sex, Mood, Age]]
s_test = "Perempuan"
m_test = "Marah"
age_test = ["Dewasa"]

#Manual OneHotEncoding
if (s_test == "Laki - Laki"):
    s_test = [1, 0]
else:
    s_test = [0, 1]
s_test = np.array(s_test)

if (m_test == "Marah"):
    m_test = [1, 0, 0]
elif (m_test == "Sedih"):
    m_test = [0, 1, 0]
else:
    m_test = [0, 0, 1]
m_test = np.array(m_test)

age_test = age_LE.fit_transform([age_test])
age_test = age_test.astype(float)
age_test = np.array(age_test)
age_test = age_test.flatten()
print(s_test, m_test, age_test)
X = np.concatenate((s_test, m_test, age_test))
print(X)
X = [X]
Ypred = forestModelFood.predict(X)
Zpred = forestModelDrink.predict(X)

print(inverse_ohe(food_LE, Ypred))
print(inverse_ohe(drink_LE, Zpred))