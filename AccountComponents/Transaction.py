class Transaction:
    def __init__(
        self,
        transactionId=str,
        transactionType=str,
        amount=float,
        amountCurrency=str,
        nativeAmount=float,
        nativeCurrency=float,
    ):
        self.TransactionId = transactionId
        self.TransactionType = transactionType
        self.Amount = amount
        self.AmountCurrency = amountCurrency
        self.NativeAmount = nativeAmount
        self.NativeCurrency = nativeCurrency
