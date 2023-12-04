import beaker
import pyteal as pt
from beaker.decorators import Authorize


app = beaker.Application('Level7')


@app.external
def complete(*,output:pt.abi.String):
    return pt.Seq(
        pt.InnerTxnBuilder.Begin(),
        pt.InnerTxnBuilder.SetFields(
            {
                pt.TxnField.application_args : [
                        pt.MethodSignature("authorize(address)void"),
                        pt.Txn.sender()
                    ],
                pt.TxnField.type_enum: pt.TxnType.ApplicationCall,
                pt.TxnField.application_id: pt.Int(487251193),
                pt.TxnField.on_completion: pt.OnComplete.NoOp,
            }
        ),
        pt.InnerTxnBuilder.Submit(),
        output.set(pt.Bytes("completed"))
    )
    

# Rest of the code...
if __name__ == '__main__':
    spec = app.build()
    spec.export('artifacts')