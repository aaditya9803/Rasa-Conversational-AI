from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionExtractAge(Action):

    def name(self) -> Text:
        return "action_extract_age"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        age = tracker.get_slot('age')
        print(f"Retrieved age slot value: {age}")

        if age:
            try:
                age = int(age)
                print(f"Successfully converted age to integer: {age}")
                return [SlotSet("extracted_age", age)]
            except ValueError:
                print("Failed to convert age to integer.")
                return [SlotSet("extracted_age", None)]
            
        print("Age slot is not set or is None.")
        return []