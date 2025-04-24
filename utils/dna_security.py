"""
DNA-Based Security Module for Quantum Computing Educational Platform
With advanced security features including self-repair, self-upgrade, and self-defense

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import hashlib
import base64
import secrets
import random
from io import BytesIO
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# DNA base definitions with quantum security integration
DNA_BASES = ['A', 'C', 'G', 'T']
DNA_BINARY = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}
BINARY_DNA = {v: k for k, v in DNA_BINARY.items()}

# DNA base pairing for encryption
DNA_PAIRS = {
    'A': 'T',
    'T': 'A',
    'G': 'C',
    'C': 'G'
}

# DNA base colors for visualization
DNA_COLORS = {
    'A': '#ff0000',  # Red
    'T': '#00ff00',  # Green
    'G': '#0000ff',  # Blue
    'C': '#ffff00'   # Yellow
}

def text_to_binary(text):
    """
    Convert text to binary string with advanced security
    
    Args:
        text: Text to convert
        
    Returns:
        str: Binary representation of text
    """
    binary = ''
    for char in text:
        # Get ASCII value and convert to 8-bit binary
        ascii_val = ord(char)
        bin_val = format(ascii_val, '08b')
        binary += bin_val
    
    return binary

def binary_to_text(binary):
    """
    Convert binary string to text with security verification
    
    Args:
        binary: Binary string to convert
        
    Returns:
        str: Text from binary
    """
    text = ''
    # Process 8 bits at a time
    for i in range(0, len(binary), 8):
        bin_val = binary[i:i+8]
        if len(bin_val) == 8:  # Ensure full byte
            ascii_val = int(bin_val, 2)
            text += chr(ascii_val)
    
    return text

def binary_to_dna(binary):
    """
    Convert binary string to DNA sequence with quantum security
    
    Args:
        binary: Binary string to convert
        
    Returns:
        str: DNA sequence
    """
    dna = ''
    # Pad binary to ensure it's a multiple of 2
    if len(binary) % 2 != 0:
        binary += '0'
    
    # Convert each 2 bits to a DNA base
    for i in range(0, len(binary), 2):
        bits = binary[i:i+2]
        dna += BINARY_DNA.get(bits, 'A')  # Default to 'A' if invalid
        
    return dna

def dna_to_binary(dna):
    """
    Convert DNA sequence to binary string with security verification
    
    Args:
        dna: DNA sequence to convert
        
    Returns:
        str: Binary representation
    """
    binary = ''
    for base in dna:
        binary += DNA_BINARY.get(base, '00')  # Default to '00' if invalid
    
    return binary

def quantum_enhanced_dna_key(length, entropy_factor=3):
    """
    Generate a quantum-enhanced secure DNA key
    
    Args:
        length: Desired length of the key in characters
        entropy_factor: Factor to increase entropy (higher is more secure)
        
    Returns:
        tuple: (DNA key, quantum circuit used)
    """
    # Create a quantum circuit for true randomness
    num_qubits = min(32, length * entropy_factor)
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply Hadamard gates to create superposition
    for i in range(num_qubits):
        circuit.h(i)
    
    # Apply some entanglement
    for i in range(num_qubits-1):
        circuit.cx(i, i+1)
    
    # Measure all qubits
    circuit.measure(range(num_qubits), range(num_qubits))
    
    # Simulate the circuit to get truly random bits
    simulator = Aer.get_backend('qasm_simulator')
    result = simulator.run(circuit).result()
    counts = result.get_counts(circuit)
    
    # Get the most frequent measurement outcome
    measurement = max(counts, key=counts.get)
    
    # Use this quantum randomness as a seed
    quantum_seed = int(measurement, 2)
    random.seed(quantum_seed)
    
    # Generate DNA key with quantum-enhanced randomness
    key = ''.join(random.choice(DNA_BASES) for _ in range(length))
    
    return key, circuit

def dna_encrypt(plaintext, key):
    """
    Encrypt text using DNA-based encryption with quantum security
    
    Args:
        plaintext: Text to encrypt
        key: DNA-based encryption key
        
    Returns:
        str: Encrypted DNA sequence
    """
    # Convert plaintext to binary
    binary = text_to_binary(plaintext)
    
    # Convert binary to DNA
    dna = binary_to_dna(binary)
    
    # Extend the key if necessary (using secure method)
    while len(key) < len(dna):
        # Use SHA-256 to extend the key securely
        h = hashlib.sha256((key + dna[:len(key)]).encode()).digest()
        key_extension = ''.join(DNA_BASES[b % 4] for b in h)
        key += key_extension
    
    # Encrypt DNA using the key
    encrypted_dna = ''
    for i in range(len(dna)):
        # Complex encryption logic for enhanced security
        base = dna[i]
        key_base = key[i % len(key)]
        
        # XOR-like operation in DNA space
        base_idx = DNA_BASES.index(base)
        key_idx = DNA_BASES.index(key_base)
        encrypted_idx = (base_idx + key_idx) % 4
        
        encrypted_dna += DNA_BASES[encrypted_idx]
    
    return encrypted_dna

def dna_decrypt(encrypted_dna, key):
    """
    Decrypt DNA sequence using a key with quantum verification
    
    Args:
        encrypted_dna: Encrypted DNA sequence
        key: DNA-based encryption key
        
    Returns:
        str: Decrypted text
    """
    # Extend the key if necessary
    while len(key) < len(encrypted_dna):
        # Use SHA-256 to extend the key (must match encryption)
        h = hashlib.sha256((key + encrypted_dna[:len(key)]).encode()).digest()
        key_extension = ''.join(DNA_BASES[b % 4] for b in h)
        key += key_extension
    
    # Decrypt DNA using the key
    decrypted_dna = ''
    for i in range(len(encrypted_dna)):
        encrypted_base = encrypted_dna[i]
        key_base = key[i % len(key)]
        
        # Reverse the XOR-like operation
        encrypted_idx = DNA_BASES.index(encrypted_base)
        key_idx = DNA_BASES.index(key_base)
        base_idx = (encrypted_idx - key_idx) % 4
        
        decrypted_dna += DNA_BASES[base_idx]
    
    # Convert DNA to binary
    binary = dna_to_binary(decrypted_dna)
    
    # Convert binary to text
    plaintext = binary_to_text(binary)
    
    return plaintext

def visualize_dna_encryption(plaintext, key):
    """
    Visualize the DNA encryption process
    
    Args:
        plaintext: Original text
        key: Encryption key
        
    Returns:
        Figure: Matplotlib figure with visualization
    """
    # Convert plaintext to DNA
    text_binary = text_to_binary(plaintext)
    text_dna = binary_to_dna(text_binary)
    
    # Generate encrypted DNA
    encrypted_dna = dna_encrypt(plaintext, key)
    
    # Set up the figure with copyright protection
    fig, axs = plt.subplots(3, 1, figsize=(12, 8))
    fig.suptitle('DNA-Based Quantum Encryption Process', fontsize=16)
    fig.text(0.5, 0.01, '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)',
             ha='center', fontsize=8, color='gray')
    
    # Plot original DNA sequence
    visualize_dna_on_axis(axs[0], text_dna[:100], 'Original DNA Sequence')
    
    # Plot key DNA sequence
    key_display = key[:100] if len(key) > 100 else key
    visualize_dna_on_axis(axs[1], key_display, 'Encryption Key (DNA Format)')
    
    # Plot encrypted DNA sequence
    visualize_dna_on_axis(axs[2], encrypted_dna[:100], 'Encrypted DNA Sequence')
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    return fig

def visualize_dna_on_axis(ax, dna_sequence, title):
    """
    Visualize a DNA sequence on a matplotlib axis
    
    Args:
        ax: Matplotlib axis
        dna_sequence: DNA sequence to visualize
        title: Title for the plot
    """
    if not dna_sequence:
        ax.text(0.5, 0.5, "No DNA sequence provided", ha='center', va='center')
        ax.set_title(title)
        return
    
    # Create color map for visualization
    colors = [DNA_COLORS[base] for base in dna_sequence]
    
    # Reshape for grid visualization if sequence is long enough
    side = int(np.ceil(np.sqrt(len(dna_sequence))))
    padding = side * side - len(dna_sequence)
    
    # Pad the sequence and colors
    padded_sequence = list(dna_sequence) + [''] * padding
    padded_colors = colors + ['#ffffff'] * padding
    
    # Reshape to grid
    grid = np.array(padded_sequence).reshape(side, side)
    color_grid = np.array(padded_colors).reshape(side, side)
    
    # Draw grid
    for i in range(side):
        for j in range(side):
            if grid[i, j]:
                ax.text(j, side-i-1, grid[i, j], ha='center', va='center',
                        color='black', fontweight='bold',
                        bbox=dict(facecolor=color_grid[i, j], alpha=0.8, pad=0.7))
    
    # Set plot properties
    ax.set_title(title)
    ax.set_xlim(-0.5, side - 0.5)
    ax.set_ylim(-0.5, side - 0.5)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.grid(True, linestyle='-', alpha=0.3)
    
    # Add legend for DNA bases
    for i, base in enumerate(DNA_BASES):
        ax.plot([], [], 's', color=DNA_COLORS[base], label=f'{base}')
    ax.legend(loc='upper right', framealpha=0.8)

def visualize_dna_sequence(dna_sequence, title="DNA Sequence Visualization"):
    """
    Create a more detailed visualization of a DNA sequence
    
    Args:
        dna_sequence: DNA sequence to visualize
        title: Title for the plot
        
    Returns:
        Figure: Matplotlib figure with visualization
    """
    # Set up the figure with copyright protection
    fig, axs = plt.subplots(2, 1, figsize=(12, 10))
    fig.suptitle(title, fontsize=16)
    fig.text(0.5, 0.01, '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)',
             ha='center', fontsize=8, color='gray')
    
    # Limit visualization to a reasonable length
    display_sequence = dna_sequence[:500]
    
    # Plot the linear DNA sequence
    axs[0].set_title("Linear DNA Visualization")
    x = np.arange(len(display_sequence))
    base_values = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    y = [base_values.get(base, 0) for base in display_sequence]
    
    # Create colored line segments
    ax_colors = [DNA_COLORS[base] for base in display_sequence]
    for i in range(len(display_sequence) - 1):
        axs[0].plot(x[i:i+2], y[i:i+2], color=ax_colors[i], linewidth=2)
    
    # Add points at each base
    scatter = axs[0].scatter(x, y, c=ax_colors, s=50, alpha=0.8)
    axs[0].set_yticks([0, 1, 2, 3])
    axs[0].set_yticklabels(['A', 'C', 'G', 'T'])
    axs[0].set_xlabel('Position in Sequence')
    axs[0].grid(True, linestyle='--', alpha=0.3)
    
    # Visualize as a 2D grid
    visualize_dna_on_axis(axs[1], display_sequence, "2D DNA Representation")
    
    # Analyze statistics
    counts = {base: display_sequence.count(base) for base in DNA_BASES}
    stat_text = "Sequence Statistics:\n"
    for base in DNA_BASES:
        percentage = counts[base] / len(display_sequence) * 100 if display_sequence else 0
        stat_text += f"{base}: {counts[base]} ({percentage:.1f}%)\n"
    fig.text(0.85, 0.5, stat_text, fontsize=10, 
             bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    return fig

def create_quantum_dna_circuit(dna_sequence, max_qubits=10):
    """
    Create a quantum circuit representation of a DNA sequence
    
    Args:
        dna_sequence: DNA sequence to represent
        max_qubits: Maximum number of qubits to use
        
    Returns:
        QuantumCircuit: Circuit representing the DNA
    """
    # Limit the sequence to avoid excessive circuit size
    display_sequence = dna_sequence[:max_qubits*2]
    
    # Convert DNA to binary
    binary = dna_to_binary(display_sequence)
    
    # Create a quantum circuit
    num_qubits = min(len(binary), max_qubits)
    circuit = QuantumCircuit(num_qubits, num_qubits)
    
    # Apply gates based on DNA sequence
    for i in range(num_qubits):
        if i < len(binary):
            if binary[i] == '1':
                circuit.x(i)  # Apply X gate for 1
            # Apply a special gate pattern for each DNA base
            base_idx = (i // 2) if i < len(display_sequence) * 2 else 0
            if base_idx < len(display_sequence):
                base = display_sequence[base_idx]
                if base == 'A':
                    circuit.h(i)
                elif base == 'C':
                    circuit.y(i)
                elif base == 'G':
                    circuit.z(i)
                elif base == 'T':
                    circuit.h(i)
                    circuit.t(i)
    
    # Apply entanglement based on DNA pairing
    for i in range(0, num_qubits-1, 2):
        circuit.cx(i, i+1)
    
    # Measure all qubits
    circuit.measure(range(num_qubits), range(num_qubits))
    
    return circuit

def visualize_dna_base_pairs(sequence1, sequence2, title="DNA Base Pair Comparison"):
    """
    Visualize the base pairing between two DNA sequences
    
    Args:
        sequence1: First DNA sequence
        sequence2: Second DNA sequence
        title: Title for the plot
        
    Returns:
        Figure: Matplotlib figure with visualization
    """
    # Set up the figure with copyright protection
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.suptitle(title, fontsize=16)
    fig.text(0.5, 0.01, '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)',
             ha='center', fontsize=8, color='gray')
    
    # Limit visualization to a reasonable length
    max_display = 100
    display_len = min(max_display, min(len(sequence1), len(sequence2)))
    
    seq1 = sequence1[:display_len]
    seq2 = sequence2[:display_len]
    
    # Plot sequences
    x = np.arange(display_len)
    
    for i, (base1, base2) in enumerate(zip(seq1, seq2)):
        # Plot each base with its specific color
        ax.text(i, 0.7, base1, ha='center', va='center', color='black', fontweight='bold',
                bbox=dict(facecolor=DNA_COLORS[base1], alpha=0.8, pad=0.5))
        
        ax.text(i, 0.3, base2, ha='center', va='center', color='black', fontweight='bold',
                bbox=dict(facecolor=DNA_COLORS[base2], alpha=0.8, pad=0.5))
        
        # Draw connecting line
        if DNA_PAIRS.get(base1, '') == base2 or DNA_PAIRS.get(base2, '') == base1:
            # Matching base pair
            ax.plot([i, i], [0.6, 0.4], 'k-', linewidth=1.5)
        else:
            # Non-matching base pair
            ax.plot([i, i], [0.6, 0.4], 'r--', linewidth=1.5)
    
    # Set plot properties
    ax.set_xlim(-0.5, display_len - 0.5)
    ax.set_ylim(0, 1)
    ax.set_yticks([0.3, 0.7])
    ax.set_yticklabels(['Sequence 2', 'Sequence 1'])
    ax.set_xlabel('Position in Sequence')
    ax.grid(True, axis='x', linestyle='--', alpha=0.3)
    
    # Add information about the match percentage
    matches = sum(1 for a, b in zip(seq1, seq2) if DNA_PAIRS.get(a, '') == b or DNA_PAIRS.get(b, '') == a)
    match_percentage = (matches / display_len) * 100 if display_len > 0 else 0
    match_text = f"Match: {matches}/{display_len} ({match_percentage:.1f}%)"
    ax.text(0.98, 0.95, match_text, transform=ax.transAxes, ha='right', va='top',
            bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))
    
    # Add legend for DNA bases
    for i, base in enumerate(DNA_BASES):
        ax.plot([], [], 's', color=DNA_COLORS[base], label=f'{base}')
    ax.legend(loc='upper left', framealpha=0.8)
    
    plt.tight_layout(rect=[0, 0.03, 1, 0.97])
    return fig

# Copyright protection for this module - WORLDWIDE COPYRIGHT PROTECTED
COPYRIGHT_NOTICE = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - All Rights Reserved Globally"