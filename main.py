from Components.ClientGetter import Client
from Components.Account import Account
from Components.Transaction import Transaction
from Components.Buy import Buy
import json

def main():
	jsonAccounts = json.loads(json.dumps(Client.get_accounts()))

	accounts = GetAccounts(jsonAccounts)


def GetAccounts(jsonAccounts):
	accounts = []

	for jsonAccount in jsonAccounts["data"]:
		account = Account()

		account.AccountId = jsonAccount["id"]
		account.Balance = jsonAccount["balance"]["amount"]
		account.AccountCurrency = jsonAccount["balance"]["currency"]
		account.NativeBalance = jsonAccount["native_balance"]["amount"]
		account.NativeCurrency = jsonAccount["native_balance"]["currency"]
		account.ExchangeRate = GetCurrentExchangeRate(account.AccountCurrency, account.NativeCurrency)
		account.DeltaValue = GetDeltaValue(account.Balance, account.NativeBalance, account.ExchangeRate)


		print("\n\n_______________________________Account_____________________________________________")
		print("Account ID: ", account.AccountId)
		print("Balance: ", account.Balance, account.AccountCurrency)
		print("Native Balance: ", account.NativeBalance, account.NativeCurrency)
		print("Current exchange rate", account.ExchangeRate, account.NativeCurrency)
		print("-------------------------------Gain/Loss---------------------------------------------")
		print("Gain/Loss: ", account.DeltaValue)
		print("-------------------------------End Gain/Loss---------------------------------------------")

		# print("-------------------------------Transactions---------------------------------------------")
		account.transactions = GetTransactions(account.AccountId)
		# print("-------------------------------End Transactions---------------------------------------------")
		print("_______________________________End Account_____________________________________________")
		accounts.append(account)

	return accounts

def GetTransactions(accountId):
	jsonTransactions = json.loads(json.dumps(Client.get_transactions(accountId)))

	transactions = []

	for jsonTransaction in jsonTransactions["data"]:
		transaction = Transaction()

		transaction.TransactionId = jsonTransaction["id"]
		transaction.TransactionType = jsonTransaction["type"]
		transaction.Amount = jsonTransaction["amount"]["amount"]
		transaction.AmountCurrency = jsonTransaction["amount"]["currency"]
		transaction.NativeAmount = jsonTransaction["native_amount"]["amount"]
		transaction.NativeCurrency = jsonTransaction["native_amount"]["currency"]

		# PrintTransaction(transaction)

		transactions.append(transaction)

	return transactions

def PrintTransaction(transaction):
    print("-------------------------------Transaction---------------------------------------------")
    print("ID: ", transaction.TransactionId)
    print("Type: ", transaction.TransactionType)
    print("Amount: ", transaction.Amount, transaction.AmountCurrency)
    print("Native Amount: ", transaction.NativeAmount, transaction.NativeCurrency)
    print("-------------------------------End Transaction---------------------------------------------")

def GetCurrentExchangeRate(accountCurrency, nativeCurrency):
	jsonExchangeRates = json.loads(json.dumps(Client.get_exchange_rates(currency=accountCurrency)))
	return jsonExchangeRates["rates"][nativeCurrency]

def GetDeltaValue(Balance, NativeBalance, exchangeRate):

	pass

def GetBuys(accountId):
	jsonBuys = json.loads(json.dumps(Client.get_buys(accountId)))
	buys = []

	for jsonBuy in jsonBuys["data"]:
		buy = Buy()

		buy.BuyId = jsonBuy["id"]
		buy.Amount = jsonBuy["amount"]["amount"]
		buy.AmountCurrency = jsonBuy["amount"]["currency"]
		buy.TotalPaid = jsonBuy["total"]["amount"]
		buy.TotalCurrency = jsonBuy["total"]["amount"]
		buy.Subtotal = jsonBuy["subtotal"]["amount"]

		buys.append(buy)

	return buys

def GetSells(accountId):
	jsonSells = json.loads(json.dumps(Client.get_buys(accountId)))
	sells = []

	for jsonSell in jsonSells["data"]:
		sell = Buy()

		sell.SellId = jsonSell["id"]
		sell.Amount = jsonSell["amount"]["amount"]
		sell.AmountCurrency = jsonSell["amount"]["currency"]
		sell.TotalPaid = jsonSell["total"]["amount"]
		sell.TotalCurrency = jsonSell["total"]["amount"]
		sell.Subtotal = jsonSell["subtotal"]["amount"]

		sells.append(sell)

	return sells

if __name__ == "__main__":
	main()