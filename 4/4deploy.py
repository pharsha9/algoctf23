import base64
from algosdk.v2client import algod,indexer
from algosdk import account, mnemonic
from algosdk import util,transaction,error
import json,base64
from beaker import client, sandbox, consts
import contract
API_KEY="LFIoc7BZFY4CAAHfCC2at53vp5ZabBio5gAQ0ntL"

def create_application():
    algod_address = "https://testnet-algorand.api.purestake.io/ps2"
    algod_token = ""
    headers = {
        "X-API-Key": API_KEY,
    }
    sender="HVRMH4TKDOYEYHLZE42SMGSY7F3F2MWFBCRMVBXWFQJQMOL5PBDXNESA3M"
    mnemoni="joy luxury trophy below slim camp rug prevent first man velvet coral license spy tourist away humble crack twice city daring virus power ability damage"
    private_key = mnemonic.to_private_key(mnemoni)

    with open("artifacts/approval.teal", "r") as f:
        approval_program = f.read()

    with open("artifacts/clear.teal", "r") as f:
        clear_program = f.read()

    acct=sandbox.SandboxAccount(address=sender,private_key=private_key)
    algod_client = algod.AlgodClient(algod_token, algod_address, headers)
    app_client = client.ApplicationClient(
        algod_client, contract.app, signer=acct.signer
    )

    app_id, app_address, _ = app_client.create()
    res = app_client.call(contract.set_access,acct.address)
    print(res)
    print(f"Deployed Application ID: {app_id} Address: {app_address}")


create_application()