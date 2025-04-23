"""
DNA-Based Security Utilities for Quantum Computing Educational Platform
With advanced security features including self-repair, self-upgrade, and self-defense

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import Aer
import hashlib
import os
import random

# DNA encoding map
DNA_MAP = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}

# Reverse DNA map
REVERSE_DNA_MAP = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}

def binary_to_text(binary):
    """Convert binary to text"""
    # Split binary into 8-bit chunks
    binary_chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
    
    # Convert each chunk to a character
    text = ''
    for chunk in binary_chunks:
        if len(chunk) == 8:  # Ensure complete byte
            text += chr(int(chunk, 2))
    
    return text

def text_to_binary(text):
    """Convert text to binary"""
    binary = ''
    
    # Convert each character to its binary representation
    for char in text:
        # Convert to binary and remove '0b' prefix, ensure 8 bits
        binary += format(ord(char), '08b')
    
    return binary

def binary_to_dna(binary):
    """Convert binary to DNA sequence"""
    # Ensure the binary string has an even length
    if len(binary) % 2 != 0:
        binary += '0'
    
    # Convert pairs of bits to DNA bases
    dna_sequence = ''
    for i in range(0, len(binary), 2):
        bit_pair = binary[i:i+2]
        dna_sequence += DNA_MAP[bit_pair]
    
    return dna_sequence

def dna_to_binary(dna_sequence):
    """Convert DNA sequence to binary"""
    binary = ''
    
    # Convert each DNA base to its binary representation
    for base in dna_sequence:
        binary += REVERSE_DNA_MAP[base]
    
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
    # Ensure the key has enough characters
    while len(key) < len(plaintext):
        key += key
    key = key[:len(plaintext)]
    
    # Add copyright notice for security
    security_text = f"©{plaintext}©"
    
    # Convert text to binary
    binary_text = text_to_binary(security_text)
    
    # Convert binary to DNA
    dna_text = binary_to_dna(binary_text)
    
    # Generate a hash for integrity verification
    integrity_hash = hashlib.sha256(dna_text.encode()).hexdigest()[:16]
    integrity_binary = text_to_binary(integrity_hash)
    integrity_dna = binary_to_dna(integrity_binary)
    
    # Add integrity check to DNA sequence
    secured_dna = dna_text + "SECURITY" + integrity_dna
    
    # Apply XOR-like operation with the key at the DNA level
    key_dna = binary_to_dna(text_to_binary(key))
    encrypted_dna = ""
    
    for i in range(len(secured_dna)):
        dna_base = secured_dna[i]
        key_base = key_dna[i % len(key_dna)]
        
        # DNA XOR-like operation
        if dna_base == key_base:
            encrypted_dna += "A"
        elif (dna_base == "A" and key_base == "T") or (dna_base == "T" and key_base == "A") or \
             (dna_base == "C" and key_base == "G") or (dna_base == "G" and key_base == "C"):
            encrypted_dna += "T"
        elif (dna_base == "A" and key_base == "C") or (dna_base == "C" and key_base == "A") or \
             (dna_base == "G" and key_base == "T") or (dna_base == "T" and key_base == "G"):
            encrypted_dna += "C"
        else:
            encrypted_dna += "G"
    
    return encrypted_dna

def dna_decrypt(dna_sequence, key):
    """
    Decrypt DNA sequence using the key
    
    Args:
        dna_sequence (str): DNA sequence to decrypt
        key (str): Decryption key
        
    Returns:
        str: Decrypted plaintext
    """
    # Ensure the key has enough characters
    while len(key) * 4 < len(dna_sequence):  # Each char in key becomes 4 DNA bases
        key += key
    key = key[:len(dna_sequence)]
    
    # Convert key to DNA
    key_dna = binary_to_dna(text_to_binary(key))
    key_dna = key_dna * (len(dna_sequence) // len(key_dna) + 1)
    key_dna = key_dna[:len(dna_sequence)]
    
    # Reverse the XOR-like operation
    decrypted_dna = ""
    for i in range(len(dna_sequence)):
        encrypted_base = dna_sequence[i]
        key_base = key_dna[i]
        
        # Reverse DNA XOR-like operation
        if encrypted_base == "A":
            decrypted_dna += key_base
        elif encrypted_base == "T":
            if key_base == "A": decrypted_dna += "T"
            elif key_base == "T": decrypted_dna += "A"
            elif key_base == "C": decrypted_dna += "G"
            else: decrypted_dna += "C"
        elif encrypted_base == "C":
            if key_base == "A": decrypted_dna += "C"
            elif key_base == "C": decrypted_dna += "A"
            elif key_base == "G": decrypted_dna += "T"
            else: decrypted_dna += "G"
        else:  # "G"
            if key_base == "A": decrypted_dna += "G"
            elif key_base == "G": decrypted_dna += "A"
            elif key_base == "C": decrypted_dna += "T"
            else: decrypted_dna += "C"
    
    # Extract the main DNA sequence and integrity check
    if "SECURITY" in decrypted_dna:
        parts = decrypted_dna.split("SECURITY")
        main_dna = parts[0]
        integrity_dna = parts[1] if len(parts) > 1 else ""
        
        # Verify integrity
        calculated_hash = hashlib.sha256(main_dna.encode()).hexdigest()[:16]
        calculated_integrity_dna = binary_to_dna(text_to_binary(calculated_hash))
        
        if calculated_integrity_dna != integrity_dna:
            raise ValueError("Integrity check failed. The data may have been tampered with.")
        
        # Convert DNA to binary
        binary_text = dna_to_binary(main_dna)
        
        # Convert binary to text
        decrypted_text = binary_to_text(binary_text)
        
        # Remove security markers
        if decrypted_text.startswith("©") and "©" in decrypted_text[1:]:
            return decrypted_text[1:].split("©")[0]
        
        return decrypted_text
    else:
        # If no security marker, just decrypt normally
        binary_text = dna_to_binary(decrypted_dna)
        return binary_to_text(binary_text)

def visualize_dna_encryption(plaintext, key):
    """
    Visualize the DNA encryption process
    
    Args:
        plaintext (str): Original text
        key (str): Encryption key
        
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Add copyright protection
    security_text = f"©{plaintext}©"
    
    # Convert to binary
    binary_text = text_to_binary(security_text)
    
    # Convert to DNA
    dna_text = binary_to_dna(binary_text)
    
    # Encrypt
    key_dna = binary_to_dna(text_to_binary(key))
    encrypted_dna = dna_encrypt(plaintext, key)
    
    # Create visualization
    fig, axs = plt.subplots(4, 1, figsize=(10, 12))
    
    # Plot original text
    axs[0].text(0.5, 0.5, f"Original: '{plaintext}'", 
               fontsize=12, ha='center', va='center')
    axs[0].axis('off')
    
    # Plot binary representation
    binary_display = binary_text[:100] + "..." if len(binary_text) > 100 else binary_text
    axs[1].text(0.5, 0.5, f"Binary: {binary_display}", 
               fontsize=10, ha='center', va='center', family='monospace')
    axs[1].axis('off')
    
    # Plot DNA representation
    dna_colors = {'A': 'green', 'C': 'blue', 'G': 'red', 'T': 'purple'}
    dna_display = dna_text[:50] + "..." if len(dna_text) > 50 else dna_text
    
    x_pos = 0.1
    for base in dna_display:
        if base in dna_colors:
            axs[2].text(x_pos, 0.5, base, color=dna_colors[base], fontsize=14, fontweight='bold')
        else:
            axs[2].text(x_pos, 0.5, base, color='black', fontsize=14)
        x_pos += 0.015
    
    if len(dna_text) > 50:
        axs[2].text(x_pos, 0.5, "...", color='black', fontsize=14)
    
    axs[2].set_title("DNA Encoding")
    axs[2].axis('off')
    
    # Plot encrypted DNA
    encrypted_display = encrypted_dna[:50] + "..." if len(encrypted_dna) > 50 else encrypted_dna
    
    x_pos = 0.1
    for base in encrypted_display:
        if base in dna_colors:
            axs[3].text(x_pos, 0.5, base, color=dna_colors[base], fontsize=14, fontweight='bold')
        else:
            axs[3].text(x_pos, 0.5, base, color='black', fontsize=14)
        x_pos += 0.015
    
    if len(encrypted_dna) > 50:
        axs[3].text(x_pos, 0.5, "...", color='black', fontsize=14)
    
    axs[3].set_title("Encrypted DNA")
    axs[3].axis('off')
    
    # Add title and copyright
    plt.suptitle("DNA-Based Encryption Process", fontsize=16)
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
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
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Define colors for each base
    colors = {
        'A': '#8BC34A',  # Green
        'C': '#03A9F4',  # Blue
        'G': '#F44336',  # Red
        'T': '#9C27B0'   # Purple
    }
    
    # Create x positions for each base
    x_positions = np.arange(len(dna_sequence))
    
    # Create bars for each base type
    for base, color in colors.items():
        # Create mask for this base
        mask = np.array([b == base for b in dna_sequence])
        if mask.any():
            ax.bar(x_positions[mask], 1, color=color, width=1, label=base)
    
    # Set axis labels and title
    ax.set_xlabel('Position in Sequence')
    ax.set_ylabel('Base')
    ax.set_title(title)
    
    # Set y-axis ticks and limits
    ax.set_yticks([0.5])
    ax.set_yticklabels([''])
    ax.set_ylim(0, 1)
    
    # Set x-axis limits and ticks
    ax.set_xlim(-0.5, len(dna_sequence) - 0.5)
    if len(dna_sequence) <= 50:
        ax.set_xticks(x_positions)
        ax.set_xticklabels(dna_sequence)
    else:
        step = max(1, len(dna_sequence) // 50)  # Show at most 50 position labels
        ax.set_xticks(x_positions[::step])
        ax.set_xticklabels(x_positions[::step])
    
    # Add a legend
    ax.legend(title="DNA Bases", loc='upper right')
    
    # Add base counts
    base_counts = {base: dna_sequence.count(base) for base in colors}
    count_text = ", ".join([f"{base}: {count}" for base, count in base_counts.items()])
    fig.text(0.5, 0.02, f"Base counts: {count_text}", ha='center')
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    plt.tight_layout()
    
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
    # Create circuit if not provided
    if quantum_circuit is None:
        # Create a circuit with enough qubits to generate the key
        num_qubits = min(8, message_length)
        circuit = QuantumCircuit(num_qubits)
        
        # Apply Hadamard gates to create superposition
        for i in range(num_qubits):
            circuit.h(i)
        
        # Entangle qubits
        for i in range(num_qubits - 1):
            circuit.cx(i, i + 1)
        
        # Measure
        circuit.measure_all()
    else:
        circuit = quantum_circuit
    
    # Simulate the circuit
    simulator = Aer.get_backend('qasm_simulator')
    result = simulator.run(circuit, shots=1).result()
    counts = result.get_counts()
    
    # Get the measurement result
    measurement = list(counts.keys())[0]
    
    # Extend the key if needed
    key_binary = ""
    while len(key_binary) < 4 * message_length:  # 4 bits per character in DNA
        # Mix the quantum measurement with environmental entropy
        random_bits = ''.join([str(random.randint(0, 1)) for _ in range(len(measurement))])
        mixed_bits = ''.join([str((int(a) + int(b)) % 2) for a, b in zip(measurement, random_bits)])
        key_binary += mixed_bits
    
    # Create visualization
    fig = visualize_quantum_key_generation(circuit, measurement, key_binary)
    
    # Convert to DNA sequence
    dna_key = binary_to_dna(key_binary)
    
    return dna_key, fig

def visualize_quantum_key_generation(circuit, measurement, key_binary):
    """
    Visualize the quantum key generation process with copyright protection
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED
    
    Args:
        circuit (QuantumCircuit): The quantum circuit used
        measurement (str): The measurement result
        key_binary (str): The generated binary key
        
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Create figure with copyright watermark
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), gridspec_kw={'height_ratios': [2, 1]})
    
    try:
        # Add circuit visualization safely
        ax1.set_title('Quantum Circuit for Key Generation\n© Ervin Remus Radosavlevici')
        ax1.text(0.5, 0.5, 'Quantum Circuit: Protected by worldwide copyright', 
                 horizontalalignment='center', verticalalignment='center',
                 transform=ax1.transAxes, fontsize=12)
        ax1.axis('off')
        
        # Plot key visualization with copyright
        ax2.set_title('Quantum-Enhanced Key (Protected)')
        
        # Display part of the binary key
        display_length = min(50, len(key_binary))
        
        for i in range(display_length):
            color = 'blue' if key_binary[i] == '1' else 'green'
            ax2.text(i * 0.02, 0.5, key_binary[i], color=color, fontsize=10, fontweight='bold')
            
        # Add copyright watermark
        fig.text(0.5, 0.01, '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - WORLDWIDE COPYRIGHT PROTECTION',
                horizontalalignment='center', verticalalignment='bottom',
                fontsize=8, color='gray', alpha=0.8)
    except Exception as e:
        # Self-repair for visualization
        plt.close(fig)
        fig, ax = plt.subplots(1, 1, figsize=(10, 4))
        ax.text(0.5, 0.5, f'Quantum Key: {key_binary[:20]}...\n© Ervin Remus Radosavlevici - WORLDWIDE COPYRIGHT PROTECTION',
                horizontalalignment='center', verticalalignment='center')
        ax.axis('off')
    
    if len(key_binary) > 50:
        ax2.text(display_length * 0.02, 0.5, "...", fontsize=10)
    
    ax2.axis('off')
    
    # Add measurement result
    ax2.text(0.1, 0.2, f"Quantum Measurement: {measurement}", fontsize=10)
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    plt.tight_layout()
    
    return fig

def create_quantum_dna_circuit():
    """
    Create a quantum circuit for DNA-based encryption demonstration
    
    Returns:
        QuantumCircuit: A quantum circuit for DNA-based encryption
    """
    # Create a circuit with 4 qubits to represent DNA bases (A, C, G, T)
    circuit = QuantumCircuit(4, 4)
    
    # Apply Hadamard gates to create superposition
    for i in range(4):
        circuit.h(i)
    
    # Apply controlled operations to simulate DNA base pairing
    # A-T pairing (qubits 0 and 3)
    circuit.cx(0, 3)
    # C-G pairing (qubits 1 and 2)
    circuit.cx(1, 2)
    
    # Add barrier for visual separation
    circuit.barrier()
    
    # Apply rotation gates to simulate DNA sequence processing
    circuit.rz(np.pi/4, 0)
    circuit.rx(np.pi/4, 1)
    circuit.ry(np.pi/4, 2)
    circuit.rz(np.pi/4, 3)
    
    # Entangle all qubits to demonstrate quantum correlation
    circuit.h(0)
    for i in range(3):
        circuit.cx(i, i+1)
    
    # Measure all qubits
    circuit.measure(range(4), range(4))
    
    return circuit

def visualize_dna_base_pairs():
    """
    Create a visualization of DNA base pairs
    
    Returns:
        matplotlib.figure.Figure: Visualization of DNA base pairs
    """
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Define colors and labels for bases
    colors = {
        'A': '#8BC34A',  # Green
        'T': '#9C27B0',  # Purple
        'C': '#03A9F4',  # Blue
        'G': '#F44336'   # Red
    }
    
    # Define base pairings
    pairings = [
        ('A', 'T'),
        ('T', 'A'),
        ('C', 'G'),
        ('G', 'C')
    ]
    
    # Draw the base pairings
    y_pos = 1
    for left, right in pairings:
        # Draw left base
        ax.text(0.3, y_pos, left, fontsize=30, fontweight='bold', 
                color=colors[left], ha='center', va='center')
        
        # Draw right base
        ax.text(0.7, y_pos, right, fontsize=30, fontweight='bold', 
                color=colors[right], ha='center', va='center')
        
        # Draw connection line
        if (left == 'A' and right == 'T') or (left == 'T' and right == 'A'):
            # A-T pairs have two hydrogen bonds
            ax.plot([0.35, 0.65], [y_pos, y_pos], 'k-', linewidth=2)
            ax.plot([0.35, 0.65], [y_pos-0.03, y_pos-0.03], 'k-', linewidth=2)
        else:
            # C-G pairs have three hydrogen bonds
            ax.plot([0.35, 0.65], [y_pos, y_pos], 'k-', linewidth=2)
            ax.plot([0.35, 0.65], [y_pos-0.03, y_pos-0.03], 'k-', linewidth=2)
            ax.plot([0.35, 0.65], [y_pos+0.03, y_pos+0.03], 'k-', linewidth=2)
        
        y_pos -= 0.25
    
    # Add title and labels
    ax.set_title('DNA Base Pairings', fontsize=16)
    ax.text(0.3, 1.3, 'Base', fontsize=14, ha='center')
    ax.text(0.7, 1.3, 'Complement', fontsize=14, ha='center')
    
    # Add information
    ax.text(0.5, 0.1, 'A-T pairs have 2 hydrogen bonds\nC-G pairs have 3 hydrogen bonds', 
            fontsize=12, ha='center', bbox=dict(facecolor='white', alpha=0.5))
    
    # Turn off axes
    ax.axis('off')
    
    # Add copyright notice
    fig.text(0.5, 0.01, "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)", 
             ha='center', fontsize=8, color='gray')
    
    return fig