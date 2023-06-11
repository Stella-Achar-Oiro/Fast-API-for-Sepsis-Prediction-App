from fastapi import FastAPI

# Define your ML model input schema
class PredictionInput(BaseModel):
    PRG: int
    PL: int
    PR: int
    SK: int
    TS: int
    M11: float
    BD2: float
    Age: int
    Insurance: int

# Load the exported objects
with open('/content/encoder.pkl', 'rb') as file:
    encoder = pickle.load(file)

with open('/content/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('/content/model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the FastAPI app
app = FastAPI(title='Sepsis API', description='An API that takes input and displays the predictions', version='0.1.0')

# Define the prediction endpoint
@app.post('/Sepsis')
def predict(input_data: PredictionInput):
    # Preprocess the input features
    encoded_features = encoder.transform([[input_data.PRG, input_data.PL, input_data.PR, input_data.SK, input_data.TS, input_data.M11, input_data.BD2, input_data.Age, input_data.Insurance]])
    scaled_features = scaler.transform(encoded_features)

    # Make predictions using the model
    predictions = model.predict(scaled_features)

    # Labeling Model output
    if prediction[0] < 0.5:
        prediction_label = "Negative. This person does not have Sepsis."
    else:
        prediction_label = "Positive. This person has Sepsis."

    # Return the predictions
    return {'predictions': predictions.tolist()}


