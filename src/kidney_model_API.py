# load libraries
from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

# instance of fastapi
app = FastAPI()

# class for the BaseModel
class model_input(BaseModel):
    Age : int
    Creatinine_Level : float
    BUN : float
    Diabetes : int
    Hypertension : int
    GFR : float
    Urine_Output : float
    CKD_Status : int

# load the model
kidney_model = pickle.load(
    open("model/kidney_model.sav", "rb")
)
# kidney_model = pickle.load(open('/Users/macbookpro/Desktop/End-to-End Projects/kidney_disease/model/kidney_model.sav', 'rb'))

# create endpoint
@app.post('/kidney_prediction')

# function for input parameters
def kidney_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    Age = input_dictionary['Age']
    Creatinine_Level = input_dictionary['Creatinine_Level']
    BUN = input_dictionary['BUN']
    Diabetes = input_dictionary['Diabetes']
    Hypertension = input_dictionary['Hypertension']
    GFR = input_dictionary['GFR']
    Urine_Output = input_dictionary['Urine_Output']
    CKD_Status = input_dictionary['CKD_Status']

    input_list = [Age, Creatinine_Level, BUN, Diabetes, Hypertension, GFR, Urine_Output, CKD_Status]

    prediction = kidney_model.predict([input_list])

    if prediction[0] == 0:
        return 'DIALYSIS ABSENT'
    else:
        return 'DIALYSIS PRESENT'