from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble
import numpy as np

# Fonction pour appliquer une porte de phase contrôlée
def apply_controlled_phase(qc, control, target, k):
    qc.cp(2 * np.pi / 2**k, control, target)

# Créez les registres quantique et classique
qr = QuantumRegister(3, 'q')
cr = ClassicalRegister(3, 'c')
qc = QuantumCircuit(qr, cr)

# Appliquez les portes nécessaires pour la transformation de Fourier quantique
# Qubit 2
qc.h(qr[2])
apply_controlled_phase(qc, qr[1], qr[2], 2)
apply_controlled_phase(qc, qr[0], qr[2], 3)

# Qubit 1
qc.h(qr[1])
apply_controlled_phase(qc, qr[0], qr[1], 2)

# Qubit 0
qc.h(qr[0])

# Ajoutez les mesures
qc.measure(qr, cr)

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
