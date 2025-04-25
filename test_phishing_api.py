"""
Script pentru testarea API-ului de detecție phishing

© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
Toate drepturile rezervate global. Protejat prin legile internaționale de copyright.
"""

import requests
import json

def test_phishing_detection():
    url = "http://localhost:5001/api/analyze"
    data = {"url": "http://janeway.replit.dev"}
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Verifică dacă cererea a avut succes
        
        result = response.json()
        
        print("Status Code:", response.status_code)
        print("Response:")
        print(json.dumps(result, indent=2))
        
        # Verifică dacă rezultatul conține informațiile așteptate
        assert 'domain' in result, "Rezultatul ar trebui să conțină domeniul analizat"
        assert 'combined_risk_score' in result, "Rezultatul ar trebui să conțină un scor de risc"
        
        if result.get('is_likely_phishing'):
            print("\nAtenție! URL-ul a fost detectat ca fiind phishing!")
            print(f"Scor de risc: {result.get('combined_risk_score')}/100")
            print("Recomandare:", result.get('recommendation', 'Nedisponibilă'))
            
            # Afișează indicatorii suspicioși
            print("\nIndicatori suspicioși detectați:")
            url_patterns = result.get('suspicious_patterns', {}).get('url', [])
            content_patterns = result.get('suspicious_patterns', {}).get('content', [])
            
            if url_patterns:
                print("\nÎn URL:")
                for pattern in url_patterns:
                    print(f"- {pattern}")
            
            if content_patterns:
                print("\nÎn conținut:")
                for pattern in content_patterns:
                    print(f"- {pattern}")
        else:
            print("\nURL-ul pare sigur.")
        
        return result
    
    except requests.exceptions.ConnectionError:
        print("Eroare de conexiune! Asigurați-vă că serverul Phishing Detection rulează pe portul 5001.")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"Eroare HTTP: {e}")
        return None
    except Exception as e:
        print(f"Eroare neașteptată: {e}")
        return None

if __name__ == "__main__":
    print("Testare API de detecție phishing pentru janeway.replit.dev")
    print("=" * 60)
    test_phishing_detection()