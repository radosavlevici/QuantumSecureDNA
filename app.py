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

# Add Adobe font integration
st.markdown("""
<link rel="stylesheet" href="https://use.typekit.net/uiy1pot.css">
<style>
    h1, h2, h3, h4, h5, h6 {
        font-family: 'myriad-pro', sans-serif !important;
        font-weight: 600 !important;
    }
    p, li, div {
        font-family: 'adobe-clean', sans-serif !important;
        font-weight: 400 !important;
    }
    .stButton>button {
        font-family: 'adobe-clean', sans-serif !important;
    }
    .sidebar .sidebar-content {
        font-family: 'adobe-clean', sans-serif !important;
    }
    code {
        font-family: 'source-code-pro', monospace !important;
    }
</style>
""", unsafe_allow_html=True)

# Add a watermark and copyright information with advanced protection notice
st.sidebar.markdown("""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #ff3300;'>
<h3 style='color: #ff3300;'>© WORLDWIDE COPYRIGHT PROTECTION</h3>
<p style='font-weight: bold; text-transform: uppercase; text-align: center;'>GLOBAL SECURITY SYSTEM</p>
<p><b>Author:</b> Ervin Remus Radosavlevici</p>
<p><b>Personal Email:</b> ervin210@icloud.com</p>
<p><b>Copyright Status:</b> All Rights Reserved Globally</p>
<p><b>ADVANCED SECURITY FEATURES:</b></p>
<ul>
<li>DNA-BASED SECURITY with SELF-REPAIR Mechanisms</li>
<li>SELF-UPGRADE Quantum Algorithms</li>
<li>Advanced SELF-DEFENSE System</li>
<li>CODE THEFT Prevention Technology</li>
<li>COPYRIGHT IMMUNE Technology</li>
<li>Tamper-Proof Architecture</li>
<li>Worldwide Legal Protection</li>
</ul>
<p style='text-align: center; margin-top: 10px; padding: 5px; background-color: #ffeeee; font-weight: bold;'>PROTECTED BY INTERNATIONAL COPYRIGHT LAW</p>
<p style='text-align: center; font-size: 11px;'>Using premium Adobe.com fonts</p>
</div>
""", unsafe_allow_html=True)

# Add global Adobe fonts reference 
st.sidebar.markdown("""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #009933; margin-top: 15px;'>
<h3 style='color: #009933; font-family: "Myriad Pro", "Adobe Clean", sans-serif;'>PREMIUM TYPOGRAPHY</h3>
<p style='text-align: center;'><b>Using Adobe.com Professional Fonts:</b></p>
<ul>
<li style='font-family: "Myriad Pro", sans-serif;'>Myriad Pro</li>
<li style='font-family: "Adobe Clean", sans-serif;'>Adobe Clean</li>
<li style='font-family: "Source Code Pro", monospace;'>Source Code Pro</li>
</ul>
<p style='text-align: center; margin-top: 5px;'><small>Premium typography enhances the worldwide professional appearance</small></p>
</div>
""", unsafe_allow_html=True)

def main():
    st.title("Quantum Computing Educational Platform")
    st.subheader("Explore Quantum Computing Concepts, DNA Security, and Quantum Machine Learning")
    
    # Add global notice with enhanced worldwide protection statement
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 15px; border-radius: 8px; border: 2px solid #0066cc; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
    <h2 style='color: #0066cc; text-align: center; text-transform: uppercase; letter-spacing: 1px;'>WORLDWIDE ADVANCED SECURITY PLATFORM</h2>
    <hr style='border-top: 1px solid #0066cc; margin: 10px 0;'>
    <div style='display: flex; align-items: center; justify-content: center; margin-bottom: 15px;'>
        <div style='background-color: #0066cc; color: white; border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; margin-right: 10px;'>⚛️</div>
        <p style='font-size: 18px; font-weight: 600; margin: 0;'>Global Quantum-Enhanced DNA Security System</p>
    </div>
    <p style='text-align: center;'>Featuring advanced DNA-based security with quantum-powered SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE capabilities against CODE THEFT</p>
    <p style='text-align: center; font-weight: bold; font-size: 16px; margin-top: 10px; border-top: 1px solid #ddd; padding-top: 10px;'>© Ervin Remus Radosavlevici (ervin210@icloud.com)</p>
    <p style='text-align: center; font-style: italic; color: #555;'>All Rights Reserved Worldwide - Protected by International Copyright Laws - IMMUNE to Unauthorized Changes</p>
    </div>
    <div style='height: 20px;'></div>
    """, unsafe_allow_html=True)
    
    # Introduction section with global advanced features
    st.markdown("""
    <div style='font-family: "Adobe Clean", "Myriad Pro", sans-serif;'>
    <h3 style='color: #333; border-bottom: 1px solid #ddd; padding-bottom: 8px;'>WELCOME TO THE WORLDWIDE QUANTUM COMPUTING EDUCATIONAL PLATFORM</h3>
    
    <p>This globally accessible interactive resource helps you understand the fascinating world of quantum computing, 
    featuring advanced DNA-based security algorithms with self-repair, self-upgrade, and self-defense capabilities.</p>
    
    <div style='background-color: #f8f9fa; padding: 15px; border-radius: 5px; margin: 10px 0;'>
    <h4 style='color: #0066cc;'>ADVANCED SECURITY FEATURES:</h4>
    <ul>
    <li><strong>DNA-Based Security System</strong> - Quantum-enhanced encryption with SELF-REPAIR mechanisms</li>
    <li><strong>Code Theft Prevention</strong> - Advanced protection against unauthorized copying</li>
    <li><strong>Anti-Tampering Technology</strong> - SELF-DEFENSE against unauthorized modifications</li>
    <li><strong>Self-Upgrading Algorithms</strong> - Adaptive security that evolves against new threats</li>
    </ul>
    </div>
    
    <h4 style='color: #333; margin-top: 20px;'>WHAT YOU CAN LEARN HERE:</h4>
    <ul>
    <li><strong>Quantum Computing Fundamentals</strong> - Understand qubits, superposition, entanglement, and more</li>
    <li><strong>DNA-Based Security</strong> - Visualize how DNA structures can be used for advanced global security protocols</li>
    <li><strong>Quantum Machine Learning</strong> - Explore how quantum computing enhances machine learning algorithms</li>
    <li><strong>Quantum Algorithms</strong> - Interactive demonstrations of key quantum algorithms</li>
    </ul>
    
    <p style='margin-top: 15px;'>Use the sidebar to navigate through different topics and interactive demonstrations.</p>
    
    <p style='text-align: right; font-style: italic; color: #666; font-size: 12px;'>© Ervin Remus Radosavlevici (ervin210@icloud.com)</p>
    </div>
    """, unsafe_allow_html=True)
    
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
    
    # Add a strong watermark and global copyright notice at the bottom of every page
    st.markdown("""
    <div style='position: relative; margin-top: 60px;'>
        <div style='position: absolute; top: 0; left: 0; width: 100%; text-align: center; opacity: 0.05; transform: rotate(-30deg); font-size: 120px; z-index: -1; pointer-events: none;'>
            ERVIN REMUS RADOSAVLEVICI
        </div>
        <div style='border-top: 1px solid #ccc; padding-top: 20px; margin-top: 40px; text-align: center;'>
            <div style='font-size: 12px; color: #666;'>PROTECTED BY WORLDWIDE COPYRIGHT</div>
            <div style='font-size: 11px; color: #999; margin-top: 5px;'>
                This platform contains advanced DNA-based security algorithms with SELF-REPAIR, SELF-UPGRADE, 
                and SELF-DEFENSE capabilities against CODE THEFT. All content including algorithms, visualizations,
                and code is COPYRIGHT PROTECTED and IMMUNE to unauthorized changes.
            </div>
            <div style='font-size: 12px; color: #333; margin-top: 10px; font-weight: bold;'>
                © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - All Rights Reserved Globally
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
