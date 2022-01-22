payload =  json.dumps({
  "method": "construction.build_transaction",
  "params": {
    "actions": [
      {
        "type": "CreateFixedSupplyToken",
        "to": "fill with your address",
        "publicKeyOfSigner": "fill with your public key address",
        "symbol": "your token's symbol e.g RDX",
        "name": "your token's name e.g radix",
        "description": "your token's desciption",
        "iconUrl": "your token's icon url",
        "tokenUrl": "your token's website",
        "supply": "your token's supply eg '1000000000000000000' for '1' (you have to add 18 additional zeros)"
      }
    ],
    "feePayer": "fill with address who will pay gas fee"
  },
  "id": 0
}) 
headers = {"Content-Type": "application/json"}
url = "https://mainnet.radixdlt.com/construction" 

response = requests.request("POST", url, headers=header, data=payload)

response.text
