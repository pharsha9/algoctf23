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


user_pub = "HVRMH4TKDOYEYHLZE42SMGSY7F3F2MWFBCRMVBXWFQJQMOL5PBDXNESA3M"
user_private = mnemonic.to_private_key("joy luxury trophy below slim camp rug prevent first man velvet coral license spy tourist away humble crack twice city daring virus power ability damage")



opt_in_txn = transaction.ApplicationOptInTxn(user_pub, algod_client.suggested_params(), 487250388,foreign_apps=[487250303])
paymnt_txn = transaction.PaymentTxn(user_pub,algod_client.suggested_params(),"4XPWWMNZSHAWRM4CHWP6XBGAEZG3KHN742XXQGF2I4DATDYUIPECMDC2KE",util.algos_to_microalgos(1.0))

transaction.assign_group_id([paymnt_txn,opt_in_txn])

sopt_in_txn = opt_in_txn.sign(user_private)
spaymnt_txn = paymnt_txn.sign(user_private)

signed_group = [spaymnt_txn,sopt_in_txn]

tx_id = algod_client.send_transactions(signed_group)

result = transaction.wait_for_confirmation(
    algod_client, tx_id, 4
)
print(f"txID: {tx_id}\nresult: {result}")