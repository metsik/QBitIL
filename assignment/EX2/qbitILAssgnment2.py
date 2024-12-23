from classiq import *


@qfunc
def main(cntrl: Output[QArray[QBit]], target: Output[QBit]) -> None:
    allocate(20, cntrl)
    allocate(1, target)
    hadamard_transform(cntrl)
    control(ctrl=cntrl, stmt_block=lambda: X(target))

qmodForEx1 = create_model(main)

quantum_programWidth = synthesize(qmodForEx1)
show(quantum_programWidth)

