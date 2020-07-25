from Components.ClientGetter import CoinbaseClient
from Components.Account import Account
from Components.Transaction import Transaction
from Components.Buy import Buy
import pandas as pd
import json

def main():
	jsonAccounts = json.loads(json.dumps(CoinbaseClient.get_accounts()))
	accounts = GetAccounts(jsonAccounts)
	accountIdKey = "Account ID"
	balanceKey = "Balance"
	accountCurrencyKey = "Account Currency"
	nativeBalanceKey = "Native Balance"
	nativeCurrencyKey = "Native Currency"
	exchangeRateKey = "Exchange Rate"

	accountDict = {
		accountIdKey: [],
		balanceKey: [],
		accountCurrencyKey: [],
		nativeBalanceKey: [],
		nativeCurrencyKey: [],
		exchangeRateKey: [],
		}

	for account in accounts:
		accountDict[accountIdKey].append(account.AccountId)
		accountDict[balanceKey].append(account.Balance)
		accountDict[accountCurrencyKey].append(account.AccountCurrency)
		accountDict[nativeBalanceKey].append(account.NativeBalance)
		accountDict[nativeCurrencyKey].append(account.NativeCurrency)
		accountDict[exchangeRateKey].append(account.ExchangeRate)

	df = pd.DataFrame(accountDict)
	pd.set_option("display.max_rows", None, "display.max_columns", None)

	print(df)


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

		# print("\n\n_______________________________Account_____________________________________________")
		# print("Account ID: ", account.AccountId)
		# print("Balance: ", account.Balance, account.AccountCurrency)
		# print("Native Balance: ", account.NativeBalance, account.NativeCurrency)
		# print("Current exchange rate: ", account.ExchangeRate, account.NativeCurrency)
		# print("-------------------------------Gain/Loss---------------------------------------------")
		# print("Gain/Loss: ", account.DeltaValue)
		# print("-------------------------------End Gain/Loss---------------------------------------------")

		# print("-------------------------------Transactions---------------------------------------------")
		account.Transactions = GetTransactions(account.AccountId)
		# print("-------------------------------End Transactions---------------------------------------------")
		account.TotalBought = GetTotalBought(account.Transactions)
		account.TotalSold = GetTotalSold(account.Transactions)
		account.DeltaValue = GetDeltaValue(account.NativeBalance, account.TotalBought, account.TotalSold)
		# print("DeltaValue: ", account.DeltaValue)

		# print("_______________________________End Account_____________________________________________")
		accounts.append(account)

	return accounts

def GetTransactions(accountId):
	jsonTransactions = json.loads(json.dumps(CoinbaseClient.get_transactions(accountId)))

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
	jsonExchangeRates = json.loads(json.dumps(CoinbaseClient.get_exchange_rates(currency=accountCurrency)))
	return jsonExchangeRates["rates"][nativeCurrency]

def GetTotalBought(transactions):
	total = 0
	for transaction in transactions:
		if (transaction.TransactionType != "sell"):
			total += float(transaction.NativeAmount)
	# print(total)
	return total

def GetTotalSold(transactions):
	total = 0
	for transaction in transactions:
		if (transaction.TransactionType == "sell"):
			total += float(transaction.NativeAmount)
	return total

def GetDeltaValue(nativeBalance, totalBought, totalSold):
	delta = float(nativeBalance) - float(totalBought) + float(totalSold)
	return delta

def GetBuys(accountId):
	jsonBuys = json.loads(json.dumps(CoinbaseClient.get_buys(accountId)))
	buys = []

	for jsonBuy in jsonBuys["data"]:
		buy = Buy()

		if (jsonBuy["status"] != "completed"):
			continue
		buy.BuyId = jsonBuy["id"]
		buy.Amount = jsonBuy["amount"]["amount"]
		buy.AmountCurrency = jsonBuy["amount"]["currency"]
		buy.TotalPaid = jsonBuy["total"]["amount"]
		buy.TotalCurrency = jsonBuy["total"]["amount"]
		buy.Subtotal = jsonBuy["subtotal"]["amount"]

		buys.append(buy)

	return buys

def GetSells(accountId):
	jsonSells = json.loads(json.dumps(CoinbaseClient.get_buys(accountId)))
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