"""
Script pentru testarea API-urilor Web Content

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

import requests
import json
from pprint import pprint

def test_extract_text_api():
    print("Testare API extract_text")
    print("=" * 60)
    
    url = "http://localhost:5001/api/extract_text"
    data = {"url": "https://www.python.org"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        print(f"Status Code: {response.status_code}")
        print(f"Text Length: {result.get('text_length')} caractere")
        print(f"Truncated: {result.get('truncated')}")
        
        # Afișează primele 200 de caractere din text
        text = result.get('text', '')
        print("\nExtras din text (primele 200 caractere):")
        print("-" * 60)
        print(text[:200] + "..." if len(text) > 200 else text)
        print("-" * 60)
        
        return result
    
    except Exception as e:
        print(f"Eroare în timpul testului: {e}")
        return None

def test_analyze_content_api():
    print("\nTestare API analyze_content")
    print("=" * 60)
    
    url = "http://localhost:5001/api/analyze_content"
    data = {"url": "https://www.python.org"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        print(f"Status Code: {response.status_code}")
        print(f"Content Length: {result.get('content_length')} bytes")
        print(f"Text Length: {result.get('text_length')} caractere")
        
        # Afișează statisticile textului
        text_stats = result.get('text_statistics', {})
        print("\nStatistici Text:")
        print(f"- Cuvinte: {text_stats.get('word_count')}")
        print(f"- Propoziții: {text_stats.get('sentence_count')}")
        print(f"- Paragrafe: {text_stats.get('paragraph_count')}")
        
        # Afișează cele mai frecvente cuvinte
        print("\nCele mai frecvente cuvinte:")
        top_words = text_stats.get('top_words', [])
        for word, count in top_words[:5]:
            print(f"- {word}: {count} apariții")
        
        # Afișează analiza de phishing
        phishing = result.get('phishing_analysis', {})
        if phishing:
            print("\nAnaliză Phishing:")
            print(f"- Risc: {phishing.get('risk_level')}")
            print(f"- Scor: {phishing.get('combined_risk_score')}/100")
            print(f"- Recomandare: {phishing.get('recommendation')}")
        
        # Afișează analiza de securitate
        security = result.get('security_analysis', {})
        if security:
            print("\nAnaliză Securitate:")
            print(f"- Amenințări detectate: {security.get('threats_detected')}")
            for category in security.get('threat_categories', []):
                print(f"- Categorie de amenințare: {category}")
        
        return result
    
    except Exception as e:
        print(f"Eroare în timpul testului: {e}")
        return None

def test_phishing_site():
    print("\nTestare site potențial phishing")
    print("=" * 60)
    
    url = "http://localhost:5001/api/analyze_content"
    data = {"url": "http://janeway.replit.dev"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        
        result = response.json()
        
        # Verifică analiza de phishing
        phishing = result.get('phishing_analysis', {})
        if phishing:
            print("\nAnaliză Phishing pentru domeniul suspect:")
            print(f"- Domeniu: {phishing.get('domain')}")
            print(f"- Risc: {phishing.get('risk_level')}")
            print(f"- Scor: {phishing.get('combined_risk_score')}/100")
            print(f"- Recomandare: {phishing.get('recommendation')}")
            
            # Afișează motivele detectării
            print("\nIndicatori suspicioși:")
            suspicious = phishing.get('suspicious_patterns', {})
            
            url_patterns = suspicious.get('url', [])
            if url_patterns:
                print("\nÎn URL:")
                for pattern in url_patterns:
                    print(f"- {pattern}")
            
            content_patterns = suspicious.get('content', [])
            if content_patterns:
                print("\nÎn conținut:")
                for pattern in content_patterns:
                    print(f"- {pattern}")
        
        return result
    
    except Exception as e:
        print(f"Eroare în timpul testului: {e}")
        return None

if __name__ == "__main__":
    print("Testare API-uri pentru Analiza Conținutului Web")
    print("=" * 60)
    
    # Testează API-urile
    test_extract_text_api()
    test_analyze_content_api()
    test_phishing_site()