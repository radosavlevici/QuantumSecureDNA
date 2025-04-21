import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import sys
import os

# Add the utils directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.quantum_utils import simulate_circuit, plot_quantum_state, visualize_quantum_fourier_transform

def app():
    st.title("Quantum Algorithms")
    
    # Introduction
    st.markdown("""
    # Quantum Algorithms
    
    Quantum algorithms leverage the principles of quantum mechanics to solve certain problems more efficiently than classical algorithms.
    This page explores key quantum algorithms and demonstrates their implementation using quantum circuits.
    """)
    
    # Create tabs for different algorithms
    tabs = st.tabs(["Grover's Algorithm", "Shor's Algorithm", "Quantum Fourier Transform", "Quantum Phase Estimation", "QAOA"])
    
    # Grover's Algorithm tab
    with tabs[0]:
        st.header("Grover's Algorithm")
        
        st.markdown("""
        ### Introduction to Grover's Algorithm
        
        Grover's algorithm is a quantum search algorithm that finds with high probability the unique input to a black box function that produces a particular output value.
        
        In plain terms, it can search an unsorted database quadratically faster than the best classical algorithm. For a database with N elements:
        - Classical search requires O(N) operations in the worst case
        - Grover's algorithm requires O(√N) operations
        
        This quadratic speedup is significant for large databases.
        """)
        
        # Illustrate the problem setup
        st.subheader("Problem Setup")
        
        st.markdown("""
        Imagine you have a database with N = 8 items, and you're looking for a specific item x:
        """)
        
        # Create visualization of a database search
        fig, ax = plt.subplots(figsize=(10, 4))
        
        # Draw database elements
        database_items = ['000', '001', '010', '011', '100', '101', '110', '111']
        marked_item = '101'  # The item we're looking for
        
        for i, item in enumerate(database_items):
            color = 'green' if item == marked_item else 'lightblue'
            rect = plt.Rectangle((i, 0), 0.8, 0.8, facecolor=color, alpha=0.7)
            ax.add_patch(rect)
            ax.text(i+0.4, 0.4, item, ha='center', va='center')
        
        ax.set_xlim(-0.2, len(database_items))
        ax.set_ylim(-0.2, 1)
        ax.set_title("Database with 8 items (N=8)")
        ax.text(len(database_items)/2, -0.1, "Green item is what we're searching for", ha='center')
        ax.axis('off')
        
        st.pyplot(fig)
        
        st.markdown("""
        **Classical Search**: In the worst case, we'd need to check all 8 items one by one.
        
        **Quantum Search**: Using Grover's algorithm, we can find the item in approximately √8 ≈ 3 operations.
        """)
        
        # Algorithm steps
        st.subheader("Algorithm Steps")
        
        st.markdown("""
        Grover's algorithm consists of the following steps:
        
        1. **Initialization**: Prepare a uniform superposition of all basis states
        2. **Oracle**: Apply an oracle function that marks the solution state by flipping its sign
        3. **Diffusion Operator**: Apply an operator that performs "inversion about the mean"
        4. **Repeat**: Steps 2-3 are repeated approximately √N times
        5. **Measurement**: Measure the register to obtain the solution with high probability
        
        After these operations, the amplitude of the marked state will be significantly larger than the others,
        making it much more likely to be observed upon measurement.
        """)
        
        # Interactive Grover's algorithm for 2 qubits
        st.subheader("Interactive Grover's Algorithm (2 qubits)")
        
        # Let the user choose which state to mark
        marked_state = st.selectbox(
            "Select state to search for:",
            ['00', '01', '10', '11'],
            index=2
        )
        
        # Create Grover's circuit based on the selected marked state
        def create_grover_circuit(marked_state):
            # Create a 2-qubit circuit
            qc = QuantumCircuit(2, 2)
            
            # Step 1: Initialize in uniform superposition
            qc.h(0)
            qc.h(1)
            qc.barrier()
            
            # Step 2: Oracle - mark the selected state
            if marked_state == '00':
                # For |00⟩, we need to flip the sign of |00⟩
                qc.z(0)  # Phase flip on |0⟩
                qc.z(1)  # Phase flip on |0⟩
            elif marked_state == '01':
                # For |01⟩, we need to flip the sign of |01⟩
                qc.z(0)  # Phase flip on |0⟩
                qc.x(1)  # Flip |1⟩ to |0⟩
                qc.z(1)  # Phase flip on |0⟩
                qc.x(1)  # Flip back
            elif marked_state == '10':
                # For |10⟩, we need to flip the sign of |10⟩
                qc.x(0)  # Flip |1⟩ to |0⟩
                qc.z(0)  # Phase flip on |0⟩
                qc.x(0)  # Flip back
                qc.z(1)  # Phase flip on |0⟩
            elif marked_state == '11':
                # For |11⟩, we need to flip the sign of |11⟩
                qc.x(0)  # Flip |1⟩ to |0⟩
                qc.x(1)  # Flip |1⟩ to |0⟩
                qc.z(0)  # Phase flip on |0⟩
                qc.z(1)  # Phase flip on |0⟩
                qc.x(0)  # Flip back
                qc.x(1)  # Flip back
            
            qc.barrier()
            
            # Step 3: Diffusion operator (inversion about the mean)
            qc.h(0)
            qc.h(1)
            qc.x(0)
            qc.x(1)
            qc.h(1)
            qc.cx(0, 1)
            qc.h(1)
            qc.x(0)
            qc.x(1)
            qc.h(0)
            qc.h(1)
            
            # Add measurement
            qc.measure([0, 1], [0, 1])
            
            return qc
        
        # Create the circuit
        grover_circuit = create_grover_circuit(marked_state)
        
        # Display the circuit
        st.markdown("**Grover's Algorithm Circuit for finding state |" + marked_state + "⟩:**")
        circuit_fig = grover_circuit.draw(output='mpl')
        st.pyplot(circuit_fig)
        
        # Run the simulation
        if st.button("Run Grover's Algorithm", key="run_grover"):
            # Execute the circuit
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(grover_circuit, simulator, shots=1024)
            result = job.result()
            counts = result.get_counts(grover_circuit)
            
            # Display the results
            st.markdown("### Measurement Results")
            
            hist_fig = plot_histogram(counts)
            st.pyplot(hist_fig)
            
            # Check if the marked state has the highest probability
            max_state = max(counts, key=counts.get)
            if max_state == marked_state:
                st.success(f"Success! The algorithm found the marked state |{marked_state}⟩ with high probability.")
            else:
                st.error(f"The algorithm did not find the marked state with highest probability. This could happen due to noise or other factors.")
            
            st.markdown("""
            Grover's algorithm found the marked state with much higher probability than the 25% we would expect from random guessing.
            
            This demonstrates the quadratic speedup that quantum searching provides. For larger databases, the advantage becomes even more significant.
            """)
        
        st.markdown("""
        ### Applications of Grover's Algorithm
        
        Grover's algorithm has many potential applications, including:
        
        - **Database searching**: Finding specific records in unsorted databases
        - **Cryptanalysis**: Breaking symmetric cryptographic systems
        - **Optimization problems**: Finding solutions to constraint satisfaction problems
        - **Element distinctness**: Determining if all elements in a set are distinct
        - **Collision finding**: Finding inputs that produce the same output from a function
        
        Many quantum algorithms use Grover's algorithm as a subroutine to achieve speedups.
        """)
    
    # Shor's Algorithm tab
    with tabs[1]:
        st.header("Shor's Algorithm")
        
        st.markdown("""
        ### Introduction to Shor's Algorithm
        
        Shor's algorithm is a quantum algorithm for integer factorization, developed by Peter Shor in 1994. It finds the prime factors of an integer N in polynomial time, offering an exponential speedup over the best-known classical algorithms.
        
        This has profound implications for cryptography, as many cryptographic systems (like RSA) rely on the difficulty of factoring large numbers.
        
        **Classical vs. Quantum Factoring:**
        - Best classical algorithm: sub-exponential time O(e^(1.9 * (log N)^(1/3) * (log log N)^(2/3)))
        - Shor's algorithm: polynomial time O((log N)^2 * (log log N) * (log log log N))
        
        For a 2048-bit number, this is the difference between billions of years and minutes.
        """)
        
        # Illustrate the problem
        st.subheader("The Factoring Problem")
        
        # Let user input a number to factor
        number_to_factor = st.number_input("Enter a number to factor:", min_value=4, max_value=100, value=15)
        
        if number_to_factor:
            # Find factors
            factors = []
            for i in range(2, int(np.sqrt(number_to_factor)) + 1):
                if number_to_factor % i == 0:
                    factors.append(i)
                    if i != number_to_factor // i:
                        factors.append(number_to_factor // i)
            
            factors.sort()
            
            if factors:
                factor_str = " × ".join([str(f) for f in factors])
                st.markdown(f"Factors of {number_to_factor}: {factor_str}")
            else:
                st.markdown(f"{number_to_factor} is a prime number (no factors other than 1 and itself)")
        
        st.markdown("""
        ### How Shor's Algorithm Works
        
        Shor's algorithm works by reducing the factoring problem to the problem of finding the period of a function, which can be solved efficiently using a quantum computer.
        
        The algorithm has two parts:
        
        1. **Classical Part**:
           - Choose a random number a < N
           - Check if a and N share factors using GCD (greatest common divisor)
           - If they do, we've found factors and can stop
           - If not, proceed to the quantum part
        
        2. **Quantum Part**:
           - Create a quantum circuit to find the period r of the function f(x) = a^x mod N
           - Use Quantum Fourier Transform to efficiently find the period
           - Once we have the period r, we can calculate factors with high probability using GCD
        """)
        
        # Simplified demonstration of Shor's Algorithm
        st.subheader("Simplified Demonstration")
        
        st.markdown("""
        A full implementation of Shor's algorithm requires many qubits and is beyond the scope of this demonstration.
        Instead, let's look at a simplified example showing the key quantum part - finding the period of a function using
        the Quantum Fourier Transform.
        
        Consider factoring N = 15:
        1. Choose a = 7 (random number coprime to 15)
        2. Calculate powers of a modulo N:
           - 7^1 mod 15 = 7
           - 7^2 mod 15 = 4
           - 7^3 mod 15 = 13
           - 7^4 mod 15 = 1
           - 7^5 mod 15 = 7 (repeats)
        
        The period is r = 4
        """)
        
        # Visualize the period function
        fig, ax = plt.subplots(figsize=(10, 5))
        
        # Choose some example parameters
        N = 15
        a = 7
        
        # Calculate the period
        values = []
        for x in range(12):
            values.append(pow(a, x, N))  # a^x mod N
        
        # Plot the function
        ax.plot(range(12), values, 'bo-', markersize=8)
        ax.grid(True)
        ax.set_xlabel('x')
        ax.set_ylabel('a^x mod N')
        ax.set_title(f'Period Finding: f(x) = {a}^x mod {N}')
        
        # Highlight the period
        period = 4  # For a=7, N=15, the period is 4
        ax.axvspan(0, period, alpha=0.2, color='red')
        ax.axvspan(period, 2*period, alpha=0.2, color='green')
        ax.axvspan(2*period, 3*period, alpha=0.2, color='blue')
        
        ax.text(period/2, max(values) + 0.5, f"Period = {period}", ha='center')
        
        st.pyplot(fig)
        
        st.markdown("""
        Once we know the period r = 4, we can find factors of N = 15:
        
        1. Calculate a^(r/2) = 7^2 = 49 ≡ 4 (mod 15)
        2. Calculate gcd(a^(r/2) - 1, N) = gcd(4 - 1, 15) = gcd(3, 15) = 3
        3. Calculate gcd(a^(r/2) + 1, N) = gcd(4 + 1, 15) = gcd(5, 15) = 5
        
        So the factors of 15 are 3 and 5.
        
        The key quantum part is finding this period efficiently using the Quantum Fourier Transform.
        """)
        
        # Show a simplified circuit for QFT
        st.subheader("Quantum Fourier Transform")
        
        st.markdown("""
        The Quantum Fourier Transform (QFT) is a key component of Shor's algorithm. It transforms the quantum state to the frequency domain, allowing us to extract the period information.
        
        Here's a simplified QFT circuit for 3 qubits:
        """)
        
        # Create a QFT circuit
        qft_circuit = visualize_quantum_fourier_transform(3)
        
        # Draw the circuit
        qft_fig = qft_circuit.draw(output='mpl')
        st.pyplot(qft_fig)
        
        st.markdown("""
        In the actual Shor's algorithm, the QFT is applied to the output register after computing the modular exponentiation function in superposition. This allows us to extract the period with high probability.
        
        ### Implications for Cryptography
        
        Shor's algorithm has profound implications for cryptography:
        
        - **RSA Cryptosystem** would be broken, as it relies on the difficulty of factoring large numbers
        - **Elliptic Curve Cryptography** would also be vulnerable
        - **Post-Quantum Cryptography** is being developed to resist quantum attacks
        
        This is why quantum-resistant cryptographic methods are an active area of research.
        """)
    
    # Quantum Fourier Transform tab
    with tabs[2]:
        st.header("Quantum Fourier Transform")
        
        st.markdown("""
        ### Introduction to Quantum Fourier Transform
        
        The Quantum Fourier Transform (QFT) is the quantum analogue of the classical Discrete Fourier Transform.
        It transforms a quantum state from the computational basis to the Fourier basis, essentially converting
        between the time and frequency domains.
        
        The QFT is a fundamental building block for many quantum algorithms, including:
        - Shor's factoring algorithm
        - Quantum phase estimation
        - Quantum counting
        - Hidden subgroup problems
        
        What makes the QFT powerful is that it can be implemented efficiently on a quantum computer, requiring
        only O(n²) gates for an n-qubit system, compared to O(2ⁿ log 2ⁿ) operations for the classical FFT on 2ⁿ points.
        """)
        
        # Mathematical description
        st.subheader("Mathematical Description")
        
        st.markdown("""
        Mathematically, the QFT on an n-qubit state |x⟩ is defined as:
        
        $$|x\\rangle \\mapsto \\frac{1}{\\sqrt{2^n}} \\sum_{y=0}^{2^n-1} e^{2\\pi i xy/2^n} |y\\rangle$$
        
        where x and y are integers from 0 to 2ⁿ-1.
        
        In other words, it maps each basis state |x⟩ to a superposition of all basis states, with amplitudes
        determined by complex exponentials related to the original state.
        """)
        
        # QFT Circuit
        st.subheader("QFT Circuit")
        
        st.markdown("""
        The QFT circuit consists of Hadamard gates and controlled rotation gates.
        Let's build and visualize the QFT circuit for different numbers of qubits:
        """)
        
        # Let user select the number of qubits
        num_qubits = st.slider("Number of qubits for QFT:", 2, 5, 3, key="qft_qubits")
        
        # Create QFT circuit
        qft_circuit = visualize_quantum_fourier_transform(num_qubits)
        
        # Draw the circuit
        qft_fig = qft_circuit.draw(output='mpl')
        st.pyplot(qft_fig)
        
        st.markdown(f"""
        This circuit implements the QFT on {num_qubits} qubits. It consists of:
        
        1. Hadamard gates on each qubit
        2. Controlled phase rotations between qubits
        3. Swap gates at the end to reverse the qubit order
        
        The circuit has a total of O(n²) gates, making it efficient compared to the classical FFT.
        """)
        
        # Example: QFT applied to a basis state
        st.subheader("Example: QFT on a Basis State")
        
        # Let user select a basis state
        if num_qubits <= 3:
            basis_states = [f"|{format(i, '0' + str(num_qubits) + 'b')}⟩" for i in range(2**num_qubits)]
            selected_state = st.selectbox("Select a basis state:", basis_states, key="qft_state")
            state_index = basis_states.index(selected_state)
            
            # Create circuit to prepare the selected state
            qft_demo = QuantumCircuit(num_qubits)
            
            # Prepare the selected basis state
            state_bits = format(state_index, '0' + str(num_qubits) + 'b')
            for i, bit in enumerate(state_bits):
                if bit == '1':
                    qft_demo.x(i)
            
            # Apply QFT
            qft_demo.barrier()
            
            # Add Hadamard gates
            for qubit in range(num_qubits):
                qft_demo.h(qubit)
                
                # Apply controlled phase rotations
                for target_qubit in range(qubit + 1, num_qubits):
                    qft_demo.cp(np.pi/float(2**(target_qubit-qubit)), qubit, target_qubit)
            
            # Swap qubits
            for qubit in range(num_qubits//2):
                qft_demo.swap(qubit, num_qubits-qubit-1)
            
            # Draw circuit
            st.markdown(f"**QFT applied to {selected_state}:**")
            demo_fig = qft_demo.draw(output='mpl')
            st.pyplot(demo_fig)
            
            # Run simulation
            if st.button("Simulate QFT", key="sim_qft"):
                # Get statevector result
                statevector = simulate_circuit(qft_demo, get_statevector=True)
                
                # Display the result
                st.markdown("**Output State After QFT:**")
                
                # Create a bar chart of the amplitudes
                fig, ax = plt.subplots(figsize=(10, 6))
                
                # Get state labels and probabilities
                states = [format(i, '0' + str(num_qubits) + 'b') for i in range(2**num_qubits)]
                probs = np.abs(statevector)**2
                
                # Plot the probabilities
                ax.bar(states, probs)
                ax.set_ylim(0, 1)
                ax.set_xlabel('Basis States')
                ax.set_ylabel('Probability')
                ax.set_title(f'Quantum State After QFT on {selected_state}')
                
                st.pyplot(fig)
                
                # Display phase information
                st.markdown("**Phase Information:**")
                
                # Create a polar plot to show phases
                fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
                
                # Get the phases
                phases = np.angle(statevector)
                
                # Plot the phases
                for i, (prob, phase) in enumerate(zip(probs, phases)):
                    if prob > 0.01:  # Only show significant amplitudes
                        ax.plot([0, phase], [0, np.sqrt(prob)], marker='o', label=f'|{states[i]}⟩')
                
                ax.set_rticks([0.25, 0.5, 0.75, 1])
                ax.set_rlabel_position(45)
                ax.set_title('Phase Information (Polar Plot)')
                ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
                
                st.pyplot(fig)
                
                st.markdown(f"""
                After applying the QFT to {selected_state}, we get a superposition of all basis states with
                different phases. This demonstrates how the QFT transforms a single basis state into a
                superposition with specific phase relationships.
                """)
        else:
            st.markdown("""
            For more than 3 qubits, the state visualization becomes too complex to display here.
            """)
        
        # Applications of QFT
        st.subheader("Applications of QFT")
        
        st.markdown("""
        The Quantum Fourier Transform has many important applications in quantum computing:
        
        1. **Shor's Algorithm**: QFT is used to find the period of a function, which enables factoring large numbers.
        
        2. **Quantum Phase Estimation**: QFT helps estimate the eigenvalues of a unitary operator.
        
        3. **Quantum Counting**: QFT is used to estimate the number of solutions to a search problem.
        
        4. **Hidden Subgroup Problem**: QFT is essential for solving problems like finding hidden periods and subgroups.
        
        5. **Quantum Signal Processing**: QFT can be used to analyze quantum signals, similar to how classical FFT is used for signal processing.
        
        The QFT's ability to efficiently transform between time and frequency domains is what makes
        many quantum algorithms exponentially faster than their classical counterparts.
        """)
    
    # Quantum Phase Estimation tab
    with tabs[3]:
        st.header("Quantum Phase Estimation")
        
        st.markdown("""
        ### Introduction to Quantum Phase Estimation
        
        Quantum Phase Estimation (QPE) is a quantum algorithm for estimating the eigenvalues of a unitary operator.
        It is a fundamental subroutine in many quantum algorithms, including Shor's algorithm and quantum simulation.
        
        Given a unitary operator U and an eigenstate |ψ⟩ such that U|ψ⟩ = e^(2πiθ)|ψ⟩, the QPE algorithm estimates
        the phase θ with high precision.
        
        This is incredibly useful because many quantum problems can be reduced to finding eigenvalues of unitary operators.
        """)
        
        # Phase estimation problem
        st.subheader("The Phase Estimation Problem")
        
        st.markdown("""
        Consider a unitary operator U with an eigenstate |ψ⟩ such that:
        
        $$U|\\psi\\rangle = e^{2\\pi i \\theta}|\\psi\\rangle$$
        
        where θ is the phase we want to estimate.
        
        In many quantum algorithms, knowing this phase gives us the answer to the computational problem.
        For example, in Shor's algorithm, the phase encodes information about the period of a function.
        """)
        
        # Visualization of eigenvalues on unit circle
        fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
        
        # Draw unit circle
        theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(theta, np.ones_like(theta), 'k-', alpha=0.3)
        
        # Draw some eigenvalues
        phases = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi, 5*np.pi/4, 3*np.pi/2, 7*np.pi/4]
        labels = ['1', 'e^(iπ/4)', 'i', 'e^(3iπ/4)', '-1', 'e^(5iπ/4)', '-i', 'e^(7iπ/4)']
        
        for phase, label in zip(phases, labels):
            ax.plot([0, phase], [0, 1], marker='o', markersize=8)
            ax.text(phase, 1.1, label, ha='center', va='center')
        
        ax.set_rticks([])
        ax.set_xticks(phases)
        ax.set_xticklabels([])
        ax.set_title('Eigenvalues of a Unitary Operator (Unit Circle)')
        
        st.pyplot(fig)
        
        # QPE Algorithm steps
        st.subheader("Quantum Phase Estimation Algorithm")
        
        st.markdown("""
        The QPE algorithm consists of the following steps:
        
        1. **Initialization**:
           - Create register 1 with t qubits initialized to |0⟩
           - Create register 2 initialized to the eigenstate |ψ⟩
        
        2. **Superposition**: Apply Hadamard gates to all qubits in register 1
        
        3. **Controlled Unitary Operations**:
           - Apply controlled-U^(2^0) to the first qubit and register 2
           - Apply controlled-U^(2^1) to the second qubit and register 2
           - ...
           - Apply controlled-U^(2^(t-1)) to the t-th qubit and register 2
        
        4. **Inverse QFT**: Apply the inverse Quantum Fourier Transform to register 1
        
        5. **Measurement**: Measure register 1 to obtain an estimate of the phase θ
        """)
        
        # Simplified QPE circuit
        st.subheader("Quantum Phase Estimation Circuit")
        
        st.markdown("""
        Let's examine a simplified Quantum Phase Estimation circuit:
        """)
        
        # Create a simplified QPE circuit
        precision_qubits = 3  # Number of qubits for precision
        eigenstate_qubits = 1  # Number of qubits for eigenstate
        
        qpe_circuit = QuantumCircuit(precision_qubits + eigenstate_qubits, precision_qubits)
        
        # Label the qubits
        qpe_circuit.barrier()
        
        # Step 1: Initialize the eigenstate in the last qubit
        # (For simplicity, we'll use |1⟩ as our eigenstate of a phase gate)
        qpe_circuit.x(precision_qubits)
        qpe_circuit.barrier()
        
        # Step 2: Apply Hadamard gates to the precision qubits
        for qubit in range(precision_qubits):
            qpe_circuit.h(qubit)
        qpe_circuit.barrier()
        
        # Step 3: Apply controlled unitary operations
        # For simplicity, we'll use a phase gate with phase π/4 as our unitary U
        for qubit in range(precision_qubits):
            angle = 2**qubit * np.pi/4
            # Equivalent to applying U^(2^qubit)
            qpe_circuit.cp(angle, qubit, precision_qubits)
        qpe_circuit.barrier()
        
        # Step 4: Apply inverse QFT to the precision qubits
        # For 3 qubits:
        qpe_circuit.h(2)
        qpe_circuit.cp(-np.pi/2, 1, 2)
        qpe_circuit.h(1)
        qpe_circuit.cp(-np.pi/4, 0, 2)
        qpe_circuit.cp(-np.pi/2, 0, 1)
        qpe_circuit.h(0)
        qpe_circuit.barrier()
        
        # Step 5: Measure the precision qubits
        for qubit in range(precision_qubits):
            qpe_circuit.measure(qubit, qubit)
        
        # Draw the circuit
        qpe_fig = qpe_circuit.draw(output='mpl')
        st.pyplot(qpe_fig)
        
        st.markdown("""
        In this example, we're estimating the phase of a unitary operator (a phase gate with phase π/4).
        The precision qubits determine how accurately we can estimate the phase.
        """)
        
        # Run simulation
        if st.button("Run Phase Estimation", key="run_qpe"):
            # Execute the circuit
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(qpe_circuit, simulator, shots=1024)
            result = job.result()
            counts = result.get_counts(qpe_circuit)
            
            # Display the results
            st.markdown("### Measurement Results")
            
            hist_fig = plot_histogram(counts)
            st.pyplot(hist_fig)
            
            st.markdown("""
            The measurement results show the binary representation of our estimated phase.
            
            For this example, we used a unitary with phase θ = 1/8 (π/4 normalized to 2π),
            so the ideal measurement should be binary "001" (reading from right to left),
            which represents the fraction 1/8.
            
            The fact that we see this with high probability indicates the algorithm is working correctly.
            """)
        
        # Applications
        st.subheader("Applications of Quantum Phase Estimation")
        
        st.markdown("""
        Quantum Phase Estimation is a crucial subroutine in many quantum algorithms:
        
        1. **Shor's Algorithm**: QPE is used to find the period of a function for factoring.
        
        2. **Quantum Simulation**: QPE helps determine energy levels of quantum systems.
        
        3. **HHL Algorithm**: QPE is used in solving linear systems of equations.
        
        4. **Quantum Counting**: QPE enables counting the number of solutions to a problem.
        
        5. **Quantum Machine Learning**: Many QML algorithms use QPE for eigenvalue estimation.
        
        The ability to efficiently estimate eigenvalues gives quantum computers an advantage
        for many scientific and mathematical problems.
        """)
    
    # QAOA tab
    with tabs[4]:
        st.header("Quantum Approximate Optimization Algorithm (QAOA)")
        
        st.markdown("""
        ### Introduction to QAOA
        
        The Quantum Approximate Optimization Algorithm (QAOA) is a hybrid quantum-classical algorithm designed to find approximate solutions to combinatorial optimization problems. Developed by Edward Farhi, Jeffrey Goldstone, and Sam Gutmann in 2014, it's particularly well-suited for near-term quantum computers.
        
        QAOA is important because:
        - It can tackle NP-hard problems that are difficult for classical computers
        - It's implementable on NISQ (Noisy Intermediate-Scale Quantum) devices
        - It has applications in logistics, finance, machine learning, and more
        - It bridges classical and quantum computing through its hybrid approach
        """)
        
        # Explain optimization problems
        st.subheader("Combinatorial Optimization Problems")
        
        st.markdown("""
        QAOA aims to solve combinatorial optimization problems of the form:
        
        $$\\text{Maximize or Minimize } C(z) = \\sum_i C_i(z)$$
        
        where:
        - $z$ is a bit string representing a candidate solution
        - $C(z)$ is a cost function to be optimized
        - $C_i(z)$ are terms in the cost function
        
        Examples of such problems include:
        - MaxCut (partition a graph to maximize cut edges)
        - Traveling Salesman Problem
        - Maximum Independent Set
        - Portfolio Optimization
        """)
        
        # Example: MaxCut problem
        st.subheader("Example: MaxCut Problem")
        
        st.markdown("""
        Let's consider the MaxCut problem as an example:
        
        **Goal**: Divide the nodes of a graph into two sets such that the number of edges between the sets is maximized.
        
        For a simple undirected graph:
        """)
        
        # Create a visualization of a simple graph
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Define a simple graph
        G = {
            'nodes': [(0.3, 0.7), (0.7, 0.7), (0.5, 0.3), (0.2, 0.4), (0.8, 0.4)],
            'edges': [(0, 1), (0, 3), (1, 2), (1, 4), (2, 3), (2, 4), (3, 4)]
        }
        
        # Draw the graph
        for i, (x, y) in enumerate(G['nodes']):
            circle = plt.Circle((x, y), 0.05, facecolor='skyblue', edgecolor='black')
            ax.add_patch(circle)
            ax.text(x, y, str(i), ha='center', va='center')
        
        for i, j in G['edges']:
            xi, yi = G['nodes'][i]
            xj, yj = G['nodes'][j]
            ax.plot([xi, xj], [yi, yj], 'k-')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_title('Example Graph for MaxCut')
        ax.axis('off')
        
        st.pyplot(fig)
        
        st.markdown("""
        A possible cut of this graph might put nodes 0, 3 in one set and nodes 1, 2, 4 in another set.
        This cut would have 4 edges crossing between the sets.
        
        The MaxCut problem can be formulated as minimizing the cost function:
        
        $$C(z) = -\\sum_{(i,j) \\in E} \\frac{1 - z_i z_j}{2}$$
        
        where $z_i, z_j \\in \\{-1, 1\\}$ represent which set each node belongs to.
        """)
        
        # QAOA algorithm steps
        st.subheader("How QAOA Works")
        
        st.markdown("""
        QAOA works through the following steps:
        
        1. **Problem Encoding**: Map the optimization problem to a Hamiltonian (quantum energy function)
        
        2. **Circuit Construction**: Create a parameterized quantum circuit with:
           - A mixer Hamiltonian ($H_B$) that explores the solution space
           - A problem Hamiltonian ($H_C$) that encodes the cost function
        
        3. **Quantum Evolution**: Apply these Hamiltonians in alternating layers:
           $e^{-i\\beta_p H_B} e^{-i\\gamma_p H_C} \\cdots e^{-i\\beta_1 H_B} e^{-i\\gamma_1 H_C}$
        
        4. **Measurement**: Measure the resulting quantum state to obtain candidate solutions
        
        5. **Classical Optimization**: Use classical algorithms to optimize the parameters ($\\beta_i, \\gamma_i$)
        
        6. **Iteration**: Repeat steps 3-5 until convergence
        """)
        
        # Create a QAOA circuit for MaxCut
        st.subheader("QAOA Circuit for MaxCut")
        
        st.markdown("""
        Let's create a simple QAOA circuit for a MaxCut problem on a 3-node graph:
        """)
        
        # Create a simplified QAOA circuit for a 3-node graph
        qaoa_circuit = QuantumCircuit(3, 3)
        
        # Parameters (would be optimized in practice)
        gamma = 0.8  # Problem Hamiltonian parameter
        beta = 0.6   # Mixer Hamiltonian parameter
        
        # Initial state: superposition of all states
        for i in range(3):
            qaoa_circuit.h(i)
        qaoa_circuit.barrier()
        
        # Problem Hamiltonian evolution for edges (0,1), (1,2), (0,2)
        # For edge (i,j), we apply exp(-i*gamma*Z_i*Z_j)
        
        # Edge (0,1)
        qaoa_circuit.cx(0, 1)
        qaoa_circuit.rz(2*gamma, 1)
        qaoa_circuit.cx(0, 1)
        
        # Edge (1,2)
        qaoa_circuit.cx(1, 2)
        qaoa_circuit.rz(2*gamma, 2)
        qaoa_circuit.cx(1, 2)
        
        # Edge (0,2)
        qaoa_circuit.cx(0, 2)
        qaoa_circuit.rz(2*gamma, 2)
        qaoa_circuit.cx(0, 2)
        
        qaoa_circuit.barrier()
        
        # Mixer Hamiltonian evolution
        for i in range(3):
            qaoa_circuit.rx(2*beta, i)
        
        qaoa_circuit.barrier()
        
        # Measure all qubits
        for i in range(3):
            qaoa_circuit.measure(i, i)
        
        # Draw the circuit
        qaoa_fig = qaoa_circuit.draw(output='mpl')
        st.pyplot(qaoa_fig)
        
        st.markdown("""
        This circuit demonstrates a single layer (p=1) of QAOA for a 3-node graph with edges between all pairs of nodes.
        
        In practice:
        - We would use multiple layers (higher p) for better approximation
        - The parameters γ and β would be optimized using a classical optimizer
        - The circuit would be run many times to sample from the probability distribution
        """)
        
        # Run QAOA simulation
        if st.button("Run QAOA Simulation", key="run_qaoa"):
            # Execute the circuit
            simulator = Aer.get_backend('qasm_simulator')
            job = execute(qaoa_circuit, simulator, shots=1024)
            result = job.result()
            counts = result.get_counts(qaoa_circuit)
            
            # Display the results
            st.markdown("### Measurement Results")
            
            hist_fig = plot_histogram(counts)
            st.pyplot(hist_fig)
            
            # Evaluate the cut values
            st.markdown("### Cut Evaluation")
            
            # Define the cost function
            def evaluate_cut(bitstring):
                # Convert bitstring to spin values (-1 or 1)
                spins = [1 if bit == '0' else -1 for bit in bitstring]
                
                # Evaluate the cut size
                edges = [(0,1), (1,2), (0,2)]
                cut_size = sum(1 for i, j in edges if spins[i] != spins[j])
                
                return cut_size, spins
            
            # Evaluate all measured states
            results = []
            for bitstring, count in counts.items():
                cut_size, spins = evaluate_cut(bitstring)
                partition = ["Set A" if spin == 1 else "Set B" for spin in spins]
                results.append((bitstring, count, cut_size, partition))
            
            # Sort by count (most frequently observed)
            results.sort(key=lambda x: x[1], reverse=True)
            
            # Display the top results
            st.markdown("**Top measured states and their cut sizes:**")
            
            for bitstring, count, cut_size, partition in results[:5]:
                prob = count / 1024
                st.markdown(f"- State |{bitstring}⟩: Probability = {prob:.4f}, Cut Size = {cut_size}")
                st.markdown(f"  Partition: Node 0 → {partition[0]}, Node 1 → {partition[1]}, Node 2 → {partition[2]}")
            
            # Find the optimal solution
            optimal = max(results, key=lambda x: x[2])
            
            st.markdown(f"""
            **Best solution found:**
            - State |{optimal[0]}⟩ with Cut Size = {optimal[2]}
            - This partitions the nodes as: Node 0 → {optimal[3][0]}, Node 1 → {optimal[3][1]}, Node 2 → {optimal[3][2]}
            
            This demonstrates how QAOA samples from solutions with a bias toward better cuts.
            With more circuit layers and optimized parameters, the probability of sampling the
            optimal solution would increase.
            """)
        
        # Applications and advantages
        st.subheader("Applications and Advantages of QAOA")
        
        st.markdown("""
        ### Advantages of QAOA:
        
        - **Implementable on NISQ devices**: Doesn't require error correction
        - **Versatile**: Can be applied to many combinatorial optimization problems
        - **Tunable accuracy**: The approximation ratio improves with more circuit layers
        - **Hybrid approach**: Leverages the strengths of both quantum and classical computing
        
        ### Applications:
        
        - **Logistics and Supply Chain**: Vehicle routing, scheduling, facility location
        - **Finance**: Portfolio optimization, risk management
        - **Machine Learning**: Feature selection, clustering
        - **Network Design**: Traffic flow optimization, communication network design
        - **Chemistry**: Molecular configuration optimization
        
        QAOA represents one of the most promising near-term applications of quantum computing,
        with potential to deliver practical advantages before fully fault-tolerant quantum computers
        are available.
        """)

if __name__ == "__main__":
    app()
