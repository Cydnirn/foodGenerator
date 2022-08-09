from os import path
import numpy as np
import pickle, sys, json

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

def simplifyAge(age):
    if age > 0  and age <= 5:
        return "Balita"
    elif age > 5 and age <= 12:
        return "Anak - anak"
    elif age > 12 and age <= 18:
        return "Remaja"
    elif age > 18 and age <= 50:
        return "Dewasa"
    elif age > 50 and age <= 200:
        return "lansia"

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

#Input data from node.js
#data = sys.argv[1]
#data = json.loads(data)

jsonFilePath = path.join(dirPath,"pred.json")

#TEST DATA
#
#with open(jsonFilePath) as jsondata:
#    dataPred = json.load(jsondata)
#data = {"sex":"Laki - Laki", "mood":"Senang", "age":"20"}
#data = json.dumps(data)
#dataPred = json.loads(data)

dataPred = json.loads(sys.argv[1])

sexData = list(dataPred.values())[0]
moodData = list(dataPred.values())[1]
ageData = list(dataPred.values())[2]

ageData = simplifyAge(int(ageData))

#OneHotEncoding data
def encodeSex(data):
    if(data == "Laki - Laki"):
        data = [1, 0]
    else:
        data = [0, 1]
    data = np.array(data)
    return data

def encodeMood(data):
    if (data == "Marah"):
        data = [1, 0, 0]
    elif (data == "Sedih"):
        data = [0, 1, 0]
    else:
        data = [0, 0, 1]
    data = np.array(data)
    return data

sexData = encodeSex(sexData)
moodData = encodeMood(moodData)

ageData = age_LE.fit_transform([[ageData]])
ageData = ageData.astype(float)
ageData = np.array(ageData)
ageData = ageData.flatten()

X = np.concatenate((sexData, moodData, ageData))

X = [X]
Ypred = forestModelFood.predict(X)
Zpred = forestModelDrink.predict(X)

foodRes = inverse_ohe(food_LE, Ypred)
drinkRes = inverse_ohe(drink_LE, Zpred)

foodRes = foodRes[0]
drinkRes = drinkRes[0]

def defaultJson(t):
    return f'{t}'

resultpred = {'food': foodRes, 'drink': drinkRes}
resultpred = json.dumps(resultpred)

print(resultpred)