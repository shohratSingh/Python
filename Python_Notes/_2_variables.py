#variables are the containers used to store values or memory address

#multi veriable and multi value
a,b,c,d=1,2,3,4
print(a,b,c,d)

#single veriable and multi value also known as "Tuple"
t=10,20,30,40,50
print(type(t))


#some more examples of veriables

#CASE 1:-

name = "Shohrat Singh Rajput"
address = "5175/12, Surat Nagar Phase-1, Gurugram 122006"
course = "Python full stack with data analytics"
institute = "Qspiders Gurugram"
place = "Gurugram"
state = "Haryana"
age = 22
gender = "Masculine"
year_of_passout = 2025

details = [name,address,course,institute,place,state,age,gender,year_of_passout]

print(details)

#CASE 2:-

first_name, last_name, percentage, degree, collage_name, university, ug, pg = "Shohrat", "Singh", 85, "BCA", "BM Group of Istitution", "Gurugram University", "N/A", "N/A"
print(first_name)
print(last_name)
print(percentage)
print(degree)
print(collage_name)
print(university)
print(ug)
print(pg)


#CASE 3:-

rapido = "username", "password", "login", "home", "new ride", "origin", "destination", "payment method", " payment", "ride_rating"
print(rapido) 

events = "cook without fire", "chess", "cricket", "badminton", "group discussion", "dancing", "singing", "rangoli", "debate", "e-sports"
print(events) 

signup = "first name", "middle name", "last name","phone number", "email", "username","password", "signup"
print(signup)

gmail = "all inboxes", "primary", "promotions", "social", "updates", "starred", "snoozed", "important", "sent", "scheduled", "outbox", "drafts", "all mail", "spam", "trash"
print(gmail)