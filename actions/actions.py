# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionHelloWorld(Action):

    def name(self):
        return "action_extract_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age = tracker.get_slot('age')

        if age:
            # Convert age to integer
            try:
                age = int(age)
                return [SlotSet("extracted_age", age)]
            except ValueError:
                return [SlotSet("extracted_age", None)]

        # dispatcher.utter_message(text="Hello World!")

        return []
    
    # def extract_age(self, dispatcher, tracker, domain):
    #     age_entity = next(tracker.get_latest_entity_values('age'), None)
    #     if age_entity:
    #         print(age_entity)
    #         return int(age_entity)
    #     return None
