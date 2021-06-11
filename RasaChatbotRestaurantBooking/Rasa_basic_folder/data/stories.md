## Greet
* greet
    - utter_greet
> check_greet

## Happy path
> check_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"is_loc_supported":true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "big"}
    - slot{"price":"big"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id":"ahbcdj@dkj.com"}
    - slot{"mail_id":"ahbcdj@dkj.com"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 1
> check_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
    - slot{"is_loc_supported": false}
    - utter_we_dont_operate
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price_range
* restaurant_search{"price": "big"}
    - slot{"price": "big"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id": "xyz@sth.edu"}
    - slot{"mail_id": "xyz@sth.edu"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 2
> check_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail
    - utter_ask_emailid
* provide_mail{"mail_id": "jddk.2jmd@kdl.co.in"}
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 3
> check_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_location
    - slot{"is_loc_supported": false}
    - utter_we_dont_operate
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail
    - utter_ask_emailid
* provide_mail{"mail_id": "jddk.2jmd@kdl.co.in"}
    - slot{"mail_id": "jddk.2jmd@kdl.co.in"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 4
> check_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* deny
    - utter_not_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 5
> check_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Puducherry"}
    - slot{"location": "Puducherry"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": "Puducherry"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id": "random@gmail.com"}
    - slot{"mail_id": "random@gmail.com"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 6
> check_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "moderate"}
    - slot{"price": "moderate"}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* deny
    - utter_not_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 7
> check_greet
* restaurant_search{"cuisine": "american", "location": "Kolhapur"}
    - slot{"location": "Kolhapur"}
    - slot{"cuisine": "american"}
    - action_check_location
    - slot{"is_loc_supported": false}
    - utter_we_dont_operate
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "big"}
    - slot{"price": "big"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id": "qwert@bot.co.io"}
    - slot{"mail_id": "qwert@bot.co.io"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 8
> check_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Sangli"}
    - slot{"location": "Sangli"}
    - action_check_location
    - slot{"is_loc_supported": false}
    - utter_we_dont_operate
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* deny
    - utter_not_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 9
> check_greet
* restaurant_search{"price": "low", "cuisine": "south indian", "location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - slot{"cuisine": "south indian"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail
    - utter_ask_emailid
* provide_mail{"mail_id": "gty@ipc.re"}
    - slot{"mail_id": "gty@ipc.re"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 10
> check_greet
* restaurant_search{"cuisine": "chinese", "location": "Jalgaon", "price": "big"}
    - slot{"location": "Jalgaon"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "big"}
    - action_check_location
    - slot{"is_loc_supported": false}
    - utter_we_dont_operate
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* deny
    - utter_not_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 11
> check_greet
* restaurant_search{"price": " big", "cuisine": "american"}
    - slot{"cuisine": "american"}
    - slot{"price": " big"}
    - utter_ask_location
* restaurant_search{"location": "New Delhi"}
    - slot{"location": "New Delhi"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - action_search_restaurants
    - slot{"location": "New Delhi"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id": "random@gmail.com"}
    - slot{"mail_id": "random@gmail.com"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 12
> check_greet
* restaurant_search{"price": "big"}
    - slot{"price": "big"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* deny
    - utter_not_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 13
> check_greet
* restaurant_search{"price": "big"}
    - slot{"price": "big"}
    - utter_ask_location
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": true}
    - utter_send_on_email
* provide_mail{"mail_id": "rty@io.com"}
    - slot{"mail_id": "rty@io.com"}
    - action_send_mail
    - utter_sent
    - action_reset_slots
* goodbye
    - utter_goodbye

## Interactive story 14
> check_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": false}
    - utter_no_results_found
* goodbye
    - utter_goodbye

## Interactive story 15
> check_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_price_range
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": false}
    - utter_no_results_found
* goodbye
    - utter_goodbye

## Interactive story 16
> check_greet
* restaurant_search{"price": "low"}
    - slot{"price": "low"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"mail_response": "Results"}
    - slot{"results_found": false}
    - utter_no_results_found
* goodbye
    - utter_goodbye

## Interactive story 17
> check_greet
* restaurant_search{"price": "low", "cuisine": "chinese", "location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "low"}
    - action_check_location
    - slot{"is_loc_supported": true}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - slot{"mail_response": "Foodie found the following restaurants for you:\n"}
    - slot{"results_found": false}
    - utter_no_results_found
* goodbye
    - utter_goodbye
