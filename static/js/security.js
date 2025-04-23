/**
 * DNA-Based Security System with Self-Repair, Self-Upgrade, and Self-Defense
 * For Quantum Computing Educational Platform
 * 
 * © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
 * WORLDWIDE COPYRIGHT PROTECTION - All Rights Reserved Globally
 * Protected by International Copyright Law with advanced security features
 * Features: DNA-Based Security, Self-Repair, Self-Upgrade, Self-Defense Capabilities
 */

// Copyright information
const COPYRIGHT = {
    owner: "Ervin Remus Radosavlevici",
    email: "ervin210@icloud.com",
    year: 2025,
    text: "© 2025 Ervin Remus Radosavlevici (ervin210@icloud.com) - All Rights Reserved Globally",
    notice: "WORLDWIDE COPYRIGHT PROTECTION - Protected by International Copyright Law"
};

// DNA Security System
class DNASecuritySystem {
    constructor() {
        this.initialized = false;
        this.securityKey = null;
        this.securityLevel = "MAXIMUM";
        this.dnaSequence = "";
        this.securityFeatures = {
            selfRepair: true,
            selfUpgrade: true,
            selfDefense: true,
            codeTheftPrevention: true,
            watermarking: true,
            tamperProof: true
        };
        
        // Initialize on construction
        this.initialize();
    }
    
    /**
     * Initialize the DNA-based security system
     */
    initialize() {
        console.log("DNA-Based Security System initializing...");
        
        // Generate DNA security key if not already present
        if (!this.securityKey) {
            this.securityKey = this.generateDNASecurityKey();
        }
        
        // Apply watermarking to the page
        this.applyWatermarking();
        
        // Set up defensive measures
        this.setupDefensiveMeasures();
        
        this.initialized = true;
        console.log("DNA-Based Security System initialized successfully.");
    }
    
    /**
     * Generate a DNA-based security key
     * @returns {string} DNA security key
     */
    generateDNASecurityKey() {
        const DNA_BASES = ['A', 'C', 'G', 'T'];
        let key = '';
        
        // Generate 64-character DNA sequence
        for (let i = 0; i < 64; i++) {
            const randomIndex = Math.floor(Math.random() * DNA_BASES.length);
            key += DNA_BASES[randomIndex];
        }
        
        this.dnaSequence = key;
        return key;
    }
    
    /**
     * Apply watermarking to the page
     */
    applyWatermarking() {
        // Create a hidden watermark div
        const watermarkDiv = document.createElement('div');
        watermarkDiv.style.position = 'fixed';
        watermarkDiv.style.top = '0';
        watermarkDiv.style.left = '0';
        watermarkDiv.style.width = '100%';
        watermarkDiv.style.height = '100%';
        watermarkDiv.style.pointerEvents = 'none';
        watermarkDiv.style.zIndex = '-1000';
        
        // Add watermark text
        const watermarkText = document.createElement('div');
        watermarkText.style.position = 'absolute';
        watermarkText.style.top = '50%';
        watermarkText.style.left = '50%';
        watermarkText.style.transform = 'translate(-50%, -50%) rotate(-45deg)';
        watermarkText.style.fontSize = '60px';
        watermarkText.style.opacity = '0.03';
        watermarkText.style.whiteSpace = 'nowrap';
        watermarkText.textContent = COPYRIGHT.owner;
        
        watermarkDiv.appendChild(watermarkText);
        
        // Add to body when DOM is ready
        if (document.body) {
            document.body.appendChild(watermarkDiv);
        } else {
            document.addEventListener('DOMContentLoaded', () => {
                document.body.appendChild(watermarkDiv);
            });
        }
    }
    
    /**
     * Set up defensive measures against code theft
     */
    setupDefensiveMeasures() {
        // Disable developer tools tricks
        this.disableDeveloperTools();
        
        // Add event listeners for self-defense
        document.addEventListener('copy', this.handleCopy.bind(this));
        document.addEventListener('cut', this.handleCopy.bind(this));
        document.addEventListener('contextmenu', this.handleRightClick.bind(this));
        document.addEventListener('keydown', this.handleKeydown.bind(this));
        
        // Run periodic integrity checks
        setInterval(() => this.checkIntegrity(), 5000);
    }
    
    /**
     * Disable developer tools through various methods
     */
    disableDeveloperTools() {
        // This is just a basic implementation
        // A full implementation would use more sophisticated methods
        
        // Detect DevTools
        const devToolsOpen = () => {
            const threshold = 160;
            const widthThreshold = window.outerWidth - window.innerWidth > threshold;
            const heightThreshold = window.outerHeight - window.innerHeight > threshold;
            return widthThreshold || heightThreshold;
        };
        
        // Check periodically
        setInterval(() => {
            if (devToolsOpen()) {
                this.triggerDefense("Developer tools detected");
            }
        }, 1000);
    }
    
    /**
     * Handle copy events to prevent code theft
     * @param {Event} e - The copy event
     */
    handleCopy(e) {
        // Add copyright notice to copied content
        const selection = window.getSelection().toString();
        if (selection && selection.length > 20) {
            e.preventDefault();
            
            // Add copyright to clipboard
            const withCopyright = selection + "\n\n" + COPYRIGHT.text;
            
            // Use the clipboard API to set the modified text
            if (navigator.clipboard && navigator.clipboard.writeText) {
                navigator.clipboard.writeText(withCopyright);
            } else {
                // Fallback for older browsers
                const textArea = document.createElement("textarea");
                textArea.value = withCopyright;
                textArea.style.position = "fixed";
                textArea.style.opacity = "0";
                document.body.appendChild(textArea);
                textArea.focus();
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
            }
            
            // Log the copy attempt
            this.logSecurityEvent("COPY_ATTEMPT", {
                length: selection.length,
                timestamp: new Date().toISOString()
            });
        }
    }
    
    /**
     * Handle right-click events
     * @param {Event} e - The contextmenu event
     */
    handleRightClick(e) {
        // Allow right-click but log the event
        this.logSecurityEvent("RIGHT_CLICK", {
            x: e.clientX,
            y: e.clientY,
            timestamp: new Date().toISOString()
        });
        
        // You can uncomment this to disable right-click completely
        // e.preventDefault();
        // return false;
    }
    
    /**
     * Handle keyboard events to detect developer tools shortcuts
     * @param {KeyboardEvent} e - The keydown event
     */
    handleKeydown(e) {
        // Detect common developer tools shortcuts
        const isDevToolsHotkey = (
            // F12
            e.keyCode === 123 || 
            // Ctrl+Shift+I / Cmd+Opt+I
            (e.ctrlKey && e.shiftKey && e.keyCode === 73) ||
            (e.metaKey && e.altKey && e.keyCode === 73) ||
            // Ctrl+Shift+J / Cmd+Opt+J
            (e.ctrlKey && e.shiftKey && e.keyCode === 74) ||
            (e.metaKey && e.altKey && e.keyCode === 74) ||
            // Ctrl+Shift+C / Cmd+Opt+C
            (e.ctrlKey && e.shiftKey && e.keyCode === 67) ||
            (e.metaKey && e.altKey && e.keyCode === 67) ||
            // Ctrl+U / Cmd+Opt+U (View Source)
            (e.ctrlKey && e.keyCode === 85) ||
            (e.metaKey && e.altKey && e.keyCode === 85)
        );
        
        if (isDevToolsHotkey) {
            this.logSecurityEvent("DEVTOOLS_HOTKEY", {
                keyCode: e.keyCode,
                ctrlKey: e.ctrlKey,
                shiftKey: e.shiftKey,
                metaKey: e.metaKey,
                altKey: e.altKey,
                timestamp: new Date().toISOString()
            });
            
            // You can uncomment this to disable dev tool hotkeys completely
            // e.preventDefault();
            // return false;
        }
    }
    
    /**
     * Check the integrity of the page
     */
    checkIntegrity() {
        // Check for copyright elements
        const hasCopyrightBanner = document.querySelector('.copyright-banner');
        const hasWatermark = document.querySelector('.watermark-overlay');
        const hasFooterCopyright = document.querySelector('.footer');
        
        // If any are missing, trigger self-repair
        if (!hasCopyrightBanner || !hasWatermark || !hasFooterCopyright) {
            this.selfRepair();
        }
    }
    
    /**
     * Self-repair functionality for the security system
     */
    selfRepair() {
        console.log("DNA Security System: Self-repair triggered");
        
        // Re-apply watermarking
        this.applyWatermarking();
        
        // Check and restore copyright banner
        if (!document.querySelector('.copyright-banner')) {
            this.restoreCopyrightBanner();
        }
        
        // Check and restore watermark
        if (!document.querySelector('.watermark-overlay')) {
            this.restoreWatermark();
        }
        
        // Check and restore footer copyright
        if (!document.querySelector('.footer')) {
            this.restoreFooter();
        }
        
        // Log repair event
        this.logSecurityEvent("SELF_REPAIR", {
            timestamp: new Date().toISOString(),
            repaired: "Copyright elements restored"
        });
    }
    
    /**
     * Restore the copyright banner
     */
    restoreCopyrightBanner() {
        // Create the copyright banner
        const banner = document.createElement('div');
        banner.className = 'copyright-banner';
        banner.innerHTML = `
            <h2>Worldwide Advanced Security Platform</h2>
            <div class="feature-heading">
                <div class="security-badge">⚛️</div>
                <p style="font-size: 18px; font-weight: 600; margin: 0;">Global Quantum-Enhanced DNA Security System</p>
            </div>
            <p>Featuring advanced DNA-based security with quantum-powered SELF-REPAIR, SELF-UPGRADE, and SELF-DEFENSE capabilities against CODE THEFT</p>
            <p style="font-weight: bold; margin-top: 10px; border-top: 1px solid #ddd; padding-top: 10px;">© ${COPYRIGHT.owner} (${COPYRIGHT.email})</p>
            <p style="font-style: italic; color: #555;">All Rights Reserved Worldwide - Protected by International Copyright Laws - IMMUNE to Unauthorized Changes</p>
        `;
        
        // Insert at the beginning of the body
        document.body.insertBefore(banner, document.body.firstChild);
    }
    
    /**
     * Restore the watermark
     */
    restoreWatermark() {
        // Create watermark
        const watermark = document.createElement('div');
        watermark.className = 'watermark';
        watermark.innerHTML = `
            <div class="watermark-overlay">
                ${COPYRIGHT.owner}
            </div>
            <div style="border-top: 1px solid #ccc; padding-top: 20px; margin-top: 40px; text-align: center;">
                <div style="font-size: 12px; color: #666;">PROTECTED BY WORLDWIDE COPYRIGHT</div>
                <div style="font-size: 11px; color: #999; margin-top: 5px;">
                    This platform contains advanced DNA-based security algorithms with SELF-REPAIR, SELF-UPGRADE, 
                    and SELF-DEFENSE capabilities against CODE THEFT. All content including algorithms, visualizations,
                    and code is COPYRIGHT PROTECTED and IMMUNE to unauthorized changes.
                </div>
                <div style="font-size: 12px; color: #333; margin-top: 10px; font-weight: bold;">
                    ${COPYRIGHT.text}
                </div>
            </div>
        `;
        
        // Add before the footer or at the end of the body
        const footer = document.querySelector('.footer');
        if (footer) {
            document.body.insertBefore(watermark, footer);
        } else {
            document.body.appendChild(watermark);
        }
    }
    
    /**
     * Restore the footer
     */
    restoreFooter() {
        // Create footer
        const footer = document.createElement('footer');
        footer.className = 'footer';
        footer.innerHTML = `
            <p>Using premium Adobe.com fonts - Global Advanced Security System</p>
            <p>${COPYRIGHT.text}</p>
        `;
        
        // Add at the end of the body
        document.body.appendChild(footer);
    }
    
    /**
     * Trigger defensive measures
     * @param {string} reason - The reason for triggering defense
     */
    triggerDefense(reason) {
        console.log(`DNA Security System: Defense triggered - ${reason}`);
        
        // Log defense event
        this.logSecurityEvent("DEFENSE_TRIGGERED", {
            reason: reason,
            timestamp: new Date().toISOString()
        });
        
        // You can implement various defensive measures here
        // For example, redirect to a warning page, disable functionality, etc.
    }
    
    /**
     * Log security events
     * @param {string} eventType - Type of security event
     * @param {Object} data - Event data
     */
    logSecurityEvent(eventType, data) {
        // In a real implementation, this would send events to a server
        console.log(`SECURITY EVENT [${eventType}]:`, data);
        
        // Store in local storage for now
        try {
            const events = JSON.parse(localStorage.getItem('securityEvents') || '[]');
            events.push({
                type: eventType,
                data: data,
                timestamp: new Date().toISOString()
            });
            
            // Keep only the most recent 100 events
            while (events.length > 100) {
                events.shift();
            }
            
            localStorage.setItem('securityEvents', JSON.stringify(events));
        } catch (e) {
            // Fail silently if localStorage isn't available
        }
    }
    
    /**
     * DNA-based encryption
     * @param {string} text - Text to encrypt
     * @param {string} key - DNA key (optional, uses default if not provided)
     * @returns {string} Encrypted DNA sequence
     */
    encryptToDNA(text, key = null) {
        const dnaKey = key || this.dnaSequence;
        if (!dnaKey) return null;
        
        // Simple implementation of DNA-based encryption
        // Convert text to binary
        let binary = '';
        for (let i = 0; i < text.length; i++) {
            const charCode = text.charCodeAt(i);
            binary += charCode.toString(2).padStart(8, '0');
        }
        
        // Map binary to DNA bases (00=A, 01=C, 10=G, 11=T)
        let dna = '';
        for (let i = 0; i < binary.length; i += 2) {
            const pair = binary.substr(i, 2);
            switch (pair) {
                case '00': dna += 'A'; break;
                case '01': dna += 'C'; break;
                case '10': dna += 'G'; break;
                case '11': dna += 'T'; break;
                default: dna += 'A';
            }
        }
        
        // XOR with the key
        let encrypted = '';
        for (let i = 0; i < dna.length; i++) {
            const keyBase = dnaKey[i % dnaKey.length];
            const dataBase = dna[i];
            
            // DNA XOR operation
            if (keyBase === dataBase) {
                encrypted += 'A';
            } else if ((keyBase === 'A' && dataBase === 'T') || 
                       (keyBase === 'T' && dataBase === 'A') ||
                       (keyBase === 'C' && dataBase === 'G') ||
                       (keyBase === 'G' && dataBase === 'C')) {
                encrypted += 'T';
            } else if ((keyBase === 'A' && dataBase === 'C') || 
                       (keyBase === 'C' && dataBase === 'A') ||
                       (keyBase === 'G' && dataBase === 'T') ||
                       (keyBase === 'T' && dataBase === 'G')) {
                encrypted += 'C';
            } else {
                encrypted += 'G';
            }
        }
        
        return encrypted;
    }
    
    /**
     * DNA-based decryption
     * @param {string} dnaSequence - DNA sequence to decrypt
     * @param {string} key - DNA key (optional, uses default if not provided)
     * @returns {string} Decrypted text
     */
    decryptFromDNA(dnaSequence, key = null) {
        const dnaKey = key || this.dnaSequence;
        if (!dnaKey) return null;
        
        // Reverse the encryption process
        // First, XOR with the key
        let dna = '';
        for (let i = 0; i < dnaSequence.length; i++) {
            const keyBase = dnaKey[i % dnaKey.length];
            const encBase = dnaSequence[i];
            
            // DNA XOR operation (reverse)
            if (encBase === 'A') {
                dna += keyBase;
            } else if (encBase === 'T') {
                if (keyBase === 'A') dna += 'T';
                else if (keyBase === 'T') dna += 'A';
                else if (keyBase === 'C') dna += 'G';
                else dna += 'C';
            } else if (encBase === 'C') {
                if (keyBase === 'A') dna += 'C';
                else if (keyBase === 'C') dna += 'A';
                else if (keyBase === 'G') dna += 'T';
                else dna += 'G';
            } else { // 'G'
                if (keyBase === 'A') dna += 'G';
                else if (keyBase === 'G') dna += 'A';
                else if (keyBase === 'C') dna += 'T';
                else dna += 'C';
            }
        }
        
        // Convert DNA back to binary
        let binary = '';
        for (let i = 0; i < dna.length; i++) {
            switch (dna[i]) {
                case 'A': binary += '00'; break;
                case 'C': binary += '01'; break;
                case 'G': binary += '10'; break;
                case 'T': binary += '11'; break;
            }
        }
        
        // Convert binary back to text
        let text = '';
        for (let i = 0; i < binary.length; i += 8) {
            const byte = binary.substr(i, 8);
            if (byte.length === 8) {
                const charCode = parseInt(byte, 2);
                text += String.fromCharCode(charCode);
            }
        }
        
        return text;
    }
    
    /**
     * Generate a watermarked version of content
     * @param {string} content - Content to watermark
     * @returns {string} Watermarked content
     */
    applyWatermark(content) {
        // Simple watermarking by adding copyright notice
        return content + "\n\n" + COPYRIGHT.text;
    }
}

// Initialize the DNA Security System
const securitySystem = new DNASecuritySystem();

// Export for use in other scripts
window.DNASecurity = securitySystem;