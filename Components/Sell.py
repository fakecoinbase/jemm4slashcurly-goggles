class Sell():
	def __init__(
		self,
		sellId = str,
		amount = float,
		amountCurrency = str,
		totalPaid = float,
		totalCurrency = str,
		subtotal = float
		):
		self.SellId = sellId
		self.Amount = amount
		self.AmountCurrency = amountCurrency
		self.TotalPaid = totalPaid
		self.TotalCurrency = totalCurrency
		self.Subtotal = subtotal