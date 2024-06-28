import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector
from matplotlib import pyplot as plt

# Créez les registres quantique et classique
qr = QuantumRegister(1, 'q')
cr = ClassicalRegister(1, 'c')
qc = QuantumCircuit(qr, cr)

def prepare_arbitrary_state(a, b):
    """
    Prépare un qubit dans l'état a|0> + b|1>.
    a et b doivent être des nombres complexes.
    """
    # Normaliser les coefficients
    norm = np.sqrt(np.abs(a)**2 + np.abs(b)**2)
    a = a / norm
    b = b / norm

    # Calcul des angles de rotation
    theta = 2 * np.arccos(np.abs(a))
    phi = np.angle(b) - np.angle(a)

    # Application des rotations nécessaires
    qc.ry(theta, 0)
    qc.rz(phi, 0)

def choixPorte():
    # Demande à l'utilisateur d'entrer les coefficients a et b
    a_real = float(input("Entrez la partie réelle de a: ").strip())
    a_imag = float(input("Entrez la partie imaginaire de a: ").strip())
    b_real = float(input("Entrez la partie réelle de b: ").strip())
    b_imag = float(input("Entrez la partie imaginaire de b: ").strip())

    # Convertir les entrées en nombres complexes
    a = complex(a_real, a_imag)
    b = complex(b_real, b_imag)

    # Prépare l'état arbitraire avec les coefficients donnés
    prepare_arbitrary_state(a, b)

    # Demande à l'utilisateur de choisir la porte à appliquer
    name = input("Choisissez la porte à utiliser parmi ces portes ('H', 'X', 'Y', 'Z' ou 'rien'): ").strip()

    if name == 'H':
        qc.h(qr[0])
    elif name == 'rien':
        pass
    elif name == 'X':
        qc.x(qr[0])
    elif name == 'Y':
        qc.y(qr[0])
    elif name == 'Z':
        qc.z(qr[0])
    else:
        print("Combinaison non reconnue. Veuillez choisir parmi 'H', 'X', 'Y', 'Z' ou 'rien'.")
        return

choixPorte()

# Obtenir l'état après l'opération
state = Statevector.from_instruction(qc)
plot_bloch_multivector(state)
plt.title(f"État après application de la porte")
plt.show()
