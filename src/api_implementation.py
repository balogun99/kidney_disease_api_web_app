import json
import requests

url = 'http://127.0.0.1:8000/kidney_prediction'

input_data_for_model = {
    'Age' : 71,
    'Creatinine_Level' : 0.3,
    'BUN' : 40.9,
    'Diabetes' : 0,
    'Hypertension' : 1,
    'GFR' : 46.8,
    'Urine_Output' : 1622,
    'CKD_Status' : 1 
}

input_json = json.dumps(input_data_for_model)
response = requests.post(url, data=input_json)

print(response.text)