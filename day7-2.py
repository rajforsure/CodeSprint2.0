n = int(input())
prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for price in prices[1:]:
  profit = price - min_price
  if profit > max_profit:
    max_profit = profit
  if price < min_price:
    min_price = price

print(max_profit if max_profit >= 2 else 0)