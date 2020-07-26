from AccountComponents.Sell import Sell


class SellGetter:
    def __init__(self, accountId):
        self.AccountId = accountId
        self.Sells = []

    def GetSells(self):
        jsonSells = json.loads(json.dumps(CoinbaseClient.get_Sells(self.AccountId)))

        for jsonSell in jsonSells["data"]:
            sell = Sell()

            sell.SellId = jsonSell["id"]
            sell.Amount = jsonSell["amount"]["amount"]
            sell.AmountCurrency = jsonSell["amount"]["currency"]
            sell.TotalPaid = jsonSell["total"]["amount"]
            sell.TotalCurrency = jsonSell["total"]["amount"]
            sell.Subtotal = jsonSell["subtotal"]["amount"]

            self.Sells.append(sell)

        return self.Sells
