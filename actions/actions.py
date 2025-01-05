
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class Extract_symptopms(Action):

    def name(self) -> Text:
        return "action_symptoms_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptom = next(tracker.get_latest_entity_values('disease'), None)

        if symptom:
            dispatcher.utter_message(text="I see you have a symptom of {symptom}".format(symptom))
        else:
            dispatcher.utter_message(text="I could not find any symptom")
        return []