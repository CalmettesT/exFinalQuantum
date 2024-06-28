from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

def codage_bits_classiques():
    # Créez les registres quantique et classique
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, cr)

    # Créez un état de Bell entre qr[0] et qr[1]
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])

    # Demandez à l'utilisateur de choisir les bits à envoyer (00, 01, 10, 11)
    bits = input("Choisissez les bits à envoyer parmi les combinaisons possibles (00, 01, 10, 11): ").strip()

    # Appliquez les portes X et Z en fonction des bits choisis
    if bits == '00':
        pass  # Aucune porte
    elif bits == '01':
        qc.z(qr[0])
    elif bits == '10':
        qc.x(qr[0])
    elif bits == '11':
        qc.z(qr[0])
        qc.x(qr[0])
    else:
        print("Combinaison non reconnue. Veuillez choisir parmi '00', '01', '10' ou '11'.")
        return

    # Ajoutez les portes supplémentaires selon les instructions initiales
    qc.cx(qr[0], qr[1])
    qc.h(qr[0])

    # Mesure des qubits qr[0] et qr[1]
    qc.measure(qr[0], cr[0])
    qc.measure(qr[1], cr[1])

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

# Exécutez la fonction
codage_bits_classiques()
