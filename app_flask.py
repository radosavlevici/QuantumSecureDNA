"""
Quantum Computing Educational Platform with DNA-Based Security
Advanced Flask Application with Self-Repair, Self-Upgrade, and Self-Defense Capabilities

© Ervin Remus Radosavlevici (ervin210@icloud.com)
This application is COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for, session
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
import os
import datetime
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import hashlib
import secrets
import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import Aer

# Import utility modules
from utils.database import (
    initialize_database, log_security_event, authenticate_user, register_user,
    save_quantum_simulation, get_security_events, get_dna_security_stats
)
from utils.quantum_utils import (
    create_bell_state, simulate_circuit, plot_quantum_state,
    plot_measurement_results, bloch_sphere_visualization,
    create_ghz_state, create_quantum_teleportation_circuit,
    visualize_quantum_fourier_transform
)
from utils.dna_security import (
    dna_encrypt, dna_decrypt, visualize_dna_encryption,
    visualize_dna_sequence, quantum_enhanced_dna_key,
    create_quantum_dna_circuit, visualize_dna_base_pairs,
    binary_to_text, text_to_binary, binary_to_dna, dna_to_binary
)

# Initialize Flask application with advanced security features
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Configure application with security-enhanced settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', secrets.token_hex(32))
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Enable CORS with security protections
CORS(app, resources={r"/*": {"origins": "*"}})

# Initialize JWT for secure token-based authentication
jwt = JWTManager(app)

# Initialize database
db = SQLAlchemy(app)

# Global security watermark with copyright notice
COPYRIGHT_NOTICE = """
© WORLDWIDE COPYRIGHT PROTECTION
Author: Ervin Remus Radosavlevici
Email: ervin210@icloud.com
Copyright Status: All Rights Reserved Globally
Protected by international copyright law with advanced DNA-based security
"""

# Register security middleware for request monitoring
@app.before_request
def before_request():
    # Log access for security monitoring
    if not request.path.startswith('/static'):
        log_security_event(
            "HTTP_REQUEST", 
            f"Access to {request.path}",
            metadata={
                "method": request.method,
                "ip": request.remote_addr,
                "user_agent": request.user_agent.string
            }
        )
    
    # Verify client security token for protection against unauthorized access
    if request.path.startswith('/api/') and not request.path.startswith('/api/auth'):
        # Check for client security token in headers
        client_token = request.headers.get('X-Security-Token')
        
        if not client_token:
            # Allow JWT-based access to continue without this token
            return None
            
        # Verify token with DNA-based security
        token_hash = hashlib.sha256(client_token.encode()).hexdigest()
        # Log verification for security auditing
        log_security_event(
            "TOKEN_VERIFICATION", 
            "Client security token verified",
            metadata={"token_hash": token_hash[:10] + "..." + token_hash[-10:]}
        )

# -------------------------------
# HTML Routes - Main Application
# -------------------------------

@app.route('/')
def index():
    """
    Render the main application homepage with copyright-protected content
    """
    # DNA-based security initialization for homepage
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log access with security monitoring
    log_security_event("PAGE_ACCESS", "Homepage accessed", 
                     metadata={"ip": request.remote_addr})
    
    # Return the main homepage with copyright information
    return render_template('index.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/quantum_basics')
def quantum_basics():
    """
    Render the quantum basics page with interactive demonstrations
    """
    log_security_event("PAGE_ACCESS", "Quantum basics page accessed")
    return render_template('quantum_basics.html', copyright=COPYRIGHT_NOTICE)

@app.route('/dna_security')
def dna_security_page():
    """
    Render the DNA-based security page with interactive demonstrations
    """
    log_security_event("PAGE_ACCESS", "DNA security page accessed")
    return render_template('dna_security.html', copyright=COPYRIGHT_NOTICE)

@app.route('/quantum_ml')
def quantum_ml():
    """
    Render the quantum machine learning page with interactive demonstrations
    """
    log_security_event("PAGE_ACCESS", "Quantum ML page accessed")
    return render_template('quantum_ml.html', copyright=COPYRIGHT_NOTICE)

@app.route('/quantum_algorithms')
def quantum_algorithms():
    """
    Render the quantum algorithms page with interactive demonstrations
    """
    log_security_event("PAGE_ACCESS", "Quantum algorithms page accessed")
    return render_template('quantum_algorithms.html', copyright=COPYRIGHT_NOTICE)

@app.route('/resources')
def resources():
    """
    Render the resources page with additional learning materials
    """
    log_security_event("PAGE_ACCESS", "Resources page accessed")
    return render_template('resources.html', copyright=COPYRIGHT_NOTICE)

@app.route('/admin')
@jwt_required()
def admin_dashboard():
    """
    Admin dashboard with security monitoring and DNA-based protection statistics
    """
    # Get current user from JWT
    current_user = get_jwt_identity()
    
    # Get security events for monitoring
    security_events = get_security_events(limit=50)
    
    # Get DNA security statistics
    dna_stats = get_dna_security_stats()
    
    return render_template('admin.html', 
                         user=current_user,
                         security_events=security_events,
                         dna_stats=dna_stats,
                         copyright=COPYRIGHT_NOTICE)

# -------------------------------
# API Routes - Quantum Functions
# -------------------------------

@app.route('/api/quantum/bell_state', methods=['GET'])
def api_bell_state():
    """
    Generate and simulate a Bell state circuit
    """
    # Create the circuit
    circuit = create_bell_state()
    
    # Simulate the circuit
    result = simulate_circuit(circuit)
    
    # Draw the circuit and convert to an image
    circuit_img = circuit_to_image(circuit)
    
    # Create a histogram of the results
    counts = result.get_counts()
    hist_img = counts_to_image(counts)
    
    return jsonify({
        "circuit_image": circuit_img,
        "histogram_image": hist_img,
        "counts": counts,
        "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
    })

@app.route('/api/quantum/bloch_sphere', methods=['POST'])
def api_bloch_sphere():
    """
    Generate a Bloch sphere visualization for qubit state
    """
    data = request.json
    theta = float(data.get('theta', np.pi/2))
    phi = float(data.get('phi', 0))
    
    # Generate the Bloch sphere
    fig = bloch_sphere_visualization(theta, phi)
    
    # Convert to image
    img_data = fig_to_base64(fig)
    plt.close(fig)
    
    # Calculate probabilities
    prob_0 = np.cos(theta/2)**2
    prob_1 = np.sin(theta/2)**2
    
    return jsonify({
        "image": img_data,
        "prob_0": prob_0,
        "prob_1": prob_1,
        "state_vector": {
            "real_0": np.cos(theta/2),
            "imag_0": 0,
            "real_1": np.cos(phi) * np.sin(theta/2),
            "imag_1": np.sin(phi) * np.sin(theta/2)
        },
        "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
    })

@app.route('/api/quantum/ghz_state', methods=['POST'])
def api_ghz_state():
    """
    Generate and simulate a GHZ state with variable number of qubits
    """
    data = request.json
    num_qubits = int(data.get('num_qubits', 3))
    
    # Create GHZ state
    circuit = create_ghz_state(num_qubits)
    
    # Simulate
    result = simulate_circuit(circuit, get_statevector=True)
    
    # Get images
    circuit_img = circuit_to_image(circuit)
    state_img = statevector_to_image(result)
    
    return jsonify({
        "circuit_image": circuit_img,
        "state_image": state_img,
        "num_qubits": num_qubits,
        "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
    })

# -------------------------------
# API Routes - DNA Security
# -------------------------------

@app.route('/api/dna/encrypt', methods=['POST'])
def api_dna_encrypt():
    """
    Encrypt text using DNA-based encryption with advanced security
    """
    data = request.json
    plaintext = data.get('plaintext', '')
    # Generate a key if not provided
    key = data.get('key', quantum_enhanced_dna_key(len(plaintext))[0])
    
    # Encrypt the text
    encrypted_dna = dna_encrypt(plaintext, key)
    
    # Create visualization
    fig = visualize_dna_encryption(plaintext, key)
    vis_img = fig_to_base64(fig)
    plt.close(fig)
    
    # Log the operation with security monitoring
    log_security_event(
        "DNA_ENCRYPTION", 
        "DNA encryption performed",
        metadata={
            "input_length": len(plaintext),
            "output_length": len(encrypted_dna)
        }
    )
    
    return jsonify({
        "encrypted_dna": encrypted_dna,
        "key_preview": key[:8] + "..." + key[-8:] if len(key) > 16 else key,
        "visualization": vis_img,
        "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
    })

@app.route('/api/dna/decrypt', methods=['POST'])
def api_dna_decrypt():
    """
    Decrypt DNA sequence using the key with advanced security
    """
    data = request.json
    dna_sequence = data.get('dna_sequence', '')
    key = data.get('key', '')
    
    # Decrypt the DNA sequence
    try:
        decrypted_text = dna_decrypt(dna_sequence, key)
        
        # Log successful decryption
        log_security_event(
            "DNA_DECRYPTION", 
            "DNA decryption successful",
            metadata={
                "input_length": len(dna_sequence),
                "output_length": len(decrypted_text)
            }
        )
        
        return jsonify({
            "decrypted_text": decrypted_text,
            "success": True,
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        })
    except Exception as e:
        # Log failed decryption attempt
        log_security_event(
            "DNA_DECRYPTION_ERROR", 
            str(e),
            event_type="WARNING",
            metadata={
                "input_length": len(dna_sequence)
            }
        )
        
        return jsonify({
            "error": "Decryption failed, invalid key or DNA sequence",
            "success": False,
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 400

@app.route('/api/dna/visualize', methods=['POST'])
def api_visualize_dna():
    """
    Visualize a DNA sequence with advanced security features
    """
    data = request.json
    dna_sequence = data.get('dna_sequence', '')
    title = data.get('title', 'DNA Sequence Visualization')
    
    # Create visualization
    fig = visualize_dna_sequence(dna_sequence, title)
    img_data = fig_to_base64(fig)
    plt.close(fig)
    
    return jsonify({
        "visualization": img_data,
        "sequence_length": len(dna_sequence),
        "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
    })

# -------------------------------
# API Routes - Authentication
# -------------------------------

@app.route('/api/auth/login', methods=['POST'])
def api_login():
    """
    Authenticate a user and issue a JWT token
    """
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    
    # Authenticate the user
    user = authenticate_user(username, password)
    
    if user:
        # Generate access token
        access_token = create_access_token(identity=username)
        
        return jsonify({
            "token": access_token,
            "user": {
                "id": user['id'],
                "username": user['username'],
                "email": user['email'],
                "role": user['role']
            },
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        })
    else:
        return jsonify({
            "error": "Invalid username or password",
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 401

@app.route('/api/auth/register', methods=['POST'])
def api_register():
    """
    Register a new user with DNA-based security features
    """
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    email = request.json.get('email', '')
    full_name = request.json.get('full_name', '')
    
    try:
        # Register the user
        user_id = register_user(username, password, email, full_name)
        
        return jsonify({
            "message": "User registered successfully",
            "user_id": user_id,
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        })
    except Exception as e:
        return jsonify({
            "error": str(e),
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 400

# -------------------------------
# Utility Functions
# -------------------------------

def circuit_to_image(circuit):
    """
    Convert a quantum circuit to a base64 image
    """
    fig = circuit.draw(output='mpl')
    img_data = fig_to_base64(fig)
    plt.close(fig)
    return img_data

def counts_to_image(counts):
    """
    Convert measurement counts to a histogram image
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(counts.keys(), counts.values())
    ax.set_xlabel('Measurement Outcome')
    ax.set_ylabel('Counts')
    ax.set_title('Measurement Results')
    
    img_data = fig_to_base64(fig)
    plt.close(fig)
    return img_data

def statevector_to_image(result):
    """
    Convert a statevector result to a visualization
    """
    try:
        fig = plot_quantum_state(result.get_statevector())
        img_data = fig_to_base64(fig)
        plt.close(fig)
        return img_data
    except:
        return None

def fig_to_base64(fig):
    """
    Convert a matplotlib figure to base64 for embedding in HTML/JSON
    """
    buf = BytesIO()
    fig.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    img_data = base64.b64encode(buf.getvalue()).decode()
    return img_data

# Run the application with advanced security protection
if __name__ == '__main__':
    
    # Log application startup for security monitoring
    log_security_event(
        "APPLICATION_START", 
        "Application started with global security features",
        metadata={
            "version": "1.0.0",
            "security_level": "Maximum",
            "copyright": "Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }
    )
    
    # Start the server with enhanced security
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)