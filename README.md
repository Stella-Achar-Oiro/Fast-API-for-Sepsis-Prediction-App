# Sepsis Prediction API

This project implements a machine learning model for sepsis prediction and exposes it as a RESTful API using FastAPI. The sepsis prediction model is trained on a dataset containing various clinical features and aims to predict the likelihood of sepsis in patients.

## Features

Utilizes logistic regression, random forest, and gradient boosting algorithms for sepsis prediction.
Performs data preprocessing and feature engineering to prepare the dataset for model training.
Implements cross-validation and hyperparameter tuning to ensure the robustness and generalizability of the selected model.
Exposes the trained model as a RESTful API using FastAPI.
Supports real-time predictions by accepting patient information as JSON input and returning the sepsis prediction.

## Installation


Clone this repository:
 ```
git clone https://github.com/Stella-Achar-Oiro/Fast-API-for-Sepsis-Prediction-App.git
```
Install the required dependencies: 

```
pip install -r requirements.txt
```

## Usage

* Train the sepsis prediction model: Run the train_model.py script to train the model using the provided dataset.
* Start the FastAPI server: Run the main.py script to start the FastAPI server and make the sepsis prediction API available.
* Send prediction requests: Use a tool like cURL or an API testing tool to send POST requests to the API endpoint (http://localhost:8000/predict) with patient information in JSON format. The API will return the predicted sepsis probability.

## Dockerization

The project also provides Docker support to containerize the application. You can build a Docker image using the provided Dockerfile and deploy the application as a container.

To build the Docker image, execute the following command in the project directory:

```
docker build -t sepsis-prediction-api .
```

To run the Docker container, execute the following command:

```
docker run -p 8000:8000 sepsis-prediction-api
```

The application will be accessible at http://localhost:8000 inside the Docker container.

### Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.

### License

This project is licensed under the MIT License. 


