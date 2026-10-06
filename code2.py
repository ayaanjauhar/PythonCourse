account_id = "AC1025"
opening_balance = 15000
transaction_amount = 4500
account_status = "active"
closing_balance = opening_balance - transaction_amount
print("account id = ", account_id)
print("opening balance = ", opening_balance)
print("transaction amount = ", transaction_amount)
print("account status = ", account_status)
print("closing balance = ", closing_balance)
if opening_balance >= transaction_amount:
    print(True)
else:
    print(False)

amount_posistive = transaction_amount > 0
sufficient_fundas = opening_balance >= transaction_amount
valid_withdrawal = (
    amount_posistive
    and sufficient_fundas
    and account_status
)
print(amount_posistive, sufficient_fundas, account_status, valid_withdrawal)