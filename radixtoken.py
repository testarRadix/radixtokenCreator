from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from mnemonic import Mnemonic
from hdwallet import HDWallet
import bech32
from ecdsa.util import sigencode_der
import ecdsa
import json
import requests

# Password used when creating wallet
password = ""

# Key Derivation Function (kdf) parameters from wallet.json
salt = ""

lengthOfDerivedKey =32
blockSize = 8
parallelizationParameter = 1
costParameterN = 8192

# Derive AES Symmetrical Key using Scrypt
symmetrical_key = scrypt( \
                            password, \
                            bytearray.fromhex(salt), \
                            key_len=lengthOfDerivedKey, \
                            N=costParameterN, \
                            r=blockSize, \
                            p=parallelizationParameter \
                         )

print("Symetrical Key:", symmetrical_key.hex())

# Decrypt Ciphertext into Entropy using Symmetrical Key
# Use Mac to verify decryption is correct for provided parameters

# Crypto parameters from wallet.json
ciphertext = ""
nonce = ""
mac = ""

cipher = AES.new(symmetrical_key, AES.MODE_GCM, nonce=bytearray.fromhex(nonce))

entropy = cipher.decrypt_and_verify(bytearray.fromhex(ciphertext), bytearray.fromhex(mac))
print("Entropy:", entropy.hex())

# Derive Mnemonic words from Entropy
mnemo = Mnemonic("english")
words = mnemo.to_mnemonic(entropy)
print("Words:", words)

# Use Mnemonic words to derive Wallet Seed
password=""

seed = Mnemonic.to_seed(words, passphrase=password)
print("Seed:", seed.hex())

# Generate Wallet Keys and Addresses from Seed using Derivation Paths
purpose = 44
coinType = 1022
account = 0
change = 0

# Increment this for every new wallet
addressIndex = 0

hdwallet = HDWallet()
hdwallet.from_seed(seed=seed.hex())

hdwallet.from_index(purpose, hardened=True)
hdwallet.from_index(coinType, hardened=True)
hdwallet.from_index(account, hardened=True)
hdwallet.from_index(change)
hdwallet.from_index(addressIndex, hardened=True)

print("Derivation Path:", hdwallet.path())
print("Private Key:", hdwallet.private_key())
print("Public Key:", hdwallet.public_key())

# Derivation Path: m/44'/1022'/0'/0/0'
# Private Key: 320018f5ebf4730e5dfff4af7d41afb3dc7323523af9cb3b5875ee1eabf405c8
# Public Key: 03094afd7e5a5d0891518a20e5a232edfc0862308865c7cd0c91645527f34b13a1

# Add 04 byte to beginning of public key to create a Radix Engine Address
readdr = b"\x04" + bytearray.fromhex(hdwallet.public_key())

# Bech32 encode the Radix Engine Address with an HRP of "rdx" for Mainnet
readdr_bytes5 = bech32.convertbits(readdr, 8, 5)
wallet_addr = bech32.bech32_encode("rdx", readdr_bytes5)

print("Wallet Address: ", wallet_addr)

# Wallet Address: rdx1qspsjjha0ed96zy32x9zpedzxtklczrzxzyxt37dpjgkg4f87d938gg2x9nn8

# sign 
# sk = ecdsa.SigningKey.from_string(bytearray.fromhex(hdwallet.private_key()), curve=ecdsa.SECP256k1)
# signature = sk.sign_digest(bytes.fromhex('hastosign'), sigencode=sigencode_der).hex()