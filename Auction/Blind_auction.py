import Auction_art

print(Auction_art.logo)
print("WELCOME TO THE AUCTION HOUSE!")

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ''
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bidder:
            highest_bidder = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


while not bidding_finished:
    name = input("To begin, please type your name: ")
    price = int(input("How much would you like to bid? $"))
    bids[name] = price
    other_bidders = input("Are there any other bidders? -- Yes or No").lower()
    if other_bidders == "no":
        bidding_finished = True
        find_highest_bidder(bids)
