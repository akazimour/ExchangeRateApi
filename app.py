import time
from libs.openexchange import OpenExchangeClient


API_ID = "39b73bb1a8964d1b94235d815e708388"
client = OpenExchangeClient(API_ID)
usd_amount = 1000

start = time.time()
gbp_amount=client.convert(usd_amount,"USD", "GBP")
end = time.time()
print(end - start)
print(f"USD {usd_amount} is equal with GBP {gbp_amount:.2f}")

start = time.time()
gbp_amount=client.convert(usd_amount,"USD", "GBP")
end = time.time()
print(f"USD {usd_amount} is equal with GBP {gbp_amount:.2f}")
print(end - start)

start = time.time()
gbp_amount=client.convert(usd_amount,"USD", "GBP")
end = time.time()
print(f"USD {usd_amount} is equal with GBP {gbp_amount:.2f}")
print(end - start)


