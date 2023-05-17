from fastapi import FastAPI

app = FastAPI()

# Define the prediction endpoint
@app.post("/predict")
def predict_sepsis(data: InputData):
    # Convert input data to a feature vector
    feature_vector = [[
        data.Age,
        data.Insurance,
        data.PRG,
        data.PL,
        data.PR,
        data.SK,
        data.TS,
        data.M11
    ]]

    # Make the prediction
    prediction = model.predict(feature_vector)
    probability = model.predict_proba(feature_vector)[:, 1]

    # Prepare the response
    response = {
        "prediction": prediction[0],
        "probability": probability[0]
    }

    return response
