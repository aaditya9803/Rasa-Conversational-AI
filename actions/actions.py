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


        age = tracker.get_slot('age')
        gender = tracker.get_slot('gender')
        hypertension = tracker.get_slot('hypertension')
        heart_disease = tracker.get_slot('heart_disease')
        ever_married = tracker.get_slot('ever_married')
        work_type = tracker.get_slot('work_type')
        residence_type = tracker.get_slot('Residence_type')
        avg_glucose_level = tracker.get_slot('avg_glucose_level')
        bmi = tracker.get_slot('bmi')
        smoking_status = tracker.get_slot('smoking_status')


        print(f"Debug: Age = {age}, Gender = {gender}, Hypertension = {hypertension}, "
              f"Heart Disease = {heart_disease}, Ever Married = {ever_married}, "
              f"Work Type = {work_type}, Residence Type = {residence_type}, "
              f"Avg Glucose Level = {avg_glucose_level}, BMI = {bmi}, "
              f"Smoking Status = {smoking_status}")

        if not age:
            dispatcher.utter_message(response="utter_greet")
        elif not gender:
            dispatcher.utter_message(response="utter_ask_gender")
        elif not hypertension:
            dispatcher.utter_message(response="utter_ask_hypertension")
        elif not heart_disease:
            dispatcher.utter_message(response="utter_ask_heart_disease")
        elif not ever_married:
            dispatcher.utter_message(response="utter_ask_ever_married")
        elif not work_type:
            dispatcher.utter_message(response="utter_ask_work_type")
        elif not residence_type:
            dispatcher.utter_message(response="utter_ask_residence_type")
        elif not avg_glucose_level:
            dispatcher.utter_message(response="utter_ask_avg_glucose_level")
        elif not bmi:
            dispatcher.utter_message(response="utter_ask_bmi")
        elif not smoking_status:
            dispatcher.utter_message(response="utter_ask_smoking_status")
        else:
            dispatcher.utter_message(response="utter_thank_you")


        return []