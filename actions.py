import re, math, random
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, ActionExecutionRejection
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

# from email_connector import sendMail
# from excelsheet import datastore
from database_connector import DataUpdate, UserDataUpdate

reg_phone = '^[6-9]{1}[0-9]{1}[0-9]{8}$'
reg_name = '^[A-Za-z\s]{3,30}$'

mailOTP = ""

# def generateOTP():

#     global mailOTP

#     digits = "0123456789"
#     OTP = ""

#     for i in range(4):
#         OTP += digits[math.floor(random.random() * 10)]

#     mailOTP = OTP

#     print("OTP generated")

class ActionSaveData(Action):

    def name(self) -> Text:
        return "action_save_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         datastore(tracker.get_slot("name"),
#                   tracker.get_slot("phone"),
#                   tracker.get_slot("email"))
        # dispatcher.utter_message(text="Data Stored Successfully.")
        return []

class UserForm(FormAction):
    """Example of a custom form action"""

    def name(self):
        # type: () -> Text
        """Unique identifier of the form"""

        return "user_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["name", "phone"]   
        

    def slot_mappings(self):
        # type: () -> Dict[Text: Union[Dict, List[Dict]]]
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {"name": self.from_text(intent=None),
                "phone": self.from_text(intent=None)}
                
    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_name(  self,
                        value: Text,
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate Name."""
        name = value.lower()
        if (re.search(reg_name, name)):
            return {"name": name}
        else:
            # validation failed, set this slot to None, meaning the
            dispatcher.utter_template('utter_wrong_name', tracker)
            # user will be asked for the slot again
            return {"name": None}

    def validate_phone( self,
                        value: Text,
                        dispatcher: CollectingDispatcher,
                        tracker: Tracker,
                        domain: Dict[Text, Any]) -> Optional[Text]:
        """Validate phone value."""
        
        if (re.search(reg_phone, value)):
            if self.is_int(value):
                return {"phone": value}
        else:
            dispatcher.utter_template('utter_wrong_phone', tracker)
            # validation failed, set slot to None
            return {"phone": None}


    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_template('', tracker)
        return []


class EmailForm(FormAction):
    
        """Example of a custom form actions"""

        def name(self):
            """Unique identifier of the form"""

            return "email_form"

        @staticmethod
        def required_slots(tracker: Tracker) -> List[Text]:
            """A list of required slots that the form has to fill"""

            return ["email"]
            # ,"otp"]

        def slot_mappings(self):
            # -> Dict[Text, Union[Dict, List[Dict]]]:
            """A dictionary to map required slots to
                - an extracted entity
                - intent: value pairs
                - a whole message
                or a list of them, where a first match will be picked"""

            return {
                "email": self.from_text(intent=None),
                # "otp": self.from_text()
                }
        
        @staticmethod
        def is_int(string: Text) -> bool:
            """Check if a string is an integer"""
            try:
                int(string)
                return True
            except ValueError:
                return False

        def validate_email( self,
                            value: Text,
                            dispatcher: CollectingDispatcher,
                            tracker: Tracker,
                            domain: Dict[Text, Any]) -> Optional[Text]:
            """Validate email value."""
            
            reg_email = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

            if (re.search(reg_email, value)):
                # generateOTP()
                # sendMail(value, tracker.get_slot("name"), mailOTP)
                return {"email": value}
            else:
                dispatcher.utter_template('utter_wrong_email', tracker)
                # validation failed, set slot to None
                return {"email": None}

        # def validate_otp( self,
        #                 value: Text,
        #                 dispatcher: CollectingDispatcher,
        #                 tracker: Tracker,
        #                 domain: Dict[Text, Any]) -> Optional[Text]:
        #     """Validate email otp value."""

        #     reg_otp = '^[0-9]{4}$'

        #     if (re.match(reg_otp, value)) and str(value) == mailOTP:
        #         return {"otp": value}
        #     else:
        #         dispatcher.utter_message(template="utter_wrong_otp")
        #         return {"otp": None}
    
        def submit(self,
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict]:
            """Define what the form has to do
                after all required slots are filled"""

            UserDataUpdate(tracker.get_slot("name"), tracker.get_slot("phone"), tracker.get_slot("email"))

            dispatcher.utter_message(template="utter_submit")
            return []


class FeedbackForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""


        return "feedback_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["feedback"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "feedback": self.from_text()
        }

    @staticmethod

    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_feedback(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate feedback value"""

        reg_num = '^[0-5]{1}$'
        if (re.search(reg_num,value)):
            if self.is_int(value):
                return {"feedback": value}
        else:
            dispatcher.utter_message(template="utter_wrong_feedback")

            return {"feedback": None}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        # dispatcher.utter_message(template="utter_submit")
        return []
