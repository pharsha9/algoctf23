import beaker
import pyteal as pt
from beaker.decorators import Authorize


app = beaker.Application('Level6')


@app.external
def sum(one:pt.abi.Uint64,two:pt.abi.Uint64,*,output:pt.abi.Uint64):
    return pt.Seq(
        output.set(pt.Add(one.get(),two.get()))
    )

# Rest of the code...
if __name__ == '__main__':
    spec = app.build()
    spec.export('artifacts')