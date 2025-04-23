from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Create a quantum circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Get simulator backend
simulator = Aer.get_backend('qasm_simulator')

# Execute circuit
job = simulator.run(qc, shots=1000)
result = job.result()
counts = result.get_counts(qc)
print("Counts:", counts)

print("\nMethod for running circuits:")
print(f"simulator.run method: {simulator.run}")