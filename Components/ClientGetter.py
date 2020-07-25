from coinbase.wallet.client import Client
import os
from dotenv import load_dotenv

class ClientGetter():
	def __init__(self, api_key, secret_key):
		self.api_key = api_key
		self.secret_key = secret_key

	def GetClient(self):
		client = Client(self.api_key, self.secret_key)
		return client

load_dotenv()
CoinbaseClient = ClientGetter(os.getenv("API_KEY"), os.getenv("API_SECRET")).GetClient()
ProClient = ClientGetter(os.getenv("PRO_API_KEY"), os.getenv("PRO_SECRET")).GetClient()