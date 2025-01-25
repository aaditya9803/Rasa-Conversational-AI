from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHandleDirectInput(Action):

    def name(self) -> Text:
        return "action_handle_direct_input"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age = tracker.get_slot('age')
        height = tracker.get_slot('height')
        weight = tracker.get_slot('weight')

        if age and not height:
            dispatcher.utter_message(response="utter_ask_height")
        elif height and not weight:
            dispatcher.utter_message(response="utter_ask_weight")
        elif weight and not age:
            dispatcher.utter_message(response="utter_greet")
        else:
            dispatcher.utter_message(response="utter_direct_input")

        return []


class ActionCalculateBMI(Action):

    def name(self) -> Text:
        return "action_calculate_bmi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        height = tracker.get_slot('height')
        weight = tracker.get_slot('weight')

        if height and weight:
            try:
                height = float(height)
                weight = float(weight)
                bmi = weight / (height ** 2)
                bmi_category = self.get_bmi_category(bmi)
                dispatcher.utter_message(response="utter_bmi_result", bmi=bmi, bmi_category=bmi_category)
                return [SlotSet("bmi", bmi), SlotSet("bmi_category", bmi_category)]
            except ValueError:
                dispatcher.utter_message(text="Sorry, I couldn't calculate your BMI. Please provide valid height and weight.")
                return []
        else:
            dispatcher.utter_message(text="I need both your height and weight to calculate your BMI.")
            return []

    def get_bmi_category(self, bmi: float) -> Text:
        if bmi < 18.5:
            return "underweight"
        elif 18.5 <= bmi < 25:
            return "normal weight"
        elif 25 <= bmi < 30:
            return "overweight"
        else:
            return "obese"