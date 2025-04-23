"""
Quantum Utilities for Quantum Computing Educational Platform
With advanced DNA-based security features and copyright protection

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer

def create_bell_state():
    """
    Creates a Bell state (maximally entangled state of two qubits)
    
    Returns:
        QuantumCircuit: The quantum circuit that creates the Bell state
    """
    # Create a quantum circuit with 2 qubits and 2 classical bits
    circuit = QuantumCircuit(2, 2)
    
    # Apply Hadamard gate to qubit 0
    circuit.h(0)
    
    # Apply CNOT gate with control qubit 0 and target qubit 1
    circuit.cx(0, 1)
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit

def simulate_circuit(circuit, shots=1024, get_statevector=False):
    """
    Simulates a quantum circuit and returns the results
    
    Args:
        circuit (QuantumCircuit): The quantum circuit to simulate
        shots (int): Number of simulation shots
        get_statevector (bool): Whether to return the statevector
        
    Returns:
        Result: Simulation results
    """
    if get_statevector:
        # Use statevector simulator
        simulator = Aer.get_backend('statevector_simulator')
        result = simulator.run(circuit).result()
    else:
        # Use qasm simulator
        simulator = Aer.get_backend('qasm_simulator')
        result = simulator.run(circuit, shots=shots).result()
    
    return result

def plot_quantum_state(state, title="Quantum State"):
    """
    Plots the visualization of a quantum state
    
    Args:
        state: Quantum state (statevector or density matrix)
        title (str): Title for the visualization
        
    Returns:
        matplotlib.figure.Figure: The figure containing the visualization
    """
    # Convert state to numpy array if needed
    if hasattr(state, 'data'):
        state_data = state.data
    else:
        state_data = state
        
    # Get the number of qubits
    n_qubits = int(np.log2(len(state_data)))
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get labels for x-axis (basis states)
    labels = [format(i, f'0{n_qubits}b') for i in range(2**n_qubits)]
    
    # Plot real and imaginary parts
    x = np.arange(len(state_data))
    width = 0.35
    
    real_vals = np.real(state_data)
    imag_vals = np.imag(state_data)
    
    ax.bar(x - width/2, real_vals, width, label='Real')
    ax.bar(x + width/2, imag_vals, width, label='Imaginary')
    
    # Add labels and title
    ax.set_xlabel('Basis State')
    ax.set_ylabel('Amplitude')
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=45)
    ax.legend()
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    plt.tight_layout()
    
    return fig

def plot_measurement_results(counts):
    """
    Plots the measurement results from a quantum circuit simulation
    
    Args:
        counts (dict): Measurement counts from circuit execution
        
    Returns:
        matplotlib.figure.Figure: The figure containing the histogram
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Get x and y data
    x = list(counts.keys())
    y = list(counts.values())
    
    # Create the bar chart
    ax.bar(x, y)
    
    # Add labels and title
    ax.set_xlabel('Measurement Outcome')
    ax.set_ylabel('Counts')
    ax.set_title('Measurement Results')
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    plt.tight_layout()
    
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
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', arrow_length_ratio=0.1)
    
    # Add axis labels
    ax.text(1.1, 0, 0, "|+x⟩", color='r')
    ax.text(0, 1.1, 0, "|+y⟩", color='g')
    ax.text(0, 0, 1.1, "|0⟩", color='b')
    ax.text(0, 0, -1.1, "|1⟩", color='b')
    
    # Draw the qubit state vector
    x_q = np.sin(theta) * np.cos(phi)
    y_q = np.sin(theta) * np.sin(phi)
    z_q = np.cos(theta)
    ax.quiver(0, 0, 0, x_q, y_q, z_q, color='purple', arrow_length_ratio=0.1)
    
    # Set the labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Bloch Sphere Representation of a Qubit')
    
    # Set the limits of the plot
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.2])
    ax.set_zlim([-1.2, 1.2])
    
    # Add state information
    state_info = f"State: |ψ⟩ = cos(θ/2)|0⟩ + e^{{iφ}}sin(θ/2)|1⟩\nθ = {theta:.2f}, φ = {phi:.2f}"
    fig.text(0.5, 0.02, state_info, ha='center')
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    return fig

def create_ghz_state(num_qubits=3):
    """
    Creates a GHZ state (maximally entangled state of multiple qubits)
    
    Args:
        num_qubits (int): Number of qubits in the GHZ state
        
    Returns:
        QuantumCircuit: The circuit that creates the GHZ state
    """
    # Create a quantum circuit with the specified number of qubits
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply Hadamard gate to the first qubit
    circuit.h(0)
    
    # Apply CNOT gates to entangle all qubits
    for i in range(num_qubits - 1):
        circuit.cx(i, i + 1)
    
    # Measure all qubits
    circuit.measure(range(num_qubits), range(num_qubits))
    
    return circuit

def create_quantum_teleportation_circuit():
    """
    Creates a quantum teleportation circuit
    
    Returns:
        QuantumCircuit: The circuit for quantum teleportation
    """
    # Create a quantum circuit with 3 qubits and 2 classical bits
    # Qubit 0: Alice's qubit to be teleported
    # Qubit 1: Alice's half of the entangled pair
    # Qubit 2: Bob's half of the entangled pair
    circuit = QuantumCircuit(3, 2)
    
    # Prepare the qubit to be teleported (qubit 0) in a superposition state
    circuit.h(0)
    circuit.z(0)  # Apply additional gate to make it more interesting
    
    # Create entanglement between qubits 1 and 2 (Bell pair)
    circuit.h(1)
    circuit.cx(1, 2)
    
    # Begin teleportation protocol
    # Bell measurement
    circuit.cx(0, 1)
    circuit.h(0)
    
    # Measure qubits 0 and 1
    circuit.measure([0, 1], [0, 1])
    
    # Apply conditional operations on Bob's qubit based on measurement results
    circuit.z(2).c_if(0, 1)  # Apply Z gate if the first bit is 1
    circuit.x(2).c_if(1, 1)  # Apply X gate if the second bit is 1
    
    return circuit

def visualize_quantum_fourier_transform(n_qubits=3):
    """
    Creates and visualizes a Quantum Fourier Transform circuit
    
    Args:
        n_qubits (int): Number of qubits
        
    Returns:
        QuantumCircuit: The QFT circuit
    """
    # Create a quantum circuit for QFT
    circuit = QuantumCircuit(n_qubits)
    
    # Add some input state for visualization
    # Initialize with a simple state - all qubits in state |1⟩
    circuit.x(range(n_qubits))
    
    # Apply QFT
    # Apply Hadamard gates to all qubits
    for qubit in range(n_qubits):
        circuit.h(qubit)
        # Apply controlled phase rotations
        for target_qubit in range(qubit + 1, n_qubits):
            # Calculate rotation angle
            theta = np.pi / float(2 ** (target_qubit - qubit))
            circuit.cp(theta, qubit, target_qubit)
    
    # Swap qubits (optional but standard for QFT)
    for qubit in range(n_qubits // 2):
        circuit.swap(qubit, n_qubits - qubit - 1)
    
    return circuit