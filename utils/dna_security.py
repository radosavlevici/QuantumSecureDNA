import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from qiskit import QuantumCircuit, Aer, execute

# DNA base pairs
DNA_BASES = ['A', 'T', 'G', 'C']

# Mapping DNA bases to binary
DNA_TO_BINARY = {
    'A': '00',
    'T': '01',
    'G': '10',
    'C': '11'
}

# Mapping binary to DNA bases
BINARY_TO_DNA = {
    '00': 'A',
    '01': 'T',
    '10': 'G',
    '11': 'C'
}

def binary_to_text(binary):
    """Convert binary to text"""
    binary_values = [binary[i:i+8] for i in range(0, len(binary), 8)]
    ascii_values = [int(binary_value, 2) for binary_value in binary_values]
    text = ''.join(chr(ascii_value) for ascii_value in ascii_values)
    return text

def text_to_binary(text):
    """Convert text to binary"""
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_dna(binary):
    """Convert binary to DNA sequence"""
    # Ensure the binary length is a multiple of 2
    if len(binary) % 2 != 0:
        binary += '0'
    
    dna_sequence = ''
    for i in range(0, len(binary), 2):
        dna_sequence += BINARY_TO_DNA[binary[i:i+2]]
    
    return dna_sequence

def dna_to_binary(dna_sequence):
    """Convert DNA sequence to binary"""
    binary = ''
    for base in dna_sequence:
        binary += DNA_TO_BINARY[base]
    
    return binary

def dna_encrypt(plaintext, key):
    """
    Encrypt plaintext using DNA encoding and a key
    
    Args:
        plaintext (str): Text to encrypt
        key (str): Encryption key
        
    Returns:
        str: DNA sequence representing encrypted data
    """
    # Convert plaintext to binary
    binary_plaintext = text_to_binary(plaintext)
    
    # Convert key to binary
    binary_key = text_to_binary(key)
    
    # Ensure key is long enough (repeat if necessary)
    while len(binary_key) < len(binary_plaintext):
        binary_key += binary_key
    
    # Truncate key if it's too long
    binary_key = binary_key[:len(binary_plaintext)]
    
    # XOR the plaintext with the key
    binary_result = ''
    for i in range(len(binary_plaintext)):
        binary_result += '1' if binary_plaintext[i] != binary_key[i] else '0'
    
    # Convert binary to DNA sequence
    dna_sequence = binary_to_dna(binary_result)
    
    return dna_sequence

def dna_decrypt(dna_sequence, key):
    """
    Decrypt DNA sequence using the key
    
    Args:
        dna_sequence (str): DNA sequence to decrypt
        key (str): Decryption key
        
    Returns:
        str: Decrypted plaintext
    """
    # Convert DNA to binary
    binary_ciphertext = dna_to_binary(dna_sequence)
    
    # Convert key to binary
    binary_key = text_to_binary(key)
    
    # Ensure key is long enough (repeat if necessary)
    while len(binary_key) < len(binary_ciphertext):
        binary_key += binary_key
    
    # Truncate key if it's too long
    binary_key = binary_key[:len(binary_ciphertext)]
    
    # XOR the ciphertext with the key to get plaintext
    binary_result = ''
    for i in range(len(binary_ciphertext)):
        binary_result += '1' if binary_ciphertext[i] != binary_key[i] else '0'
    
    # Convert binary back to text
    try:
        plaintext = binary_to_text(binary_result)
        return plaintext
    except:
        return "Decryption failed. Invalid key or corrupted DNA sequence."

def visualize_dna_encryption(plaintext, key):
    """
    Visualize the DNA encryption process
    
    Args:
        plaintext (str): Original text
        key (str): Encryption key
        
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Get the encryption steps
    binary_plaintext = text_to_binary(plaintext)
    binary_key = text_to_binary(key)
    
    # Ensure key is long enough (repeat if necessary)
    while len(binary_key) < len(binary_plaintext):
        binary_key += binary_key
    
    # Truncate key if it's too long
    binary_key = binary_key[:len(binary_plaintext)]
    
    # XOR the plaintext with the key
    binary_result = ''
    for i in range(len(binary_plaintext)):
        binary_result += '1' if binary_plaintext[i] != binary_key[i] else '0'
    
    # Convert binary to DNA sequence
    dna_sequence = binary_to_dna(binary_result)
    
    # Create a visualization
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))
    
    # Show the original text and binary representation
    axes[0].text(0.5, 0.5, f"Original Text: {plaintext}", 
                 fontsize=12, ha='center', va='center')
    axes[0].text(0.5, 0.2, f"Binary: {binary_plaintext[:50]}{'...' if len(binary_plaintext) > 50 else ''}", 
                fontsize=10, ha='center', va='center')
    axes[0].axis('off')
    
    # Show the key and binary representation
    axes[1].text(0.5, 0.5, f"Key: {key}", 
                 fontsize=12, ha='center', va='center')
    axes[1].text(0.5, 0.2, f"Binary: {binary_key[:50]}{'...' if len(binary_key) > 50 else ''}", 
                fontsize=10, ha='center', va='center')
    axes[1].axis('off')
    
    # Show the XOR result
    axes[2].text(0.5, 0.5, "XOR Operation", 
                 fontsize=12, ha='center', va='center')
    axes[2].text(0.5, 0.2, f"Result: {binary_result[:50]}{'...' if len(binary_result) > 50 else ''}", 
                fontsize=10, ha='center', va='center')
    axes[2].axis('off')
    
    # Show the DNA encoding
    axes[3].text(0.5, 0.5, "DNA Encoding", 
                 fontsize=12, ha='center', va='center')
    axes[3].text(0.5, 0.2, f"DNA Sequence: {dna_sequence[:50]}{'...' if len(dna_sequence) > 50 else ''}", 
                fontsize=10, ha='center', va='center')
    axes[3].axis('off')
    
    plt.tight_layout()
    return fig

def visualize_dna_sequence(dna_sequence, title="DNA Sequence Visualization"):
    """
    Visualize a DNA sequence with color-coded bases
    
    Args:
        dna_sequence (str): DNA sequence to visualize
        title (str): Title for the visualization
        
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Color mapping for bases
    color_map = {
        'A': '#00FF00',  # Green
        'T': '#FF0000',  # Red
        'G': '#0000FF',  # Blue
        'C': '#FFFF00'   # Yellow
    }
    
    # Create the visualization
    fig, ax = plt.subplots(figsize=(12, 3))
    
    # Plot each base with its color
    for i, base in enumerate(dna_sequence[:100]):  # Limit to first 100 bases for clarity
        ax.text(i, 0, base, fontsize=14, ha='center', va='center', 
                color='black', bbox=dict(facecolor=color_map[base], alpha=0.7))
    
    ax.set_xlim(-1, min(len(dna_sequence), 100))
    ax.set_ylim(-0.5, 0.5)
    ax.set_title(title)
    ax.axis('off')
    
    if len(dna_sequence) > 100:
        ax.text(99, -0.3, "...", fontsize=20, ha='center', va='center')
    
    return fig

def quantum_enhanced_dna_key(message_length, quantum_circuit=None):
    """
    Generate a quantum-enhanced encryption key for DNA-based encryption
    
    Args:
        message_length (int): Length of the message to encrypt
        quantum_circuit (QuantumCircuit, optional): Custom quantum circuit
        
    Returns:
        tuple: (binary_key, visualization)
    """
    # Calculate number of qubits needed (each qubit gives us 1 bit)
    num_bits_needed = message_length * 8  # 8 bits per character
    num_qubits = num_bits_needed
    
    # Create a quantum circuit if not provided
    if quantum_circuit is None:
        # Create a circuit with quantum randomness
        qc = QuantumCircuit(num_qubits, num_qubits)
        
        # Apply Hadamard gates to create superposition
        for i in range(num_qubits):
            qc.h(i)
        
        # Measure all qubits
        qc.measure(range(num_qubits), range(num_qubits))
    else:
        qc = quantum_circuit
    
    # Run the simulation
    simulator = Aer.get_backend('qasm_simulator')
    result = execute(qc, simulator, shots=1).result()
    counts = result.get_counts(qc)
    
    # Get the binary key from the measurement
    binary_key = list(counts.keys())[0]
    
    # Create a visualization
    fig, ax = plt.subplots(figsize=(12, 4))
    
    # Show circuit (limited view for large circuits)
    if num_qubits <= 5:
        circuit_diagram = qc.draw(output='mpl')
        return binary_key, circuit_diagram
    else:
        # For larger circuits, just show a representation
        ax.text(0.5, 0.7, "Quantum Random Key Generation", 
                fontsize=14, ha='center', va='center')
        ax.text(0.5, 0.5, f"Generated {num_qubits} random qubits", 
                fontsize=12, ha='center', va='center')
        ax.text(0.5, 0.3, f"Binary Key (first 50 bits): {binary_key[:50]}...", 
                fontsize=10, ha='center', va='center')
        ax.axis('off')
        
        return binary_key, fig

def create_quantum_dna_circuit():
    """
    Create a quantum circuit for DNA-based encryption demonstration
    
    Returns:
        QuantumCircuit: A quantum circuit for DNA-based encryption
    """
    # Create a 4-qubit circuit to represent the 4 DNA bases
    qc = QuantumCircuit(4, 4)
    
    # Create superposition of all possible states
    for i in range(4):
        qc.h(i)
    
    # Create some entanglement between qubits (representing base pair relationships)
    qc.cx(0, 1)  # A-T relationship
    qc.cx(2, 3)  # G-C relationship
    
    # Measure all qubits
    qc.measure(range(4), range(4))
    
    return qc

def visualize_dna_base_pairs():
    """
    Create a visualization of DNA base pairs
    
    Returns:
        matplotlib.figure.Figure: Visualization of DNA base pairs
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Base pair colors
    colors = {
        'A': '#00FF00',  # Green
        'T': '#FF0000',  # Red
        'G': '#0000FF',  # Blue
        'C': '#FFFF00'   # Yellow
    }
    
    # Draw the backbone
    backbone_left = [(1, i) for i in range(0, 10)]
    backbone_right = [(5, i) for i in range(0, 10)]
    
    for i in range(len(backbone_left)-1):
        ax.plot([backbone_left[i][0], backbone_left[i+1][0]], 
                [backbone_left[i][1], backbone_left[i+1][1]], 'k-', linewidth=2)
        ax.plot([backbone_right[i][0], backbone_right[i+1][0]], 
                [backbone_right[i][1], backbone_right[i+1][1]], 'k-', linewidth=2)
    
    # Base pairs
    base_pairs = [
        ('A', 'T'),
        ('T', 'A'),
        ('G', 'C'),
        ('C', 'G'),
        ('A', 'T'),
        ('G', 'C'),
        ('T', 'A'),
        ('C', 'G'),
        ('A', 'T')
    ]
    
    # Draw the base pairs
    for i, (left, right) in enumerate(base_pairs):
        # Left base
        ax.text(0.7, i+0.5, left, fontsize=16, ha='center', va='center',
               color='black', bbox=dict(facecolor=colors[left], alpha=0.7))
        
        # Right base
        ax.text(5.3, i+0.5, right, fontsize=16, ha='center', va='center',
               color='black', bbox=dict(facecolor=colors[right], alpha=0.7))
        
        # Connection between bases
        ax.plot([1.3, 4.7], [i+0.5, i+0.5], 'k-', alpha=0.6)
    
    # Base pair explanations
    ax.text(3, 10.5, "DNA Base Pairs", fontsize=18, ha='center', va='center')
    ax.text(3, 9.5, "A pairs with T, G pairs with C", fontsize=14, ha='center', va='center')
    
    ax.set_xlim(0, 6)
    ax.set_ylim(-0.5, 11)
    ax.axis('off')
    
    return fig
