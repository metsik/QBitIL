from classiq import *
import numpy as np
import matplotlib.pyplot as plt


@qfunc
def main(cntrl: Output[QArray[QBit]], target: Output[QBit]) -> None:
    allocate(20, cntrl)
    allocate(1, target)
    hadamard_transform(cntrl)
    control(ctrl=cntrl, stmt_block=lambda: X(target))


width = np.zeros(31-22, dtype=int)
depth = np.zeros(31-22, dtype=int)

widthtranspiled = np.zeros(31-22, dtype=int)
depthtranspiled = np.zeros(31-22, dtype=int)

for implementationNum, implementationWidth in enumerate(range(22,31)):
    qmodForEx3 = create_model(main)

    constrainedqmodForEx3ByDepth = set_constraints(qmodForEx3, Constraints(optimization_parameter="depth", max_width=implementationWidth))

    quantum_program = synthesize(constrainedqmodForEx3ByDepth)


    # Save width and depth
    width[implementationNum] = int(QuantumProgram.from_qprog(quantum_program).data.width)
    depth[implementationNum] = int(QuantumProgram.from_qprog(quantum_program).transpiled_circuit.depth)
    # show(quantum_program)
    print(f"width={implementationWidth}, depth={depth[implementationNum]}")

# Plot
plt.plot(width, depth, marker='x', linestyle='-', color='r', label="Traspiled Depth")
plt.xlabel("Width")
plt.ylabel("Depth")
plt.title("transpiled implementation")
plt.show(block=True)






    