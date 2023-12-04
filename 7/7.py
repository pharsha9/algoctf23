from algosdk.v2client import algod,indexer
from algosdk import account, mnemonic
from algosdk import util,transaction,error
from beaker import client, sandbox
import pyteal as pt
import contract
API_KEY="LFIoc7BZFY4CAAHfCC2at53vp5ZabBio5gAQ0ntL"

algod_address = "https://testnet-algorand.api.purestake.io/ps2"
algod_token = ""
headers = {
    "X-API-Key": API_KEY,
}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)


user_pub = "HVRMH4TKDOYEYHLZE42SMGSY7F3F2MWFBCRMVBXWFQJQMOL5PBDXNESA3M"
user_private = mnemonic.to_private_key("joy luxury trophy below slim camp rug prevent first man velvet coral license spy tourist away humble crack twice city daring virus power ability damage")

acct=sandbox.SandboxAccount(address=user_pub,private_key=user_private)
app_client = client.ApplicationClient(
        algod_client, contract.app, signer=acct.signer
    )


autorize_txn = transaction.ApplicationCallTxn(user_pub,algod_client.suggested_params(),491028995,on_complete=transaction.OnComplete.NoOpOC,app_args=["HG".encode("utf-8")],foreign_apps=[487251193])
opt_in_txn = transaction.ApplicationOptInTxn(user_pub, algod_client.suggested_params(), 487251193,foreign_apps=[487251018])

# txid=algod_client.send_transaction(signed_autorize_txn)
# autorize_result = transaction.wait_for_confirmation(algod_client, txid, 4)
# print(txid)
# print(autorize_result)


transaction.assign_group_id([autorize_txn,opt_in_txn])


signed_autorize_txn = autorize_txn.sign(user_private)
signed_opt_in = opt_in_txn.sign(user_private)


signed_group = [signed_autorize_txn,signed_opt_in]

tx_id = algod_client.send_transactions(signed_group)

result = transaction.wait_for_confirmation(
    algod_client, tx_id, 4
)
print(f"txID: {tx_id}\nresult: {result}")

# txid = algod_client.send_transaction(signed_opt_in)
# optin_result = transaction.wait_for_confirmation(algod_client, txid, 4)
# print(txid)
# print(optin_result)