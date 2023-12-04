from algosdk.v2client import algod,indexer
from algosdk import account, mnemonic
from algosdk import util,transaction,error
from beaker import client, sandbox
import pyteal as pt
API_KEY="LFIoc7BZFY4CAAHfCC2at53vp5ZabBio5gAQ0ntL"

algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": API_KEY,
}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)


user_pub = "HVRMH4TKDOYEYHLZE42SMGSY7F3F2MWFBCRMVBXWFQJQMOL5PBDXNESA3M"
user_private = mnemonic.to_private_key("joy luxury trophy below slim camp rug prevent first man velvet coral license spy tourist away humble crack twice city daring virus power ability damage")

sug = algod_client.suggested_params()
sug.fee = 2*1000
sug.flat_fee = True

opt_in_txn = transaction.ApplicationOptInTxn(user_pub, sug, 487251018,foreign_apps=[487250808,491024108])
signed_opt_in = opt_in_txn.sign(user_private)
txid = algod_client.send_transaction(signed_opt_in)
optin_result = transaction.wait_for_confirmation(algod_client, txid, 4)
print(txid)
print(optin_result)