import pywhatkit

phone_number = input("Enter Your Phone Number: ")
pywhatkit.sendwhatmsg(phone_number, "Message", 20, 30)