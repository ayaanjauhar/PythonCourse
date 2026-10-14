budget = int(input("Enter the budget of the month: "))
count = 1
numberofexpenses = int(input("Enter the number of expenses you have: "))
while count <= numberofexpenses:
    expense = input("Name of expense: ")
    expenseamount = int(input("Amount for the expense: "))
    budget = budget - expenseamount
    count = count + 1
if budget < 0:
    print("over the budget")
else:
    print("under the budget")
