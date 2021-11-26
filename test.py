from kucoin.client import Client as ClientKucoin
import asyncio
import threading

api_key = '619d3516a198580001b81a36'
api_secret = '726efe1d-127c-4b20-948f-4553c176fcc7'
api_passphrase = 'allora_adesso_scopo'

clientkucoin = ClientKucoin(api_key, api_secret, api_passphrase)
indexes=0
valid=[]
threads=[]
def req_async(symbol):
    volume = float(clientkucoin.get_24hr_stats(symbol)['volValue'])
    if volume < 100000:
        valid.append(symbol)

for x in clientkucoin.get_symbols():

    if x['symbol'].endswith("USDT") and x['isMarginEnabled']==False and "3S" not in x['symbol'] and "3L" not in x['symbol']:
        print(x)
        req_async(x['symbol'])

        indexes+=1


validindex=0
for s in valid:
    print(s)
    validindex+=1
print(indexes," ",validindex)