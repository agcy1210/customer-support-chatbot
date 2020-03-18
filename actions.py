# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "address"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionServiceSearch(Action):

    def name(self) -> Text:
        return "action_service_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        service = tracker.get_slot("service_type")
        location = tracker.get_slot("location")
        address = "300 Hyde St, {}".format(location)
        cost = "$5000"

        dispatcher.utter_message(
            "Here is the address of the {}: {} and the cost is {}".format(service, address, cost))

        return [SlotSet("address", address), SlotSet("cost", cost)]


