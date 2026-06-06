# load libraries
from fastapi import FastAPI
from pydantic import BaseModel
import json
import pickle
import uvicorn
from pyngrok import ngrok
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio

# load fastapi
app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*']
)

class model_input(BaseModel):
    Age : int
    Creatinine_Level : float
    BUN : float
    Diabetes : int
    Hypertension : int
    GFR : float
    Urine_Output : float
    CKD_Status : int

# load the saved model
kidney_model = pickle.load(open('/Users/macbookpro/Desktop/End-to-End Projects/kidney_disease/model/kidney_model.sav', 'rb'))

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
    
NGROK_AUTH_TOKEN = '3EcCW65C1UuqV4b0Ai7KYl1WOVx_5rrMqXtFLFKXNXHj4uSFw'
ngrok.set_auth_token(NGROK_AUTH_TOKEN)

ngrok_tunnel = ngrok.connect()
print('Public URL: ', ngrok_tunnel.public_url)
nest_asyncio.apply()
uvicorn.run(app, port=8000)
