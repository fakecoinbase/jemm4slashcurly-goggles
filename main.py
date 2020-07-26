import pandas as pd
from Components.AccountGetter import AccountGetter

accountIdKey = "Account ID"
balanceKey = "Balance"
accountCurrencyKey = "Account Currency"
nativeBalanceKey = "Native Balance"
nativeCurrencyKey = "Native Currency"
exchangeRateKey = "Exchange Rate"
totalBoughtKey = "Total Bought"
totalSoldKey = "Total Sold"
transactionsKey = "Transactions"
transactionIdKey = "Transaction ID"
transactionTypeKey = "Transaction Type"
amountKey = "Transaction Amount"
amountCurrencyKey = "Transaction Currency"
nativeAmountKey = "Transaction Native Amount"
transactionNativeCurrencyKey = "Transaction Native Currency"


def main():
    accountGetter = AccountGetter()
    accounts = accountGetter.GetAccounts()
    PrintAccountAndTransactionDataFrames(accounts)


def PrintAccountAndTransactionDataFrames(accounts):
    accountDict = {
        accountIdKey: [],
        balanceKey: [],
        accountCurrencyKey: [],
        nativeBalanceKey: [],
        nativeCurrencyKey: [],
        exchangeRateKey: [],
        totalBoughtKey: [],
        totalSoldKey: [],
    }

    transactionDict = {
        transactionIdKey: [],
        transactionTypeKey: [],
        amountKey: [],
        amountCurrencyKey: [],
        nativeAmountKey: [],
        transactionNativeCurrencyKey: [],
    }

    for account in accounts:
        accountDict[accountIdKey].append(account.AccountId)
        accountDict[balanceKey].append(account.Balance)
        accountDict[accountCurrencyKey].append(account.AccountCurrency)
        accountDict[nativeBalanceKey].append(account.NativeBalance)
        accountDict[nativeCurrencyKey].append(account.NativeCurrency)
        accountDict[exchangeRateKey].append(account.ExchangeRate)
        accountDict[totalBoughtKey].append(account.TotalBought)
        accountDict[totalSoldKey].append(account.TotalSold)

        transactionDict = GetTransactionDict(transactionDict, account.Transactions)

    pd.set_option("display.max_rows", None, "display.max_columns", None)
    accountDataFrame = pd.DataFrame(accountDict)
    print("Account Data Frame\n", accountDataFrame)

    transactionDataFrame = pd.DataFrame(transactionDict)
    print("Transactions Data Frame\n", transactionDataFrame)


def GetTransactionDict(transactionDict, transactions):
    for transaction in transactions:
        transactionDict[transactionIdKey].append(transaction.TransactionId)
        transactionDict[transactionTypeKey].append(transaction.TransactionType)
        transactionDict[amountKey].append(transaction.Amount)
        transactionDict[amountCurrencyKey].append(transaction.AmountCurrency)
        transactionDict[nativeAmountKey].append(transaction.NativeAmount)
        transactionDict[transactionNativeCurrencyKey].append(transaction.NativeCurrency)
    return transactionDict


if __name__ == "__main__":
    main()
