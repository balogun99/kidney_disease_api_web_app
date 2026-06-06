import streamlit as st
import numpy as np
import pickle
# from src.kidney_model_API import kidney_pred

kidney_model = pickle.load(
    open("model/kidney_model.sav", "rb")
)

# kidney_model = pickle.load(open('/Users/macbookpro/Desktop/End-to-End Projects/kidney_disease/model/kidney_model.sav', 'rb'))
# kidney_model = pickle.load(open('/Users/macbookpro/Desktop/End-to-End Projects/kidney_disease/notebooks/kidney_model_present.sav', 'rb'))


def kidney_pred(input_data):
    # load the dataset data
    # input_data = (71,0.3,40.9,0,1,46.8,1622,1) # Dialysis Absent

# change the input data into a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
    input_reshaped = input_data_as_numpy_array.reshape(1,-1)

# make predictions
    predictions = kidney_model.predict(input_reshaped)
    print(predictions)

# system check
    if (predictions[0] == 0):
        return 'DIALYSIS ABSENT'
    else:
        return "DIALYSIS PRESENT"

def main():

    st.set_page_config(page_title="Kidney Disease Prediction")
    st.title("Kidney Disease Predictive System")

    Age = st.sidebar.slider("Age", 20,90)
    Creatinine_Level = st.sidebar.slider("Creatinine_Level", 0.3,4.13)
    BUN = st.sidebar.slider("BUN", 5.0,61.9)
    Diabetes = st.sidebar.slider("Diabetes", 0,1)
    Hypertension = st.sidebar.slider("Hypertension", 0,1)
    GFR = st.sidebar.slider("GFR", 5,120)
    Urine_Output = st.sidebar.slider("Urine_Output", 100,2899)
    CKD_Status = st.sidebar.slider("CKD_Status", 0,1)

    result = ''

    if st.button('Predict Kidney Disease'):
        result = kidney_pred([Age, Creatinine_Level, BUN, Diabetes, Hypertension, GFR, Urine_Output, CKD_Status])

    st.success(result)

if __name__ == '__main__':
    main()