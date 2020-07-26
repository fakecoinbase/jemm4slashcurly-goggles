class Account:
    def __init__(
        self,
        accountId=str,
        balance=float,
        accountCurrency=str,
        nativeBalance=float,
        nativeCurrency=str,
        exchangeRate=float,
        transactions=list,
        totalBought=float,
        totalSold=float,
    ):
        self.AccountId = accountId
        self.Balance = balance
        self.AccountCurrency = accountCurrency
        self.NativeBalance = nativeBalance
        self.NativeCurrency = nativeCurrency
        self.ExchangeRate = exchangeRate
        self.Transactions = transactions
        self.TotalBought = totalBought
        self.TotalSold = totalSold
