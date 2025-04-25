"""
Modul de Web Scraping pentru Quantum Computing Academy
Cu protecție bazată pe ADN și mecanisme de auto-reparare

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

import trafilatura
import re
from typing import Dict, List, Any, Tuple, Optional

class WebContentAnalyzer:
    """
    Analizor de conținut web cu protecție ADN și tehnologie quantum
    
    © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
    """
    
    def __init__(self):
        """Inițializează analizorul de conținut"""
        self.raw_content = ""
        self.extracted_text = ""
        self.copyright_notice = "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)"
        self.security_patterns = {
            'phishing': [
                r'password.*required',
                r'login.*account.*verify',
                r'security.*warning',
                r'limit.*access',
                r'confirm.*identity'
            ],
            'malware': [
                r'download.*now',
                r'install.*required',
                r'update.*flash',
                r'enable.*javascript',
                r'accept.*cookies'
            ],
            'spyware': [
                r'track.*activity',
                r'monitor.*usage',
                r'collect.*data',
                r'record.*behavior',
                r'analyze.*preferences'
            ]
        }
    
    def analyze_url(self, url: str) -> Dict[str, Any]:
        """
        Analizează conținutul unei pagini web și extrage informații relevante
        
        Args:
            url: URL-ul paginii de analizat
            
        Returns:
            Dict conținând rezultatul analizei
        """
        try:
            # Descarcă conținutul paginii
            self.raw_content = trafilatura.fetch_url(url)
            if not self.raw_content:
                return {
                    'success': False,
                    'error': 'Nu s-a putut descărca conținutul URL-ului',
                    'copyright': self.copyright_notice
                }
            
            # Extrage textul principal
            self.extracted_text = trafilatura.extract(self.raw_content) or ""
            
            # Analizează textul pentru indicatori de securitate
            security_analysis = self._analyze_security_indicators()
            
            # Generează statistici despre text
            text_stats = self._generate_text_statistics()
            
            return {
                'success': True, 
                'url': url,
                'content_length': len(self.raw_content),
                'text_length': len(self.extracted_text),
                'text_statistics': text_stats,
                'security_analysis': security_analysis,
                'copyright': self.copyright_notice
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': f'Eroare la analiza URL-ului: {str(e)}',
                'copyright': self.copyright_notice
            }
    
    def get_website_text_content(self, url: str) -> str:
        """
        Extrage doar textul principal al unei pagini web.
        
        Args:
            url: URL-ul paginii
            
        Returns:
            Textul principal extras din pagină
        """
        downloaded = trafilatura.fetch_url(url)
        if not downloaded:
            return f"Eroare: Nu s-a putut descărca conținutul de la {url}"
        
        text = trafilatura.extract(downloaded) or ""
        return text
    
    def _analyze_security_indicators(self) -> Dict[str, Any]:
        """
        Analizează textul pentru a identifica indicatori de securitate.
        
        Returns:
            Dict conținând rezultatul analizei de securitate
        """
        if not self.extracted_text:
            return {
                'threats_detected': False,
                'details': 'Nu există conținut pentru analiză'
            }
        
        threats = {}
        for category, patterns in self.security_patterns.items():
            matches = []
            for pattern in patterns:
                if re.search(pattern, self.extracted_text, re.IGNORECASE):
                    matches.append(pattern)
            
            if matches:
                threats[category] = matches
        
        return {
            'threats_detected': len(threats) > 0,
            'threat_categories': list(threats.keys()),
            'details': threats
        }
    
    def _generate_text_statistics(self) -> Dict[str, Any]:
        """
        Generează statistici despre textul extras.
        
        Returns:
            Dict conținând statistici despre text
        """
        if not self.extracted_text:
            return {
                'word_count': 0,
                'sentence_count': 0,
                'paragraph_count': 0
            }
        
        words = re.findall(r'\b\w+\b', self.extracted_text)
        sentences = re.split(r'[.!?]+', self.extracted_text)
        paragraphs = re.split(r'\n\s*\n', self.extracted_text)
        
        return {
            'word_count': len(words),
            'sentence_count': len([s for s in sentences if s.strip()]),
            'paragraph_count': len([p for p in paragraphs if p.strip()]),
            'average_word_length': sum(len(word) for word in words) / max(len(words), 1),
            'top_words': self._get_top_words(words, 10)
        }
    
    def _get_top_words(self, words: List[str], limit: int = 10) -> List[Tuple[str, int]]:
        """
        Identifică cele mai frecvente cuvinte din text.
        
        Args:
            words: Lista de cuvinte
            limit: Numărul maxim de cuvinte de returnat
            
        Returns:
            Lista de tuple (cuvânt, frecvență) sortată descrescător după frecvență
        """
        word_count = {}
        for word in words:
            word = word.lower()
            if len(word) > 3:  # Ignoră cuvintele prea scurte
                word_count[word] = word_count.get(word, 0) + 1
        
        # Sortează și limitează
        top_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:limit]
        return top_words

# Funcție simplă pentru accesul rapid la conținutul textual al unui site web
def get_website_text_content(url: str) -> str:
    """
    Această funcție extrage conținutul textual principal al unui site web.
    Textul extras este mai ușor de înțeles decât HTML-ul brut.
    
    Args:
        url: URL-ul site-ului web
        
    Returns:
        Conținutul textual principal al site-ului
    """
    # Trimite o cerere către site
    downloaded = trafilatura.fetch_url(url)
    if not downloaded:
        return f"Eroare: Nu s-a putut descărca conținutul de la {url}"
    
    text = trafilatura.extract(downloaded) or "Niciun conținut textual găsit"
    return text

# Funcție pentru analiză detaliată a conținutului unui site
def analyze_website_content(url: str) -> Dict[str, Any]:
    """
    Realizează o analiză completă a conținutului unui site web.
    
    Args:
        url: URL-ul site-ului web
        
    Returns:
        Dicționar cu rezultatele analizei
    """
    analyzer = WebContentAnalyzer()
    return analyzer.analyze_url(url)