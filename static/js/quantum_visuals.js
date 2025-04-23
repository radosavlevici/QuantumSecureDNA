/**
 * Quantum Visualization System for Quantum Computing Educational Platform
 * 
 * © 2025 Ervin Remus Radosavlevici (ervin210@icloud.com)
 * WORLDWIDE COPYRIGHT PROTECTED. All Rights Reserved Globally.
 * Protected by International Copyright Law.
 * 
 * This module provides interactive quantum visualizations including:
 * - Bloch sphere representations
 * - Quantum circuit animations
 * - DNA-based encryption visualizations
 * - Quantum state visualizations
 */

// Global configuration
const QUANTUM_CONFIG = {
    author: "Ervin Remus Radosavlevici",
    email: "ervin210@icloud.com",
    copyrightYear: "2025",
    animationSpeed: 1000,
    particleCount: 50,
    colors: {
        primary: '#6200ea',
        secondary: '#03dac6',
        accent: '#ff4081',
        qubit0: '#8BC34A',
        qubit1: '#FF5722',
        superposition: '#FFC107'
    }
};

// Initialize all quantum visualizations when the document is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Initialize homepage visual if it exists
    const homepageVisual = document.getElementById('homepage-visual');
    if (homepageVisual) {
        initQuantumParticleSystem(homepageVisual);
    }
    
    // Other visualizations would be initialized here based on page content
    initAllVisualizations();
    
    // Add copyright watermark to all visualizations
    addCopyrightWatermarks();
});

// Initialize all visualizations throughout the page
function initAllVisualizations() {
    // Find all visualization containers
    document.querySelectorAll('.quantum-visual, .dna-visual, .bloch-sphere').forEach(container => {
        // Check the type of visualization needed
        if (container.classList.contains('bloch-sphere')) {
            initBlochSphere(container);
        } else if (container.classList.contains('dna-visual')) {
            initDNAVisualization(container);
        } else {
            // Default to quantum particle system for other visuals
            initQuantumParticleSystem(container);
        }
    });
}

// Initialize quantum particle system visualization
function initQuantumParticleSystem(container) {
    // Set a copyright attribute
    container.setAttribute('data-copyright', `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`);
    
    // Create canvas for particles
    const canvas = document.createElement('canvas');
    canvas.width = container.clientWidth;
    canvas.height = container.clientHeight;
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    container.appendChild(canvas);
    
    // Get context and initialize particles
    const ctx = canvas.getContext('2d');
    const particles = [];
    
    // Create particles
    for (let i = 0; i < QUANTUM_CONFIG.particleCount; i++) {
        particles.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            size: Math.random() * 3 + 1,
            speedX: (Math.random() - 0.5) * 2,
            speedY: (Math.random() - 0.5) * 2,
            color: getRandomColor()
        });
    }
    
    // Animation function
    function animate() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Update and draw particles
        particles.forEach(particle => {
            // Update position
            particle.x += particle.speedX;
            particle.y += particle.speedY;
            
            // Boundary check
            if (particle.x < 0 || particle.x > canvas.width) particle.speedX *= -1;
            if (particle.y < 0 || particle.y > canvas.height) particle.speedY *= -1;
            
            // Draw particle
            ctx.beginPath();
            ctx.arc(particle.x, particle.y, particle.size, 0, Math.PI * 2);
            ctx.fillStyle = particle.color;
            ctx.fill();
        });
        
        // Draw connections between nearby particles
        particles.forEach((p1, i) => {
            particles.slice(i + 1).forEach(p2 => {
                const dx = p1.x - p2.x;
                const dy = p1.y - p2.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < 100) {
                    ctx.beginPath();
                    ctx.moveTo(p1.x, p1.y);
                    ctx.lineTo(p2.x, p2.y);
                    ctx.strokeStyle = `rgba(98, 0, 234, ${0.8 - distance / 100})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            });
        });
        
        // Continue animation
        requestAnimationFrame(animate);
    }
    
    // Start animation
    animate();
    
    // Add a small copyright notice to the bottom right
    const copyrightDiv = document.createElement('div');
    copyrightDiv.style.position = 'absolute';
    copyrightDiv.style.right = '5px';
    copyrightDiv.style.bottom = '5px';
    copyrightDiv.style.fontSize = '8px';
    copyrightDiv.style.color = 'rgba(0, 0, 0, 0.5)';
    copyrightDiv.style.pointerEvents = 'none';
    copyrightDiv.textContent = `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`;
    container.appendChild(copyrightDiv);
}

// Initialize Bloch sphere visualization
function initBlochSphere(container) {
    // Set a copyright attribute
    container.setAttribute('data-copyright', `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`);
    
    // Create canvas for Bloch sphere
    const canvas = document.createElement('canvas');
    canvas.width = container.clientWidth;
    canvas.height = container.clientHeight;
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    
    // Get theta and phi from data attributes or use defaults
    const theta = parseFloat(container.getAttribute('data-theta') || Math.PI / 4);
    const phi = parseFloat(container.getAttribute('data-phi') || 0);
    
    // Animation variables
    let rotation = 0;
    
    // Draw Bloch sphere
    function drawBlochSphere() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set origin to center
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = Math.min(centerX, centerY) * 0.8;
        
        // Draw sphere
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Draw X, Y, Z axes
        // X axis (red)
        ctx.beginPath();
        ctx.moveTo(centerX - radius, centerY);
        ctx.lineTo(centerX + radius, centerY);
        ctx.strokeStyle = 'rgba(255, 0, 0, 0.7)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Y axis (green)
        ctx.beginPath();
        ctx.moveTo(centerX, centerY - radius);
        ctx.lineTo(centerX, centerY + radius);
        ctx.strokeStyle = 'rgba(0, 255, 0, 0.7)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Z axis with perspective (blue)
        ctx.beginPath();
        ctx.moveTo(
            centerX + radius * 0.7 * Math.cos(rotation),
            centerY + radius * 0.7 * Math.sin(rotation)
        );
        ctx.lineTo(
            centerX - radius * 0.7 * Math.cos(rotation),
            centerY - radius * 0.7 * Math.sin(rotation)
        );
        ctx.strokeStyle = 'rgba(0, 0, 255, 0.7)';
        ctx.lineWidth = 1;
        ctx.stroke();
        
        // Calculate qubit vector position
        const x = Math.sin(theta) * Math.cos(phi);
        const y = Math.sin(theta) * Math.sin(phi);
        const z = Math.cos(theta);
        
        // Adjust for rotation
        const rotatedX = x * Math.cos(rotation) - z * Math.sin(rotation);
        const rotatedZ = x * Math.sin(rotation) + z * Math.cos(rotation);
        
        // Draw qubit vector
        ctx.beginPath();
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(
            centerX + radius * rotatedX,
            centerY + radius * y
        );
        ctx.strokeStyle = QUANTUM_CONFIG.colors.primary;
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Draw qubit point
        ctx.beginPath();
        ctx.arc(
            centerX + radius * rotatedX,
            centerY + radius * y,
            5,
            0,
            Math.PI * 2
        );
        ctx.fillStyle = QUANTUM_CONFIG.colors.accent;
        ctx.fill();
        
        // Add labels
        ctx.font = '12px Arial';
        ctx.fillStyle = 'rgba(0, 0, 0, 0.7)';
        ctx.fillText('|0⟩', centerX, centerY - radius - 10);
        ctx.fillText('|1⟩', centerX, centerY + radius + 20);
        ctx.fillText('|+⟩', centerX + radius + 10, centerY);
        ctx.fillText('|-⟩', centerX - radius - 20, centerY);
        
        // Update rotation for animation
        rotation += 0.01;
        
        // Continue animation
        requestAnimationFrame(drawBlochSphere);
    }
    
    // Start animation
    drawBlochSphere();
    
    // Add a small copyright notice to the bottom right
    const copyrightDiv = document.createElement('div');
    copyrightDiv.style.position = 'absolute';
    copyrightDiv.style.right = '5px';
    copyrightDiv.style.bottom = '5px';
    copyrightDiv.style.fontSize = '8px';
    copyrightDiv.style.color = 'rgba(0, 0, 0, 0.5)';
    copyrightDiv.style.pointerEvents = 'none';
    copyrightDiv.textContent = `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`;
    container.appendChild(copyrightDiv);
}

// Initialize DNA visualization
function initDNAVisualization(container) {
    // Set a copyright attribute
    container.setAttribute('data-copyright', `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`);
    
    // Create canvas for DNA visualization
    const canvas = document.createElement('canvas');
    canvas.width = container.clientWidth;
    canvas.height = container.clientHeight;
    canvas.style.position = 'absolute';
    canvas.style.top = '0';
    canvas.style.left = '0';
    canvas.style.width = '100%';
    canvas.style.height = '100%';
    container.appendChild(canvas);
    
    const ctx = canvas.getContext('2d');
    
    // Animation variables
    let rotation = 0;
    const dnaStrandCount = 20;
    const dnaColors = {
        A: '#8BC34A',  // Green
        T: '#9C27B0',  // Purple
        C: '#03A9F4',  // Blue
        G: '#F44336'   // Red
    };
    
    // Generate random DNA sequence
    const bases = ['A', 'T', 'C', 'G'];
    const dnaSequence = Array(dnaStrandCount).fill(0).map(() => 
        bases[Math.floor(Math.random() * bases.length)]
    );
    
    // Draw DNA helix
    function drawDNAHelix() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const dnaLength = canvas.height * 0.8;
        const dnaWidth = canvas.width * 0.3;
        
        // Draw backbone
        for (let i = 0; i < 2; i++) {
            ctx.beginPath();
            
            for (let y = 0; y < dnaLength; y += 1) {
                const yPos = centerY - dnaLength / 2 + y;
                const phase = y / 30 + rotation;
                const xOffset = Math.sin(phase) * dnaWidth / 2;
                
                const xPos = i === 0 ? centerX + xOffset : centerX - xOffset;
                
                if (y === 0) {
                    ctx.moveTo(xPos, yPos);
                } else {
                    ctx.lineTo(xPos, yPos);
                }
            }
            
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.3)';
            ctx.lineWidth = 2;
            ctx.stroke();
        }
        
        // Draw base pairs
        for (let i = 0; i < dnaStrandCount; i++) {
            const yPos = centerY - dnaLength / 2 + (dnaLength / dnaStrandCount) * (i + 0.5);
            const phase = yPos / 30 + rotation;
            const xOffset = Math.sin(phase) * dnaWidth / 2;
            
            const startX = centerX - xOffset;
            const endX = centerX + xOffset;
            
            // Draw connection line
            ctx.beginPath();
            ctx.moveTo(startX, yPos);
            ctx.lineTo(endX, yPos);
            ctx.strokeStyle = 'rgba(0, 0, 0, 0.2)';
            ctx.lineWidth = 1;
            ctx.stroke();
            
            // Draw base pair nucleotides
            const base = dnaSequence[i];
            const complementaryBase = base === 'A' ? 'T' : base === 'T' ? 'A' : base === 'C' ? 'G' : 'C';
            
            // Left base
            ctx.beginPath();
            ctx.arc(startX, yPos, 8, 0, Math.PI * 2);
            ctx.fillStyle = dnaColors[base];
            ctx.fill();
            ctx.fillStyle = 'white';
            ctx.font = '8px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(base, startX, yPos);
            
            // Right base
            ctx.beginPath();
            ctx.arc(endX, yPos, 8, 0, Math.PI * 2);
            ctx.fillStyle = dnaColors[complementaryBase];
            ctx.fill();
            ctx.fillStyle = 'white';
            ctx.font = '8px Arial';
            ctx.textAlign = 'center';
            ctx.textBaseline = 'middle';
            ctx.fillText(complementaryBase, endX, yPos);
        }
        
        // Update rotation for animation
        rotation += 0.02;
        
        // Continue animation
        requestAnimationFrame(drawDNAHelix);
    }
    
    // Start animation
    drawDNAHelix();
    
    // Add a small copyright notice to the bottom right
    const copyrightDiv = document.createElement('div');
    copyrightDiv.style.position = 'absolute';
    copyrightDiv.style.right = '5px';
    copyrightDiv.style.bottom = '5px';
    copyrightDiv.style.fontSize = '8px';
    copyrightDiv.style.color = 'rgba(0, 0, 0, 0.5)';
    copyrightDiv.style.pointerEvents = 'none';
    copyrightDiv.textContent = `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`;
    container.appendChild(copyrightDiv);
}

// Add copyright watermarks to all visualizations
function addCopyrightWatermarks() {
    document.querySelectorAll('canvas').forEach(canvas => {
        const container = canvas.parentElement;
        
        // Skip if container already has a copyright notice
        if (container.querySelector('div[class*="copyright"]')) return;
        
        // Add a small copyright notice to the bottom right
        const copyrightDiv = document.createElement('div');
        copyrightDiv.style.position = 'absolute';
        copyrightDiv.style.right = '5px';
        copyrightDiv.style.bottom = '5px';
        copyrightDiv.style.fontSize = '8px';
        copyrightDiv.style.color = 'rgba(0, 0, 0, 0.5)';
        copyrightDiv.style.pointerEvents = 'none';
        copyrightDiv.className = 'visual-copyright';
        copyrightDiv.textContent = `© ${QUANTUM_CONFIG.copyrightYear} ${QUANTUM_CONFIG.author}`;
        container.appendChild(copyrightDiv);
    });
}

// Utility function to get a random color
function getRandomColor() {
    const colors = [
        QUANTUM_CONFIG.colors.primary + '80',  // With transparency
        QUANTUM_CONFIG.colors.secondary + '80',
        QUANTUM_CONFIG.colors.accent + '80',
        QUANTUM_CONFIG.colors.qubit0 + '80',
        QUANTUM_CONFIG.colors.qubit1 + '80'
    ];
    return colors[Math.floor(Math.random() * colors.length)];
}

// Export configuration for global access
window.QUANTUM_CONFIG = QUANTUM_CONFIG;