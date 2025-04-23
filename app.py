import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import qiskit
from qiskit import QuantumCircuit

st.set_page_config(
    page_title="Quantum Computing Education Platform",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add a watermark and copyright information
st.sidebar.markdown("""
### © Copyright Information
- **Author:** Ervin Remus Radosavlevici
- **Email:** ervin210@icloud.com
- **Copyright:** All Rights Reserved
- **Features:** DNA-Based Security, Quantum Computing, Quantum Machine Learning
- **Security:** Self-repair, Self-upgrade, Self-defense capabilities
""")

# Add security notice
st.sidebar.info("""
**SECURITY NOTICE:**
This application includes advanced security features:
- DNA-based encryption
- Quantum secure protocols
- Copyright protection
- Immunity to unauthorized changes
""")

def main():
    st.title("Quantum Computing Educational Platform")
    st.subheader("Explore Quantum Computing Concepts, DNA Security, and Quantum Machine Learning")
    
    # Add global notice
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #0066cc;'>
    <h3 style='color: #0066cc;'>WORLDWIDE ADVANCED SECURITY PLATFORM</h3>
    <p>Featuring DNA-based security with self-repair, self-upgrade, and self-defense capabilities.</p>
    <p><b>© Ervin Remus Radosavlevici (ervin210@icloud.com)</b> - All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction section
    st.markdown("""
    Welcome to the Quantum Computing Educational Platform! This interactive resource helps you
    understand the fascinating world of quantum computing, DNA-based security algorithms, and
    quantum machine learning.
    
    ### What You Can Learn Here:
    - **Quantum Computing Fundamentals** - Understand qubits, superposition, entanglement, and more
    - **DNA-Based Security** - Visualize how DNA structures can be used for advanced security protocols
    - **Quantum Machine Learning** - Explore how quantum computing enhances machine learning algorithms
    - **Quantum Algorithms** - Interactive demonstrations of key quantum algorithms
    
    Use the sidebar to navigate through different topics and interactive demonstrations.
    """)
    
    # Featured visualization - Simple Qubit visualization
    st.header("Featured: Qubit Visualization")
    st.markdown("""
    A quantum bit or **qubit** is the fundamental unit of quantum information. Unlike
    classical bits that can be either 0 or 1, qubits can exist in a superposition of both
    states simultaneously.
    """)
    
    # Simple Bloch sphere visualization
    col1, col2 = st.columns([1, 1])
    
    with col1:
        theta = st.slider("Theta (θ) - Rotation from Z-axis", 0.0, np.pi, np.pi/2)
        phi = st.slider("Phi (φ) - Rotation around Z-axis", 0.0, 2*np.pi, 0.0)
    
    with col2:
        # Create a simple Bloch sphere visualization
        fig = plt.figure(figsize=(6, 6))
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
        
        # Draw the qubit state vector
        x_q = np.sin(theta) * np.cos(phi)
        y_q = np.sin(theta) * np.sin(phi)
        z_q = np.cos(theta)
        ax.quiver(0, 0, 0, x_q, y_q, z_q, color='purple', arrow_length_ratio=0.1)
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Bloch Sphere Representation of a Qubit')
        
        # Set the limits of the plot
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        
        st.pyplot(fig)
    
    # State information
    st.markdown(f"""
    ### Current Qubit State:
    - State vector: $|\\psi\\rangle = \\cos(\\theta/2)|0\\rangle + e^{{i\\phi}}\\sin(\\theta/2)|1\\rangle$
    - Probability of measuring $|0\\rangle$: {np.cos(theta/2)**2:.4f}
    - Probability of measuring $|1\\rangle$: {np.sin(theta/2)**2:.4f}
    """)
    
    # Navigation section
    st.header("Explore Topics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Quantum Basics")
        st.markdown("""
        - Qubits and superposition
        - Quantum gates
        - Quantum entanglement
        - Quantum teleportation
        """)
        if st.button("Explore Quantum Basics"):
            st.switch_page("pages/quantum_basics.py")
    
    with col2:
        st.subheader("DNA-Based Security")
        st.markdown("""
        - DNA encoding methods
        - DNA cryptography
        - Quantum-secured DNA algorithms
        - Applications in cybersecurity
        """)
        if st.button("Explore DNA Security"):
            st.switch_page("pages/dna_security.py")
    
    with col3:
        st.subheader("Quantum Machine Learning")
        st.markdown("""
        - Quantum neural networks
        - Quantum support vector machines
        - Quantum feature maps
        - Hybrid quantum-classical models
        """)
        if st.button("Explore Quantum ML"):
            st.switch_page("pages/quantum_ml.py")
    
    # Create a quantum circuit demonstration
    st.header("Quick Demo: Quantum Circuit")
    
    # Create a simple quantum circuit
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)  # Apply Hadamard gate to qubit 0
    circuit.cx(0, 1)  # Apply CNOT gate with control qubit 0 and target qubit 1
    circuit.measure([0, 1], [0, 1])  # Measure both qubits
    
    # Display the circuit
    st.text("Bell State Preparation Circuit:")
    circuit_svg = circuit.draw(output='mpl')
    st.pyplot(circuit_svg)
    
    st.markdown("""
    This simple circuit creates a **Bell state** - one of the most fundamental entangled 
    quantum states. It demonstrates quantum entanglement where the states of two qubits 
    become correlated in a way that's impossible in classical physics.
    """)

if __name__ == "__main__":
    main()
