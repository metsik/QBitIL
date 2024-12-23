from classiq import *


@qfunc
def main(cntrl: Output[QArray[QBit]], target: Output[QBit]) -> None:
    allocate(5, cntrl)
    allocate(1, target)
    hadamard_transform(cntrl)
    control(ctrl=cntrl, stmt_block=lambda: X(target))

qmodForEx1 = create_model(main)

#optimize by width
constrainedqmodForEx1ByWidth = set_constraints(qmodForEx1, Constraints(optimization_parameter = "width"))

quantum_programWidth = synthesize(constrainedqmodForEx1ByWidth)
show(quantum_programWidth)


#optimize by depth

constrainedqmodForEx1ByDepth = set_constraints(qmodForEx1, Constraints(optimization_parameter = "depth"))

quantum_programDepth = synthesize(constrainedqmodForEx1ByDepth)
show(quantum_programDepth)

#optimize in between

constrainedqmodForEx1ByDepth = set_constraints(qmodForEx1, Constraints(optimization_parameter = "depth", max_width=7))

quantum_programDepth = synthesize(constrainedqmodForEx1ByDepth)
show(quantum_programDepth)
