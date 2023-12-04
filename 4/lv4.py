from algosdk.v2client import algod,indexer
from algosdk import account, mnemonic
from algosdk import util,transaction,error
from beaker import client, sandbox
API_KEY="LFIoc7BZFY4CAAHfCC2at53vp5ZabBio5gAQ0ntL"

algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": API_KEY,
}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)


user_pub = "SVJOCGUG3ESR2Y3PQ4P4HLKKYOZZN422CVJ7ZYY3DBZ324VRP6BZ5Y55CA"
user_private = mnemonic.to_private_key("alpha road wedding gallery explain fabric setup recycle rotate spike neck cruel author share green welcome mandate earn time roof talent alcohol frequent abandon kid")



opt_in_txn = transaction.ApplicationOptInTxn(user_pub, algod_client.suggested_params(), 487250596,foreign_apps=[487250503,491015132])
signed_opt_in = opt_in_txn.sign(user_private)
txid = algod_client.send_transaction(signed_opt_in)
optin_result = transaction.wait_for_confirmation(algod_client, txid, 4)
print(txid)
print(optin_result)