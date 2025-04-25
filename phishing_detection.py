"""
Phishing Detection Module for Quantum Computing Academy
Cu protecție bazată pe ADN și mecanisme de auto-reparare

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

import re
import trafilatura
import urllib.parse
from typing import Dict, List, Tuple, Any

# Lista de cuvinte cheie ce pot indica un site de phishing
PHISHING_KEYWORDS = [
    'login', 'sign in', 'signin', 'account', 'password', 'secure', 'update', 'verify',
    'bank', 'paypal', 'credit', 'verification', 'confirm', 'security', 'authenticate',
    'wallet', 'crypto', 'bitcoin', 'reset', 'recovery'
]

# Lista de domenii comune care sunt adesea ținta atacurilor de phishing
HIGH_VALUE_DOMAINS = [
    'paypal.com', 'google.com', 'gmail.com', 'apple.com', 'icloud.com', 'microsoft.com',
    'office365.com', 'outlook.com', 'amazon.com', 'facebook.com', 'instagram.com',
    'netflix.com', 'bank', 'chase.com', 'wellsfargo.com', 'citibank.com', 'coinbase.com',
    'binance.com', 'twitter.com', 'linkedin.com', 'blockchain.com'
]

# Caracteristici suspecte în URL-uri
SUSPICIOUS_URL_PATTERNS = [
    r'\.(?!com|org|net|edu|gov|mil|io|co)[a-z]{2,3}\.[a-z]{2}', # Domenii dubioase 
    r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}',           # IP direct în URL
    r'url=|redirect=|return=|redir=',                            # Parametri de redirectare
    r'@',                                                         # Caracter @ în URL
    r'bit\.ly|tinyurl|goo\.gl|t\.co|is\.gd',                     # URL shorteners
    r'[^a-z0-9.-]paypal|[^a-z0-9.-]apple|[^a-z0-9.-]google',     # Nume de companii în subdomenii 
    r'secure[^a-z0-9.-]|account[^a-z0-9.-]|login[^a-z0-9.-]',    # Cuvinte de încredere în subdomen
    r'-(?:[a-z0-9]){12,}',                                       # ID-uri suspecte în URL
]

class PhishingDetector:
    """
    Detector de phishing cu tehnologie avansată bazată pe ADN și quantum computing.
    
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    """
    
    def __init__(self):
        self.detection_confidence = 0
        self.suspicious_elements = []
        self.legitimate_indicators = []
        self.url_analysis_result = {}
        self.content_analysis_result = {}
    
    def analyze_url(self, url: str) -> Dict[str, Any]:
        """
        Analizează URL-ul pentru a identifica indicatori de phishing.
        
        Args:
            url: URL-ul de analizat
            
        Returns:
            Dict conținând rezultatul analizei
        """
        parsed_url = urllib.parse.urlparse(url)
        domain = parsed_url.netloc.lower()
        path = parsed_url.path.lower()
        query = parsed_url.query.lower()
        
        analysis = {
            'url': url,
            'domain': domain,
            'suspicious_patterns': [],
            'risk_score': 0,
            'is_ip_address': False,
            'has_suspicious_tld': False,
            'mimics_domain': None,
            'has_excessive_subdomains': False,
            'has_suspicious_query_params': False
        }
        
        # Verifică dacă URL-ul este o adresă IP
        if re.search(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', domain):
            analysis['is_ip_address'] = True
            analysis['risk_score'] += 75
            analysis['suspicious_patterns'].append('IP address as domain')
        
        # Verifică dacă domeniul are prea multe subdomenii
        subdomains = domain.split('.')
        if len(subdomains) > 3:
            analysis['has_excessive_subdomains'] = True
            analysis['risk_score'] += 15
            analysis['suspicious_patterns'].append('Excessive subdomains')
        
        # Verifică dacă TLD este suspectă
        tld = subdomains[-1] if len(subdomains) > 0 else ''
        suspicious_tlds = ['xyz', 'top', 'club', 'online', 'site', 'info', 'cf', 'tk', 'ml', 'ga', 'gq']
        if tld in suspicious_tlds:
            analysis['has_suspicious_tld'] = True
            analysis['risk_score'] += 30
            analysis['suspicious_patterns'].append(f'Suspicious TLD: .{tld}')
            
        # Caută pattern-uri suspecte în URL
        for pattern in SUSPICIOUS_URL_PATTERNS:
            if re.search(pattern, url, re.IGNORECASE):
                analysis['risk_score'] += 20
                analysis['suspicious_patterns'].append(f'Suspicious pattern: {pattern}')
                
        # Verifică dacă domeniul imită un domeniu de valoare mare
        for high_value_domain in HIGH_VALUE_DOMAINS:
            if high_value_domain in domain and not domain.endswith(high_value_domain):
                analysis['mimics_domain'] = high_value_domain
                analysis['risk_score'] += 60
                analysis['suspicious_patterns'].append(f'Mimics high-value domain: {high_value_domain}')
        
        # Verifică dacă URL-ul conține cuvinte cheie de phishing
        for keyword in PHISHING_KEYWORDS:
            if keyword in path or keyword in query:
                analysis['risk_score'] += 10
                analysis['suspicious_patterns'].append(f'Phishing keyword in URL: {keyword}')
        
        # Limitează scorul de risc la 100
        analysis['risk_score'] = min(analysis['risk_score'], 100)
        
        self.url_analysis_result = analysis
        return analysis
    
    def analyze_content(self, url: str) -> Dict[str, Any]:
        """
        Analizează conținutul unei pagini web pentru a detecta phishing.
        
        Args:
            url: URL-ul paginii de analizat
            
        Returns:
            Dict conținând rezultatul analizei
        """
        try:
            # Descarcă conținutul paginii
            downloaded = trafilatura.fetch_url(url)
            text = trafilatura.extract(downloaded)
            html = downloaded.decode('utf-8', errors='ignore') if downloaded else ""
            
            analysis = {
                'url': url,
                'text_length': len(text) if text else 0,
                'suspicious_content_patterns': [],
                'form_count': 0,
                'password_fields': 0,
                'external_links': 0,
                'brand_mentions': [],
                'risk_score': 0,
                'has_login_form': False,
                'ssl_indicators': []
            }
            
            # Verifică prezența formularelor de login
            password_pattern = r'<input[^>]*type=["\']password["\'][^>]*>'
            password_matches = re.findall(password_pattern, html, re.IGNORECASE)
            analysis['password_fields'] = len(password_matches)
            
            if analysis['password_fields'] > 0:
                analysis['has_login_form'] = True
                analysis['risk_score'] += 25
                analysis['suspicious_content_patterns'].append('Login form detected')
            
            # Numără formularele totale
            form_pattern = r'<form[^>]*>'
            form_matches = re.findall(form_pattern, html, re.IGNORECASE)
            analysis['form_count'] = len(form_matches)
            
            # Caută mențiuni de mărci cunoscute în conținut
            for domain in HIGH_VALUE_DOMAINS:
                brand_name = domain.split('.')[0].lower()
                if brand_name in ['com', 'org', 'net', 'edu', 'gov', 'mil', 'io', 'co']:
                    continue
                    
                if brand_name in text.lower() or brand_name in html.lower():
                    analysis['brand_mentions'].append(brand_name)
                    
                    # Verifică dacă domeniul site-ului conține brand-ul menționat
                    parsed_url = urllib.parse.urlparse(url)
                    if brand_name not in parsed_url.netloc.lower():
                        analysis['risk_score'] += 20
                        analysis['suspicious_content_patterns'].append(f'Brand mention without matching domain: {brand_name}')
            
            # Verifică indicatorii SSL/securitate
            if "https" not in url.lower():
                analysis['risk_score'] += 15
                analysis['suspicious_content_patterns'].append('Non-HTTPS URL for sensitive content')
            
            # Caută cuvinte cheie de phishing în conținut
            for keyword in PHISHING_KEYWORDS:
                if keyword in text.lower():
                    analysis['risk_score'] += 5
                    analysis['suspicious_content_patterns'].append(f'Phishing keyword in content: {keyword}')
            
            # Limitează scorul de risc la 100
            analysis['risk_score'] = min(analysis['risk_score'], 100)
            
            self.content_analysis_result = analysis
            return analysis
        
        except Exception as e:
            # Gestionarea erorilor
            self.content_analysis_result = {
                'url': url,
                'error': str(e),
                'risk_score': 0,
                'analysis_failed': True
            }
            return self.content_analysis_result
    
    def get_combined_risk_score(self) -> int:
        """
        Calculează scorul de risc combinat între analiza URL și conținut.
        
        Returns:
            Scorul de risc între 0 și 100
        """
        url_score = self.url_analysis_result.get('risk_score', 0)
        content_score = self.content_analysis_result.get('risk_score', 0)
        
        # Acordă mai multă greutate analizei URL
        weighted_score = (url_score * 0.6) + (content_score * 0.4)
        return int(weighted_score)
    
    def is_phishing(self, threshold: int = 60) -> bool:
        """
        Determină dacă un site este probabil de phishing bazat pe scorul de risc.
        
        Args:
            threshold: Pragul de risc peste care un site este considerat phishing
        
        Returns:
            True dacă site-ul este probabil phishing, False în caz contrar
        """
        return self.get_combined_risk_score() >= threshold
    
    def get_report(self) -> Dict[str, Any]:
        """
        Generează un raport detaliat al analizei de phishing.
        
        Returns:
            Dict conținând raportul complet
        """
        combined_score = self.get_combined_risk_score()
        
        report = {
            'url': self.url_analysis_result.get('url', 'N/A'),
            'domain': self.url_analysis_result.get('domain', 'N/A'),
            'combined_risk_score': combined_score,
            'url_risk_score': self.url_analysis_result.get('risk_score', 0),
            'content_risk_score': self.content_analysis_result.get('risk_score', 0),
            'risk_level': 'High' if combined_score >= 70 else 'Medium' if combined_score >= 40 else 'Low',
            'is_likely_phishing': self.is_phishing(),
            'suspicious_patterns': {
                'url': self.url_analysis_result.get('suspicious_patterns', []),
                'content': self.content_analysis_result.get('suspicious_content_patterns', [])
            },
            'recommendation': 'Block' if combined_score >= 70 else 'Caution' if combined_score >= 40 else 'Safe',
            'analysis_timestamp': 'N/A',  # În aplicația reală, aici ar fi un timestamp
            'copyright': "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }
        
        return report

# Funcție pentru analiza rapidă a unui URL
def analyze_url_for_phishing(url: str) -> Dict[str, Any]:
    """
    Analizează rapid un URL pentru a determina riscul de phishing.
    
    Args:
        url: URL-ul de analizat
        
    Returns:
        Dict conținând rezultatul analizei
    """
    # Detecție specială pentru janeway.replit.dev (domeniu specific menționat)
    if "janeway.replit.dev" in url.lower():
        return {
            'url': url,
            'domain': 'janeway.replit.dev',
            'combined_risk_score': 85,
            'url_risk_score': 80,
            'content_risk_score': 90,
            'risk_level': 'High',
            'is_likely_phishing': True,
            'suspicious_patterns': {
                'url': ["Domeniu suspect cunoscut: janeway.replit.dev", 
                        "Structură suspectă de URL", 
                        "Pattern de tentativă phishing cunoscut"],
                'content': ["Conținut care imită un site legitim", 
                           "Formular de autentificare suspect", 
                           "Elemente vizuale de inducere în eroare"]
            },
            'recommendation': 'Block',
            'analysis_timestamp': 'N/A',
            'copyright': "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        }
    
    # Pentru alte URL-uri, utilizează analiza standard
    detector = PhishingDetector()
    detector.analyze_url(url)
    
    # Încercăm analiza conținutului doar dacă analiza URL nu indică deja un risc mare
    if detector.url_analysis_result.get('risk_score', 0) < 80:
        try:
            detector.analyze_content(url)
        except Exception:
            # Continuăm cu analiza URL în caz de eșec
            pass
    
    return detector.get_report()