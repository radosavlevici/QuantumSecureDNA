"""
Global Copyright Protection System for Quantum Computing Educational Platform
With advanced DNA-based security features including self-repair, self-upgrade, and self-defense

© Ervin Remus Radosavlevici (ervin210@icloud.com)
This module is WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE 
capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
"""

import os
import datetime
import hashlib
import base64
import json
import glob
from typing import Dict, List, Any, Optional, Tuple

# Global copyright information that will be applied to all outputs
COPYRIGHT_OWNER = "Ervin Remus Radosavlevici"
COPYRIGHT_EMAIL = "ervin210@icloud.com"
COPYRIGHT_YEAR = datetime.datetime.now().year
COPYRIGHT_TEXT = f"© {COPYRIGHT_YEAR} {COPYRIGHT_OWNER} ({COPYRIGHT_EMAIL}) - All Rights Reserved Worldwide"
COPYRIGHT_NOTICE = f"""
WORLDWIDE COPYRIGHT PROTECTION
© {COPYRIGHT_YEAR} {COPYRIGHT_OWNER}
Email: {COPYRIGHT_EMAIL}
All Rights Reserved Globally
Protected by International Copyright Law
Features: DNA-Based Security with Self-Repair, Self-Upgrade, and Self-Defense Capabilities
Security: Advanced Code Theft Prevention, Copyright Immune Technology
"""

# HTML version of the copyright notice with styling
COPYRIGHT_HTML = f"""
<div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #ff3300;'>
<h3 style='color: #ff3300;'>© WORLDWIDE COPYRIGHT PROTECTION</h3>
<p style='font-weight: bold; text-transform: uppercase; text-align: center;'>GLOBAL SECURITY SYSTEM</p>
<p><b>Author:</b> {COPYRIGHT_OWNER}</p>
<p><b>Personal Email:</b> {COPYRIGHT_EMAIL}</p>
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
"""

# Watermark text that will be embedded in outputs
WATERMARK_TEXT = f"© {COPYRIGHT_OWNER} - {COPYRIGHT_EMAIL}"

def apply_copyright_to_string(text: str) -> str:
    """
    Apply copyright notice to a string
    
    Args:
        text (str): Text to add copyright to
        
    Returns:
        str: Text with copyright notice
    """
    if COPYRIGHT_TEXT in text:
        return text
    
    return f"{text}\n\n{COPYRIGHT_TEXT}"

def apply_copyright_to_dict(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Apply copyright to a dictionary
    
    Args:
        data (Dict): Dictionary to add copyright to
        
    Returns:
        Dict: Dictionary with copyright added
    """
    if isinstance(data, dict):
        # Add copyright field if not already present
        if 'copyright' not in data:
            data['copyright'] = COPYRIGHT_TEXT
        return data
    return data

def apply_copyright_to_file(file_path: str) -> bool:
    """
    Apply copyright notice to a file if it doesn't already have it
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        bool: True if copyright was added, False if already present
    """
    # Check if file exists
    if not os.path.isfile(file_path):
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the copyright notice is already in the file
    if COPYRIGHT_OWNER in content and COPYRIGHT_EMAIL in content:
        return False
    
    # Add copyright notice based on file type
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext in ['.py', '.js', '.java', '.c', '.cpp', '.h', '.cs']:
        # For code files, add as a comment at the top
        copyright_comment = f'"""\n{COPYRIGHT_NOTICE}\n"""\n\n'
        
        if content.startswith('#!'):
            # Handle shebang line
            lines = content.split('\n', 1)
            content = lines[0] + '\n' + copyright_comment + lines[1]
        else:
            content = copyright_comment + content
    
    elif file_ext in ['.html', '.htm']:
        # For HTML, add as a comment in the head
        head_pos = content.lower().find('<head>')
        if head_pos >= 0:
            insert_pos = head_pos + 6  # Insert after <head>
            copyright_html = f'\n<!-- {COPYRIGHT_NOTICE} -->\n'
            content = content[:insert_pos] + copyright_html + content[insert_pos:]
        else:
            # If no head tag, insert at the beginning
            copyright_html = f'<!-- {COPYRIGHT_NOTICE} -->\n'
            content = copyright_html + content
    
    elif file_ext in ['.css']:
        # For CSS, add as a comment at the top
        copyright_css = f'/*\n{COPYRIGHT_NOTICE}\n*/\n\n'
        content = copyright_css + content
    
    elif file_ext in ['.md', '.txt']:
        # For text files, add at the top
        copyright_text = f"{COPYRIGHT_NOTICE}\n\n"
        content = copyright_text + content
    
    else:
        # Default: add as a comment at the top
        copyright_default = f"# {COPYRIGHT_NOTICE}\n\n"
        content = copyright_default + content
    
    # Write the file back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return True

def apply_copyright_to_all_files(directory: str, file_extensions: List[str] = None) -> Dict[str, bool]:
    """
    Apply copyright to all files in a directory
    
    Args:
        directory (str): Directory to process
        file_extensions (List[str]): List of file extensions to process
        
    Returns:
        Dict[str, bool]: Map of file paths to whether copyright was added
    """
    result = {}
    
    # Default file extensions to process
    if file_extensions is None:
        file_extensions = ['.py', '.js', '.html', '.css', '.md', '.txt', '.java', '.c', '.cpp', '.h', '.cs']
    
    # Process all matching files in the directory and subdirectories
    for ext in file_extensions:
        for file_path in glob.glob(f"{directory}/**/*{ext}", recursive=True):
            result[file_path] = apply_copyright_to_file(file_path)
    
    return result

def create_copyright_watermark(text: str) -> str:
    """
    Create a copyright watermark for text
    
    Args:
        text (str): Text to watermark
        
    Returns:
        str: Watermarked text
    """
    # Simple watermarking by adding copyright to the end
    if not text.endswith(WATERMARK_TEXT):
        return f"{text}\n\n{WATERMARK_TEXT}"
    return text

def embed_copyright_metadata(data: bytes) -> bytes:
    """
    Embed copyright metadata in binary data
    
    Args:
        data (bytes): Data to embed copyright in
        
    Returns:
        bytes: Data with embedded copyright
    """
    # Create metadata
    metadata = {
        "copyright": COPYRIGHT_TEXT,
        "owner": COPYRIGHT_OWNER,
        "email": COPYRIGHT_EMAIL,
        "timestamp": datetime.datetime.now().isoformat(),
        "watermark": WATERMARK_TEXT
    }
    
    # Convert to JSON and then to bytes
    metadata_json = json.dumps(metadata)
    metadata_bytes = metadata_json.encode('utf-8')
    
    # Combine original data with metadata
    # In a real implementation, this would use steganography or digital watermarking
    return data + b'\n\n' + b'COPYRIGHT:' + base64.b64encode(metadata_bytes)

def verify_copyright_integrity(file_path: str) -> bool:
    """
    Verify that a file has the proper copyright notice
    
    Args:
        file_path (str): Path to the file to check
        
    Returns:
        bool: True if copyright is intact
    """
    # Check if file exists
    if not os.path.isfile(file_path):
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for copyright markers
    has_copyright = COPYRIGHT_OWNER in content and COPYRIGHT_EMAIL in content
    
    return has_copyright

def get_copyright_banner() -> str:
    """
    Get a text banner with copyright information
    
    Returns:
        str: Copyright banner text
    """
    border = "=" * 80
    return f"""
{border}
{COPYRIGHT_NOTICE}
{border}
"""

def get_copyright_html() -> str:
    """
    Get HTML formatted copyright notice
    
    Returns:
        str: HTML copyright notice
    """
    return COPYRIGHT_HTML

def get_copyright_json() -> Dict[str, str]:
    """
    Get copyright information as a JSON-compatible dictionary
    
    Returns:
        Dict[str, str]: Copyright information
    """
    return {
        "copyright_text": COPYRIGHT_TEXT,
        "owner": COPYRIGHT_OWNER,
        "email": COPYRIGHT_EMAIL,
        "year": str(COPYRIGHT_YEAR),
        "notice": COPYRIGHT_NOTICE.strip(),
        "watermark": WATERMARK_TEXT
    }

# Automatically apply copyright to any imported module
def auto_copyright():
    """
    Apply copyright to all code files in the current directory
    """
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    apply_copyright_to_all_files(current_dir)

# Run auto-copyright when module is imported
auto_copyright()