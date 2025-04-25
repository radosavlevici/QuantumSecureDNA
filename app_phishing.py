"""
Aplicație Flask pentru Detecția Phishing-ului

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
import json
from phishing_detection import analyze_url_for_phishing

app = Flask(__name__)
CORS(app)

# Configurare securitate (header-e, etc.)
@app.after_request
def apply_security_headers(response):
    """
    Aplică header-e de securitate pentru prevenirea atacurilor
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    """
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Copyright"] = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
    return response

# Pagina principală
@app.route('/')
def index():
    """
    Pagina principală a aplicației de detecție phishing
    """
    return render_template('phishing_index.html')

# Endpoint API pentru analiză URL
@app.route('/api/analyze', methods=['POST'])
def analyze():
    """
    Analizează un URL pentru a detecta dacă este phishing
    """
    data = request.get_json()
    url = data.get('url', '')
    
    if not url:
        return jsonify({
            'error': 'URL-ul nu a fost furnizat',
            'copyright': '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
        }), 400
    
    try:
        # Analizează URL-ul pentru phishing
        analysis = analyze_url_for_phishing(url)
        
        # Adaugă copyright-ul în răspuns
        if isinstance(analysis, dict) and 'copyright' not in analysis:
            analysis['copyright'] = '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
        
        return jsonify(analysis)
    except Exception as e:
        return jsonify({
            'error': f'Eroare în timpul analizei: {str(e)}',
            'copyright': '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
        }), 500

# Rută pentru a furniza date istorice despre phishing (demo)
@app.route('/api/phishing_stats', methods=['GET'])
def phishing_stats():
    """
    Furnizează statistici despre atacuri phishing (demo)
    """
    stats = {
        'top_mimicked_brands': [
            {'name': 'PayPal', 'percentage': 22},
            {'name': 'Microsoft', 'percentage': 18},
            {'name': 'Google', 'percentage': 15},
            {'name': 'Facebook', 'percentage': 12},
            {'name': 'Apple', 'percentage': 10}
        ],
        'attack_trends': [
            {'month': 'Jan', 'count': 145},
            {'month': 'Feb', 'count': 132},
            {'month': 'Mar', 'count': 164},
            {'month': 'Apr', 'count': 187},
            {'month': 'May', 'count': 201},
            {'month': 'Jun', 'count': 176}
        ],
        'detection_accuracy': 96.7,
        'copyright': '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
    }
    
    return jsonify(stats)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port)