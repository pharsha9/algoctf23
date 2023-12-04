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


sug = algod_client.suggested_params()
sug.fee = 0
sug.flat_fee = True

sug2 = algod_client.suggested_params()
sug2.fee = 2*1000
sug2.flat_fee = True

opt_in_txn = transaction.ApplicationOptInTxn(user_pub, sug, 487250445,foreign_apps=[487250388])
paymnt_txn = transaction.PaymentTxn(user_pub,sug2,"QDCPGXSWY5FQWTSARZIT2CCDJXASCN5TBGN6VUGQVPDEMF4ZT63IZD7NWM",util.algos_to_microalgos(1.0))

transaction.assign_group_id([opt_in_txn,paymnt_txn])

sopt_in_txn = opt_in_txn.sign(user_private)
spaymnt_txn = paymnt_txn.sign(user_private)

signed_group = [sopt_in_txn,spaymnt_txn]

tx_id = algod_client.send_transactions(signed_group)

result = transaction.wait_for_confirmation(
    algod_client, tx_id, 4
)
print(f"txID: {tx_id}\nresult: {result}")