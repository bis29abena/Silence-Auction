from bis29 import clear
import art as art

print(art.logo)

#Creating an empty dictionary
auction_dictionary = {}

#Taking inputs from the user
#Thats the name and amount he wants to bid
Bidders_name = input("What is your name: ")
Bidders_amount = input("What is your bid GH₵")

def auction(name, amount):
    """Takes in two parameters that is
        name and ammount
        this function selects the name with the highest bidder 
        In a dictionary
    """

    #Adding the name and its corresponding amount into the dictionary
    #The name as key and the amount as the value
    auction_dictionary[name] = amount

    #Checking if the is anothe bidder
    Yes_or_no = input("Are there any other bidders, Type yes or no " ).lower()

    #If yes 
    #The function auction should keep on adding bidders and amount into the dictionary 
    if Yes_or_no == "yes":
        
        #Is a class that clears the users screen
        clear.clear()

        Bidders_name_def = input("What is your name: ")
        Bidders_amount_def = input("What is your bid GH₵")
        auction(Bidders_name_def,Bidders_amount_def)

    #If no it should print out the highest bidder and its corresponding amount
    elif Yes_or_no == "no":
        max_of_price = []

        for key_value in auction_dictionary:
            max_of_price.append(auction_dictionary[key_value])
        
        #This is used to get the key of the one with the highest amount
        max_key = max(auction_dictionary, key=auction_dictionary.get)
        #This is used to get the highest amount in the dictionary
        max_bid = max(max_of_price)

        print(f"The winner is {max_key} with a bid of {max_bid}")

auction(Bidders_name, Bidders_amount)

    

