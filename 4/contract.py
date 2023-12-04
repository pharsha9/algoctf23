import beaker
import pyteal as pt
from beaker.decorators import Authorize

class MyAppState:

    access = beaker.GlobalStateValue(
        stack_type=pt.TealType.bytes
    )


app = beaker.Application('Level4', state=MyAppState())


@app.external
def set_access(*,output:pt.abi.String):
    return pt.Seq(
        app.state.access.set(pt.Txn.sender()),
        output.set(pt.Bytes("Set"))
    )

# Rest of the code...
if __name__ == '__main__':
    spec = app.build()
    spec.export('artifacts')