from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, cr)

# Préparez les qubits en superposition
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])

# Implémentez l'oracle
#qc.z(qr[0])
qc.z(qr[1])
qc.z(qr[2])

# Appliquez l'étape de diffusion
qc.h(qr[0])
qc.h(qr[1])
qc.h(qr[2])


# Ajoutez les mesures
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])
qc.measure(qr[2], cr[2])

# Transpilez et assemblez le circuit pour le simulateur
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)

# Exécutez le circuit
job = simulator.run(qobj)
result = job.result()

# Affichez les résultats
counts = result.get_counts(qc)
print("Résultats de la mesure :", counts)