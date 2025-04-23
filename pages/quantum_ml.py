import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from sklearn import datasets
import sys
import os

# Add the utils directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.qml_utils import (load_iris_data, create_quantum_classifier, 
                           visualize_quantum_classifier_results, create_quantum_feature_map,
                           visualize_quantum_encoding, visualize_quantum_kernel_method,
                           create_hybrid_quantum_classical_nn)

def app():
    st.title("Quantum Machine Learning")
    
    # Add copyright and advanced security notice
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #0066cc;'>
    <h3 style='color: #0066cc;'>ADVANCED QUANTUM MACHINE LEARNING</h3>
    <p>Featuring quantum-enhanced ML algorithms with proprietary optimizations</p>
    <p><b>© Ervin Remus Radosavlevici (ervin210@icloud.com)</b> - All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    # Quantum Machine Learning Concepts
    
    Quantum Machine Learning (QML) combines quantum computing with machine learning algorithms to potentially 
    achieve computational advantages over classical approaches. This page explores how quantum computing 
    can enhance machine learning and demonstrates key QML concepts and algorithms.
    """)
    
    # Create tabs for different concepts
    tabs = st.tabs(["QML Fundamentals", "Quantum Kernels", "Quantum Neural Networks", "QML Applications"])
    
    # QML Fundamentals tab
    with tabs[0]:
        st.header("QML Fundamentals")
        
        st.markdown("""
        ### What is Quantum Machine Learning?
        
        Quantum Machine Learning (QML) is an emerging field that combines quantum computing with machine learning methods. 
        The goal is to use quantum computers to enhance machine learning algorithms, potentially achieving exponential 
        speedups for certain tasks.
        
        ### Key Concepts in QML:
        
        **1. Quantum Data Encoding**  
        Classical data must be encoded into quantum states before processing. Common methods include:
        - Amplitude encoding
        - Basis encoding
        - Angle encoding
        - Quantum feature maps
        
        **2. Quantum Feature Spaces**  
        Quantum computers can access higher-dimensional feature spaces that might be inaccessible to classical computers.
        
        **3. Quantum Advantages**  
        - Potential exponential speedups for certain ML tasks
        - Access to quantum feature spaces
        - Enhanced pattern recognition capabilities
        - Ability to process quantum data directly
        
        **4. Hybrid Quantum-Classical Approaches**  
        Most current QML algorithms use a hybrid approach:
        - Classical computers handle pre/post-processing
        - Quantum computers perform specialized computational tasks
        - Parameters are optimized classically
        """)
        
        # Quantum data encoding visualization
        st.subheader("Quantum Data Encoding")
        
        st.markdown("""
        One of the fundamental steps in QML is encoding classical data into quantum states.
        The most common method is using a quantum feature map, which encodes data points 
        into the quantum Hilbert space.
        
        Let's visualize how a simple 2D data point can be encoded into a quantum state:
        """)
        
        # Show the quantum encoding visualization
        circuit_diagram, encoding_fig = visualize_quantum_encoding()
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("**Quantum Circuit for Data Encoding:**")
            st.pyplot(circuit_diagram)
        
        with col2:
            st.markdown("**Data Encoding Process:**")
            st.pyplot(encoding_fig)
        
        st.markdown("""
        In this example, a classical 2D data point is encoded into a quantum state using 
        rotation gates and entangling operations. The angles of rotation depend on the 
        feature values, creating a quantum state that represents the original data point.
        
        This encoding allows us to process the data using quantum operations, potentially
        revealing patterns that would be difficult to detect classically.
        """)
        
        # QML vs Classical ML comparison
        st.subheader("QML vs. Classical ML")
        
        # Create comparison table
        comparison_data = {
            "Feature": ["Data Processing", "Feature Spaces", "Training", "Speedup Potential", "Current Practical Uses"],
            "Classical ML": [
                "Sequential or parallel on classical hardware", 
                "Limited by computational resources", 
                "Gradient-based optimization, sampling, etc.", 
                "Limited by hardware improvements", 
                "Wide range of production applications"
            ],
            "Quantum ML": [
                "Quantum superposition and parallelism", 
                "Exponentially large Hilbert spaces", 
                "Variational circuits, quantum gradient estimation", 
                "Potential exponential speedup for specific problems", 
                "Experimental, promising for specific domains"
            ]
        }
        
        # Convert to DataFrame and display
        import pandas as pd
        comparison_df = pd.DataFrame(comparison_data)
        st.table(comparison_df)
        
        # Simple QML example
        st.subheader("Simple QML Example: Binary Classification")
        
        st.markdown("""
        Let's look at a simple example of how quantum computing can be used for classification.
        We'll create a basic quantum circuit that can separate two classes of data:
        """)
        
        # Create a simple classification circuit
        classification_circuit = QuantumCircuit(2, 1)
        classification_circuit.h(0)  # Create superposition
        classification_circuit.cx(0, 1)  # Entangle qubits
        classification_circuit.h(0)  # Apply Hadamard again
        classification_circuit.measure(0, 0)  # Measure first qubit
        
        # Draw the circuit
        st.markdown("**Simple Quantum Classification Circuit:**")
        circuit_fig = classification_circuit.draw(output='mpl')
        st.pyplot(circuit_fig)
        
        st.markdown("""
        This circuit can be used as a component in a variational quantum classifier.
        The parameters of the circuit would be adjusted during training to correctly
        classify data points.
        """)
    
    # Quantum Kernels tab
    with tabs[1]:
        st.header("Quantum Kernels")
        
        st.markdown("""
        ### Quantum Kernel Methods
        
        Kernel methods are a class of algorithms for pattern analysis. They work by mapping 
        data to a high-dimensional feature space where patterns become more easily separable.
        
        **Quantum kernels** leverage quantum computers to calculate kernel functions that might
        be exponentially expensive to compute classically.
        
        ### How Quantum Kernels Work:
        
        1. **Data Encoding**: Classical data points are encoded into quantum states
        2. **Kernel Evaluation**: The inner product between quantum states is calculated
        3. **Classical Processing**: The resulting kernel matrix is used in classical algorithms like SVM
        
        The key advantage is that quantum computers can efficiently access exponentially large
        feature spaces, potentially finding patterns that classical kernels cannot detect.
        """)
        
        # Quantum kernel visualization
        st.subheader("Quantum Kernel Visualization")
        
        # Show the quantum kernel method visualization
        kernel_fig = visualize_quantum_kernel_method()
        st.pyplot(kernel_fig)
        
        st.markdown("""
        The quantum kernel method uses a quantum computer to calculate the similarity between
        data points in a quantum feature space. This similarity measure (kernel) can then be
        used in classical machine learning algorithms like Support Vector Machines (SVM).
        
        The quantum advantage comes from the ability to calculate kernels in feature spaces
        that would be inaccessible to classical computers.
        """)
        
        # Interactive quantum kernel classifier
        st.subheader("Interactive Quantum Kernel Classifier")
        
        st.markdown("""
        Let's see a quantum kernel method in action for classifying the famous Iris dataset.
        We'll use a quantum kernel with a Support Vector Classifier (QSVC):
        """)
        
        # Prepare the data
        X_train, X_test, y_train, y_test, class_names = load_iris_data()
        
        st.markdown("""
        We've loaded the Iris dataset and taken the first two features for visualization.
        The dataset is split into training (80%) and testing (20%) sets.
        
        Now let's create and train a quantum kernel classifier:
        """)
        
        if st.button("Train Quantum Kernel Classifier", key="train_qkernel"):
            with st.spinner("Training quantum kernel classifier..."):
                # Create and train the quantum classifier
                qsvc = create_quantum_classifier(X_train, y_train)
                
                # Evaluate the classifier
                st.markdown("### Quantum Kernel SVM Results")
                results_fig = visualize_quantum_classifier_results(
                    qsvc, X_test, y_test, X_train, y_train, class_names
                )
                
                st.pyplot(results_fig)
                
                st.markdown("""
                The visualization shows:
                - Left: The decision boundary learned by the quantum kernel SVM
                - Right: The classification results showing correct and incorrect predictions
                
                The quantum kernel method can find complex decision boundaries by implicitly
                working in a high-dimensional quantum feature space.
                """)
        
        st.markdown("""
        ### Advantages of Quantum Kernels:
        
        - **Potentially Richer Features**: Access to quantum feature spaces
        - **Efficient Computation**: Quantum speedup for kernel calculation
        - **Novel Patterns**: Ability to detect patterns hard to find classically
        
        ### Challenges and Limitations:
        
        - **Noise in Current Devices**: Quantum noise affects accuracy
        - **Limited Qubits**: Restricts the size of problems
        - **Encoding Overhead**: Data encoding can be costly
        """)
    
    # Quantum Neural Networks tab
    with tabs[2]:
        st.header("Quantum Neural Networks")
        
        st.markdown("""
        ### Quantum Neural Networks (QNNs)
        
        Quantum Neural Networks are quantum circuits designed to perform machine learning tasks,
        analogous to classical neural networks. They typically consist of:
        
        1. **Data Encoding Layer**: Encodes classical data into quantum states
        2. **Trainable Layer(s)**: Quantum gates with adjustable parameters
        3. **Measurement Layer**: Extracts classical information for output
        
        QNNs are trained using variational methods, where the parameters are adjusted
        to minimize a cost function.
        """)
        
        # Visualize a hybrid quantum-classical neural network
        st.subheader("Hybrid Quantum-Classical Neural Network")
        
        # Show the hybrid QNN visualization
        hybrid_nn_fig = create_hybrid_quantum_classical_nn()
        st.pyplot(hybrid_nn_fig)
        
        st.markdown("""
        Most practical QNNs are hybrid quantum-classical networks, as shown above.
        They combine quantum circuits with classical neural network components:
        
        - Classical data is preprocessed and encoded into quantum states
        - Quantum circuits perform specialized computations
        - Results are processed by classical neural network layers
        - The entire system is trained end-to-end
        
        This hybrid approach allows us to leverage the strengths of both quantum and 
        classical computing.
        """)
        
        # QNN example
        st.subheader("Quantum Neural Network Example")
        
        st.markdown("""
        Let's examine a simple Quantum Neural Network circuit. This circuit
        consists of a data encoding layer followed by a trainable variational layer:
        """)
        
        # Create a simple QNN circuit
        num_qubits = 2
        qnn_circuit = QuantumCircuit(num_qubits)
        
        # Data encoding layer (fixed)
        qnn_circuit.h(0)
        qnn_circuit.h(1)
        qnn_circuit.rz(np.pi/4, 0)  # Placeholder for data-dependent rotation
        qnn_circuit.rz(np.pi/4, 1)  # Placeholder for data-dependent rotation
        qnn_circuit.cx(0, 1)
        
        # Trainable variational layer
        qnn_circuit.rz(np.pi/6, 0)  # Trainable parameter
        qnn_circuit.ry(np.pi/4, 0)  # Trainable parameter
        qnn_circuit.rz(np.pi/3, 1)  # Trainable parameter
        qnn_circuit.ry(np.pi/5, 1)  # Trainable parameter
        qnn_circuit.cx(0, 1)
        qnn_circuit.ry(np.pi/7, 0)  # Trainable parameter
        qnn_circuit.ry(np.pi/9, 1)  # Trainable parameter
        
        # Draw the circuit
        st.markdown("**Simple Quantum Neural Network Circuit:**")
        qnn_fig = qnn_circuit.draw(output='mpl')
        st.pyplot(qnn_fig)
        
        st.markdown("""
        In this QNN:
        - The first part (Hadamard and Rz gates) encodes the input data
        - The second part (Ry, Rz gates and CNOT) contains trainable parameters
        - When measured, the circuit output can be used for classification
        
        During training, we would adjust the angles of the rotational gates to 
        minimize the prediction error, similar to how we update weights in 
        classical neural networks.
        """)
        
        st.markdown("""
        ### QNN Training Process:
        
        1. **Forward Pass**: 
           - Encode classical data into quantum states
           - Apply parameterized quantum circuit
           - Measure to get predictions
        
        2. **Loss Calculation**:
           - Compare predictions with true labels
           - Calculate loss function
        
        3. **Parameter Update**:
           - Calculate gradients (using parameter shift or other methods)
           - Update parameters to minimize loss
        
        4. **Repeat** until convergence
        
        ### Potential Advantages of QNNs:
        
        - **Expressivity**: Ability to represent complex functions compactly
        - **Quantum Data**: Natural for processing quantum information
        - **Barren Plateaus**: Challenges in optimization due to flat gradients
        - **Hardware Limitations**: Current quantum devices have limited qubits and noise
        """)
        
        # Barren plateaus visualization
        st.subheader("Challenge: Barren Plateaus")
        
        # Create a visualization of the barren plateau problem
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create a 3D-looking surface with a mostly flat region
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        
        # Create a function with mostly flat regions and some structure
        Z = 0.01 * (X**2 + Y**2) + np.exp(-(X**2 + Y**2)/8) * np.cos(np.sqrt(X**2 + Y**2))
        
        # Plot the surface
        c = ax.contourf(X, Y, Z, 50, cmap='viridis')
        plt.colorbar(c, ax=ax, label='Loss value')
        
        # Add points to show optimization trajectory
        trajectory_x = [-4, -3, -2, -1.5, -1.2, -1.0, -0.8, -0.7, -0.65, -0.63]
        trajectory_y = [3, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0]
        ax.plot(trajectory_x, trajectory_y, 'ro-', markersize=6, linewidth=2)
        
        ax.set_xlabel('Parameter θ₁')
        ax.set_ylabel('Parameter θ₂')
        ax.set_title('Barren Plateau in QNN Loss Landscape')
        
        # Add text explanation
        ax.text(-4.5, 4.5, "Optimization becomes\nextremely slow in\nflat regions", 
                fontsize=12, bbox=dict(facecolor='white', alpha=0.7))
        
        st.pyplot(fig)
        
        st.markdown("""
        **Barren plateaus** are a significant challenge in training quantum neural networks.
        As the number of qubits increases, the loss landscape tends to become exponentially flat,
        making gradient-based optimization extremely difficult.
        
        Researchers are developing various strategies to address this challenge, including:
        - Careful circuit design and initialization
        - Layer-wise training approaches
        - Alternative optimization techniques
        - Problem-specific structure exploitation
        """)
    
    # QML Applications tab
    with tabs[3]:
        st.header("QML Applications")
        
        st.markdown("""
        ### Promising Applications of Quantum Machine Learning
        
        Quantum Machine Learning has the potential to impact numerous fields. Here are some of the
        most promising application areas:
        """)
        
        # Create expandable sections for different applications
        with st.expander("**Chemistry and Materials Science**", expanded=True):
            st.markdown("""
            Quantum Machine Learning can help discover new materials and optimize chemical reactions:
            
            - **Molecular Property Prediction**: QML models can predict properties of molecules more accurately
            - **Drug Discovery**: Accelerating the search for new pharmaceutical compounds
            - **Catalyst Design**: Finding better catalysts for industrial processes
            - **Materials Discovery**: Identifying materials with desired electronic or structural properties
            
            QML is particularly well-suited for these applications because quantum computers can naturally
            simulate quantum mechanical systems like molecules.
            """)
            
            # Create a simple visualization for chemistry applications
            fig, ax = plt.subplots(figsize=(8, 6))
            
            # Draw a simple molecule representation
            centers = [(0.5, 0.5), (0.3, 0.7), (0.7, 0.7), (0.4, 0.3), (0.6, 0.3)]
            labels = ['C', 'N', 'O', 'H', 'H']
            colors = ['black', 'blue', 'red', 'gray', 'gray']
            
            # Draw bonds
            ax.plot([centers[0][0], centers[1][0]], [centers[0][1], centers[1][1]], 'k-', linewidth=2)
            ax.plot([centers[0][0], centers[2][0]], [centers[0][1], centers[2][1]], 'k-', linewidth=2)
            ax.plot([centers[0][0], centers[3][0]], [centers[0][1], centers[3][1]], 'k-', linewidth=2)
            ax.plot([centers[0][0], centers[4][0]], [centers[0][1], centers[4][1]], 'k-', linewidth=2)
            
            # Draw atoms
            for (x, y), label, color in zip(centers, labels, colors):
                circle = plt.Circle((x, y), 0.08, facecolor=color, edgecolor='black', alpha=0.7)
                ax.add_patch(circle)
                ax.text(x, y, label, fontsize=14, ha='center', va='center', color='white')
            
            # Add quantum circuit representation
            circuit_x = 0.8
            circuit_y = 0.5
            circuit_width = 0.15
            circuit_height = 0.3
            
            # Draw quantum circuit box
            rect = plt.Rectangle((circuit_x - circuit_width/2, circuit_y - circuit_height/2),
                                circuit_width, circuit_height, facecolor='lightblue', alpha=0.7)
            ax.add_patch(rect)
            
            # Draw qubit lines
            line_y = [circuit_y - 0.1, circuit_y, circuit_y + 0.1]
            for y in line_y:
                ax.plot([circuit_x - circuit_width/2, circuit_x + circuit_width/2], 
                       [y, y], 'k-', linewidth=1)
            
            # Draw gates
            gate_positions = [(circuit_x - circuit_width/4, line_y[0]), 
                             (circuit_x, line_y[1]),
                             (circuit_x + circuit_width/4, line_y[2])]
            
            for x, y in gate_positions:
                gate = plt.Rectangle((x - 0.02, y - 0.02), 0.04, 0.04, facecolor='orange')
                ax.add_patch(gate)
            
            # Draw connection between molecule and circuit
            ax.arrow(0.7, 0.5, 0.05, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
            
            # Add prediction output
            ax.text(0.9, 0.5, "Properties\nPrediction", ha='center', va='center', fontsize=10,
                   bbox=dict(facecolor='green', alpha=0.2))
            
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.set_title("QML for Molecular Property Prediction")
            ax.axis('off')
            
            st.pyplot(fig)
        
        with st.expander("**Finance and Optimization**"):
            st.markdown("""
            QML can potentially transform financial modeling and optimization problems:
            
            - **Portfolio Optimization**: Finding optimal asset allocations more efficiently
            - **Risk Assessment**: Better modeling of complex financial risks
            - **Fraud Detection**: Identifying unusual patterns in transaction data
            - **Trading Strategies**: Discovering profitable trading algorithms
            - **Supply Chain Optimization**: Solving complex logistics problems
            
            Quantum algorithms like the Quantum Approximate Optimization Algorithm (QAOA) 
            are particularly promising for these combinatorial optimization problems.
            """)
        
        with st.expander("**Machine Learning Enhancement**"):
            st.markdown("""
            QML can enhance existing machine learning techniques:
            
            - **Faster Training**: Potential speedups for training large models
            - **Feature Selection**: Better identification of relevant features
            - **Dimensionality Reduction**: More effective data compression
            - **Clustering**: Finding complex patterns in high-dimensional data
            - **Anomaly Detection**: Identifying outliers with greater sensitivity
            
            These enhancements could improve machine learning across all application domains.
            """)
        
        with st.expander("**Quantum Data Processing**"):
            st.markdown("""
            QML is naturally suited for processing data from quantum systems:
            
            - **Quantum Sensor Data**: Processing output from quantum sensors
            - **Quantum Communication Networks**: Optimizing quantum networks
            - **Quantum Error Correction**: Improving quantum error correction codes
            - **Quantum Control**: Better control of quantum systems
            
            As quantum technologies advance, the ability to process quantum data
            will become increasingly important.
            """)
        
        # QML in DNA Security
        st.subheader("QML for DNA-Based Security")
        
        st.markdown("""
        Quantum Machine Learning offers unique advantages for DNA-based security systems:
        
        ### 1. Enhanced Pattern Recognition
        
        QML can identify complex patterns in DNA sequences that might be invisible to
        classical algorithms, enabling more sophisticated encryption and authentication schemes.
        
        ### 2. Quantum-Enhanced DNA Authentication
        
        Combining quantum states with DNA fingerprints creates multi-factor authentication
        systems that are extremely difficult to forge:
        
        - DNA provides a unique biological identifier
        - Quantum processing adds an additional security layer
        - QML algorithms verify the combined security features
        
        ### 3. Adaptive DNA Cryptography
        
        QML algorithms can continuously optimize DNA-based cryptographic protocols:
        
        - Learning from attack patterns
        - Adapting encryption parameters
        - Generating stronger quantum-DNA keys
        
        ### 4. Anomaly Detection in DNA Databases
        
        QML can detect unauthorized access or tampering in DNA databases:
        
        - Identifying suspicious patterns in access logs
        - Detecting subtle alterations to DNA records
        - Recognizing unauthorized data extraction attempts
        """)
        
        # Create a visualization of QML in DNA security
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Draw the DNA-QML security visualization
        # Add title
        ax.text(0.5, 0.95, "Quantum ML for DNA Security Applications", fontsize=16, ha='center', va='center')
        
        # Create four quadrants for different applications
        # Quadrant 1: Pattern Recognition
        ax.add_patch(plt.Rectangle((0.05, 0.55), 0.4, 0.35, fill=True, alpha=0.1, color='blue'))
        ax.text(0.25, 0.85, "Pattern Recognition", fontsize=12, ha='center', va='center')
        
        # Draw a DNA sequence pattern
        for i in range(10):
            ax.text(0.1 + i*0.035, 0.65, "ATGC"[i % 4], fontsize=10, ha='center', va='center',
                   color=['green', 'red', 'blue', 'purple'][i % 4])
        
        ax.plot([0.1, 0.45], [0.7, 0.7], 'k--', alpha=0.5)
        ax.text(0.25, 0.75, "QML Pattern Analysis", fontsize=8, ha='center', va='center')
        
        # Quadrant 2: Authentication
        ax.add_patch(plt.Rectangle((0.55, 0.55), 0.4, 0.35, fill=True, alpha=0.1, color='red'))
        ax.text(0.75, 0.85, "DNA Authentication", fontsize=12, ha='center', va='center')
        
        # Draw authentication elements
        ax.add_patch(plt.Rectangle((0.65, 0.65), 0.2, 0.1, fill=True, alpha=0.3, color='green'))
        ax.text(0.75, 0.7, "DNA + Quantum\nAuthentication", fontsize=8, ha='center', va='center')
        ax.text(0.75, 0.6, "✓ Verified", fontsize=10, ha='center', va='center', color='green')
        
        # Quadrant 3: Adaptive Cryptography
        ax.add_patch(plt.Rectangle((0.05, 0.1), 0.4, 0.35, fill=True, alpha=0.1, color='green'))
        ax.text(0.25, 0.4, "Adaptive Cryptography", fontsize=12, ha='center', va='center')
        
        # Draw adaptive elements
        ax.add_patch(plt.Circle((0.25, 0.25), 0.1, fill=True, alpha=0.3, color='purple'))
        ax.text(0.25, 0.25, "QML\nOptimizer", fontsize=8, ha='center', va='center')
        ax.arrow(0.25, 0.15, 0, -0.05, head_width=0.02, head_length=0.02, fc='black', ec='black')
        ax.text(0.25, 0.1, "Optimized Parameters", fontsize=8, ha='center', va='center')
        
        # Quadrant 4: Anomaly Detection
        ax.add_patch(plt.Rectangle((0.55, 0.1), 0.4, 0.35, fill=True, alpha=0.1, color='orange'))
        ax.text(0.75, 0.4, "Anomaly Detection", fontsize=12, ha='center', va='center')
        
        # Draw anomaly elements
        ax.plot([0.6, 0.7, 0.8, 0.9], [0.2, 0.25, 0.2, 0.2], 'b-', linewidth=1)
        ax.plot([0.7], [0.3], 'ro', markersize=8)
        ax.text(0.7, 0.3, "!", fontsize=10, ha='center', va='center', color='white')
        ax.text(0.75, 0.15, "Detected Anomaly", fontsize=8, ha='center', va='center', color='red')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        st.pyplot(fig)
        
        # Current limitations
        st.subheader("Current Limitations of QML")
        
        st.markdown("""
        Despite its promise, QML faces several important limitations:
        
        1. **Hardware Constraints**:
           - Limited number of qubits in current quantum computers
           - High error rates (noise) in quantum operations
           - Short coherence times
        
        2. **Algorithm Challenges**:
           - Difficulty in loading classical data efficiently
           - Barren plateau problem in training
           - Limited number of proven quantum advantages
        
        3. **Practical Considerations**:
           - Quantum resources are expensive and scarce
           - Need for hybrid approaches and quantum-classical interfaces
           - Lack of standardized tools and frameworks
        
        These limitations are active areas of research, and progress is being made
        in addressing each of them.
        """)
        
        # Future outlook
        st.subheader("Future Outlook")
        
        st.markdown("""
        The field of Quantum Machine Learning is evolving rapidly. Here are some trends
        to watch for in the coming years:
        
        - **Fault-Tolerant QML**: Algorithms designed to work on future fault-tolerant quantum computers
        - **NISQ-Era Applications**: Practical applications suitable for current noisy quantum devices
        - **Domain-Specific Advantage**: Identifying specific domains where QML provides the most value
        - **New Quantum Models**: Novel quantum-native machine learning models beyond classical analogs
        - **Integrated Quantum-Classical Systems**: Seamless integration of quantum components in classical ML pipelines
        
        As quantum hardware improves and algorithms mature, we can expect QML to play an increasingly
        important role in solving complex problems across multiple domains.
        """)

if __name__ == "__main__":
    app()
