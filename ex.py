from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')  # 3 qubits pour l'encodage et la téléportation
cr = ClassicalRegister(3, 'c')  # 3 bits classiques pour stocker les résultats de mesure
qc = QuantumCircuit(qr, cr)

# Message à encoder (par exemple, 01)
message = [0, 1]

# Préparation de l'état du message à encoder
if message[0] == 1:
    qc.x(qr[0])
if message[1] == 1:
    qc.x(qr[1])

# Créez une paire EPR (état de Bell) entre qr[1] et qr[2]
qc.h(qr[1])
qc.cx(qr[1], qr[2])

# Téléportation quantique du message de qr[0] vers qr[2]
qc.cx(qr[0], qr[1])
qc.h(qr[0])

# Mesure des qubits qr[0] et qr[1]
qc.measure(qr[0], cr[0])
qc.measure(qr[1], cr[1])

# Applique des corrections basées sur les mesures
qc.cx(qr[1], qr[2])
qc.cz(qr[0], qr[2])

# Mesure le qubit de destination
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
