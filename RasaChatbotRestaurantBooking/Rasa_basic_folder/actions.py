from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ZomatoData = pd.read_csv('zomato.csv')
ZomatoData = ZomatoData.drop_duplicates().reset_index(drop=True)
WeOperate = ['New Delhi', 'Gurgaon', 'Noida', 'Faridabad', 'Allahabad', 'Bhubaneshwar', 'Mangalore', 'Mumbai', 'Ranchi', 'Patna', 'Mysore', 'Aurangabad', 'Amritsar', 'Puducherry', 'Varanasi', 'Nagpur', 'Vadodara', 'Dehradun', 'Vizag', 'Agra', 'Ludhiana', 'Kanpur', 'Lucknow', 'Surat', 'Kochi', 'Indore', 'Ahmedabad', 'Coimbatore', 'Chennai', 'Guwahati', 'Jaipur', 'Hyderabad', 'Bangalore', 'Nashik', 'Pune', 'Kolkata', 'Bhopal', 'Goa', 'Chandigarh', 'Ghaziabad', 'Ooty', 'Gangtok', 'Shimla']
Mail_Response = ""

def RestaurantSearch(City,Cuisine,Budget):
	TEMP = ZomatoData[(ZomatoData['Cuisines'].apply(lambda x: Cuisine.lower() in x.lower())) & (ZomatoData['City'].apply(lambda x: City.lower() in x.lower()))]
	if Budget == "low":
		TEMP = TEMP[TEMP["Average Cost for two"] < 300]
	elif Budget == "moderate":
		TEMP = TEMP[(TEMP["Average Cost for two"] >= 300) & (TEMP["Average Cost for two"] <= 700)]
	elif Budget == "big":
		TEMP = TEMP[TEMP["Average Cost for two"] > 700]

	TEMP = TEMP.sort_values(axis=0, by='Aggregate rating', ascending=False)
	return TEMP[['Restaurant Name','Address','Average Cost for two','Aggregate rating']]

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):
		#config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('price')
		results = RestaurantSearch(City=loc,Cuisine=cuisine,Budget=budget)
		response=""
		result_response = []
		results_found = False
		if results.shape[0] == 0:
			response= "no results"
		else:
			index = 0
			for restaurant in results.iloc[:10].iterrows():
				index += 1
				restaurant = restaurant[1]
				result_response.append(F"{index}. {restaurant['Restaurant Name']} in {restaurant['Address']} with avg cost of Rs. {restaurant['Average Cost for two']} and has been rated {restaurant['Aggregate rating']}")
			results_found = True

		dispatcher_response = "\n\n".join(result_response[:5])
		Mail_Response = "\n\n".join(result_response)
		Mail_Response = "Foodie found the following restaurants for you:\n" +  Mail_Response
		dispatcher.utter_message("Found the following searches:\n"+dispatcher_response)
		return [SlotSet('location',loc), SlotSet('mail_response', Mail_Response), SlotSet('results_found', results_found)]

class ActionSendMail(Action):
	def name(self):
		return 'action_send_mail'

	def run(self, dispatcher, tracker, domain):
		MailID = tracker.get_slot('mail_id')
		#sendmail(MailID,response)
		#return [SlotSet('mail_id',MailID)]
		Mail_Response = tracker.get_slot('mail_response')
		dispatcher.utter_message("Sending message:"+Mail_Response)

		#The mail addresses and password
		sender_address = 'rohanbhalerasabot@gmail.com'
		sender_pass = 'rasabot2488'
		receiver_address = MailID

		#Setup the MIME
		message = MIMEMultipart()
		message['From'] = sender_address
		message['To'] = receiver_address
		message['Subject'] = 'Restaurant search results'   #The subject line
		#The body and the attachments for the mail
		message.attach(MIMEText(Mail_Response, 'plain'))
		#Create SMTP session for sending the mail
		session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
		session.starttls() #enable security
		session.login(sender_address, sender_pass) #login with mail_id and password
		text = message.as_string()
		session.sendmail(sender_address, receiver_address, text)
		session.quit()

class ActionCheckLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location = tracker.get_slot('location')
		location = location.lower()
		print("Validating location:", location)
		weOperateLower = [city.lower() for city in WeOperate]
		result = location in weOperateLower
		if result:
			val_loc = "true"
		else:
			val_loc = "false"
		print(location, ":", result)
		return [SlotSet('is_loc_supported',result)]

class ActionResetSlots(Action):
	def name(self):
		return 'action_reset_slots'

	def run(self, dispatcher, tracker, domain):
		return [SlotSet('location',None),
		 SlotSet('cuisine',None), 
		 SlotSet('price',None), 
		 SlotSet('mail_id',None), 
		 SlotSet('is_loc_supported',True), 
		 SlotSet('mail_response',None), 
		 SlotSet('results_found',False)] 