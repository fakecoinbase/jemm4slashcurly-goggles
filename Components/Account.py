class Account():
	def __init__(
		self,
		accountId = str,
		balance = float,
		accountCurrency = str,
		nativeBalance = float,
		nativeCurrency = str,
		transactions = list,
		exchangeRate = float,
	):
		self.AccountId = accountId
		self.Balance = balance
		self.AccountCurrency = accountCurrency
		self.NativeBalance = nativeBalance
		self.NativeCurrency = nativeCurrency
		self.Transactions = transactions
		self.ExchangeRate = exchangeRate