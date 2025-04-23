import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
import sys
import os

# Add the utils directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.dna_security import (DNA_BASES, DNA_TO_BINARY, BINARY_TO_DNA, 
                              dna_encrypt, dna_decrypt, visualize_dna_encryption, 
                              visualize_dna_sequence, quantum_enhanced_dna_key,
                              create_quantum_dna_circuit, visualize_dna_base_pairs)

def app():
    st.title("DNA-Based Security")
    
    # Add copyright and advanced security notice
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #0066cc;'>
    <h3 style='color: #0066cc;'>ADVANCED DNA-BASED SECURITY SYSTEM</h3>
    <p>Self-repair | Self-upgrade | Self-defense | Anti-theft protection</p>
    <p><b>© Ervin Remus Radosavlevici (ervin210@icloud.com)</b> - All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    # DNA-Based Security Algorithms
    
    DNA (deoxyribonucleic acid) cryptography is an emerging field that uses DNA properties and biological operations
    for encryption and security. When combined with quantum computing, it offers potentially unbreakable encryption methods.
    
    This page explores the concepts of DNA-based security and how quantum computing enhances these techniques.
    """)
    
    # Create tabs for different concepts
    tabs = st.tabs(["DNA Basics", "DNA Encoding", "Quantum-Enhanced DNA Security", "Applications"])
    
    # DNA Basics tab
    with tabs[0]:
        st.header("DNA Structure and Properties")
        
        st.markdown("""
        DNA (deoxyribonucleic acid) is a molecule composed of two polynucleotide chains that coil around each other
        to form a double helix. It carries genetic instructions for the development, functioning, growth, and reproduction
        of all known organisms.
        
        ### DNA Building Blocks
        
        DNA consists of four nucleotide bases:
        - **Adenine (A)** - pairs with Thymine
        - **Thymine (T)** - pairs with Adenine
        - **Guanine (G)** - pairs with Cytosine
        - **Cytosine (C)** - pairs with Guanine
        
        These base pairs form the rungs of the DNA ladder, while sugar and phosphate molecules form the sides.
        """)
        
        # DNA visualization
        st.subheader("DNA Double Helix Structure")
        
        dna_fig = visualize_dna_base_pairs()
        st.pyplot(dna_fig)
        
        st.markdown("""
        ### DNA Properties Useful for Cryptography
        
        DNA has several properties that make it valuable for cryptographic applications:
        
        1. **Massive Parallelism** - DNA can perform many operations simultaneously
        2. **Huge Storage Capacity** - 1 gram of DNA can store up to 215 petabytes of data
        3. **Complementary Base Pairing** - Provides a natural mechanism for encoding/decoding
        4. **Randomness and Complexity** - DNA sequences can be highly random and complex
        5. **Energy Efficiency** - DNA computing requires much less energy than electronic computing
        
        These properties make DNA an interesting medium for encryption and security algorithms.
        """)
    
    # DNA Encoding tab
    with tabs[1]:
        st.header("DNA Encoding Methods")
        
        st.markdown("""
        ### Binary-to-DNA Encoding
        
        One of the basic methods of DNA cryptography is encoding binary data using DNA bases.
        A common encoding scheme maps 2 bits to each DNA base:
        
        - 00 → A (Adenine)
        - 01 → T (Thymine)
        - 10 → G (Guanine)
        - 11 → C (Cytosine)
        
        Using this encoding, any binary data can be represented as a DNA sequence.
        """)
        
        # Interactive encoding example
        st.subheader("Interactive DNA Encoding")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Text to DNA Encoder**")
            plaintext = st.text_input("Enter text to encode as DNA:", "Hello World")
            
            if plaintext:
                # Convert to binary
                binary = ''.join(format(ord(char), '08b') for char in plaintext)
                
                # Convert binary to DNA
                dna_sequence = ''
                for i in range(0, len(binary), 2):
                    if i+1 < len(binary):
                        dna_sequence += BINARY_TO_DNA[binary[i:i+2]]
                    else:
                        dna_sequence += BINARY_TO_DNA[binary[i] + '0']
                
                # Display results
                st.markdown(f"**Binary representation:** `{binary[:50]}{'...' if len(binary) > 50 else ''}`")
                st.markdown(f"**DNA sequence:** `{dna_sequence[:50]}{'...' if len(dna_sequence) > 50 else ''}`")
                
                # Visualize the DNA sequence
                dna_viz = visualize_dna_sequence(dna_sequence, "Encoded DNA Sequence")
                st.pyplot(dna_viz)
        
        with col2:
            st.markdown("**DNA to Text Decoder**")
            dna_input = st.text_input("Enter DNA sequence to decode:", "ACTGACTG")
            
            valid_input = all(base in DNA_BASES for base in dna_input.upper())
            
            if dna_input and valid_input:
                # Convert DNA to binary
                binary = ''
                for base in dna_input.upper():
                    binary += DNA_TO_BINARY[base]
                
                # Convert binary to text
                text = ''
                for i in range(0, len(binary), 8):
                    if i+8 <= len(binary):
                        byte = binary[i:i+8]
                        text += chr(int(byte, 2))
                
                # Display results
                st.markdown(f"**Binary representation:** `{binary[:50]}{'...' if len(binary) > 50 else ''}`")
                st.markdown(f"**Decoded text:** `{text}`")
            elif dna_input:
                st.error("Invalid DNA sequence. Use only A, T, G, C.")
        
        st.markdown("""
        ### DNA-Based Encryption
        
        DNA-based encryption typically involves:
        
        1. **Encoding** - Converting plaintext to DNA sequence
        2. **Encryption Operations** - Manipulating the DNA sequence (e.g., substitution, insertion, deletion)
        3. **Key Generation** - Using DNA or hybrid methods to generate keys
        4. **Decryption** - Reversing the encryption operations using the key
        
        Let's explore a simple DNA XOR encryption method:
        """)
        
        # DNA XOR encryption example
        st.subheader("DNA XOR Encryption")
        
        plaintext = st.text_input("Enter text to encrypt:", "Secret message", key="encrypt_text")
        key = st.text_input("Enter encryption key:", "quantum", key="encrypt_key")
        
        if plaintext and key:
            # Encrypt the plaintext
            encrypted_dna = dna_encrypt(plaintext, key)
            
            # Display the encryption visualization
            st.markdown("### Encryption Process")
            encryption_viz = visualize_dna_encryption(plaintext, key)
            st.pyplot(encryption_viz)
            
            # Display the encrypted DNA
            st.markdown(f"**Encrypted DNA sequence:** `{encrypted_dna[:50]}{'...' if len(encrypted_dna) > 50 else ''}`")
            
            # Decrypt button
            if st.button("Decrypt", key="decrypt_button"):
                decrypted_text = dna_decrypt(encrypted_dna, key)
                
                if decrypted_text == plaintext:
                    st.success(f"Successfully decrypted: {decrypted_text}")
                else:
                    st.error(f"Decryption failed or produced incorrect result: {decrypted_text}")
    
    # Quantum-Enhanced DNA Security tab
    with tabs[2]:
        st.header("Quantum-Enhanced DNA Security")
        
        st.markdown("""
        Combining quantum computing with DNA-based cryptography creates extremely powerful security methods.
        Quantum computing can enhance DNA cryptography in several ways:
        
        1. **Quantum Key Generation** - Using quantum randomness for truly random keys
        2. **Quantum Encryption** - Applying quantum operations to DNA-encoded data
        3. **Quantum Authentication** - Verifying identity using quantum properties
        4. **Quantum-Safe Protocols** - Designing protocols resistant to quantum attacks
        
        Let's explore some of these concepts:
        """)
        
        # Quantum key generation for DNA encryption
        st.subheader("Quantum Key Generation for DNA Encryption")
        
        st.markdown("""
        Quantum computers can generate truly random encryption keys using quantum randomness.
        These keys can then be used in DNA cryptography for enhanced security.
        
        The following demonstration shows how a quantum circuit can generate a random key for DNA encryption:
        """)
        
        # Create a quantum key generation demonstration
        message_length = st.slider("Message length (characters):", 5, 50, 10, key="qkey_length")
        
        if st.button("Generate Quantum Key", key="qkey_button"):
            # Generate a quantum-enhanced key
            binary_key, qkey_viz = quantum_enhanced_dna_key(message_length)
            
            # Convert to DNA for visualization
            dna_key = ''
            for i in range(0, len(binary_key), 2):
                if i+1 < len(binary_key):
                    dna_key += BINARY_TO_DNA[binary_key[i:i+2]]
            
            # Display the visualization
            st.pyplot(qkey_viz)
            
            st.markdown(f"**Generated binary key:** `{binary_key[:50]}{'...' if len(binary_key) > 50 else ''}`")
            st.markdown(f"**Equivalent DNA key:** `{dna_key[:50]}{'...' if len(dna_key) > 50 else ''}`")
            
            st.markdown("""
            This key is truly random due to quantum properties, making it impossible to predict
            even with unlimited computational power.
            """)
        
        # Quantum-DNA circuit
        st.subheader("Quantum-DNA Circuit")
        
        st.markdown("""
        Here's a simple quantum circuit that demonstrates how quantum operations can be used
        with DNA-encoded data. This circuit uses 4 qubits to represent the 4 DNA bases and 
        creates quantum correlations between them:
        """)
        
        # Create and display the quantum-DNA circuit
        qdna_circuit = create_quantum_dna_circuit()
        qdna_fig = qdna_circuit.draw(output='mpl')
        st.pyplot(qdna_fig)
        
        st.markdown("""
        In this circuit:
        - Qubits 0-3 represent DNA bases A, T, G, C
        - Hadamard gates create superpositions of all possible bases
        - CNOT gates create correlations between complementary base pairs (A-T, G-C)
        
        When measured, this circuit produces patterns that can be used for DNA encryption or authentication.
        """)
        
        # Simulate the quantum-DNA circuit
        if st.button("Simulate Quantum-DNA Circuit", key="qdna_sim"):
            # Run the simulation
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(qdna_circuit, simulator, shots=1024)
            result = job.result()
            counts = result.get_counts(qdna_circuit)
            
            # Display the results
            st.markdown("### Measurement Results")
            from qiskit.visualization import plot_histogram
            hist_fig = plot_histogram(counts)
            st.pyplot(hist_fig)
            
            st.markdown("""
            The measurement results show the probability distribution of different bit patterns.
            These patterns can be mapped back to DNA sequences for use in cryptography.
            
            Notice that certain patterns appear more frequently due to the quantum correlations
            we introduced in the circuit. This demonstrates how quantum properties can influence
            DNA-based encryption.
            """)
        
        st.markdown("""
        ### Quantum-Resistant DNA Cryptography
        
        As quantum computers advance, they may threaten traditional cryptographic methods.
        However, DNA-based quantum cryptography offers resistance to quantum attacks by:
        
        1. **High Complexity** - Using the vast complexity of DNA sequences
        2. **Biological Operations** - Incorporating operations that are difficult to simulate quantumly
        3. **Hybrid Approaches** - Combining quantum and classical techniques
        4. **Multi-layer Security** - Implementing multiple layers of encryption
        
        These approaches make DNA-based quantum cryptography a promising candidate for
        post-quantum cryptographic systems.
        """)
    
    # Applications tab
    with tabs[3]:
        st.header("Applications of DNA-Based Quantum Security")
        
        st.markdown("""
        DNA-based quantum security has numerous potential applications across various fields:
        
        ### 1. Secure Communication
        
        **DNA-QKD (Quantum Key Distribution)** - Using DNA to store and transmit quantum encryption keys.
        
        **Bio-Quantum Channels** - Creating communication channels that combine biological and quantum properties.
        
        **Steganographic Methods** - Hiding encrypted messages within longer DNA sequences.
        """)
        
        # DNA steganography visualization
        st.subheader("DNA Steganography Example")
        
        # Create a simple visualization of DNA steganography
        fig, ax = plt.subplots(figsize=(10, 3))
        
        # Create a mock DNA sequence with hidden message
        visible_dna = "ATGCATGCATGCATGCATGCATGCATGCATGCATGCATGCATGC"
        hidden_message = "SECRET"
        hidden_positions = [4, 12, 20, 28, 36, 38]
        
        # Color map for bases
        color_map = {
            'A': '#00FF00',  # Green
            'T': '#FF0000',  # Red
            'G': '#0000FF',  # Blue
            'C': '#FFFF00'   # Yellow
        }
        
        # Display the DNA sequence with hidden message highlighted
        for i, base in enumerate(visible_dna):
            if i in hidden_positions:
                ax.text(i, 0, base, fontsize=14, ha='center', va='center', 
                        color='white', bbox=dict(facecolor='purple', alpha=0.9))
            else:
                ax.text(i, 0, base, fontsize=14, ha='center', va='center', 
                        color='black', bbox=dict(facecolor=color_map[base], alpha=0.7))
        
        ax.set_xlim(-1, len(visible_dna))
        ax.set_ylim(-0.5, 0.5)
        ax.set_title("DNA Steganography: Secret Message Hidden in DNA Sequence")
        ax.axis('off')
        
        st.pyplot(fig)
        
        st.markdown("""
        In DNA steganography, secret messages are hidden within larger DNA sequences. The positions of 
        specific bases or patterns can encode information, making it extremely difficult to detect 
        that a message exists.
        
        ### 2. Cybersecurity
        
        **Bio-inspired Authentication** - Using DNA-like patterns for multi-factor authentication.
        
        **Quantum DNA Signatures** - Creating unforgeable digital signatures based on quantum DNA properties.
        
        **Secure Data Storage** - Storing sensitive data in DNA with quantum encryption.
        """)
        
        # DNA-based authentication visualization
        st.subheader("DNA-Based Authentication")
        
        # Create a visualization of DNA authentication
        fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
        
        # User DNA "fingerprint"
        user_dna = "ATCGATCGATCG"
        ax1.text(0.5, 0.5, "User DNA Profile", fontsize=12, ha='center', va='center')
        ax1.text(0.5, 0.3, user_dna, fontsize=10, ha='center', va='center', 
                bbox=dict(facecolor='lightblue', alpha=0.5))
        ax1.axis('off')
        
        # Quantum processing
        ax2.text(0.5, 0.7, "Quantum Verification", fontsize=12, ha='center', va='center')
        ax2.text(0.5, 0.5, "1. Encode as qubits\n2. Apply quantum operations\n3. Measure results", 
                fontsize=10, ha='center', va='center')
        ax2.text(0.5, 0.2, "Quantum Circuit", fontsize=10, ha='center', va='center', 
                bbox=dict(facecolor='lightgreen', alpha=0.5))
        ax2.axis('off')
        
        # Authentication result
        ax3.text(0.5, 0.5, "Authentication Result", fontsize=12, ha='center', va='center')
        ax3.text(0.5, 0.3, "Access Granted", fontsize=14, ha='center', va='center', 
                color='white', bbox=dict(facecolor='green', alpha=0.7))
        ax3.axis('off')
        
        # Add arrows connecting the steps
        plt.tight_layout()
        st.pyplot(fig)
        
        st.markdown("""
        ### 3. Healthcare and Bioinformatics
        
        **Secure Genomic Data** - Protecting sensitive genomic information with quantum-DNA encryption.
        
        **Private Biomedical Analysis** - Enabling secure computation on encrypted biological data.
        
        **Personalized Medicine** - Securing patient-specific medical information.
        
        ### 4. Financial and Legal Applications
        
        **Quantum-DNA Blockchain** - Creating immutable ledgers with DNA-based quantum security.
        
        **Smart Contracts** - Implementing self-executing contracts with DNA-based verification.
        
        **Intellectual Property Protection** - Securing patents and trade secrets with DNA watermarks.
        
        ### 5. Government and Defense
        
        **Covert Communications** - Developing undetectable communication channels.
        
        **Secure Military Communications** - Creating military-grade encryption systems.
        
        **Intelligence Gathering** - Securing sensitive intelligence data.
        """)
        
        # Future applications
        st.subheader("Future Potential Applications")
        
        st.markdown("""
        As quantum computing and DNA technologies advance, we can expect many more applications:
        
        - **Quantum DNA Computing** - New computational paradigms that combine quantum and DNA computing
        - **Synthetic Biology Security** - Security protocols based on engineered biological systems
        - **Quantum-Bio Sensors** - Hybrid sensors with unprecedented sensitivity and security
        - **Self-Healing Security Systems** - Systems that adapt and evolve against new threats
        - **Brain-Computer Interface Security** - Securing direct neural interfaces with quantum-DNA methods
        
        The integration of quantum computing, DNA science, and cybersecurity is still in its early stages,
        but it represents one of the most promising frontiers in information security.
        """)

if __name__ == "__main__":
    app()
