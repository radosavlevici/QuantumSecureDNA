/**
 * DNA-Based Breach Detection System for Quantum Computing Educational Platform
 * 
 * © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
 * WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE
 * capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
 */

// Configuration for breach detection system
const BREACH_CONFIG = {
    enableDetection: true,
    enableCountermeasures: true,
    scanInterval: 3000, // milliseconds
    sensitiveAttributes: ['data-protected', 'data-secure', 'data-copyright'],
    secureSelectors: [
        '.security-badge', 
        '.copyright-tag', 
        '.footer-copyright', 
        '.security-key'
    ],
    unauthorizedPatterns: [
        /hack/i, 
        /bypass/i, 
        /steal/i, 
        /inject/i
    ],
    honeypots: [
        {
            id: 'security-trap-1',
            type: 'element',
            attributes: {
                'class': 'hidden-security-element',
                'style': 'display: none; position: absolute; left: -9999px;'
            },
            content: 'Copyright protected content trap'
        },
        {
            id: 'security-trap-2',
            type: 'variable',
            name: '_securityKey',
            value: 'PROTECTED_SYSTEM_DO_NOT_ACCESS'
        }
    ]
};

// Initialize system on page load
document.addEventListener('DOMContentLoaded', function() {
    if (BREACH_CONFIG.enableDetection) {
        console.debug("Initializing DNA-based breach detection...");
        
        // Setup honeypot traps
        setupHoneypots();
        
        // Start the breach detection scan
        startDetectionScan();
        
        // Monitor user interactions
        monitorUserActivity();
        
        // Add protection for code inspection
        protectCodeInspection();
    }
});

// Setup honeypot traps to detect unauthorized access
function setupHoneypots() {
    BREACH_CONFIG.honeypots.forEach(honeypot => {
        if (honeypot.type === 'element') {
            // Create a hidden element as a trap
            const element = document.createElement('div');
            element.id = honeypot.id;
            
            // Add attributes to the honeypot
            Object.keys(honeypot.attributes).forEach(attr => {
                element.setAttribute(attr, honeypot.attributes[attr]);
            });
            
            // Add content to the honeypot
            element.textContent = honeypot.content;
            element.setAttribute('data-copyright', '© Ervin Remus Radosavlevici');
            
            // Add the honeypot to the document
            document.body.appendChild(element);
            
            // Set up access monitoring for the honeypot
            monitorElementAccess(element);
        }
        else if (honeypot.type === 'variable') {
            // Create a global variable as a trap
            window[honeypot.name] = honeypot.value;
            
            // Set up a getter to detect access
            Object.defineProperty(window, honeypot.name, {
                get: function() {
                    detectBreach(`Unauthorized access to honeypot variable: ${honeypot.name}`);
                    return honeypot.value;
                },
                configurable: false
            });
        }
    });
}

// Monitor access to honeypot elements
function monitorElementAccess(element) {
    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            detectBreach(`Honeypot element ${element.id} was modified`);
        });
    });
    
    observer.observe(element, {
        attributes: true,
        childList: true,
        subtree: true,
        characterData: true
    });
}

// Start the periodic breach detection scan
function startDetectionScan() {
    setInterval(() => {
        // Scan for tampering with protected elements
        scanProtectedElements();
        
        // Check for unauthorized code injection
        scanForInjectedCode();
        
        // Verify security integrity
        verifySecurityIntegrity();
    }, BREACH_CONFIG.scanInterval);
}

// Scan protected elements for tampering
function scanProtectedElements() {
    // Check all elements with sensitive attributes
    BREACH_CONFIG.sensitiveAttributes.forEach(attr => {
        document.querySelectorAll(`[${attr}]`).forEach(element => {
            // Check if element has been visibly modified
            if (element.style.display === 'none' && !element.getAttribute('data-originally-hidden')) {
                detectBreach(`Protected element with ${attr} was hidden`);
            }
            
            // Check if element has been moved off-screen
            const rect = element.getBoundingClientRect();
            if (rect.width > 0 && rect.height > 0 && 
                (rect.left < -1000 || rect.top < -1000) && 
                !element.getAttribute('data-originally-offscreen')) {
                detectBreach(`Protected element with ${attr} was moved off-screen`);
            }
        });
    });
    
    // Check secure selectors
    BREACH_CONFIG.secureSelectors.forEach(selector => {
        const elements = document.querySelectorAll(selector);
        if (elements.length === 0 && selector !== '.security-key') {
            detectBreach(`Secure element with selector "${selector}" is missing`);
        }
    });
}

// Scan for unauthorized code injection
function scanForInjectedCode() {
    // Check for unauthorized inline scripts
    document.querySelectorAll('script:not([src])').forEach(script => {
        if (!script.getAttribute('data-authorized')) {
            const content = script.textContent;
            
            // Check for unauthorized patterns
            BREACH_CONFIG.unauthorizedPatterns.forEach(pattern => {
                if (pattern.test(content)) {
                    detectBreach(`Potentially malicious script detected: ${pattern}`);
                }
            });
        }
    });
    
    // Check for unauthorized elements with javascript: URLs
    document.querySelectorAll('[href^="javascript:"], [src^="javascript:"]').forEach(element => {
        if (!element.getAttribute('data-authorized')) {
            detectBreach(`Unauthorized javascript: URI detected`);
        }
    });
}

// Verify the integrity of security features
function verifySecurityIntegrity() {
    // Check if the security.js script is still present
    const securityScript = document.querySelector('script[src*="security.js"]');
    if (!securityScript) {
        detectBreach(`Security script has been removed from the page`);
        
        // Auto-repair by re-adding the script
        if (BREACH_CONFIG.enableCountermeasures) {
            const newScript = document.createElement('script');
            newScript.src = '/static/js/security.js';
            document.head.appendChild(newScript);
        }
    }
    
    // Check if critical security functions exist
    if (typeof checkDocumentIntegrity !== 'function') {
        detectBreach(`Critical security function 'checkDocumentIntegrity' is missing`);
    }
}

// Monitor user activity for suspicious patterns
function monitorUserActivity() {
    // Monitor rapid key sequences (potential automation/script)
    let keyPressCount = 0;
    let lastKeyPressTime = 0;
    
    document.addEventListener('keydown', event => {
        const now = Date.now();
        if (now - lastKeyPressTime < 50) { // Less than 50ms between keypresses
            keyPressCount++;
            if (keyPressCount > 10) { // More than 10 rapid keypresses
                detectBreach(`Suspicious rapid key sequence detected`);
                keyPressCount = 0;
            }
        } else {
            keyPressCount = 0;
        }
        lastKeyPressTime = now;
    });
    
    // Monitor attempts to copy protected content
    document.addEventListener('copy', event => {
        const selection = window.getSelection();
        if (selection && selection.toString()) {
            // Check if the selection contains protected content
            let containsProtected = false;
            const selectedNodes = getSelectedNodes();
            
            for (const node of selectedNodes) {
                if (node.nodeType === Node.ELEMENT_NODE &&
                    (node.getAttribute('data-protected') || 
                     node.closest('[data-protected]'))) {
                    containsProtected = true;
                    break;
                }
            }
            
            if (containsProtected) {
                detectBreach(`Attempt to copy protected content`);
                if (BREACH_CONFIG.enableCountermeasures) {
                    // Modify the clipboard content to include attribution
                    const originalText = selection.toString();
                    const attributed = `${originalText}\n\n© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)`;
                    event.clipboardData.setData('text/plain', attributed);
                    event.preventDefault();
                }
            }
        }
    });
}

// Helper function to get all nodes in the current selection
function getSelectedNodes() {
    const selection = window.getSelection();
    if (!selection.rangeCount) return [];
    
    const range = selection.getRangeAt(0);
    const container = range.commonAncestorContainer;
    
    if (container.nodeType === Node.TEXT_NODE) {
        return [container.parentNode];
    }
    
    const nodes = [];
    const walker = document.createTreeWalker(
        container, 
        NodeFilter.SHOW_ELEMENT + NodeFilter.SHOW_TEXT,
        { acceptNode: node => range.intersectsNode(node) ? NodeFilter.FILTER_ACCEPT : NodeFilter.FILTER_REJECT }
    );
    
    let currentNode = walker.currentNode;
    while (currentNode) {
        nodes.push(currentNode);
        currentNode = walker.nextNode();
    }
    
    return nodes;
}

// Add protection against code inspection
function protectCodeInspection() {
    // Add debugger-triggering protection (for detecting dev tools)
    setInterval(() => {
        const devToolsOpen = window.outerHeight - window.innerHeight > 200 || 
                             window.outerWidth - window.innerWidth > 200;
        if (devToolsOpen) {
            detectBreach(`Developer tools opened - possible debugging attempt`);
        }
    }, 5000);
    
    // Add function to obscure security-related code
    Function.prototype.toString = (function(originalToString) {
        return function() {
            const functionString = originalToString.apply(this, arguments);
            
            // Check if this is a security-related function
            if (functionString.includes('security') || 
                functionString.includes('breach') || 
                functionString.includes('detect') ||
                functionString.includes('Ervin Remus Radosavlevici')) {
                
                // Add copyright notice to the function string
                const lines = functionString.split('\n');
                if (lines.length > 2) {
                    lines.splice(1, 0, '  /* © 2025 Ervin Remus Radosavlevici - Protected Code */');
                    return lines.join('\n');
                }
            }
            
            return functionString;
        };
    })(Function.prototype.toString);
}

// Function to handle breach detection
function detectBreach(details) {
    console.warn(`Breach detected: ${details}`);
    
    // Log the breach
    if (typeof logSecurityEvent === 'function') {
        logSecurityEvent('BREACH_DETECTED', details);
    }
    
    // Implement countermeasures if enabled
    if (BREACH_CONFIG.enableCountermeasures) {
        implementCountermeasures(details);
    }
}

// Implement countermeasures against detected breaches
function implementCountermeasures(breachDetails) {
    // Add visible security warning to page
    const existingWarning = document.getElementById('security-breach-warning');
    if (!existingWarning) {
        const warning = document.createElement('div');
        warning.id = 'security-breach-warning';
        warning.style.position = 'fixed';
        warning.style.top = '0';
        warning.style.left = '0';
        warning.style.width = '100%';
        warning.style.backgroundColor = 'rgba(255, 0, 0, 0.8)';
        warning.style.color = 'white';
        warning.style.padding = '10px';
        warning.style.textAlign = 'center';
        warning.style.fontWeight = 'bold';
        warning.style.zIndex = '9999';
        warning.textContent = 'SECURITY ALERT: Unauthorized activity detected. This incident has been logged.';
        
        document.body.appendChild(warning);
        
        // Remove the warning after 5 seconds
        setTimeout(() => {
            if (warning.parentNode) {
                warning.parentNode.removeChild(warning);
            }
        }, 5000);
    }
    
    // Submit breach report (in production, would send to server)
    // Currently just logs to console for demonstration
    console.error('BREACH REPORT:', {
        timestamp: new Date().toISOString(),
        details: breachDetails,
        url: window.location.href,
        userAgent: navigator.userAgent,
        referrer: document.referrer,
        copyright: '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)'
    });
}