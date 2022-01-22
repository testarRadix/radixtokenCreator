import edcsa
from ecdsa.util import sigencode_der

# sign 
# dont delete the quote (')
sk = ecdsa.SigningKey.from_string(bytearray.fromhex('your private key'), curve=ecdsa.SECP256k1)
# this command will show signatured code that we will use at step 3
print(sk.sign_digest(bytes.fromhex('blobhastosign'), sigencode=sigencode_der).hex())
