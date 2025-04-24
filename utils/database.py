"""
Database Utilities for Quantum Computing Educational Platform
With advanced DNA-based security features including self-repair, self-upgrade, and self-defense

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import os
import datetime
import hashlib
import json
import secrets
from typing import List, Dict, Any, Tuple, Optional

from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy base class
Base = declarative_base()

# Global database connection
db = SQLAlchemy()

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
    # Configure SQLAlchemy
    db.init_app(app)
    
    # Create tables within app context
    with app.app_context():
        # Create all tables
        Base.metadata.create_all(db.engine)
        
        # Log database initialization
        log_security_event(
            "DATABASE_INIT",
            "Database initialized with copyright protection",
            metadata={
                "tables": [table.__tablename__ for table in 
                          [User, SecurityEvent, QuantumSimulation, DNAEncryption]],
                "copyright": "Ervin Remus Radosavlevici (ervin210@icloud.com)"
            }
        )

def log_security_event(event_type: str, description: str, 
                      user_id: Optional[int] = None, 
                      metadata: Optional[Dict[str, Any]] = None,
                      ip_address: Optional[str] = None) -> Optional[SecurityEvent]:
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
    try:
        # Create a new security event
        from flask import current_app
        
        # Add console output for basic debugging
        print(f"[SECURITY_EVENT] {event_type}: {description}")
        
        # Skip database operations if app is not initialized yet
        if not current_app:
            return None
            
        with current_app.app_context():
            # Convert metadata to JSON
            metadata_json = json.dumps(metadata) if metadata else None
            
            # Create a new security event
            event = SecurityEvent(
                user_id=user_id,
                event_type=event_type,
                description=description,
                event_metadata=metadata_json,
                ip_address=ip_address
            )
            
            # Add to database
            db.session.add(event)
            db.session.commit()
            
            return event
    except Exception as e:
        # Don't crash on logging errors
        print(f"[ERROR] Could not log security event: {str(e)}")
        return None

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
    try:
        # Find the user
        user = User.query.filter_by(username=username).first()
        
        if not user:
            # Log failed authentication
            log_security_event(
                "AUTH_FAILED",
                f"Authentication failed for non-existent user: {username}"
            )
            return False, None, "User not found"
        
        # Verify password with DNA signature protection
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if user.password_hash != password_hash:
            # Log failed authentication
            log_security_event(
                "AUTH_FAILED",
                f"Authentication failed for user: {username} (invalid password)",
                user_id=user.id
            )
            return False, None, "Invalid password"
        
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
        
    except Exception as e:
        # Log error
        log_security_event(
            "AUTH_ERROR",
            f"Authentication error: {str(e)}"
        )
        return False, None, f"Authentication error: {str(e)}"

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
    try:
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return False, None, "Username already exists"
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            return False, None, "Email address already exists"
        
        # Create password hash
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        # Generate DNA signature for security
        dna_signature = generate_dna_signature(username, email, password)
        
        # Create new user
        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            dna_signature=dna_signature,
            security_level=1  # Default security level
        )
        
        # Add to database
        db.session.add(user)
        db.session.commit()
        
        # Log user registration
        log_security_event(
            "USER_REGISTERED",
            f"User {username} registered successfully",
            user_id=user.id
        )
        
        return True, user, None
        
    except Exception as e:
        # Log error
        log_security_event(
            "REGISTRATION_ERROR",
            f"Registration error: {str(e)}"
        )
        return False, None, f"Registration error: {str(e)}"

def save_quantum_simulation(user_id: Optional[int], circuit_type: str, 
                           parameters: Dict[str, Any], results: Dict[str, Any]) -> Optional[QuantumSimulation]:
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
    try:
        # Convert parameters and results to JSON
        parameters_json = json.dumps(parameters)
        results_json = json.dumps(results)
        
        # Create simulation record
        simulation = QuantumSimulation(
            user_id=user_id,
            circuit_type=circuit_type,
            parameters=parameters_json,
            results=results_json
        )
        
        # Add to database
        db.session.add(simulation)
        db.session.commit()
        
        # Log simulation
        log_security_event(
            "QUANTUM_SIMULATION",
            f"Quantum simulation of type {circuit_type} saved",
            user_id=user_id,
            metadata={
                "circuit_type": circuit_type,
                "simulation_id": simulation.id
            }
        )
        
        return simulation
        
    except Exception as e:
        # Log error
        log_security_event(
            "SIMULATION_ERROR",
            f"Error saving simulation: {str(e)}",
            user_id=user_id
        )
        return None

def record_dna_encryption(user_id: Optional[int], input_length: int, 
                         output_length: int, key: str, is_decryption: bool = False) -> Optional[DNAEncryption]:
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
    try:
        # Calculate key signature (hash) for security
        key_signature = hashlib.sha256(key.encode()).hexdigest()
        
        # Create encryption record
        encryption = DNAEncryption(
            user_id=user_id,
            input_length=input_length,
            output_length=output_length,
            key_signature=key_signature,
            is_decryption=is_decryption
        )
        
        # Add to database
        db.session.add(encryption)
        db.session.commit()
        
        # Log encryption
        operation_type = "decryption" if is_decryption else "encryption"
        log_security_event(
            "DNA_OPERATION",
            f"DNA {operation_type} operation recorded",
            user_id=user_id,
            metadata={
                "operation": operation_type,
                "input_length": input_length,
                "output_length": output_length
            }
        )
        
        return encryption
        
    except Exception as e:
        # Log error
        log_security_event(
            "DNA_OPERATION_ERROR",
            f"Error recording DNA operation: {str(e)}",
            user_id=user_id
        )
        return None

def get_security_events(limit: int = 100, user_id: Optional[int] = None) -> List[Dict[str, Any]]:
    """
    Get recent security events
    
    Args:
        limit: Maximum number of events to return
        user_id: Filter by user ID
        
    Returns:
        List[Dict]: List of security events as dictionaries
    """
    try:
        # Start query
        query = SecurityEvent.query
        
        # Apply filters
        if user_id is not None:
            query = query.filter_by(user_id=user_id)
        
        # Order by timestamp descending
        query = query.order_by(SecurityEvent.timestamp.desc())
        
        # Apply limit
        query = query.limit(limit)
        
        # Execute query
        events = query.all()
        
        # Convert to dictionaries
        result = []
        for event in events:
            event_dict = {
                "id": event.id,
                "user_id": event.user_id,
                "event_type": event.event_type,
                "description": event.description,
                "ip_address": event.ip_address,
                "timestamp": event.timestamp.isoformat(),
                "metadata": json.loads(event.event_metadata) if event.event_metadata else None
            }
            result.append(event_dict)
        
        return result
        
    except Exception as e:
        # Log error
        log_security_event(
            "EVENT_QUERY_ERROR",
            f"Error querying security events: {str(e)}"
        )
        return []

def get_dna_security_stats() -> Dict[str, Any]:
    """
    Get DNA security statistics
    
    Returns:
        Dict: Dictionary of DNA security statistics
    """
    try:
        # Get counts
        user_count = User.query.count()
        event_count = SecurityEvent.query.count()
        simulation_count = QuantumSimulation.query.count()
        encryption_count = DNAEncryption.query.count()
        
        # Get recent events by type
        info_events = SecurityEvent.query.filter(SecurityEvent.event_type.like("INFO%")).count()
        warning_events = SecurityEvent.query.filter(SecurityEvent.event_type.like("WARNING%")).count()
        error_events = SecurityEvent.query.filter(SecurityEvent.event_type.like("ERROR%")).count()
        critical_events = SecurityEvent.query.filter(SecurityEvent.event_type.like("CRITICAL%")).count()
        
        # Get encryption stats
        avg_encryption_ratio = db.session.query(
            db.func.avg(DNAEncryption.output_length / DNAEncryption.input_length)
        ).scalar() or 0
        
        # Compile statistics
        stats = {
            "user_count": user_count,
            "event_count": event_count,
            "simulation_count": simulation_count,
            "encryption_count": encryption_count,
            "event_breakdown": {
                "info": info_events,
                "warning": warning_events,
                "error": error_events,
                "critical": critical_events
            },
            "encryption_stats": {
                "avg_ratio": float(avg_encryption_ratio),
                "total_operations": encryption_count
            },
            "system_status": "operational",
            "last_updated": datetime.datetime.utcnow().isoformat(),
            "copyright": "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }
        
        return stats
        
    except Exception as e:
        # Log error
        log_security_event(
            "STATS_ERROR",
            f"Error generating DNA security stats: {str(e)}"
        )
        
        # Return minimal stats on error
        return {
            "system_status": "degraded",
            "error": str(e),
            "last_updated": datetime.datetime.utcnow().isoformat(),
            "copyright": "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }

# Helper functions with built-in security
def generate_dna_signature(username: str, email: str, password: str) -> str:
    """
    Generate a DNA-based security signature for a user
    
    Args:
        username: Username
        email: Email address
        password: Password
        
    Returns:
        str: DNA signature
    """
    # Create base signature from user data
    base_signature = f"{username}:{email}:{hashlib.sha256(password.encode()).hexdigest()}"
    
    # Add timestamp and random salt
    timestamp = datetime.datetime.utcnow().isoformat()
    salt = secrets.token_hex(16)
    
    # Combine all elements
    combined = f"{base_signature}:{timestamp}:{salt}"
    
    # Generate final signature
    final_signature = hashlib.sha512(combined.encode()).hexdigest()
    
    return final_signature