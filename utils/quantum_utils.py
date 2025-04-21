import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_bloch_multivector, plot_histogram
from qiskit.quantum_info import Statevector
import streamlit as st

def create_bell_state():
    """
    Creates a Bell state (maximally entangled state of two qubits)
    """
    qc = QuantumCircuit(2)
    qc.h(0)  # Apply Hadamard gate to the first qubit
    qc.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
    
    return qc

def simulate_circuit(circuit, shots=1024, get_statevector=False):
    """
    Simulates a quantum circuit and returns the results
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to simulate
        shots (int): Number of simulation shots
        get_statevector (bool): Whether to return the statevector
        
    Returns:
        dict: Simulation results
    """
    if get_statevector:
        simulator = Aer.get_backend('statevector_simulator')
        result = execute(circuit, simulator).result()
        statevector = result.get_statevector(circuit)
        return statevector
    else:
        simulator = Aer.get_backend('qasm_simulator')
        circuit.measure_all()
        result = execute(circuit, simulator, shots=shots).result()
        counts = result.get_counts(circuit)
        return counts

def plot_quantum_state(state, title="Quantum State"):
    """
    Plots the visualization of a quantum state
    
    Args:
        state: Quantum state (statevector or density matrix)
        title (str): Title for the visualization
        
    Returns:
        matplotlib.figure.Figure: The figure containing the visualization
    """
    fig = plt.figure(figsize=(8, 6))
    plot_bloch_multivector(state, title=title, figsize=(8, 6))
    return fig

def plot_measurement_results(counts):
    """
    Plots the measurement results from a quantum circuit simulation
    
    Args:
        counts (dict): Measurement counts from circuit execution
        
    Returns:
        matplotlib.figure.Figure: The figure containing the histogram
    """
    fig = plt.figure(figsize=(10, 6))
    plot_histogram(counts, figsize=(10, 6))
    plt.title("Measurement Results")
    return fig

def bloch_sphere_visualization(theta, phi):
    """
    Creates a Bloch sphere visualization of a qubit state
    
    Args:
        theta (float): Theta angle (rotation from Z-axis)
        phi (float): Phi angle (rotation around Z-axis)
        
    Returns:
        matplotlib.figure.Figure: The figure containing the Bloch sphere
    """
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw the Bloch sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x = np.sin(v) * np.cos(u)
    y = np.sin(v) * np.sin(u)
    z = np.cos(v)
    ax.plot_wireframe(x, y, z, color="gray", alpha=0.2)
    
    # Draw the axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1, label='X')
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1, label='Y')
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1, label='Z')
    
    # Draw the qubit state vector
    x_q = np.sin(theta) * np.cos(phi)
    y_q = np.sin(theta) * np.sin(phi)
    z_q = np.cos(theta)
    ax.quiver(0, 0, 0, x_q, y_q, z_q, color='purple', arrow_length_ratio=0.1, label='State')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere Representation of a Qubit')
    ax.legend()
    
    # Set the limits of the plot
    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])
    
    return fig

def create_ghz_state(num_qubits=3):
    """
    Creates a GHZ state (maximally entangled state of multiple qubits)
    
    Args:
        num_qubits (int): Number of qubits in the GHZ state
        
    Returns:
        QuantumCircuit: The circuit that creates the GHZ state
    """
    qc = QuantumCircuit(num_qubits)
    
    # Apply Hadamard to the first qubit
    qc.h(0)
    
    # Apply CNOT gates to entangle all qubits
    for i in range(1, num_qubits):
        qc.cx(0, i)
    
    return qc

def create_quantum_teleportation_circuit():
    """
    Creates a quantum teleportation circuit
    
    Returns:
        QuantumCircuit: The circuit for quantum teleportation
    """
    qc = QuantumCircuit(3, 2)
    
    # Create the state to teleport on qubit 0
    qc.h(0)  # Create superposition - can be changed to arbitrary state
    
    # Create entangled pair between qubits 1 and 2
    qc.h(1)
    qc.cx(1, 2)
    
    # Bell measurement on qubits 0 and 1
    qc.cx(0, 1)
    qc.h(0)
    
    # Measure qubits 0 and 1
    qc.measure([0, 1], [0, 1])
    
    # Conditional operations on qubit 2 (represented classically here)
    with qc.if_test((0, 1)):
        qc.x(2)
    with qc.if_test((1, 1)):
        qc.z(2)
    
    return qc

def visualize_quantum_fourier_transform(n_qubits=3):
    """
    Creates and visualizes a Quantum Fourier Transform circuit
    
    Args:
        n_qubits (int): Number of qubits
        
    Returns:
        QuantumCircuit: The QFT circuit
    """
    qc = QuantumCircuit(n_qubits)
    
    # Apply Hadamard gates to all qubits
    for qubit in range(n_qubits):
        qc.h(qubit)
        
        # Apply controlled phase rotations
        for target_qubit in range(qubit + 1, n_qubits):
            qc.cp(np.pi/float(2**(target_qubit-qubit)), qubit, target_qubit)
    
    # Swap qubits
    for qubit in range(n_qubits//2):
        qc.swap(qubit, n_qubits-qubit-1)
    
    return qc
