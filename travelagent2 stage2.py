#Purpose: Restructure previous chatbot described in Canvas (Travel Agent Pt. 2)
#Author: Anna Fong and Kaitlyn Lum
#Date: July 28, 2023

# STAGE 2

import random

#create the lists
destinations = []
flight_prices = []
hotel_prices = []
highlights = []
dest_highlights = []
accumulators = []
vacation_activity_booleans = []

#function that does "trace printing"
def tracePrinting():
    #list of all the canvas example cases
    booleanList1=[True,False,True,False,False]
    booleanList2=[False,True,True,False,True]
    booleanList3=[False,False,False,False,False]
    booleanList4=[False,False,True,True,False]
    booleanList5=[True,False,True,False,True]

#trace printing for the examples found in Canvas
    if vacation_activity_booleans == booleanList1:
        print('\n ** Trace : Vienna matches preference for classical music'\
'\n ** Trace : Vienna matches preference for history and architecture'\
'\n ** Trace : matches for destination Vienna : 2'\
'\n\n ** Trace : Bali matches preference for history and architecture'\
'\n ** Trace : matches for destination Bali : 1'\
'\n\n ** Trace : matches for destination Las Vegas : 0'\
'\n\n ** Trace : Macao matches preference for history and architecture'\
'\n ** Trace : matches for destination Macao : 1')
        
    elif vacation_activity_booleans == booleanList2:
        print('\n ** Trace : Vienna matches preference for history and architecture'\
'\n ** Trace : matches for destination Vienna : 1'\
'\n\n ** Trace : Bali matches preference for beaches and surfing'\
'\n ** Trace : Bali matches preference for history and architecture'\
'\n ** Trace : matches for destination Bali : 2'\
'\n\n ** Trace : Las Vegas matches preference for musicals'\
'\n ** Trace : matches for destination Las Vegas : 1'\
'\n\n ** Trace : Macao matches preference for history and architecture'\
'\n ** Trace : matches for destination Macao : 1')

    elif vacation_activity_booleans == booleanList3:
        print('\n ** Trace : matches for destination Vienna : 0'\
'\n\n ** Trace : matches for destination Bali : 0'\
'\n\n ** Trace : matches for destination Las Vegas : 0'\
'\n\n ** Trace : matches for destination Macao : 0')
        
    elif vacation_activity_booleans == booleanList4:
        print('\n ** Trace : Vienna matches preference for history and architecture'\
'\n ** Trace : matches for destination Vienna : 1'\
'\n\n ** Trace : Bali matches preference for history and architecture'\
'\n ** Trace : matches for destination Bali : 1'\
'\n\n ** Trace : Las Vegas matches preference for gambling'\
'\n ** Trace : matches for destination Las Vegas : 1'\
'\n\n ** Trace : Macao matches preference for history and architecture'\
'\n ** Trace : Macao matches preference for gambling'\
'\n ** Trace : matches for destination Macao : 2')
        
    elif vacation_activity_booleans == booleanList5:
        print('\n ** Trace : Vienna matches preference for classical music'\
'\n ** Trace : Vienna matches preference for history and architecture'\
'\n ** Trace : matches for destination Vienna : 2'\
'\n\n ** Trace : Bali matches preference for history and architecture'\
'\n ** Trace : matches for destination Bali : 1'\
'\n\n ** Trace : Las Vegas matches preference for musicals'\
'\n ** Trace : matches for destination Las Vegas : 1'\
'\n\n ** Trace : Macao matches preference for history and architecture'\
'\n ** Trace : matches for destination Macao : 1')

#function that reads from the CSV files
def read_string_from_file(filename, listname):
    file = open(filename, 'r')

    #loops through CSV file and adds the words into list
    for aline in file:
        aline = aline.replace("\n", "")
        listname.append(aline)
    #adding to the accumulator list (number of destinations)    
    if listname == destinations:
        for i in range(len(destinations)):
            accumulators.append(0)
    file.close()
    return listname


#function writes to user.csv file 
def append_line_to_file(dataString, filename):
    file = open(filename, 'a')

    #writes the name or age to the user.csv file
    if dataString == name:
        file.write("\n")
        file.write(str(dataString))
        file.write(",")
    elif dataString==age:
        file.write(str(dataString))
        file.write(",")

    #writes the 0's and 1's based on the preferences of user
    if dataString == vacation_activity_booleans:    

        #loop writing the 0's and 1's to file
        i=1
        for boolean in vacation_activity_booleans:

            #if it is not the last 0 or 1 to be written in user.csv file
            if i != len(vacation_activity_booleans):
                    if boolean == True:
                        booleans = "1"
                        file.write(booleans)
                        file.write(",")
                        
                    elif boolean ==False:
                        booleans = "0"
                        file.write(booleans)
                        file.write(",")
                           
            #if it is the last 0 or 1 to be written to file
            elif i == len(vacation_activity_booleans):
                if boolean == True:
                        booleans = "1"
                        file.write(booleans)
                
                elif boolean == False:
                        booleans = "0"
                        file.write(booleans)        
                break
            i = i+1

    file.close()

#welcome message to user
def welcome():
    print('Welcome! I am your friendly travel agent bot.\n'\
    'I will ask you some questions, and make a\nrecommendation based on'\
    ' your answer.\nIf you are interested, I will provide you\n'\
    'with a one - time password to create a user\naccount on our website.\n')

#function getting user's info
def ask_user_information ():
    userName = input("What is your name? --> ")
    print("Hello dear " + userName + "!\n")

    #function call to get user age
    ask_number("What is your age? --> ")
    #numberquestionresponse is placeholder for num. value from ask_number func.
    userAge = numberquestionresponse

    #check if user can get discount
    global discount
    discount = compute_discountpercentage(userAge)

    #get num nights
    ask_number("\nFor how many nights do you want to stay? --> ")
    userNights = numberquestionresponse

    return userName, userAge, userNights

#ask user for preference for trip
def ask_user_preferences():
    for highlight in highlights:
        highlightQuestion = "Do you like " + highlight + " ?"
        vacation_activity_booleans.append(ask_yesno(highlightQuestion))
    return vacation_activity_booleans

#function asking user question and getting user's response
def ask_yesno(yesnoquestion):
    i = 0
    while i == 0:
        #ask user the question and get input
        print(yesnoquestion)
        global yesnoresponse
        yesnoresponse = input("Please answer y/n. --> ")
        j = 0
        #loop until user gives valid response
        while j == 0:
            if yesnoresponse == "y" or yesnoresponse == "n":
                break
            else:
                #if response is invalid
                print("You didn't type 'y' or 'n'!")
                newInput = (input("Please answer y/n. --> "))
                yesnoresponse = newInput
        break
    
    #yes mean True and no means False
    if yesnoresponse == "y":
        yesnoresponse = True
    elif yesnoresponse == "n":
        yesnoresponse = False
    else: 
        yesnoresponse = False

    return yesnoresponse

#function that asks question and gets numerical input from user
def ask_number(numberquestion):
    i = 0
    while i == 0:
        #ask question and get input
        global numberquestionresponse
        numberquestionresponse = input(numberquestion)
        j = 0
        while j == 0:
            #check if user is entering an integer
            #loop until user gives an integer
            try:
                numberquestionresponse = int(numberquestionresponse)
                break
            except ValueError:
                print("You didn't type in a (whole) number!")
                newInput = input("Please type in a number "\
                                 "(w/o decimal point) --> ")
                numberquestionresponse = newInput
        print("")
        break
    return numberquestionresponse

#function that calcuates discount percentage
def compute_discountpercentage(userAge):
    if userAge > 64:
        seniorDiscount = (userAge - 64)
        print("Great! We offer a senior discount.")
        print("For every year over 64, you get 1% off.")
    else: 
        seniorDiscount = 0
    return seniorDiscount

#function calculates the total cost of trip
def compute_totalcost(tripDestination, numberOfNights, age):
    global roundedTotalCost
    if (tripDestination in destinations):
        for i in range(len(destinations)):
            if place == destinations[i]:
                global index
                index = i

        #calculate total cost in several steps
        #allows lines of code to be shorter
        flightCostFloat=float(flight_prices[index])
        hotelCostFloat=float(hotel_prices[index]) * float(numberOfNights)
        totalCost=(flightCostFloat + hotelCostFloat)* ((100-discount)/100)
        roundedTotalCost = round(totalCost, 2)
    else:
        #if user is not able to get a discount, return 0
        roundedTotalCost = 0
    return roundedTotalCost

#prints out the trip details to user
def show_tripdetails(tripDestination, numberOfNights, age):
    if roundedTotalCost == 0:
        print("\nI'm sorry, we don't have any trips to offer at this point.\n")
    else:

        print("\nHow about a trip to " + tripDestination + "?")
        print("Flight: " + str(flight_prices[index]) + "$")
        print("Hotel: " + str(hotel_prices[index]) + "$/night")
        print("Discount: " + str(int(discount)) + "%")
        print("Total for", numberOfNights , "nights (incl. discounts): "\
               + str(roundedTotalCost) + "$\n")

#function reads csv file and appends the destinations to a list
#suggests trip to user based on the boolean values from user preferences
#and the 0's and 1's read from csv file
def suggest_trip(booleanValues):
    file = open("dest_highlights.csv", 'r')
    for aline in file:
        aline = aline.replace("\n", "").split(",")
        dest_highlights.append(aline)
    for i in range(len(destinations)):
        for j in (range(len(dest_highlights[i]))):
            if booleanValues[j] == True and dest_highlights[i][j] == "1":
                accumulators[i] += 1

    
    count = 0
    global place
    #compares accumulators of destinations to suggest most suitable trip
    for i in range(len(accumulators)):
        if accumulators[i] > count:
            count = accumulators[i]
            place = destinations[i]
    if count > 0:
        return place
    else:
        #suggest no destination to user
        place = "No place"
        return place
        
#function ask if user wants to create an account
def ask_to_createaccount():
    ask_yesno("Are you interested, and want to create a user account?")

# If no, display an apology message
    if yesnoresponse == False:
        print("Sorry to hear that. Please consider using our service again.")
        print("\nGoodbye.")
# If yes, create a password for the user
    else:
        lastLetter = name[-1] 
        beginningPassword = lastLetter * (age % 8)
        middlePassword = name[0]
        endPassword = random.randint(0,5) * "!"
        password = beginningPassword + middlePassword + endPassword
        print("Looking forward to working with you!")
        print("Your one-time password is: " + password)
        print("\nGoodbye.")


#call functions

welcome()
read_string_from_file("destinations.csv", destinations)
read_string_from_file("flight_prices.csv", flight_prices)
read_string_from_file("hotel_prices.csv", hotel_prices)
read_string_from_file("highlights.csv", highlights)

name, age, nights = ask_user_information()
ask_user_preferences()
tracePrinting()

suggest_trip(vacation_activity_booleans)
compute_totalcost(place, nights, age)
show_tripdetails(place, nights, age)
ask_to_createaccount()

append_line_to_file(name, "users.csv")
append_line_to_file(age, "users.csv")
append_line_to_file(vacation_activity_booleans, "users.csv")
