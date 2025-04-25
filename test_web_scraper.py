"""
Script pentru testarea modulului de Web Scraping

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

import web_scraper
import json

def test_web_content_analyzer():
    print("Testare WebContentAnalyzer - Analiză completă")
    print("=" * 60)
    
    # URL pentru testare
    test_url = "https://www.python.org"
    
    # Obține rezultate complete
    result = web_scraper.analyze_website_content(test_url)
    
    # Afișează rezultatele în format JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Verifică rezultatele
    if result.get('success'):
        print("\nSucces: Analiza a fost realizată cu succes!")
        print(f"Lungime text extras: {result.get('text_length', 0)} caractere")
        print(f"Număr cuvinte: {result.get('text_statistics', {}).get('word_count', 0)}")
        
        # Verifică amenințări
        security = result.get('security_analysis', {})
        if security.get('threats_detected'):
            print("\nAtenție! Amenințări potențiale detectate:")
            for category in security.get('threat_categories', []):
                print(f"- {category}")
        else:
            print("\nNicio amenințare de securitate detectată.")
    else:
        print("\nEroare în timpul analizei:")
        print(result.get('error', 'Eroare necunoscută'))

def test_simple_text_extraction():
    print("\n" + "=" * 60)
    print("Testare extragere simplă de text")
    print("=" * 60)
    
    # URL pentru testare
    test_url = "https://www.python.org"
    
    # Obține doar textul
    text = web_scraper.get_website_text_content(test_url)
    
    # Afișează primele 500 de caractere
    print("Primele 500 de caractere din textul extras:")
    print("-" * 60)
    print(text[:500] + "...")
    print("-" * 60)
    print(f"Lungime totală text: {len(text)} caractere")

if __name__ == "__main__":
    print("Testare modul Web Scraping")
    print("=" * 60)
    
    # Rulează testele
    test_web_content_analyzer()
    test_simple_text_extraction()