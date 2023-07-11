def deposit(money, balance):
  balance += money
  return balance

# Exercise 1
def withdraw(money):
  balance = 100
  balance -= money
  print(balance)

# Exercise 2
def withdraw2(money, balance):
  balance -= money
  return balance


# main
current_balance = 0

current_balance = deposit(100, current_balance)

print(current_balance)

current_balance = withdraw2(25, current_balance)
print(current_balance)
