import requests
from datetime import datetime

GENDER = "YOUR_GENDER"
AGE = "YOUR_AGE"
WEIGHT_KG = "YOUR_WEIGHT"
HEIGHT_CM = "YOUR_HEIGHT"

APP_ID = "Your nutritionix app id"
API_KEY = "Your nutritionix api key"
nutritionix_endpoint = "Your nutritionix endpoint"
sheety_endpoint = "Your sheety endpoint"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_text = input("Please specify your workout for today: ")

nutritionix_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "age": AGE,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
}

today = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

response = requests.post(url=nutritionix_endpoint, json=nutritionix_parameters, headers=headers)
print(response.text)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs)

    print(sheet_response.text)
