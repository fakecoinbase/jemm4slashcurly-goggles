class Buy():
	def __init__(
		self,
		buyId = str,
		amount = float,
		amountCurrency = str,
		totalPaid = float,
		totalCurrency = str,
		subtotal = float
		):
		self.BuyId = buyId
		self.Amount = amount
		self.AmountCurrency = amountCurrency
		self.TotalPaid = totalPaid
		self.TotalCurrency = totalCurrency
		self.Subtotal = subtotal