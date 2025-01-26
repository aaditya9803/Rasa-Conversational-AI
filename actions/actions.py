from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHandleConversation(Action):

    def name(self) -> Text:
        return "action_handle_conversation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_data = {
            "age": None,
            "gender": None,
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

        user_data["age"] = tracker.get_slot('age')
        user_data["gender"] = tracker.get_slot('gender')
        user_data["hypertension"] = tracker.get_slot('hypertension')
        user_data["heart_disease"] = tracker.get_slot('heart_disease')
        user_data["ever_married"] = tracker.get_slot('ever_married')
        user_data["work_type"] = tracker.get_slot('work_type')
        user_data["residence_type"] = tracker.get_slot('Residence_type')
        user_data["avg_glucose_level"] = tracker.get_slot('avg_glucose_level')
        user_data["height"] = tracker.get_slot('height')
        user_data["weight"] = tracker.get_slot('weight')
        user_data["smoking_status"] = tracker.get_slot('smoking_status')


        print(f'Debug: Age = {user_data["age"]}, Gender = {user_data["gender"]}, Hypertension = {user_data["hypertension"]}, '
              f'Heart Disease = {user_data["heart_disease"]}, Ever Married = {user_data["ever_married"]}, '
              f'Work Type = {user_data["work_type"]}, Residence Type = {user_data["residence_type"]}, '
              f'Avg Glucose Level = {user_data["avg_glucose_level"]}, Height = {user_data["height"]}, '
              f'Weight = {user_data["weight"]}, Smoking Status = {user_data["smoking_status"]}')

        for key in user_data:
            if user_data[key] is None:
                dispatcher.utter_message(response=f"utter_ask_{key}")
                break
            else:
                dispatcher.utter_message(response="utter_thank_you")
                break          
        return []