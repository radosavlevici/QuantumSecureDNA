import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st

import qiskit
from qiskit import QuantumCircuit, Aer, execute
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.algorithms import QSVC, VQC
from qiskit_machine_learning.kernels import QuantumKernel
from qiskit.visualization import plot_histogram

def load_iris_data():
    """
    Load and preprocess the Iris dataset
    
    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    # Load iris dataset
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # Take only the first two features for visualization
    y = iris.target
    
    # Standardize the features
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test, iris.target_names

def create_quantum_kernel(X_train):
    """
    Create a quantum kernel for machine learning
    
    Args:
        X_train: Training data
        
    Returns:
        QuantumKernel: A quantum kernel
    """
    # Determine the number of qubits needed based on feature dimension
    num_qubits = X_train.shape[1]
    
    # Create a feature map
    feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=2)
    
    # Create the quantum kernel
    quantum_instance = QuantumInstance(Aer.get_backend('qasm_simulator'), shots=1024)
    kernel = QuantumKernel(feature_map=feature_map, quantum_instance=quantum_instance)
    
    return kernel

def create_quantum_classifier(X_train, y_train):
    """
    Create and train a quantum support vector classifier
    
    Args:
        X_train: Training data
        y_train: Training labels
        
    Returns:
        QSVC: Trained quantum SVM classifier
    """
    # Create quantum kernel
    kernel = create_quantum_kernel(X_train)
    
    # Create the quantum SVM
    qsvc = QSVC(quantum_kernel=kernel)
    
    # Train the classifier
    qsvc.fit(X_train, y_train)
    
    return qsvc

def create_variational_quantum_classifier(X_train, y_train, num_qubits):
    """
    Create and train a variational quantum classifier
    
    Args:
        X_train: Training data
        y_train: Training labels
        num_qubits: Number of qubits to use
        
    Returns:
        VQC: Trained variational quantum classifier
    """
    # Create a feature map and variational form
    feature_map = ZZFeatureMap(feature_dimension=num_qubits, reps=2)
    var_form = RealAmplitudes(num_qubits=num_qubits, reps=1)
    
    # Create quantum instance
    quantum_instance = QuantumInstance(Aer.get_backend('qasm_simulator'), shots=1024)
    
    # Create the variational quantum classifier
    vqc = VQC(
        feature_map=feature_map,
        ansatz=var_form,
        loss='cross_entropy',
        optimizer='COBYLA',
        quantum_instance=quantum_instance
    )
    
    # Train the classifier
    vqc.fit(X_train, y_train)
    
    return vqc

def visualize_quantum_classifier_results(classifier, X_test, y_test, X_train, y_train, class_names=None):
    """
    Visualize the results of a quantum classifier
    
    Args:
        classifier: Trained quantum classifier
        X_test: Test data
        y_test: Test labels
        X_train: Training data
        y_train: Training labels
        class_names: Names of the classes
        
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Make predictions
    y_pred = classifier.predict(X_test)
    
    # Create figure with subplots
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Decision boundary plot
    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))
    
    # Create the mesh grid points as a 2D array of shape (n_points, 2)
    grid_points = np.c_[xx.ravel(), yy.ravel()]
    
    # Predict for all grid points (this may take time for quantum classifiers)
    try:
        # Limit to a smaller grid for quantum classifiers to save time
        step = max(1, len(grid_points) // 100)
        Z = classifier.predict(grid_points[::step])
        Z = np.repeat(Z, step)
        if len(Z) < len(grid_points):
            Z = np.append(Z, [Z[-1]] * (len(grid_points) - len(Z)))
        Z = Z.reshape(xx.shape)
        
        # Plot decision boundary
        axes[0].contourf(xx, yy, Z, alpha=0.3)
    except:
        # If prediction on the grid is too slow/costly, skip the contour
        pass
    
    # Plot training points
    scatter = axes[0].scatter(X_train[:, 0], X_train[:, 1], c=y_train, edgecolors='k', alpha=0.7)
    
    # Add test points
    axes[0].scatter(X_test[:, 0], X_test[:, 1], c=y_test, edgecolors='k', marker='X', s=100, alpha=0.7)
    
    if class_names is not None and len(class_names) > 0:
        axes[0].legend(handles=scatter.legend_elements()[0], labels=class_names)
    
    axes[0].set_xlabel('Feature 1')
    axes[0].set_ylabel('Feature 2')
    axes[0].set_title('Quantum Classifier Decision Boundary')
    
    # Accuracy and confusion matrix plot
    accuracy = accuracy_score(y_test, y_pred)
    
    # Create a simple confusion-like matrix visualization
    classes = np.unique(np.concatenate((y_train, y_test)))
    n_classes = len(classes)
    
    # Count prediction results
    confusion = np.zeros((n_classes, 2))  # For each class: [correct, incorrect]
    for true_label, pred_label in zip(y_test, y_pred):
        for i, class_label in enumerate(classes):
            if true_label == class_label:
                if true_label == pred_label:
                    confusion[i, 0] += 1  # Correct
                else:
                    confusion[i, 1] += 1  # Incorrect
    
    # Plot the results
    bar_width = 0.35
    indices = np.arange(n_classes)
    
    axes[1].bar(indices - bar_width/2, confusion[:, 0], bar_width, label='Correct')
    axes[1].bar(indices + bar_width/2, confusion[:, 1], bar_width, label='Incorrect')
    
    # Add class names if available
    if class_names is not None and len(class_names) == n_classes:
        axes[1].set_xticks(indices)
        axes[1].set_xticklabels(class_names)
    else:
        axes[1].set_xticks(indices)
        axes[1].set_xticklabels([f'Class {i}' for i in classes])
    
    axes[1].set_ylabel('Number of Samples')
    axes[1].set_title(f'Classification Results (Accuracy: {accuracy:.2f})')
    axes[1].legend()
    
    plt.tight_layout()
    return fig

def create_quantum_feature_map(num_qubits=2, reps=2):
    """
    Create a quantum feature map circuit for encoding classical data
    
    Args:
        num_qubits (int): Number of qubits
        reps (int): Number of repetitions of the feature map
        
    Returns:
        QuantumCircuit: Feature map circuit
    """
    # Create a quantum circuit for the feature map
    qc = QuantumCircuit(num_qubits)
    
    # Define a ZZ feature map manually for illustration
    for _ in range(reps):
        # Single-qubit rotations
        for i in range(num_qubits):
            qc.h(i)
            qc.rz(np.pi/4, i)  # Placeholder for data-dependent rotation
        
        # Two-qubit entangling gates
        for i in range(num_qubits):
            for j in range(i+1, num_qubits):
                qc.cx(i, j)
                qc.rz(np.pi/4, j)  # Placeholder for data-dependent rotation
                qc.cx(i, j)
    
    return qc

def visualize_quantum_encoding():
    """
    Create a visualization of quantum data encoding
    
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    # Create a sample 2D data point
    data_point = np.array([0.6, 0.8])
    
    # Create a feature map circuit
    feature_map = create_quantum_feature_map(num_qubits=2, reps=1)
    
    # Add data-dependent rotations to the circuit
    feature_map_with_data = QuantumCircuit(2)
    
    # First layer
    feature_map_with_data.h(0)
    feature_map_with_data.h(1)
    feature_map_with_data.rz(np.pi * data_point[0], 0)
    feature_map_with_data.rz(np.pi * data_point[1], 1)
    
    # Entangling layer
    feature_map_with_data.cx(0, 1)
    feature_map_with_data.rz(np.pi * data_point[0] * data_point[1], 1)
    feature_map_with_data.cx(0, 1)
    
    # Draw the circuit
    circuit_diagram = feature_map_with_data.draw(output='mpl', plot_barriers=False)
    
    # Create a figure to explain the encoding
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6), gridspec_kw={'width_ratios': [1, 2]})
    
    # Plot the original data point
    ax1.scatter(data_point[0], data_point[1], color='blue', s=100)
    ax1.set_xlim(-1, 1)
    ax1.set_ylim(-1, 1)
    ax1.set_xlabel('Feature 1')
    ax1.set_ylabel('Feature 2')
    ax1.set_title('Classical Data Point')
    ax1.grid(True)
    
    # Show the quantum encoding process
    ax2.text(0.5, 0.7, "Quantum Feature Encoding", fontsize=16, ha='center')
    ax2.text(0.5, 0.5, f"Data point ({data_point[0]:.2f}, {data_point[1]:.2f}) → Quantum State", 
             fontsize=14, ha='center')
    ax2.text(0.5, 0.3, "Encoded using rotation and entangling gates", fontsize=12, ha='center')
    ax2.axis('off')
    
    plt.tight_layout()
    return circuit_diagram, fig

def visualize_quantum_kernel_method():
    """
    Create a visualization explaining quantum kernel methods
    
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Create visual explanation
    ax.text(0.5, 0.9, "Quantum Kernel Methods", fontsize=20, ha='center')
    
    # Classical to quantum mapping
    ax.add_patch(plt.Rectangle((0.1, 0.7), 0.2, 0.1, fill=True, alpha=0.3, color='blue'))
    ax.text(0.2, 0.75, "Classical Data", ha='center', va='center')
    
    ax.arrow(0.3, 0.75, 0.1, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    ax.add_patch(plt.Rectangle((0.4, 0.7), 0.2, 0.1, fill=True, alpha=0.3, color='green'))
    ax.text(0.5, 0.75, "Quantum Feature Map", ha='center', va='center')
    
    ax.arrow(0.6, 0.75, 0.1, 0, head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    ax.add_patch(plt.Rectangle((0.7, 0.7), 0.2, 0.1, fill=True, alpha=0.3, color='red'))
    ax.text(0.8, 0.75, "Quantum State", ha='center', va='center')
    
    # Kernel calculation
    ax.arrow(0.2, 0.7, 0, -0.1, head_width=0.02, head_length=0.02, fc='black', ec='black')
    ax.arrow(0.8, 0.7, 0, -0.1, head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    ax.add_patch(plt.Rectangle((0.1, 0.5), 0.2, 0.1, fill=True, alpha=0.3, color='blue'))
    ax.text(0.2, 0.55, "Data Point x", ha='center', va='center')
    
    ax.add_patch(plt.Rectangle((0.7, 0.5), 0.2, 0.1, fill=True, alpha=0.3, color='red'))
    ax.text(0.8, 0.55, "Data Point y", ha='center', va='center')
    
    ax.arrow(0.2, 0.5, 0.25, -0.1, head_width=0.02, head_length=0.02, fc='black', ec='black')
    ax.arrow(0.8, 0.5, -0.25, -0.1, head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    ax.add_patch(plt.Rectangle((0.4, 0.3), 0.2, 0.1, fill=True, alpha=0.3, color='purple'))
    ax.text(0.5, 0.35, "Quantum Kernel\nK(x,y) = |⟨ϕ(x)|ϕ(y)⟩|²", ha='center', va='center')
    
    ax.arrow(0.5, 0.3, 0, -0.1, head_width=0.02, head_length=0.02, fc='black', ec='black')
    
    ax.add_patch(plt.Rectangle((0.3, 0.1), 0.4, 0.1, fill=True, alpha=0.3, color='orange'))
    ax.text(0.5, 0.15, "Classical Machine Learning Algorithm\n(e.g., SVM, Regression)", 
            ha='center', va='center')
    
    # Add explanation text
    ax.text(0.5, 0.02, "The quantum kernel measures similarity between data points\nin a quantum feature space", 
            ha='center', va='center', fontsize=10)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    return fig

def create_hybrid_quantum_classical_nn():
    """
    Create a visualization of a hybrid quantum-classical neural network
    
    Returns:
        matplotlib.figure.Figure: Visualization figure
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Draw classical input layer
    for i in range(5):
        circle = plt.Circle((0.1, 0.2 + i*0.15), 0.05, fill=True, alpha=0.7, color='blue')
        ax.add_patch(circle)
        if i == 0 or i == 4:
            ax.text(0.1, 0.2 + i*0.15, "x₁", ha='center', va='center', color='white')
        elif i == 1 or i == 3:
            ax.text(0.1, 0.2 + i*0.15, "x₂", ha='center', va='center', color='white')
        else:
            ax.text(0.1, 0.2 + i*0.15, "...", ha='center', va='center', color='white')
    
    # Draw connections to quantum layer
    for i in range(5):
        for j in range(4):
            ax.plot([0.15, 0.3], [0.2 + i*0.15, 0.3 + j*0.15], 'k-', alpha=0.3)
    
    # Draw quantum layer
    for i in range(4):
        quantum_symbol = plt.Rectangle((0.3, 0.25 + i*0.15), 0.15, 0.1, fill=True, alpha=0.7, color='green')
        ax.add_patch(quantum_symbol)
        ax.text(0.375, 0.3 + i*0.15, "Q", ha='center', va='center', color='white')
    
    # Draw connections to classical layer
    for i in range(4):
        for j in range(3):
            ax.plot([0.45, 0.6], [0.3 + i*0.15, 0.35 + j*0.15], 'k-', alpha=0.3)
    
    # Draw classical hidden layer
    for i in range(3):
        circle = plt.Circle((0.6, 0.35 + i*0.15), 0.05, fill=True, alpha=0.7, color='red')
        ax.add_patch(circle)
        ax.text(0.6, 0.35 + i*0.15, "h", ha='center', va='center', color='white')
    
    # Draw connections to output layer
    for i in range(3):
        ax.plot([0.65, 0.8], [0.35 + i*0.15, 0.5], 'k-', alpha=0.3)
    
    # Draw output layer
    circle = plt.Circle((0.8, 0.5), 0.05, fill=True, alpha=0.7, color='purple')
    ax.add_patch(circle)
    ax.text(0.8, 0.5, "y", ha='center', va='center', color='white')
    
    # Add layer labels
    ax.text(0.1, 0.8, "Classical\nInput Layer", ha='center', va='center')
    ax.text(0.375, 0.8, "Quantum\nLayer", ha='center', va='center')
    ax.text(0.6, 0.8, "Classical\nHidden Layer", ha='center', va='center')
    ax.text(0.8, 0.8, "Output\nLayer", ha='center', va='center')
    
    # Add explanation
    ax.text(0.5, 0.1, "Hybrid Quantum-Classical Neural Network", ha='center', va='center', fontsize=16)
    ax.text(0.5, 0.05, "Classical inputs are processed by quantum circuits, then further processed by classical layers",
            ha='center', va='center', fontsize=12)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    
    return fig
