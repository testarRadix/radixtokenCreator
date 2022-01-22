import json
import requests

payload =  json.dumps({
    "method": "construction.finalize_transaction",
    "params": {
        "blob": "fill with blob that we get from step 1",
        "signatureDER": "fill with signatured code",
        "publicKeyOfSigner": "fill with your public key address",
        "immediateSubmit":"true"
    },
    "id": 0
}) 
headers = {"Content-Type": "application/json"}
url = "https://mainnet.radixdlt.com/construction" 

response = requests.request("POST", url, headers=header, data=payload)

# this will show information e.g TXID
response.text
