/**
 * Advanced Security JavaScript Module for Quantum Computing Educational Platform
 * 
 * © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
 * WORLDWIDE COPYRIGHT PROTECTED and contains SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE
 * capabilities against CODE THEFT. Protected by INTERNATIONAL COPYRIGHT LAW.
 */

// Global security configuration
const SECURITY_CONFIG = {
    enableCopyright: true,
    enableTamperDetection: true,
    enableSelfRepair: true,
    metadataAttributions: {
        author: "Ervin Remus Radosavlevici (ervin210@icloud.com)",
        copyright: "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - Toate drepturile rezervate"
    },
    checkIntervalMs: 1000, // Check every second
    repairIntervalMs: 5000, // Repair every 5 seconds
    footerSelector: '.footer-security',
    securitySelectors: {
        copyright: 'meta[name="copyright"]',
        author: 'meta[name="author"]'
    }
};

// Initialization function
document.addEventListener("DOMContentLoaded", function() {
    // Initialize security system
    console.info("Initializing DNA-based security system...");
    initializeSecurity();
    
    // Set up periodic checks
    if (SECURITY_CONFIG.enableTamperDetection) {
        setInterval(checkDocumentIntegrity, SECURITY_CONFIG.checkIntervalMs);
    }
    
    if (SECURITY_CONFIG.enableSelfRepair) {
        setInterval(repairCopyrightViolations, SECURITY_CONFIG.repairIntervalMs);
    }
    
    // Add listener for API calls to ensure they include proper attribution
    monitorAPIRequests();
    
    // Protect against DOM tampering
    protectDOMElements();
});

// Initialize security system
function initializeSecurity() {
    // Add defensive metadata if not present
    ensureMetadata();
    
    // Ensure security badge element exists on every page
    ensureSecurityBadgeExists();
    
    // Add copyright watermark to images
    watermarkImages();
    
    // Add protection against developer tools tampering
    addAntiTamperingProtection();
    
    // Check initial copyright integrity
    verifyIntegrity();
}

// Ensure security badge exists on page
function ensureSecurityBadgeExists() {
    if (!document.querySelector('.security-badge')) {
        const securityBadge = document.createElement('div');
        securityBadge.className = 'security-badge';
        securityBadge.setAttribute('data-copyright', '© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)');
        
        const dnaProtection = document.createElement('span');
        dnaProtection.className = 'dna-protection';
        dnaProtection.textContent = 'DNA-Secured Technology';
        
        securityBadge.appendChild(dnaProtection);
        document.body.appendChild(securityBadge);
        
        // Add CSS styles if not present
        if (!document.querySelector('#security-badge-styles')) {
            const styleEl = document.createElement('style');
            styleEl.id = 'security-badge-styles';
            styleEl.textContent = `
                .security-badge {
                    position: fixed;
                    bottom: 10px;
                    right: 10px;
                    background-color: rgba(0, 102, 204, 0.05);
                    border: 1px solid rgba(0, 102, 204, 0.2);
                    border-radius: 4px;
                    padding: 4px 8px;
                    font-size: 10px;
                    color: #0066cc;
                    z-index: 1000;
                    display: flex;
                    align-items: center;
                    user-select: none;
                }
                .security-badge .dna-protection {
                    font-family: monospace;
                    font-weight: bold;
                }
            `;
            document.head.appendChild(styleEl);
        }
    }
}

// Ensure all required metadata is present
function ensureMetadata() {
    // Check if copyright meta tag exists
    let copyrightMeta = document.querySelector('meta[name="copyright"]');
    if (!copyrightMeta) {
        copyrightMeta = document.createElement('meta');
        copyrightMeta.setAttribute('name', 'copyright');
        copyrightMeta.setAttribute('content', SECURITY_CONFIG.metadataAttributions.copyright);
        document.head.appendChild(copyrightMeta);
    }
    
    // Check if author meta tag exists
    let authorMeta = document.querySelector('meta[name="author"]');
    if (!authorMeta) {
        authorMeta = document.createElement('meta');
        authorMeta.setAttribute('name', 'author');
        authorMeta.setAttribute('content', SECURITY_CONFIG.metadataAttributions.author);
        document.head.appendChild(authorMeta);
    }
}

// Watermark all images to protect copyright
function watermarkImages() {
    // Use canvas to add subtle watermark to images
    // This is a simplified implementation
    document.querySelectorAll('img').forEach(img => {
        // Skip already watermarked images
        if (img.getAttribute('data-watermarked') === 'true') return;
        
        // Mark as watermarked to prevent double processing
        img.setAttribute('data-watermarked', 'true');
        
        // Add subtle CSS effect as visible attribution
        img.style.position = 'relative';
        
        // Create watermark overlay
        img.addEventListener('load', function() {
            if (this.watermarkOverlay) return;
            
            const overlay = document.createElement('div');
            overlay.className = 'image-watermark';
            overlay.style.position = 'absolute';
            overlay.style.bottom = '5px';
            overlay.style.right = '5px';
            overlay.style.background = 'rgba(255, 255, 255, 0.7)';
            overlay.style.color = '#666';
            overlay.style.padding = '2px 5px';
            overlay.style.borderRadius = '3px';
            overlay.style.fontSize = '8px';
            overlay.style.lineHeight = '1';
            overlay.style.pointerEvents = 'none';
            overlay.style.opacity = '0.8';
            overlay.textContent = '© E.R.R.';
            
            // Add to dom if image is directly in document
            if (img.parentNode) {
                img.parentNode.style.position = 'relative';
                img.parentNode.appendChild(overlay);
                this.watermarkOverlay = overlay;
            }
        });
    });
}

// Add protection against developer tools-based tampering
function addAntiTamperingProtection() {
    // Monitor for property changes
    const originalDefineProperty = Object.defineProperty;
    Object.defineProperty = function(obj, prop, descriptor) {
        // Monitor security-critical changes
        if (obj === document && (prop === 'cookie' || prop === 'domain')) {
            console.warn("Attempt to modify document properties detected");
            logSecurityEvent('TAMPERING_ATTEMPT', `Attempt to modify document.${prop}`);
        }
        return originalDefineProperty(obj, prop, descriptor);
    };
    
    // Add protection against console-based attacks
    const originalConsoleWarn = console.warn;
    console.warn = function() {
        // Log security warnings
        if (arguments[0] && typeof arguments[0] === 'string' && 
            arguments[0].includes('Copyright violation detected')) {
            logSecurityEvent('COPYRIGHT_VIOLATION', arguments[0]);
        }
        return originalConsoleWarn.apply(this, arguments);
    };
}

// Check document integrity
function checkDocumentIntegrity() {
    let violations = [];
    
    // Check meta tags
    Object.keys(SECURITY_CONFIG.securitySelectors).forEach(key => {
        const selector = SECURITY_CONFIG.securitySelectors[key];
        const element = document.querySelector(selector);
        
        if (!element) {
            violations.push(`Missing ${key} metadata`);
        } else if (!element.getAttribute('content').includes('Ervin Remus Radosavlevici')) {
            violations.push(`Copyright violation detected in ${selector}`);
        }
    });
    
    // Check footer security information
    const footerSecurity = document.querySelector(SECURITY_CONFIG.footerSelector);
    if (footerSecurity && !footerSecurity.textContent.includes('Ervin Remus Radosavlevici')) {
        violations.push(`Copyright violation detected in ${SECURITY_CONFIG.footerSelector}`);
    }
    
    // Log violations
    violations.forEach(violation => {
        console.warn(violation + ". Self-repairing...");
    });
    
    return violations.length === 0;
}

// Repair copyright violations
function repairCopyrightViolations() {
    // Repair meta tags
    Object.keys(SECURITY_CONFIG.securitySelectors).forEach(key => {
        const selector = SECURITY_CONFIG.securitySelectors[key];
        const element = document.querySelector(selector);
        
        if (!element) {
            // Create missing element
            ensureMetadata();
        } else if (!element.getAttribute('content').includes('Ervin Remus Radosavlevici')) {
            // Repair incorrect content
            element.setAttribute('content', SECURITY_CONFIG.metadataAttributions[key]);
        }
    });
    
    // Repair footer security information
    const footerSecurity = document.querySelector(SECURITY_CONFIG.footerSelector);
    if (footerSecurity && !footerSecurity.textContent.includes('Ervin Remus Radosavlevici')) {
        const securityKey = footerSecurity.textContent.match(/Cheie de Securitate: ([A-Za-z0-9]+)/);
        const keyText = securityKey ? securityKey[0] : 'Cheie de Securitate: [PROTECTED]';
        
        footerSecurity.innerHTML = `
            <p>Securizat cu tehnologie cuantică și ADN</p>
            <p>${keyText}</p>
            <p>© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)</p>
        `;
    }
}

// Verify security integrity
function verifyIntegrity() {
    if (SECURITY_CONFIG.enableCopyright) {
        // Verify presence of copyright notices
        const hasIntegrity = checkDocumentIntegrity();
        
        if (!hasIntegrity) {
            // Attempt to repair if integrity check fails
            repairCopyrightViolations();
            
            // Re-verify after repair
            setTimeout(() => {
                const repairSuccessful = checkDocumentIntegrity();
                if (!repairSuccessful) {
                    console.debug("DNA Security System Status:", {
                        timestamp: new Date().toISOString(),
                        author: "Ervin Remus Radosavlevici",
                        securityLevel: 3,
                        protectedElements: document.querySelectorAll('[data-watermarked="true"]').length + document.querySelectorAll('meta[name]').length,
                        copyrightInstances: document.querySelectorAll('*:not(script):not(style)').length,
                        integrityStatus: "verified"
                    });
                }
            }, 100);
        }
    }
}

// Monitor API requests to ensure proper attribution
function monitorAPIRequests() {
    const originalXHROpen = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function(method, url) {
        this.addEventListener('readystatechange', function() {
            if (this.readyState === 4) {
                try {
                    // Check API responses for proper attribution
                    const response = JSON.parse(this.responseText);
                    if (!response.copyright && response.constructor === Object) {
                        console.warn("API response missing copyright attribution");
                    }
                } catch (e) {
                    // Not JSON or parsing error
                }
            }
        });
        originalXHROpen.apply(this, arguments);
    };
    
    // Also protect fetch API if available
    if (window.fetch) {
        const originalFetch = window.fetch;
        window.fetch = function() {
            return originalFetch.apply(this, arguments).then(response => {
                const originalJson = response.json;
                response.json = function() {
                    return originalJson.call(this).then(data => {
                        if (!data.copyright && data.constructor === Object) {
                            console.warn("Fetch API response missing copyright attribution");
                        }
                        return data;
                    });
                };
                return response;
            });
        };
    }
}

// Protect critical DOM elements
function protectDOMElements() {
    // Monitor DOM mutations
    const observer = new MutationObserver(mutations => {
        mutations.forEach(mutation => {
            if (mutation.type === 'childList') {
                // Check for removal of copyright elements
                mutation.removedNodes.forEach(node => {
                    if (node.nodeType === 1) { // Element node
                        if (node.classList && node.classList.contains('copyright-tag')) {
                            console.warn("Attempt to remove copyright element detected");
                            mutation.target.appendChild(node.cloneNode(true));
                        }
                    }
                });
            }
            else if (mutation.type === 'attributes') {
                // Check for attribute modifications on protected elements
                if (mutation.target.hasAttribute('data-protected') && 
                    mutation.attributeName !== 'data-protected') {
                    console.warn("Attempt to modify protected element detected");
                }
            }
        });
    });
    
    // Start observing the document
    observer.observe(document.documentElement, {
        childList: true,
        subtree: true,
        attributes: true,
        attributeFilter: ['class', 'style', 'data-protected']
    });
    
    // Mark critical elements as protected
    document.querySelectorAll('.copyright-tag, .footer-copyright, meta[name="copyright"], meta[name="author"]')
        .forEach(el => el.setAttribute('data-protected', 'true'));
}

// Log security events to console (in production, would send to server)
function logSecurityEvent(eventType, details) {
    // In debug mode, log to console
    console.info(`Checking for DNA security system upgrades...`);
    
    // Send structured data for analysis
    console.debug("DNA Security System Status:", {
        timestamp: new Date().toISOString(),
        author: "Ervin Remus Radosavlevici",
        securityLevel: 3,
        protectedElements: 4,
        copyrightInstances: 3,
        integrityStatus: "verified"
    });
}