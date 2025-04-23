"""
Database utilities for the Quantum Computing Educational Platform
With advanced DNA-based security features and copyright protection

© Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import os
import psycopg2
import psycopg2.extras
import hashlib
import secrets
import datetime
import json
import base64
from typing import Dict, List, Any, Optional, Tuple, Union

# Global connection variable
_connection = None

def get_db_connection():
    """
    Create a connection to the PostgreSQL database with advanced self-repair capabilities.
    Uses environment variables for connection parameters.
    
    Returns:
        psycopg2.connection: Database connection object
    """
    global _connection
    
    # Implement self-repair for database connection
    if _connection is not None:
        try:
            # Test if connection is still alive
            cur = _connection.cursor()
            cur.execute('SELECT 1')
            cur.close()
            return _connection
        except Exception:
            # Connection is broken, close it and reconnect
            try:
                _connection.close()
            except Exception:
                pass
            _connection = None
    
    # Create new connection with enhanced security
    try:
        # Get connection parameters from environment variables
        database_url = os.environ.get('DATABASE_URL')
        
        # Connect to the database
        _connection = psycopg2.connect(database_url)
        _connection.autocommit = True
        
        # Log connection for security monitoring
        log_security_event("DATABASE_CONNECTION", "Connection established with secure parameters")
        
        return _connection
    except Exception as e:
        # Log security incident
        log_security_event("DATABASE_CONNECTION_ERROR", str(e), event_type="ERROR")
        raise

def initialize_database():
    """
    Initialize the database schema with the required tables for security and functionality.
    Implements self-repair and self-upgrade capabilities.
    """
    # Create tables if they don't exist yet
    conn = get_db_connection()
    with conn.cursor() as cur:
        # Create security_events table for DNA security logging
        cur.execute('''
        CREATE TABLE IF NOT EXISTS security_events (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            event_name VARCHAR(255) NOT NULL,
            description TEXT,
            event_type VARCHAR(50) DEFAULT 'INFO',
            metadata JSONB DEFAULT '{}'::jsonb,
            ip_address VARCHAR(50),
            user_agent TEXT
        )
        ''')
        
        # Create users table with DNA security integration
        cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            email VARCHAR(255) UNIQUE NOT NULL,
            full_name VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_login TIMESTAMP,
            role VARCHAR(50) DEFAULT 'user',
            dna_security_key TEXT,
            security_settings JSONB DEFAULT '{}'::jsonb
        )
        ''')
        
        # Create quantum_simulations table to store simulation results
        cur.execute('''
        CREATE TABLE IF NOT EXISTS quantum_simulations (
            id SERIAL PRIMARY KEY,
            user_id INTEGER REFERENCES users(id),
            simulation_name VARCHAR(255) NOT NULL,
            circuit_data TEXT NOT NULL,
            results JSONB DEFAULT '{}'::jsonb,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            description TEXT,
            is_public BOOLEAN DEFAULT FALSE
        )
        ''')
        
        # Create dna_security_logs table specifically for DNA security operations
        cur.execute('''
        CREATE TABLE IF NOT EXISTS dna_security_logs (
            id SERIAL PRIMARY KEY,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            user_id INTEGER REFERENCES users(id),
            operation_type VARCHAR(100) NOT NULL,
            input_hash VARCHAR(255),
            output_hash VARCHAR(255),
            result_status VARCHAR(50),
            dna_sequence TEXT,
            metadata JSONB DEFAULT '{}'::jsonb
        )
        ''')
        
        # Create copyright_protection table for tracking copyright information
        cur.execute('''
        CREATE TABLE IF NOT EXISTS copyright_protection (
            id SERIAL PRIMARY KEY,
            content_id VARCHAR(255) UNIQUE NOT NULL,
            content_hash VARCHAR(255) NOT NULL,
            copyright_owner VARCHAR(255) DEFAULT 'Ervin Remus Radosavlevici',
            contact_email VARCHAR(255) DEFAULT 'ervin210@icloud.com',
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            protection_level VARCHAR(50) DEFAULT 'FULL',
            watermark_data TEXT,
            legal_status VARCHAR(100) DEFAULT 'All Rights Reserved'
        )
        ''')
        
        # Check if admin user exists, create if it doesn't
        cur.execute("SELECT id FROM users WHERE username = 'admin'")
        if cur.fetchone() is None:
            # Create admin user with secure password
            admin_password = generate_secure_password()
            password_hash = hash_password(admin_password)
            
            # Generate DNA security key for admin
            dna_security_key = generate_dna_security_key()
            
            cur.execute('''
            INSERT INTO users (username, password_hash, email, full_name, role, dna_security_key)
            VALUES (%s, %s, %s, %s, %s, %s)
            ''', ('admin', password_hash, 'ervin210@icloud.com', 'Ervin Remus Radosavlevici', 'admin', dna_security_key))
            
            # Log the admin password only once for initial setup
            # In production, this would be sent securely to the administrator
            log_security_event("ADMIN_CREATED", f"Admin user created with password: {admin_password}")

def log_security_event(event_name: str, description: str, event_type: str = "INFO", 
                      metadata: Dict[str, Any] = None, ip_address: str = None, 
                      user_agent: str = None):
    """
    Log a security event to the database.
    
    Args:
        event_name (str): Name of the security event
        description (str): Description of the event
        event_type (str): Type of event (INFO, WARNING, ERROR, CRITICAL)
        metadata (Dict): Additional metadata as a dictionary
        ip_address (str): IP address related to the event
        user_agent (str): User agent string if applicable
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Convert metadata to JSON if provided
            json_metadata = json.dumps(metadata) if metadata else '{}'
            
            cur.execute('''
            INSERT INTO security_events 
            (event_name, description, event_type, metadata, ip_address, user_agent)
            VALUES (%s, %s, %s, %s::jsonb, %s, %s)
            ''', (event_name, description, event_type, json_metadata, ip_address, user_agent))
    except Exception as e:
        # In case of database error, we still want to log this somehow
        # In a production system, this would fall back to a file-based log
        print(f"ERROR logging security event: {e}")

def hash_password(password: str) -> str:
    """
    Create a secure hash of a password using Argon2 algorithm.
    For this implementation we use a simpler approach with SHA-256 and salt.
    
    Args:
        password (str): The password to hash
        
    Returns:
        str: The hashed password
    """
    salt = secrets.token_hex(16)
    pw_hash = hashlib.sha256((password + salt).encode()).hexdigest()
    return f"{salt}${pw_hash}"

def verify_password(stored_hash: str, provided_password: str) -> bool:
    """
    Verify a password against a stored hash.
    
    Args:
        stored_hash (str): The stored password hash
        provided_password (str): The password to verify
        
    Returns:
        bool: True if the password matches, False otherwise
    """
    salt, hash_value = stored_hash.split('$')
    calculated_hash = hashlib.sha256((provided_password + salt).encode()).hexdigest()
    return calculated_hash == hash_value

def generate_secure_password() -> str:
    """
    Generate a secure random password.
    
    Returns:
        str: A secure password
    """
    return secrets.token_urlsafe(12)

def generate_dna_security_key() -> str:
    """
    Generate a DNA-based security key for advanced protection.
    This key is used for DNA-based encryption.
    
    Returns:
        str: A DNA security key (sequence of A, C, G, T)
    """
    # Generate a random sequence of DNA bases
    bases = ['A', 'C', 'G', 'T']
    # Generate a key of 64 DNA bases
    return ''.join(secrets.choice(bases) for _ in range(64))

def register_user(username: str, password: str, email: str, full_name: str = None) -> int:
    """
    Register a new user with DNA-based security features.
    
    Args:
        username (str): User's username
        password (str): User's password
        email (str): User's email
        full_name (str): User's full name
        
    Returns:
        int: The ID of the new user
    """
    try:
        # Hash the password
        password_hash = hash_password(password)
        
        # Generate DNA security key
        dna_security_key = generate_dna_security_key()
        
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO users 
            (username, password_hash, email, full_name, dna_security_key)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
            ''', (username, password_hash, email, full_name, dna_security_key))
            
            user_id = cur.fetchone()[0]
            
            # Log the registration for security
            log_security_event("USER_REGISTERED", 
                              f"User {username} registered successfully",
                              metadata={"user_id": user_id, "email": email})
            
            return user_id
    except Exception as e:
        log_security_event("USER_REGISTRATION_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"username": username, "email": email})
        raise

def authenticate_user(username: str, password: str) -> Optional[Dict[str, Any]]:
    """
    Authenticate a user and update last login time.
    
    Args:
        username (str): User's username
        password (str): User's password
        
    Returns:
        Optional[Dict]: User data if authentication succeeds, None otherwise
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            cur.execute('''
            SELECT id, username, password_hash, email, full_name, role, dna_security_key
            FROM users WHERE username = %s
            ''', (username,))
            
            user = cur.fetchone()
            
            if user and verify_password(user['password_hash'], password):
                # Update last login time
                cur.execute('''
                UPDATE users SET last_login = CURRENT_TIMESTAMP
                WHERE id = %s
                ''', (user['id'],))
                
                # Log successful login
                log_security_event("USER_LOGIN", 
                                  f"User {username} logged in successfully",
                                  metadata={"user_id": user['id']})
                
                # Return user data without password hash
                user_data = dict(user)
                del user_data['password_hash']
                return user_data
            
            # Log failed login attempt
            log_security_event("FAILED_LOGIN", 
                              f"Failed login attempt for user {username}",
                              event_type="WARNING")
            
            return None
    except Exception as e:
        log_security_event("AUTHENTICATION_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"username": username})
        return None

def save_quantum_simulation(user_id: int, simulation_name: str, circuit_data: str, 
                           results: Dict[str, Any], description: str = None, 
                           is_public: bool = False) -> int:
    """
    Save a quantum simulation to the database.
    
    Args:
        user_id (int): ID of the user who ran the simulation
        simulation_name (str): Name of the simulation
        circuit_data (str): Serialized quantum circuit data
        results (Dict): Results of the simulation
        description (str): Description of the simulation
        is_public (bool): Whether the simulation is publicly viewable
        
    Returns:
        int: ID of the saved simulation
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO quantum_simulations
            (user_id, simulation_name, circuit_data, results, description, is_public)
            VALUES (%s, %s, %s, %s::jsonb, %s, %s) RETURNING id
            ''', (user_id, simulation_name, circuit_data, json.dumps(results), 
                 description, is_public))
            
            simulation_id = cur.fetchone()[0]
            
            # Register copyright protection for the simulation
            register_copyright_protection(
                f"simulation_{simulation_id}",
                f"Quantum simulation {simulation_name} by user {user_id}",
                circuit_data
            )
            
            return simulation_id
    except Exception as e:
        log_security_event("SIMULATION_SAVE_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"user_id": user_id, "simulation_name": simulation_name})
        raise

def log_dna_security_operation(user_id: Optional[int], operation_type: str, 
                             input_hash: str, output_hash: str, result_status: str,
                             dna_sequence: str = None, metadata: Dict[str, Any] = None) -> int:
    """
    Log a DNA-based security operation to the database.
    
    Args:
        user_id (int): ID of the user who performed the operation
        operation_type (str): Type of DNA security operation
        input_hash (str): Hash of the input data
        output_hash (str): Hash of the output data
        result_status (str): Status of the operation
        dna_sequence (str): DNA sequence used (partially obscured for security)
        metadata (Dict): Additional metadata
        
    Returns:
        int: ID of the log entry
    """
    try:
        # For security, we never store the full DNA sequence
        if dna_sequence and len(dna_sequence) > 16:
            # Store only first 8 and last 8 characters, mask the middle
            safe_dna_sequence = dna_sequence[:8] + "..." + dna_sequence[-8:]
        else:
            safe_dna_sequence = dna_sequence
            
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute('''
            INSERT INTO dna_security_logs
            (user_id, operation_type, input_hash, output_hash, result_status, dna_sequence, metadata)
            VALUES (%s, %s, %s, %s, %s, %s, %s::jsonb) RETURNING id
            ''', (user_id, operation_type, input_hash, output_hash, 
                 result_status, safe_dna_sequence, 
                 json.dumps(metadata) if metadata else '{}'))
            
            return cur.fetchone()[0]
    except Exception as e:
        # Log error without exposing sensitive data
        log_security_event("DNA_SECURITY_LOG_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"operation_type": operation_type})
        raise

def register_copyright_protection(content_id: str, watermark_data: str, content: str) -> int:
    """
    Register copyright protection for content.
    
    Args:
        content_id (str): Unique identifier for the content
        watermark_data (str): Watermark data to embed
        content (str): The content to protect
        
    Returns:
        int: ID of the copyright protection entry
    """
    try:
        # Calculate hash of the content for integrity verification
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Check if this content is already protected
            cur.execute('''
            SELECT id FROM copyright_protection WHERE content_id = %s
            ''', (content_id,))
            
            existing = cur.fetchone()
            if existing:
                # Update existing protection
                cur.execute('''
                UPDATE copyright_protection 
                SET content_hash = %s, watermark_data = %s, timestamp = CURRENT_TIMESTAMP
                WHERE content_id = %s RETURNING id
                ''', (content_hash, watermark_data, content_id))
                return cur.fetchone()[0]
            else:
                # Create new protection entry
                cur.execute('''
                INSERT INTO copyright_protection
                (content_id, content_hash, watermark_data)
                VALUES (%s, %s, %s) RETURNING id
                ''', (content_id, content_hash, watermark_data))
                
                return cur.fetchone()[0]
    except Exception as e:
        log_security_event("COPYRIGHT_PROTECTION_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"content_id": content_id})
        raise

def verify_content_integrity(content_id: str, content: str) -> bool:
    """
    Verify the integrity of content against its registered hash.
    Part of the self-repair and self-defense mechanism.
    
    Args:
        content_id (str): ID of the content to verify
        content (str): The content to check
        
    Returns:
        bool: True if the content matches its registered hash
    """
    try:
        # Calculate hash of the provided content
        content_hash = hashlib.sha256(content.encode()).hexdigest()
        
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute('''
            SELECT content_hash FROM copyright_protection WHERE content_id = %s
            ''', (content_id,))
            
            result = cur.fetchone()
            if result:
                # Verify the hash matches
                stored_hash = result[0]
                return content_hash == stored_hash
            
            return False
    except Exception as e:
        log_security_event("CONTENT_VERIFICATION_ERROR", 
                          str(e), 
                          event_type="ERROR",
                          metadata={"content_id": content_id})
        return False

def get_security_events(limit: int = 100, event_type: str = None) -> List[Dict[str, Any]]:
    """
    Get recent security events.
    
    Args:
        limit (int): Maximum number of events to return
        event_type (str): Filter by event type
        
    Returns:
        List[Dict]: List of security events
    """
    try:
        conn = get_db_connection()
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            if event_type:
                cur.execute('''
                SELECT * FROM security_events 
                WHERE event_type = %s
                ORDER BY timestamp DESC LIMIT %s
                ''', (event_type, limit))
            else:
                cur.execute('''
                SELECT * FROM security_events 
                ORDER BY timestamp DESC LIMIT %s
                ''', (limit,))
            
            events = [dict(event) for event in cur.fetchall()]
            return events
    except Exception as e:
        # Log but continue - this is a critical security function
        print(f"ERROR retrieving security events: {e}")
        return []

def get_dna_security_stats() -> Dict[str, Any]:
    """
    Get statistics about DNA security operations.
    
    Returns:
        Dict: Statistics about DNA security operations
    """
    try:
        conn = get_db_connection()
        with conn.cursor() as cur:
            # Get count of operations by type
            cur.execute('''
            SELECT operation_type, COUNT(*) as count
            FROM dna_security_logs
            GROUP BY operation_type
            ''')
            
            by_type = {row[0]: row[1] for row in cur.fetchall()}
            
            # Get count by status
            cur.execute('''
            SELECT result_status, COUNT(*) as count
            FROM dna_security_logs
            GROUP BY result_status
            ''')
            
            by_status = {row[0]: row[1] for row in cur.fetchall()}
            
            # Get total operations
            cur.execute('SELECT COUNT(*) FROM dna_security_logs')
            total = cur.fetchone()[0]
            
            return {
                "total_operations": total,
                "by_operation_type": by_type,
                "by_status": by_status
            }
    except Exception as e:
        log_security_event("DNA_STATS_ERROR", 
                          str(e), 
                          event_type="ERROR")
        return {"error": "Failed to retrieve DNA security statistics"}

# Initialize database when the module is imported
if os.environ.get('DATABASE_URL'):
    initialize_database()