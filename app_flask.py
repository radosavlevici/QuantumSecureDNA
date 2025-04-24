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
    visualize_quantum_fourier_transform, create_hadamard_circuit,
    create_pauli_x_circuit, create_pauli_y_circuit, create_pauli_z_circuit
)
from utils.dna_security import (
    dna_encrypt, dna_decrypt, visualize_dna_encryption,
    visualize_dna_sequence, quantum_enhanced_dna_key,
    create_quantum_dna_circuit, visualize_dna_base_pairs,
    binary_to_text, text_to_binary, binary_to_dna, dna_to_binary
)

# Initialize Flask application with DNA-based security features
app = Flask(__name__, 
            static_folder='static',
            template_folder='templates')

# Add advanced security configurations
app.config['SECRET_KEY'] = secrets.token_hex(32)  # Strong secret key
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(hours=4)  # Session duration
app.config['JWT_SECRET_KEY'] = secrets.token_hex(32)  # JWT secret key
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=2)  # JWT token expiration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///quantum_edu.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions with quantum security enhancements
CORS(app)  # Enable Cross-Origin Resource Sharing
jwt = JWTManager(app)  # Initialize JWT for secure authentication

# Initialize database with DNA security
initialize_database(app)

# Global copyright notice for application protection
COPYRIGHT_NOTICE = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - Worldwide Rights Reserved"

# ------------------------------
# Middleware for Security
# ------------------------------

@app.after_request
def apply_security_headers(response):
    """
    Apply advanced security headers to prevent attacks and protect copyright
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Security headers to prevent attacks and protect copyright
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
    
    # Copyright protection headers
    response.headers['X-Copyright'] = COPYRIGHT_NOTICE
    response.headers['X-Protected'] = 'DNA-Based Quantum Security'
    
    # Log request for security monitoring
    log_security_event("HTTP_REQUEST", f"Access to {request.path}")
    
    return response

@app.before_request
def before_request():
    """
    Security checks before processing requests
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Initialize session with quantum-enhanced security if not already done
    if 'security_key' not in session:
        security_key, _ = quantum_enhanced_dna_key(32)
        session['security_key'] = security_key
    
    # Regenerate session periodically for security
    if not session.get('created_at'):
        session['created_at'] = datetime.datetime.now().isoformat()
    else:
        created_time = datetime.datetime.fromisoformat(session.get('created_at'))
        if (datetime.datetime.now() - created_time).total_seconds() > 3600:  # 1 hour
            # Regenerate security key for enhanced protection
            security_key, _ = quantum_enhanced_dna_key(32)
            session['security_key'] = security_key
            session['created_at'] = datetime.datetime.now().isoformat()

# ------------------------------
# Main Application Routes
# ------------------------------

@app.route('/')
def index():
    """
    Render the main application homepage with copyright-protected content
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Homepage accessed")
    
    # Return homepage with global copyright protection
    return render_template('index.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/quantum_basics')
def quantum_basics():
    """
    Render the quantum basics page with interactive demonstrations
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Quantum basics page accessed with copyright protection")
    
    # Return quantum basics page with global copyright protection
    return render_template('quantum_basics.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/dna_security')
def dna_security_page():
    """
    Render the DNA-based security page with interactive demonstrations
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "DNA security page accessed with copyright protection")
    
    # Return DNA security page with global copyright protection
    return render_template('dna_security.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/quantum_algorithms')
def quantum_algorithms():
    """
    Render the quantum algorithms page with interactive demonstrations
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Quantum algorithms page accessed with copyright protection")
    
    # Return quantum algorithms page with global copyright protection
    return render_template('quantum_algorithms.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/quantum_ml')
def quantum_ml():
    """
    Render the quantum machine learning page with interactive demonstrations
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Quantum ML page accessed with copyright protection")
    
    # Return quantum ML page with global copyright protection
    return render_template('quantum_ml.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/resources')
def resources():
    """
    Render the resources page with additional learning materials
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Resources page accessed with copyright protection")
    
    # Return resources page with global copyright protection
    return render_template('resources.html', 
                         copyright=COPYRIGHT_NOTICE,
                         security_key=security_key[:8] + "..." + security_key[-8:])

@app.route('/login')
def login_page():
    """
    Render the login page with DNA-based security
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Login page accessed with copyright protection")
    
    # Return login page with global copyright protection
    return render_template('login.html', 
                         security_key=security_key[:8] + "..." + security_key[-8:],
                         error=request.args.get('error'),
                         success=request.args.get('success'),
                         copyright=COPYRIGHT_NOTICE)

@app.route('/register')
def register_page():
    """
    Render the registration page with DNA-based security
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session
    security_key = session.get('security_key', quantum_enhanced_dna_key(32)[0])
    session['security_key'] = security_key
    
    # Log page access with security monitoring
    log_security_event("PAGE_ACCESS", "Registration page accessed with copyright protection")
    
    # Return registration page with global copyright protection
    return render_template('register.html', 
                         security_key=security_key[:8] + "..." + security_key[-8:],
                         error=request.args.get('error'),
                         success=request.args.get('success'),
                         copyright=COPYRIGHT_NOTICE)

@app.route('/admin')
@jwt_required()
def admin_dashboard():
    """
    Admin dashboard with security monitoring and DNA-based protection statistics
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Generate quantum DNA security key for this session with highest encryption
    security_key = session.get('security_key', quantum_enhanced_dna_key(64)[0])
    session['security_key'] = security_key
    
    # Get current user from JWT with DNA verification
    current_user = get_jwt_identity()
    
    # Log admin access with advanced security monitoring
    log_security_event("ADMIN_ACCESS", "Admin dashboard accessed with copyright protection",
                     metadata={
                         "user": current_user,
                         "copyright": "Ervin Remus Radosavlevici", 
                         "ip": request.remote_addr
                     })
    
    # Get security events for monitoring with DNA protection
    security_events = get_security_events(limit=50)
    
    # Get DNA security statistics with quantum verification
    dna_stats = get_dna_security_stats()
    
    # Return admin dashboard with global copyright protection
    return render_template('admin.html', 
                         user=current_user,
                         security_events=security_events,
                         dna_stats=dna_stats,
                         now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                         security_key=security_key[:8] + "..." + security_key[-8:],
                         copyright=COPYRIGHT_NOTICE)

# -------------------------------
# API Routes - Quantum Functions
# -------------------------------

@app.route('/api/bell_state', methods=['GET'])
@app.route('/api/quantum/bell_state', methods=['GET'])
def api_bell_state():
    """
    Generate and simulate a Bell state circuit
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
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

@app.route('/api/bloch_sphere', methods=['GET', 'POST'])
@app.route('/api/quantum/bloch_sphere', methods=['GET', 'POST'])
def api_bloch_sphere():
    """
    Generate a Bloch sphere visualization for qubit state
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Handle both GET and POST requests
    if request.method == 'POST' and request.is_json:
        data = request.json
    else:
        data = request.args
        
    # Get parameters with defaults
    try:
        theta = float(data.get('theta', np.pi/2))
        phi = float(data.get('phi', 0))
    except (ValueError, TypeError):
        # Default values if conversion fails
        theta = np.pi/2
        phi = 0
    
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

@app.route('/api/ghz_state', methods=['GET', 'POST'])
@app.route('/api/quantum/ghz_state', methods=['GET', 'POST'])
def api_ghz_state():
    """
    Generate and simulate a GHZ state with variable number of qubits
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Handle both GET and POST requests
    if request.method == 'POST' and request.is_json:
        data = request.json
    else:
        data = request.args
    
    # Get number of qubits with default
    try:
        num_qubits = int(data.get('num_qubits', 3))
        # Cap number of qubits for server resource protection
        num_qubits = min(max(num_qubits, 2), 20)  # Between 2 and 20 qubits, increased from 10
    except (ValueError, TypeError):
        num_qubits = 5  # Default if conversion fails, increased from 3
    
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

@app.route('/api/apply_gate', methods=['GET', 'POST'])
@app.route('/api/quantum/apply_gate', methods=['GET', 'POST'])
def api_apply_gate():
    """
    Apply a quantum gate to a qubit and visualize the effect
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    # Handle both GET and POST requests
    if request.method == 'POST' and request.is_json:
        data = request.json
    else:
        data = request.args

    # Get parameters with defaults
    gate = data.get('gate', 'hadamard').lower()
    
    # Parse initial state - support both array and string representations
    try:
        initial_state_param = data.get('initial_state', None)
        if initial_state_param is None:
            initial_state = [1, 0]  # |0⟩ by default
        elif isinstance(initial_state_param, str):
            if initial_state_param == '0' or initial_state_param == '|0>':
                initial_state = [1, 0]
            elif initial_state_param == '1' or initial_state_param == '|1>':
                initial_state = [0, 1]
            elif initial_state_param == '+':
                initial_state = [1/np.sqrt(2), 1/np.sqrt(2)]
            elif initial_state_param == '-':
                initial_state = [1/np.sqrt(2), -1/np.sqrt(2)]
            else:
                # Try to parse as JSON array
                try:
                    initial_state = json.loads(initial_state_param)
                except:
                    initial_state = [1, 0]
        else:
            initial_state = [1, 0]
    except:
        initial_state = [1, 0]
    
    # Apply the gate
    if gate == 'hadamard' or gate == 'h':
        circuit = create_hadamard_circuit(initial_state)
    elif gate == 'pauli_x' or gate == 'x':
        circuit = create_pauli_x_circuit(initial_state)
    elif gate == 'pauli_y' or gate == 'y':
        circuit = create_pauli_y_circuit(initial_state)
    elif gate == 'pauli_z' or gate == 'z':
        circuit = create_pauli_z_circuit(initial_state)
    else:
        return jsonify({
            "error": f"Unsupported gate: {gate}. Supported gates: hadamard/h, pauli_x/x, pauli_y/y, pauli_z/z",
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 400
    
    # Simulate the circuit
    result = simulate_circuit(circuit)
    
    # Get circuit image
    circuit_img = circuit_to_image(circuit)
    
    # Get measurement results
    counts = result.get_counts()
    hist_img = counts_to_image(counts)
    
    # Return the results
    return jsonify({
        "gate": gate,
        "initial_state": initial_state,
        "circuit_image": circuit_img,
        "histogram_image": hist_img,
        "counts": counts,
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

@app.route('/api/login', methods=['POST'])
def api_login():
    """
    Authenticate a user and issue a JWT token
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    
    # Log login attempt with security monitoring
    log_security_event(
        "LOGIN_ATTEMPT", 
        f"Login attempt for user: {username}",
        metadata={
            "ip": request.remote_addr
        }
    )
    
    # Authenticate the user with DNA verification
    success, user, error_msg = authenticate_user(username, password)
    
    if success and user:
        # Generate access token with enhanced security
        access_token = create_access_token(identity=username)
        
        # Log successful login
        log_security_event(
            "LOGIN_SUCCESS", 
            f"User {username} authenticated successfully",
            user_id=user.id,
            metadata={
                "ip": request.remote_addr
            }
        )
        
        return jsonify({
            "access_token": access_token,
            "user": username,
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        })
    else:
        # Log failed login attempt
        log_security_event(
            "LOGIN_FAILED", 
            f"Authentication failed for user: {username}",
            metadata={
                "error": error_msg,
                "ip": request.remote_addr
            }
        )
        
        return jsonify({
            "error": error_msg or "Invalid username or password",
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 401

@app.route('/api/register', methods=['POST'])
def api_register():
    """
    Register a new user with DNA-based security features
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    username = request.json.get('username', '')
    password = request.json.get('password', '')
    email = request.json.get('email', '')
    
    # Log registration attempt
    log_security_event(
        "REGISTRATION_ATTEMPT", 
        f"Registration attempt for username: {username}, email: {email}",
        metadata={
            "ip": request.remote_addr
        }
    )
    
    try:
        # Register the user with DNA security
        success, user, error_msg = register_user(username, email, password)
        
        if success and user:
            # Log successful registration
            log_security_event(
                "REGISTRATION_SUCCESS", 
                f"User {username} registered successfully",
                user_id=user.id if hasattr(user, 'id') else None,
                metadata={
                    "ip": request.remote_addr
                }
            )
            
            return jsonify({
                "success": True,
                "message": "User registered successfully with DNA-based security",
                "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
            })
        else:
            # Log failed registration
            log_security_event(
                "REGISTRATION_FAILED", 
                f"Registration failed for username: {username}",
                metadata={
                    "error": error_msg,
                    "ip": request.remote_addr
                }
            )
            
            return jsonify({
                "success": False,
                "error": error_msg or "Registration failed. Username or email may already be taken.",
                "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
            }), 400
            
    except Exception as e:
        # Log exception
        log_security_event(
            "REGISTRATION_ERROR", 
            f"Registration error: {str(e)}",
            metadata={
                "ip": request.remote_addr
            }
        )
        
        return jsonify({
            "success": False,
            "error": str(e),
            "copyright": "© Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }), 400

# -------------------------------
# Utility Functions
# -------------------------------

def circuit_to_image(circuit):
    """
    Convert a quantum circuit to a base64 image
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
    """
    fig = circuit.draw(output='mpl')
    img_data = fig_to_base64(fig)
    plt.close(fig)
    return img_data

def counts_to_image(counts):
    """
    Convert measurement counts to a histogram image
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
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
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
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
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    WORLDWIDE COPYRIGHT PROTECTED with DNA-based security
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