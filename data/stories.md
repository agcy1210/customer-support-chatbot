## hotel search happy path
* greet
  - utter_how_can_i_help
* service_provider{"service_type":"hotel", "location":"San Francisco"}
  - action_service_search
  - slot{"address": "300 Hyde St, San Francisco"}
  - slot{"cost":"$5000"}
* thanks
  - utter_goodbye

## hotel search + location
* greet
  - utter_how_can_i_help
* service_provider{"service_type":"hotel"}
  - utter_ask_location
* inform{"location":"San Francisco"}
  - action_service_search
  - slot{"address": "300 Hyde St, San Francisco"}
  - slot{"cost":"$5000"}
* thanks
  - utter_goodbye

## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
