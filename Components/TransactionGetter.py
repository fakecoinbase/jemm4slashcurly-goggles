from Components.ClientGetter import CoinbaseClient
from AccountComponents.Transaction import Transaction
import json


class TransactionGetter:
    def __init__(self, accountId):
        self.jsonTransactions = json.loads(
            json.dumps(CoinbaseClient.get_transactions(accountId))
        )
        self.Transactions = []

    def GetTransactions(self):
        for jsonTransaction in self.jsonTransactions["data"]:
            transaction = Transaction()

            transaction.TransactionId = jsonTransaction["id"]
            transaction.TransactionType = jsonTransaction["type"]
            transaction.Amount = jsonTransaction["amount"]["amount"]
            transaction.AmountCurrency = jsonTransaction["amount"]["currency"]
            transaction.NativeAmount = jsonTransaction["native_amount"]["amount"]
            transaction.NativeCurrency = jsonTransaction["native_amount"]["currency"]

            self.Transactions.append(transaction)

        return self.Transactions

    def GetTotalBought(self):
        total = 0
        for transaction in self.Transactions:
            if transaction.TransactionType != "sell":
                total += float(transaction.NativeAmount)
        return total

    def GetTotalSold(self):
        total = 0
        for transaction in self.Transactions:
            if transaction.TransactionType == "sell":
                total += float(transaction.NativeAmount)
        return total
