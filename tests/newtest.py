user_data = {
    "age": 23,
    "gender": "male",
    "hypertension": None,
    "heart_disease": None,
    "ever_married": None,
    "work_type": None,
    "residence_type": None,
    "avg_glucose_level": None,
    "height": None,
    "weight": None,
    "smoking_status": None
}

for key in user_data:
    if user_data[key] is None:
        print(f"utter_ask_{key}")
        break

