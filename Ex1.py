from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit import transpile, assemble

def execute_bell_state():
    # Créez les registres quantique et classique
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, cr)

    # Demandez à l'utilisateur quel état de Bell afficher
    state = input("Choisissez l'état de Bell à afficher (phi+, phi-, psi+, psi-): ").strip().lower()

    # Créez état de Bell selon le choix de l'utilisateur
    if state == 'phi+':
        qc.h(qr[0])
        qc.cx(qr[0], qr[1])
    elif state == 'phi-':
        qc.h(qr[0])
        qc.cx(qr[0], qr[1])
        qc.z(qr[0])
    elif state == 'psi+':
        qc.h(qr[0])
        qc.cx(qr[0], qr[1])
        qc.x(qr[1])
    elif state == 'psi-':
        qc.h(qr[0])
        qc.cx(qr[0], qr[1])
        qc.z(qr[0])
        qc.x(qr[1])
    else:
        print("État non reconnu. Veuillez choisir parmi 'phi+', 'phi-', 'psi+' ou 'psi-'.")
        return

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
execute_bell_state()