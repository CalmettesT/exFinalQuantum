import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

def ising_model_1d(n, steps):
    # Étape 1 : Création des registres quantiques et du circuit
    qr = QuantumRegister(n, 'q')
    cr = ClassicalRegister(n, 'c')
    qc = QuantumCircuit(qr, cr)

    # Étape 2 : Préparation de l'état initial
    for qubit in range(n):
        qc.h(qubit)

    # Étape 3 : Simulation des interactions du modèle d'Ising
    for step in range(steps):
        # Appliquer une porte CNOT entre chaque paire de qubits voisins
        for qubit in range(n - 1):
            qc.cx(qubit, qubit + 1)
        # Appliquer une rotation Rz sur chaque qubit
        for qubit in range(n):
            qc.rz(np.pi / 4, qubit)  # exemple de rotation

    # Étape 4 : Mesurer les qubits
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

# Demander les entrées à l'utilisateur
n = int(input("Entrez le nombre de qubits (n) : ").strip())
steps = int(input("Entrez le nombre de steps : ").strip())

# Exécuter la simulation
ising_model_1d(n, steps)
