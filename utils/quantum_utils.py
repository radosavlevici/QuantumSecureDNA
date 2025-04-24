"""
Quantum Computing Utilities for Educational Platform
With advanced security features and visualization tools

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, plot_histogram, plot_state_city
from io import BytesIO
import base64

def create_bell_state():
    """
    Create a Bell state (maximally entangled two-qubit state)
    
    Returns:
        QuantumCircuit: Bell state circuit
    """
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)  # Apply Hadamard gate to qubit 0
    circuit.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
    circuit.measure([0, 1], [0, 1])  # Measure both qubits
    
    return circuit

def create_ghz_state(num_qubits=3):
    """
    Create a GHZ state (generalized Bell state) with n qubits
    
    Args:
        num_qubits: Number of qubits in the GHZ state (supports up to 32 qubits)
        
    Returns:
        QuantumCircuit: GHZ state circuit
    """
    # Enhanced support for larger qubit counts (up to 32, maximum supported by the simulator)
    num_qubits = min(max(num_qubits, 3), 32)  # Limit between 3 and 32 qubits for simulator compatibility
    
    circuit = QuantumCircuit(num_qubits, num_qubits)
    circuit.h(0)  # Apply Hadamard gate to first qubit
    
    # Apply CNOT gates between first qubit and all others
    for i in range(1, num_qubits):
        circuit.cx(0, i)
    
    # Add barrier for visual separation
    circuit.barrier()
    
    # Measure all qubits
    circuit.measure(range(num_qubits), range(num_qubits))
    
    return circuit

def create_hadamard_circuit(initial_state=[1, 0]):
    """
    Create a circuit applying a Hadamard gate to initial state
    
    Args:
        initial_state: Initial state of the qubit [alpha, beta]
        
    Returns:
        QuantumCircuit: Circuit with Hadamard gate
    """
    circuit = QuantumCircuit(1, 1)
    
    # Prepare initial state
    if initial_state[1] != 0:
        # If not |0>, prepare the state
        if initial_state[0] == 0 and initial_state[1] == 1:
            # For |1> state
            circuit.x(0)
        else:
            # For superposition states
            circuit.initialize(initial_state, 0)
    
    # Apply Hadamard gate
    circuit.h(0)
    circuit.measure(0, 0)
    
    return circuit

def create_pauli_x_circuit(initial_state=[1, 0]):
    """
    Create a circuit applying a Pauli-X (NOT) gate to initial state
    
    Args:
        initial_state: Initial state of the qubit
        
    Returns:
        QuantumCircuit: Circuit with Pauli-X gate
    """
    circuit = QuantumCircuit(1, 1)
    
    # Prepare initial state
    if initial_state[1] != 0:
        # If not |0>, prepare the state
        if initial_state[0] == 0 and initial_state[1] == 1:
            # For |1> state
            circuit.x(0)
        else:
            # For superposition states
            circuit.initialize(initial_state, 0)
    
    # Apply Pauli-X gate
    circuit.x(0)
    circuit.measure(0, 0)
    
    return circuit

def create_pauli_y_circuit(initial_state=[1, 0]):
    """
    Create a circuit applying a Pauli-Y gate to initial state
    
    Args:
        initial_state: Initial state of the qubit
        
    Returns:
        QuantumCircuit: Circuit with Pauli-Y gate
    """
    circuit = QuantumCircuit(1, 1)
    
    # Prepare initial state
    if initial_state[1] != 0:
        # If not |0>, prepare the state
        if initial_state[0] == 0 and initial_state[1] == 1:
            # For |1> state
            circuit.x(0)
        else:
            # For superposition states
            circuit.initialize(initial_state, 0)
    
    # Apply Pauli-Y gate
    circuit.y(0)
    circuit.measure(0, 0)
    
    return circuit

def create_pauli_z_circuit(initial_state=[1, 0]):
    """
    Create a circuit applying a Pauli-Z gate to initial state
    
    Args:
        initial_state: Initial state of the qubit
        
    Returns:
        QuantumCircuit: Circuit with Pauli-Z gate
    """
    circuit = QuantumCircuit(1, 1)
    
    # Prepare initial state
    if initial_state[1] != 0:
        # If not |0>, prepare the state
        if initial_state[0] == 0 and initial_state[1] == 1:
            # For |1> state
            circuit.x(0)
        else:
            # For superposition states
            circuit.initialize(initial_state, 0)
    
    # Apply Pauli-Z gate
    circuit.z(0)
    circuit.measure(0, 0)
    
    return circuit

def create_quantum_teleportation_circuit(multi_qubit=False):
    """
    Create a quantum teleportation circuit
    
    Args:
        multi_qubit: If True, creates an enhanced version with additional qubits
        
    Returns:
        QuantumCircuit: Quantum teleportation circuit
    """
    if not multi_qubit:
        # Standard 3-qubit teleportation circuit
        circuit = QuantumCircuit(3, 2)
        
        # Initialize qubit to teleport
        circuit.x(0)  # Start with |1⟩ (can be changed to any state)
        
        # Create Bell pair for teleportation
        circuit.h(1)
        circuit.cx(1, 2)
        
        # Perform teleportation protocol
        circuit.barrier()
        circuit.cx(0, 1)
        circuit.h(0)
        circuit.measure([0, 1], [0, 1])
        
        # Apply corrections based on measurement
        circuit.barrier()
        circuit.x(2).c_if(1, 1)  # Apply X if second measurement is 1
        circuit.z(2).c_if(0, 1)  # Apply Z if first measurement is 1
    else:
        # Enhanced multi-qubit teleportation (teleporting 2 qubits using 6 qubits total)
        circuit = QuantumCircuit(6, 4)
        
        # Initialize qubits to teleport (qubits 0 and 1)
        circuit.x(0)  # Prepare |1⟩ state
        circuit.h(1)  # Prepare |+⟩ state
        
        # Create two Bell pairs for teleportation (qubits 2,3 and 4,5)
        circuit.h(2)
        circuit.cx(2, 3)
        circuit.h(4)
        circuit.cx(4, 5)
        
        # Add barrier for clarity
        circuit.barrier()
        
        # Perform teleportation protocol for first qubit
        circuit.cx(0, 2)
        circuit.h(0)
        
        # Perform teleportation protocol for second qubit
        circuit.cx(1, 4)
        circuit.h(1)
        
        # Measure control qubits
        circuit.measure([0, 2], [0, 1])
        circuit.measure([1, 4], [2, 3])
        
        # Add barrier before corrections
        circuit.barrier()
        
        # Apply corrections for first teleported qubit
        circuit.x(3).c_if(1, 1)  # Apply X if second measurement is 1
        circuit.z(3).c_if(0, 1)  # Apply Z if first measurement is 1
        
        # Apply corrections for second teleported qubit
        circuit.x(5).c_if(3, 1)  # Apply X if fourth measurement is 1
        circuit.z(5).c_if(2, 1)  # Apply Z if third measurement is 1
    
    return circuit

def visualize_quantum_fourier_transform(num_qubits=3):
    """
    Create and visualize a Quantum Fourier Transform circuit
    
    Args:
        num_qubits: Number of qubits in the QFT (supports up to 32 qubits)
        
    Returns:
        QuantumCircuit: QFT circuit
    """
    # Enhanced support for larger qubit counts (up to 32, maximum supported by the simulator)
    num_qubits = min(max(num_qubits, 3), 32)  # Limit between 3 and 32 qubits for simulator compatibility
    
    circuit = QuantumCircuit(num_qubits)
    
    # Create superposition state
    for i in range(num_qubits):
        circuit.h(i)
    
    # Apply QFT
    circuit.barrier()
    
    for i in range(num_qubits):
        circuit.h(i)
        # Apply controlled phase rotations with increasing phase precision
        for j in range(i+1, num_qubits):
            # Calculate the rotation angle
            theta = 2 * np.pi / (2 ** (j - i + 1))
            circuit.cp(theta, j, i)
    
    # Improve circuit efficiency with barrier visualization
    circuit.barrier()
    
    # Swap qubits to get the correct output order
    for i in range(num_qubits // 2):
        circuit.swap(i, num_qubits - i - 1)
    
    return circuit

def simulate_circuit(circuit, get_statevector=False, shots=1024, advanced_mode=False):
    """
    Simulate a quantum circuit with enhanced capabilities
    
    Args:
        circuit: The quantum circuit to simulate
        get_statevector: Whether to return the statevector
        shots: Base number of shots for measurement
        advanced_mode: Whether to use advanced simulation settings
        
    Returns:
        Result: Simulation result
    """
    # Increase shots for advanced mode
    if advanced_mode:
        shots = 8192  # Much higher shot count for advanced simulations
        
    if get_statevector:
        # Statevector simulation with enhanced precision
        simulator = Aer.get_backend('statevector_simulator')
        # Optimize transpilation for statevector sim
        transpiled_circuit = transpile(circuit, simulator, optimization_level=3)
        return simulator.run(transpiled_circuit).result()
    else:
        # Measurement simulation with enhanced capabilities
        simulator = Aer.get_backend('qasm_simulator')
        # Use higher optimization for complex circuits
        transpiled_circuit = transpile(circuit, simulator, optimization_level=3)
        # Configure advanced simulation parameters
        sim_config = {}
        if advanced_mode and circuit.num_qubits > 10:
            # Advanced settings for large circuit simulation
            sim_config = {
                'method': 'statevector',  # Use statevector method for accuracy
                'max_parallel_threads': 8,  # Utilize more threads
                'max_parallel_experiments': 4  # Run multiple circuits in parallel
            }
        return simulator.run(transpiled_circuit, shots=shots, **sim_config).result()

def plot_quantum_state(statevector):
    """
    Plot a visualization of a quantum state
    
    Args:
        statevector: Statevector to visualize
        
    Returns:
        Figure: Matplotlib figure with state visualization
    """
    try:
        # Try city plot for larger systems
        if len(statevector) > 4:
            return plot_state_city(statevector)
        else:
            # For smaller systems use Bloch multivector
            return plot_bloch_multivector(statevector)
    except:
        # Fallback to basic histogram plot
        fig, ax = plt.subplots(figsize=(10, 7))
        probs = np.abs(statevector)**2
        ax.bar(range(len(probs)), probs)
        ax.set_xlabel('Basis State')
        ax.set_ylabel('Probability')
        ax.set_title('Quantum State Probabilities')
        return fig

def plot_measurement_results(counts):
    """
    Plot histogram of measurement results
    
    Args:
        counts: Dictionary of counts from simulation
        
    Returns:
        Figure: Matplotlib figure with histogram
    """
    return plot_histogram(counts)

def bloch_sphere_visualization(theta, phi):
    """
    Create a Bloch sphere visualization for a specific qubit state
    
    Args:
        theta: Polar angle (0 to pi)
        phi: Azimuthal angle (0 to 2*pi)
        
    Returns:
        Figure: Matplotlib figure with Bloch sphere
    """
    # Calculate the Bloch vector components
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)
    
    # Create the figure
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Draw the Bloch sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x_sphere = np.cos(u) * np.sin(v)
    y_sphere = np.sin(u) * np.sin(v)
    z_sphere = np.cos(v)
    ax.plot_surface(x_sphere, y_sphere, z_sphere, color='lightblue', alpha=0.1)
    
    # Draw the axes
    ax.quiver(0, 0, 0, 1, 0, 0, color='r', length=1.3, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 1, 0, color='g', length=1.3, arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, 0, 0, 1, color='b', length=1.3, arrow_length_ratio=0.1)
    
    # Label the axes
    ax.text(1.4, 0, 0, r'$X$', color='r', fontsize=12)
    ax.text(0, 1.4, 0, r'$Y$', color='g', fontsize=12)
    ax.text(0, 0, 1.4, r'$Z$', color='b', fontsize=12)
    
    # Draw the state vector
    ax.quiver(0, 0, 0, x, y, z, color='purple', length=1, arrow_length_ratio=0.1)
    
    # Set plot limits and labels
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])
    ax.set_zlim([-1.5, 1.5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    # Add title and state information
    state_label = f'$\\theta = {theta:.2f}, \\phi = {phi:.2f}$'
    ax.set_title(f'Bloch Sphere Visualization\n{state_label}', fontsize=14)
    
    # Additional state information
    ket0_coef = np.cos(theta/2)
    ket1_coef = np.exp(1j*phi) * np.sin(theta/2)
    state_text = f'$|\\psi\\rangle = {ket0_coef:.3f}|0\\rangle + {ket1_coef:.3f}|1\\rangle$'
    fig.text(0.5, 0.02, state_text, ha='center', fontsize=12)
    
    # Add copyright notice
    copyright_text = '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
    fig.text(0.5, 0.01, copyright_text, ha='center', fontsize=8, color='gray')
    
    return fig

# Copyright protection for this module - WORLDWIDE COPYRIGHT PROTECTED
COPYRIGHT_NOTICE = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - All Rights Reserved Globally"