import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

def quantum_circuit_with_n_qubits(n, bitstring):
    # Étape 1 : Création des registres quantiques et du circuit
    qr = QuantumRegister(n, 'q')
    cr = ClassicalRegister(n, 'c')
    qc = QuantumCircuit(qr, cr)

    # Étape 2 : Préparez les qubits en superposition
    for qubit in range(n):
        qc.h(qubit)

    # Étape 3 : Implémentez l'oracle en appliquant Z selon le bitstring
    for qubit in range(n):
        if bitstring[qubit] == '1':
            qc.z(qubit)

    # Étape 4 : Appliquez l'étape de diffusion
    for qubit in range(n):
        qc.h(qubit)

    # Ajoutez les mesures
    for qubit in range(n):
        qc.measure(qr[qubit], cr[qubit])

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

# Demander le nombre de qubits à l'utilisateur
n = int(input("Entrez le nombre de qubits (n) : ").strip())

# Demander la configuration des qubits à l'utilisateur
bitstring = input(f"Entrez la configuration des {n} qubits (par exemple, '1101' pour 4 qubits) : ").strip()

# Vérification de la validité du bitstring
if len(bitstring) != n or any(bit not in '01' for bit in bitstring):
    raise ValueError("Le bitstring doit avoir exactement n caractères et contenir uniquement des '0' et des '1'.")

# Exécuter la simulation
quantum_circuit_with_n_qubits(n, bitstring)
