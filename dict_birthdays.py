birthdays = {
    "Pradham" : "24 November 2006",
    "Malini" : "14 October 1974",
    "Surendra" : "31 October 1972",
    "Prithvi" : "22 August 2001",
}
try:
    who = str(input("Enter whose birthday you want to look up: "))
    print(who, "s birthday is on", birthdays[who])
except:
    if who == str and KeyError:
        print("That person is not present in our records")
except TypeError:
    print("Please enter a valid input")
