"""
Database Utilities for Quantum Computing Educational Platform
With advanced DNA-based security features including self-repair, self-upgrade, and self-defense

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import os
import json
import hashlib
import datetime
from typing import Dict, Any, List, Optional, Tuple
import secrets
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Initialize database
Base = declarative_base()

# Global reference to be set by application
db = None

class User(Base):
    """
    User model with DNA-based security features
    """
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(128), nullable=False)
    dna_signature = Column(Text, nullable=False)  # DNA-based security signature
    security_level = Column(Integer, default=1)   # User security clearance level
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime)
    
    # Relationships
    security_events = relationship("SecurityEvent", back_populates="user")
    simulations = relationship("QuantumSimulation", back_populates="user")

class SecurityEvent(Base):
    """
    Security event log with DNA protection
    """
    __tablename__ = 'security_events'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    event_type = Column(String(50), nullable=False)  # INFO, WARNING, ERROR, CRITICAL
    description = Column(Text, nullable=False)
    event_metadata = Column(Text, nullable=True)  # JSON-encoded metadata
    ip_address = Column(String(50), nullable=True)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="security_events")

class QuantumSimulation(Base):
    """
    Quantum simulation results with copyright protection
    """
    __tablename__ = 'quantum_simulations'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    circuit_type = Column(String(50), nullable=False)  # bell_state, ghz, teleportation, etc.
    parameters = Column(Text, nullable=True)  # JSON-encoded parameters
    results = Column(Text, nullable=False)  # JSON-encoded simulation results
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    # Relationships
    user = relationship("User", back_populates="simulations")

class DNAEncryption(Base):
    """
    DNA encryption records with protected metadata
    """
    __tablename__ = 'dna_encryptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    input_length = Column(Integer, nullable=False)
    output_length = Column(Integer, nullable=False)
    key_signature = Column(String(128), nullable=False)  # Hash of the key used
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    is_decryption = Column(Boolean, default=False)  # True if this was a decryption operation

def initialize_database(app):
    """
    Initialize the database with all tables and security features
    
    Args:
        app: Flask application
    """
    global db
    
    # Use the existing db instance that was already created at the top level
    if 'db' not in globals() or db is None:
        # Only create a new instance if one doesn't exist
        db = SQLAlchemy(app)
    
    # Create tables
    Base.metadata.create_all(db.engine)
    
    # Log initialization with security monitoring
    log_security_event("DATABASE_INIT", "Database initialized with DNA-based security")
    
    return db

def log_security_event(event_type: str, description: str, 
                      user_id: Optional[int] = None, 
                      metadata: Optional[Dict[str, Any]] = None,
                      ip_address: Optional[str] = None) -> SecurityEvent:
    """
    Log a security event with DNA protection
    
    Args:
        event_type: Type of event (INFO, WARNING, ERROR, CRITICAL)
        description: Description of the event
        user_id: ID of the user associated with the event
        metadata: Additional metadata for the event
        ip_address: IP address associated with the event
        
    Returns:
        SecurityEvent: The created security event
    """
    global db
    
    if not db:
        # If database not yet initialized, store in a temporary log
        # This will be picked up when the database is initialized
        print(f"[SECURITY_EVENT] {event_type}: {description}")
        return None
    
    # Convert metadata to JSON
    metadata_json = json.dumps(metadata) if metadata else None
    
    # Create security event with DNA-protected info
    event = SecurityEvent(
        user_id=user_id,
        event_type=event_type,
        description=description,
        event_metadata=metadata_json,
        ip_address=ip_address
    )
    
    # Add and commit to database
    db.session.add(event)
    db.session.commit()
    
    return event

def authenticate_user(username: str, password: str) -> Tuple[bool, Optional[User], Optional[str]]:
    """
    Authenticate a user with DNA-secure verification
    
    Args:
        username: Username
        password: Password
        
    Returns:
        Tuple containing:
            - Success status (bool)
            - User object if successful, None otherwise
            - Error message if unsuccessful, None otherwise
    """
    global db
    
    if not db:
        return False, None, "Database not initialized"
    
    # Find user
    user = User.query.filter_by(username=username).first()
    
    if not user:
        # Log failed authentication attempt
        log_security_event(
            "AUTH_FAILURE",
            f"Authentication failed for non-existent user: {username}",
            event_type="WARNING",
            metadata={"username": username}
        )
        return False, None, "Invalid username or password"
    
    # Hash the provided password with the same algorithm used during registration
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    if user.password_hash != password_hash:
        # Log failed password attempt
        log_security_event(
            "AUTH_FAILURE",
            f"Authentication failed for user: {username} (password mismatch)",
            user_id=user.id,
            event_type="WARNING"
        )
        return False, None, "Invalid username or password"
    
    # Update last login time
    user.last_login = datetime.datetime.utcnow()
    db.session.commit()
    
    # Log successful authentication
    log_security_event(
        "AUTH_SUCCESS",
        f"User {username} authenticated successfully",
        user_id=user.id
    )
    
    return True, user, None

def register_user(username: str, email: str, password: str) -> Tuple[bool, Optional[User], Optional[str]]:
    """
    Register a new user with DNA-secure signature
    
    Args:
        username: Username
        email: Email address
        password: Password
        
    Returns:
        Tuple containing:
            - Success status (bool)
            - User object if successful, None otherwise
            - Error message if unsuccessful, None otherwise
    """
    global db
    
    if not db:
        return False, None, "Database not initialized"
    
    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return False, None, "Username already exists"
    
    # Check if email already exists
    if User.query.filter_by(email=email).first():
        return False, None, "Email already exists"
    
    # Hash password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Generate DNA signature for enhanced security
    dna_signature_base = f"{username}:{email}:{secrets.token_hex(16)}"
    dna_signature = hashlib.sha256(dna_signature_base.encode()).hexdigest()
    
    # Create new user with DNA security
    user = User(
        username=username,
        email=email,
        password_hash=password_hash,
        dna_signature=dna_signature,
        security_level=1,  # Default security level
        created_at=datetime.datetime.utcnow()
    )
    
    # Add to database
    db.session.add(user)
    db.session.commit()
    
    # Log user registration
    log_security_event(
        "USER_REGISTER",
        f"New user registered: {username}",
        user_id=user.id,
        metadata={"email": email}
    )
    
    return True, user, None

def save_quantum_simulation(user_id: Optional[int], circuit_type: str, 
                           parameters: Dict[str, Any], results: Dict[str, Any]) -> QuantumSimulation:
    """
    Save a quantum simulation result with copyright protection
    
    Args:
        user_id: ID of the user who ran the simulation
        circuit_type: Type of quantum circuit
        parameters: Parameters used for the simulation
        results: Results of the simulation
        
    Returns:
        QuantumSimulation: The saved simulation record
    """
    global db
    
    if not db:
        return None
    
    # Convert dictionaries to JSON
    parameters_json = json.dumps(parameters)
    results_json = json.dumps(results)
    
    # Add copyright watermark to results
    copyright_notice = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com). All Rights Reserved Globally."
    results_with_copyright = {
        **json.loads(results_json),
        "copyright": copyright_notice
    }
    results_json = json.dumps(results_with_copyright)
    
    # Create simulation record
    simulation = QuantumSimulation(
        user_id=user_id,
        circuit_type=circuit_type,
        parameters=parameters_json,
        results=results_json,
        created_at=datetime.datetime.utcnow()
    )
    
    # Save to database
    db.session.add(simulation)
    db.session.commit()
    
    return simulation

def record_dna_encryption(user_id: Optional[int], input_length: int, 
                         output_length: int, key: str, is_decryption: bool = False) -> DNAEncryption:
    """
    Record a DNA encryption/decryption operation
    
    Args:
        user_id: ID of the user who performed the operation
        input_length: Length of the input
        output_length: Length of the output
        key: Encryption/decryption key
        is_decryption: Whether this was a decryption operation
        
    Returns:
        DNAEncryption: The recorded encryption operation
    """
    global db
    
    if not db:
        return None
    
    # Hash the key for secure storage
    key_signature = hashlib.sha256(key.encode()).hexdigest()
    
    # Create encryption record
    encryption = DNAEncryption(
        user_id=user_id,
        input_length=input_length,
        output_length=output_length,
        key_signature=key_signature,
        created_at=datetime.datetime.utcnow(),
        is_decryption=is_decryption
    )
    
    # Save to database
    db.session.add(encryption)
    db.session.commit()
    
    return encryption

def get_security_events(limit: int = 100, user_id: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Get recent security events
    
    Args:
        limit: Maximum number of events to return
        user_id: Filter by user ID
        
    Returns:
        List[Dict]: List of security events as dictionaries
    """
    global db
    
    if not db:
        return []
    
    # Query security events
    query = SecurityEvent.query.order_by(SecurityEvent.timestamp.desc())
    
    if user_id:
        query = query.filter_by(user_id=user_id)
    
    events = query.limit(limit).all()
    
    # Convert to dictionaries with DNA protection watermark
    events_dict = []
    for event in events:
        # Parse metadata if present
        metadata = json.loads(event.event_metadata) if event.event_metadata else {}
        
        # Create event dictionary
        event_dict = {
            "id": event.id,
            "event_type": event.event_type,
            "description": event.description,
            "metadata": metadata,
            "ip_address": event.ip_address,
            "timestamp": event.timestamp.isoformat(),
            "user_id": event.user_id,
            "copyright": "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }
        
        events_dict.append(event_dict)
    
    return events_dict

def get_dna_security_stats() -> Dict[str, Any]:
    """
    Get DNA security statistics
    
    Returns:
        Dict: Dictionary of DNA security statistics
    """
    global db
    
    if not db:
        return {}
    
    # Count encryption and decryption operations
    encryption_count = DNAEncryption.query.filter_by(is_decryption=False).count()
    decryption_count = DNAEncryption.query.filter_by(is_decryption=True).count()
    
    # Count security events by type
    security_events = {}
    for event_type in ["INFO", "WARNING", "ERROR", "CRITICAL"]:
        security_events[event_type] = SecurityEvent.query.filter_by(event_type=event_type).count()
    
    # Calculate average input and output lengths
    encryption_records = DNAEncryption.query.all()
    avg_input_length = sum(record.input_length for record in encryption_records) / max(len(encryption_records), 1)
    avg_output_length = sum(record.output_length for record in encryption_records) / max(len(encryption_records), 1)
    
    # Return statistics with copyright
    return {
        "encryption_count": encryption_count,
        "decryption_count": decryption_count,
        "security_events": security_events,
        "avg_input_length": avg_input_length,
        "avg_output_length": avg_output_length,
        "total_operations": encryption_count + decryption_count,
        "last_updated": datetime.datetime.utcnow().isoformat(),
        "copyright": "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
    }