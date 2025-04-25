/**
 * Web Scraper Module for Quantum Computing Academy
 * With DNA-based protection and self-repair mechanisms
 * 
 * © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
 * All rights reserved globally. Protected by international copyright laws.
 */

// Variabile pentru stocare temporară
let lastScrapeResult = null;
let lastAnalysisResult = null;

/**
 * Extrage conținutul text de pe un website și afișează rezultatele
 * @param {string} url - URL-ul site-ului web de analizat
 * @param {function} onSuccess - Callback pentru succes
 * @param {function} onError - Callback pentru eroare
 */
function extractWebsiteText(url, onSuccess, onError) {
    // Verificare URL
    if (!url) {
        onError('URL-ul nu poate fi gol');
        return;
    }
    
    // Adaugă schema dacă lipsește
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        url = 'https://' + url;
    }
    
    // Trimite cererea la server
    fetch('/api/extract_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Eroare de server: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            onError(data.error);
        } else {
            // Stochează rezultatul pentru utilizare ulterioară
            lastScrapeResult = data;
            
            // Apelează callback-ul de succes
            onSuccess(data);
        }
    })
    .catch(error => {
        onError(`Eroare în timpul extragerii textului: ${error.message}`);
    });
}

/**
 * Analizează conținutul complet al unui website și returnează informații detaliate
 * @param {string} url - URL-ul site-ului web de analizat
 * @param {function} onSuccess - Callback pentru succes
 * @param {function} onError - Callback pentru eroare
 */
function analyzeWebsiteContent(url, onSuccess, onError) {
    // Verificare URL
    if (!url) {
        onError('URL-ul nu poate fi gol');
        return;
    }
    
    // Adaugă schema dacă lipsește
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        url = 'https://' + url;
    }
    
    // Trimite cererea la server
    fetch('/api/analyze_content', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Eroare de server: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            onError(data.error);
        } else {
            // Stochează rezultatul pentru utilizare ulterioară
            lastAnalysisResult = data;
            
            // Apelează callback-ul de succes
            onSuccess(data);
        }
    })
    .catch(error => {
        onError(`Eroare în timpul analizei conținutului: ${error.message}`);
    });
}

/**
 * Verifică un URL pentru a detecta dacă este phishing
 * @param {string} url - URL-ul de verificat
 * @param {function} onSuccess - Callback pentru succes
 * @param {function} onError - Callback pentru eroare
 */
function checkForPhishing(url, onSuccess, onError) {
    // Verificare URL
    if (!url) {
        onError('URL-ul nu poate fi gol');
        return;
    }
    
    // Adaugă schema dacă lipsește
    if (!url.startsWith('http://') && !url.startsWith('https://')) {
        url = 'https://' + url;
    }
    
    // Trimite cererea la server
    fetch('/api/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url: url })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Eroare de server: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        if (data.error) {
            onError(data.error);
        } else {
            // Aplică strategii de protecție a utilizatorului
            if (data.is_likely_phishing) {
                console.warn(`[AVERTISMENT] Site potențial de phishing detectat: ${url}`);
            }
            
            // Apelează callback-ul de succes
            onSuccess(data);
        }
    })
    .catch(error => {
        onError(`Eroare în timpul verificării phishing: ${error.message}`);
    });
}

/**
 * Obține cele mai frecvente cuvinte dintr-un text
 * @param {string} text - Textul de analizat
 * @param {number} limit - Numărul maxim de cuvinte de returnat
 * @returns {Array} - Array de obiecte {word, count}, sortate descrescător după count
 */
function getMostFrequentWords(text, limit = 10) {
    if (!text) return [];
    
    // Elimină semnele de punctuație și împarte în cuvinte
    const words = text.toLowerCase()
        .replace(/[^\w\s]/g, '')
        .split(/\s+/)
        .filter(word => word.length > 3);
    
    // Numără frecvența cuvintelor
    const wordCount = {};
    words.forEach(word => {
        wordCount[word] = (wordCount[word] || 0) + 1;
    });
    
    // Convertește la array și sortează
    const sortedWords = Object.entries(wordCount)
        .map(([word, count]) => ({ word, count }))
        .sort((a, b) => b.count - a.count)
        .slice(0, limit);
    
    return sortedWords;
}

/**
 * Evaluează riscul de phishing bazat pe conținutul textual
 * @param {string} text - Textul de analizat
 * @returns {object} - Obiect conținând scorul de risc și indicatorii detectați
 */
function evaluatePhishingContent(text) {
    if (!text) return { score: 0, indicators: [] };
    
    const indicators = [];
    let score = 0;
    
    // Verifică prezența cuvintelor cheie asociate cu phishing
    const phishingKeywords = [
        'password', 'login', 'account', 'verify', 'confirm', 'update', 
        'security', 'banking', 'payment', 'urgent', 'alert', 'suspended',
        'unusual', 'activity', 'authenticate', 'limited', 'access'
    ];
    
    const textLower = text.toLowerCase();
    
    // Verifică fiecare cuvânt cheie
    phishingKeywords.forEach(keyword => {
        if (textLower.includes(keyword)) {
            score += 5; // Adaugă 5 puncte pentru fiecare cuvânt cheie găsit
            indicators.push(`Conține cuvântul "${keyword}"`);
        }
    });
    
    // Verifică combinații de cuvinte
    const phishingPhrases = [
        'verify your account', 'confirm your password', 'update your information',
        'security alert', 'account suspended', 'unusual activity', 'limited access',
        'click here to login', 'verify identity', 'prompt action required'
    ];
    
    phishingPhrases.forEach(phrase => {
        if (textLower.includes(phrase)) {
            score += 10; // Adaugă 10 puncte pentru fraze specifice
            indicators.push(`Conține fraza suspectă "${phrase}"`);
        }
    });
    
    // Limitează scorul la 100
    score = Math.min(score, 100);
    
    return {
        score,
        indicators: indicators.slice(0, 5) // Returnează maximum 5 indicatori
    };
}

// Exportă funcțiile pentru utilizare în alte module
window.WebScraper = {
    extractWebsiteText,
    analyzeWebsiteContent,
    checkForPhishing,
    getMostFrequentWords,
    evaluatePhishingContent
};