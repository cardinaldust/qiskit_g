from qiskit import QuantumCircuit, transpile, assemble, Aer, execute

circuit = QuantumCircuit(2)

circuit.h(0)

wnumber = 0

qchoice = 0

def entanglement():
    global wnumber
    global qchoice

    circuit.cx(0, 1)

    circuit.measure_all()

    simulator = Aer.get_backend('qasm_simulator')

    job = execute(circuit, simulator, shots=1)

    result = job.result()

    count = result.get_counts()

    print(count)

    for key in count.keys():
        print(key, type(key))
        wnumber = int(key[0])
        qchoice = int(key[0])

    




i = int(input('Chose a number between 0 and 1: '))

entanglement()

print('The number: ', wnumber, 'Quantum Computer choice: ', qchoice, 'Your choice: ', i)