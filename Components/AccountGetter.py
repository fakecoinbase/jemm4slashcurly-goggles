from Components.ClientGetter import CoinbaseClient
from Components.TransactionGetter import TransactionGetter
from AccountComponents.Account import Account
import json


class AccountGetter:
    def __init__(self):
        self.jsonAccounts = json.loads(json.dumps(CoinbaseClient.get_accounts()))

    def GetAccounts(self):
        accounts = []

        for jsonAccount in self.jsonAccounts["data"]:
            account = Account()

            account.AccountId = jsonAccount["id"]
            account.Balance = jsonAccount["balance"]["amount"]
            account.AccountCurrency = jsonAccount["balance"]["currency"]
            account.NativeBalance = jsonAccount["native_balance"]["amount"]
            account.NativeCurrency = jsonAccount["native_balance"]["currency"]
            account.ExchangeRate = self.GetCurrentExchangeRate(
                account.AccountCurrency, account.NativeCurrency
            )

            transactionGetter = TransactionGetter(account.AccountId)
            account.Transactions = transactionGetter.GetTransactions()
            account.TotalBought = transactionGetter.GetTotalBought()
            account.TotalSold = transactionGetter.GetTotalSold()

            accounts.append(account)

        return accounts

    def GetCurrentExchangeRate(self, accountCurrency, nativeCurrency):
        jsonExchangeRates = json.loads(
            json.dumps(CoinbaseClient.get_exchange_rates(currency=accountCurrency))
        )
        return jsonExchangeRates["rates"][nativeCurrency]
