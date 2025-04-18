# After accidentally leaving an ice chest of fish and shrimp in your car for a week while you
# were on vacation, you’re now in the market for a new vehicle. Your insurance didn’t cover
# the loss, so you want to make sure you get a good deal on your new car.
# Given a Series of car asking_prices and another Series of car fair_prices, determine which
# cars for sale are a good deal. In other words, identify cars whose asking price is less than
# their fair price.
# The result should be a list of integer indices corresponding to the good deals
# in asking_prices.
import pandas as pd
def good_deals(asking_price,fair_price):
    ans = pd.Series([i for i in range(len(fair_price)) if asking_price[i] < fair_price[i]])
    return ans



# Asking prices of cars (seller's price)
asking_prices = pd.Series([18000, 22000, 25000, 30000, 27000, 32000, 15000, 21000, 28000, 35000])

# Fair market prices of cars (estimated real value)
fair_prices = pd.Series([19000, 21000, 26000, 29000, 28000, 33000, 16000, 22000, 29000, 34000])
deals =good_deals(asking_prices,fair_prices)

data =pd.DataFrame({'asking price':asking_prices,'fair price':fair_prices })
print(data[data['asking price'] <data['fair price']])

