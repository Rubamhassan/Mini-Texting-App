# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC38e1b6d5cc02a5b6eb36e4c446693f57"
auth_token = "1d21cdeed73e33a78fe10a8103024972 "
client = TwilioRestClient(account_sid, auth_token)


def add_appointment():
	user_name = raw_input("what is your name?\n")
	user_mobile_number = raw_input("what is your mobile number?\n")
	appointment_date = raw_input("what date would you like to come in?\n")
	appointment_time = raw_input("what time would you like to come in?\n")
	client.messages.create(to= user_mobile_number, from_="16506845238", body= "Dear " + user_name + ", we look forward to seeing you on " + appointment_date + " at " + appointment_time)
	return  "                     Appointment added and message has been sent!"
	print "\n"
	print "\n"

	# return {"Patient_name":user_name, "Patient_number":user_mobile_number, "Appointment":appointment_time_date}

def confirm_appointment():
	messages = client.messages.list()
	# for m in messages:
	# 	client.messages.delete(m.sid)

	# length_before = len(messages)
	# print length_before
	time_of_last_msg = messages[0].date_created 
	client.messages.create(to="+16503155608", from_="+16506845238",
                                     body= "Please confirm your scheduled appointment? Reply with C to confirm or N to cancel")
	messages = client.messages.list()
	print "Waiting for the patient response"
	# print "before loop: ", messages[0].date_created
	while True:

		messages = client.messages.list()
		# print messages[0].date_created
		# print len(messages)
		if messages[0].date_created > time_of_last_msg and (messages[0].to == '+16506845238' or messages[1].to == '+16506845238'):
			# print "in first if"
			if messages[0].body.lower() == "c" or messages[1].body.lower() == "c":
				# print "before message sent"
				client.messages.create(to="+16503155608", from_="+16506845238",
	                                     body= "We look forward to seeing you at 450 Sutter St. San Francisco Ca 94212!")
				print "\nFinal confirmation message sent to the patient successfully\n"

				# print "after message sent"
			elif messages[0].body.lower() == "n" or messages[1].body.lower() == "n":
				client.messages.create(to="+16503155608", from_="+16506845238",
	                                 body= "Please contact us to reschedule (415)221-6157. We look forward to hearing from you soon.")
				print "\nRescheduling message sent to the patient successfully\n"
			else:
				client.messages.create(to="+16503155608", from_="+16506845238",
	                                 body= "Please choose a valid option C to confirm or N to reschedule")
				print "\nValidation message sent to the patient successfully\n"
				continue

			break		


def main():
	while True:
		user_choice = raw_input("what would you like to do? enter 1 to schedule, 2 to confirm, q to quit\n")
		#ask user what would you like to do? press 1 to add appointment press 2 to confirm the appointment 
		if user_choice == "1":
			print add_appointment()
		elif user_choice == "2":
			confirm_appointment()
		elif user_choice == "q" or user_choice == "Q":
			break
		else:
			print "\nPlease choose a valid option.\n"
		
if __name__ == '__main__':
	main()
	








# if user_response == confirmed:
# 	print "We look forward to seeing you!"
# elif user_response == no:
# 	print "Please indicate what times/dates might work better for you"
# else user_response == none 
# 	print "Please contact our office to confirm your appointment"
# #Ask if medication has been picked up? if yes confirm and send pre-oberative instructions and send map/address
# #if medication is not picked up --Send text to pick up medication 24 hrs prior to surgery and follow up 1 day prior 
# patient_name = patient_one 

# Patient_mobile_number = mobile_number

# office_address = 450 Sutter Street, SF Ca 
