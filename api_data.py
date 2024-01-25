import time
from libs.openexchange import OpenExchangeClient

APP_ID = "d3f8f1713f8f47058623feeda02c90d6"

client = OpenExchangeClient(APP_ID)

usd_amount = 1000
gbp_amount = client.convert(usd_amount, "USD", "GBP")

print(f"USD{usd_amount} is GBP{gbp_amount:.2f}")
