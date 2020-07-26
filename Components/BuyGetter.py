from AccountComponents.Buy import Buy


class BuyGetter:
    def __init__(self, accountId):
        self.AccountId = accountId
        self.Buys = []

    def GetBuys(self):
        jsonBuys = json.loads(json.dumps(CoinbaseClient.get_buys(self.AccountId)))

        for jsonBuy in jsonBuys["data"]:
            buy = Buy()

            if jsonBuy["status"] != "completed":
                continue
            buy.BuyId = jsonBuy["id"]
            buy.Amount = jsonBuy["amount"]["amount"]
            buy.AmountCurrency = jsonBuy["amount"]["currency"]
            buy.TotalPaid = jsonBuy["total"]["amount"]
            buy.TotalCurrency = jsonBuy["total"]["amount"]
            buy.Subtotal = jsonBuy["subtotal"]["amount"]

            self.Buys.append(buy)

        return self.Buys
