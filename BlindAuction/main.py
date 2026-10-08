# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bidders_dictionary = {}

from art import logo
print(logo)
print("Welcome to the Blind Auction Project!")

auction_over = False
while not auction_over:
    bidder = input("What is your name?: ")
    bid = int(input(f"What is your bid?: $"))
    more_bidders = input("Are there any other bidders? Type yes or no: ").lower()

    bidders_dictionary[bidder] = bid

    if more_bidders == "no":
        auction_over = True
        print("Thank you for your participation!")
        highest_score = max(bidders_dictionary, key=bidders_dictionary.get)
        print("The highest bidder is " + f"{highest_score}: {bidders_dictionary[highest_score]}$")

