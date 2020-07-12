from Components.ClientGetter import Client
from Components.Account import Account
from Components.Transaction import Transaction
import json

def main():
	jsonAccounts = json.loads(json.dumps(Client.get_accounts()))

	accounts = GetAccounts(jsonAccounts)
	#	for account in accounts:
	#		print("\nID: " + account.id)
	#		print("Balance: " + account.balance)
	#		print("Native Balance: " + account.nativeBalance)
	difference = GetDifference(accounts)
	print(difference)


def GetAccounts(jsonAccounts):
	accounts = []

	for jsonAccount in jsonAccounts["data"]:
		account = Account()

		account.accountId = jsonAccount["id"]
		account.balance = jsonAccount["balance"]["amount"]
		account.accountCurrency = jsonAccount["balance"]["currency"]
		account.nativeBalance = jsonAccount["native_balance"]["amount"]
		account.nativeCurrency = jsonAccount["native_balance"]["currency"]

		if (float(account.balance) > 0.0):
			print("\n\n-------------------------------Account---------------------------------------------")
			print("Account ID: ", account.accountId)
			print("Balance: ", account.balance, account.accountCurrency)
			print("Native Balance: ", account.nativeBalance, account.nativeCurrency)
			account.transactions = GetTransactions(account.accountId)
			print("-----------------------------------End Account-----------------------------------------")
		accounts.append(account)

	return accounts

def GetTransactions(accountId):
	jsonTransactions = json.loads(json.dumps(Client.get_transactions(accountId)))

	transactions = []

	for jsonTransaction in jsonTransactions["data"]:
		transaction = Transaction()

		transaction.transactionId = jsonTransaction["id"]
		transaction.type = jsonTransaction["type"]
		transaction.amount = jsonTransaction["amount"]["amount"]
		transaction.amountCurrency = jsonTransaction["amount"]["currency"]
		transaction.nativeAmount = jsonTransaction["native_amount"]["amount"]
		transaction.nativeCurrency = jsonTransaction["native_amount"]["currency"]

		print("\n||||||||||||||||||||||||||||||Transactions||||||||||||||||||||||||||||||||||||||||||||||")
		print("Transaction ID: ", transaction.transactionId)
		print("Type: ", transaction.type)
		print("Amount: ", transaction.amount, transaction.amountCurrency)
		print("Native Amount: ", transaction.nativeAmount, transaction.nativeCurrency)
		print("|||||||||||||||||||||||||||||||||End Transactions|||||||||||||||||||||||||||||||||||||||||||")

		transactions.append(transaction)

	return transactions

def GetDifference(accounts):
	pass


if __name__ == "__main__":
	main()