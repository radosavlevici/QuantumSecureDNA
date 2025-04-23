import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from qiskit import QuantumCircuit
import sys
import os

# Add the utils directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def app():
    st.title("Quantum Computing Resources")
    
    # Add copyright and advanced security notice
    st.markdown("""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 5px; border-left: 5px solid #0066cc;'>
    <h3 style='color: #0066cc;'>EDUCATIONAL RESOURCES & REFERENCES</h3>
    <p>Advanced learning resources for quantum computing and DNA security</p>
    <p><b>© Ervin Remus Radosavlevici (ervin210@icloud.com)</b> - All Rights Reserved</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Introduction
    st.markdown("""
    # Educational Resources for Quantum Computing
    
    This page provides a collection of resources to help you learn more about quantum computing, 
    DNA-based security, and quantum machine learning. Whether you're a beginner or looking to 
    deepen your understanding, you'll find valuable materials to support your learning journey.
    """)
    
    # Create tabs for different resource categories
    tabs = st.tabs(["Learning Paths", "Books & Papers", "Online Courses", "Software Tools", "Glossary"])
    
    # Learning Paths tab
    with tabs[0]:
        st.header("Learning Paths")
        
        st.markdown("""
        ### For Beginners
        
        **Start Here:**
        1. Understand basic linear algebra concepts (vectors, matrices, complex numbers)
        2. Learn the fundamental principles of quantum mechanics
        3. Explore quantum computing basics (qubits, gates, circuits)
        4. Try simple quantum programming with Qiskit or Cirq
        
        **Recommended Resources:**
        - "Quantum Computing for the Very Curious" - Andy Matuschak & Michael Nielsen
        - IBM Quantum Experience - Interactive tutorials
        - Qiskit Textbook - Free online learning resource
        - "Q is for Quantum" - Terry Rudolph
        """)
        
        # Create a visual learning path for beginners
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Define the steps
        steps = [
            "Linear Algebra\nBasics",
            "Quantum\nMechanics\nFundamentals",
            "Quantum\nComputing\nConcepts",
            "Basic Quantum\nProgramming",
            "Simple\nAlgorithms",
            "Practical\nExperiments"
        ]
        
        # Draw the path
        for i, step in enumerate(steps):
            # Draw node
            circle = plt.Circle((i*2+1, 3), 0.7, facecolor='lightblue', edgecolor='blue', alpha=0.7)
            ax.add_patch(circle)
            ax.text(i*2+1, 3, str(i+1), fontsize=16, ha='center', va='center', fontweight='bold')
            ax.text(i*2+1, 1.5, step, fontsize=10, ha='center', va='center')
            
            # Draw arrow
            if i < len(steps) - 1:
                ax.arrow(i*2+1.7, 3, 0.6, 0, head_width=0.2, head_length=0.2, fc='blue', ec='blue')
        
        ax.set_xlim(0, len(steps)*2)
        ax.set_ylim(0, 6)
        ax.set_title('Beginner Learning Path')
        ax.axis('off')
        
        st.pyplot(fig)
        
        st.markdown("""
        ### For Intermediate Learners
        
        **Next Steps:**
        1. Deepen your understanding of quantum algorithms (Grover's, Shor's, VQE)
        2. Explore quantum error correction and noise mitigation
        3. Study quantum cryptography and security protocols
        4. Learn about quantum machine learning techniques
        5. Implement more complex quantum circuits
        
        **Recommended Resources:**
        - "Quantum Computation and Quantum Information" - Nielsen & Chuang
        - QML courses from MIT or University of Toronto
        - Research papers on quantum cryptography
        - Advanced Qiskit and Pennylane tutorials
        """)
        
        st.markdown("""
        ### For Advanced Learners
        
        **Advanced Topics:**
        1. Quantum error correction codes and fault-tolerant quantum computing
        2. Quantum complexity theory and quantum supremacy
        3. Advanced quantum algorithms for specific applications
        4. Quantum hardware implementation and control
        5. Cutting-edge research in quantum-DNA computing
        
        **Recommended Resources:**
        - Recent research papers from arXiv
        - Graduate-level quantum computing courses
        - Industry webinars and conference proceedings
        - Collaboration with research groups
        """)
        
        # Create roadmap for DNA-based quantum security
        st.subheader("Specialized Learning Path: DNA-Based Quantum Security")
        
        dna_path = {
            "Phase 1: Foundations": [
                "Basic molecular biology and DNA structure",
                "Fundamentals of classical cryptography",
                "Quantum computing basics",
                "Information theory essentials"
            ],
            "Phase 2: Core Concepts": [
                "DNA encoding and encryption methods",
                "Quantum key distribution protocols",
                "Quantum random number generation",
                "Basic bioinformatics"
            ],
            "Phase 3: Advanced Topics": [
                "Quantum-enhanced DNA cryptography",
                "DNA steganography techniques",
                "Hybrid quantum-classical security systems",
                "Post-quantum cryptography"
            ],
            "Phase 4: Research & Implementation": [
                "Current research in DNA-quantum security",
                "Implementation of DNA security protocols",
                "Security analysis and threat modeling",
                "Real-world applications and case studies"
            ]
        }
        
        # Display the roadmap
        for phase, topics in dna_path.items():
            st.markdown(f"**{phase}**")
            for topic in topics:
                st.markdown(f"- {topic}")
        
        # Time estimate
        st.info("""
        **Estimated Learning Time:**
        - Beginner to Intermediate: 3-6 months with consistent study
        - Intermediate to Advanced: 6-12 months with practical implementation
        - Mastery of DNA-Quantum Security: 1-2+ years including research experience
        """)
    
    # Books & Papers tab
    with tabs[1]:
        st.header("Books & Research Papers")
        
        # Essential books
        st.subheader("Essential Books")
        
        books = [
            {
                "title": "Quantum Computation and Quantum Information",
                "authors": "Michael A. Nielsen & Isaac L. Chuang",
                "description": "Often called 'Mike & Ike', this is the definitive textbook on quantum computation and information. It covers all the fundamental concepts and is suitable for students with a background in physics or computer science.",
                "level": "Intermediate to Advanced",
                "year": 2010
            },
            {
                "title": "Quantum Computing: A Gentle Introduction",
                "authors": "Eleanor G. Rieffel & Wolfgang H. Polak",
                "description": "A comprehensive introduction to quantum computing that emphasizes algorithms. It requires minimal background in physics and provides clear explanations of quantum concepts.",
                "level": "Beginner to Intermediate",
                "year": 2011
            },
            {
                "title": "Quantum Computing for Computer Scientists",
                "authors": "Noson S. Yanofsky & Mirco A. Mannucci",
                "description": "Written specifically for computer scientists, this book introduces quantum computing concepts with minimal physics requirements. It focuses on the mathematical foundations and programming aspects.",
                "level": "Beginner to Intermediate",
                "year": 2008
            },
            {
                "title": "Programming Quantum Computers: Essential Algorithms and Code Samples",
                "authors": "Eric R. Johnston, Nic Harrigan & Mercedes Gimeno-Segovia",
                "description": "A practical guide to quantum programming with examples in multiple languages. It focuses on hands-on implementation of quantum algorithms.",
                "level": "Beginner to Intermediate",
                "year": 2019
            },
            {
                "title": "Quantum Machine Learning: What Quantum Computing Means to Data Mining",
                "authors": "Peter Wittek",
                "description": "This book explores the intersection of quantum computing and machine learning, discussing how quantum algorithms can enhance machine learning techniques.",
                "level": "Intermediate to Advanced",
                "year": 2014
            },
            {
                "title": "Quantum Computing Since Democritus",
                "authors": "Scott Aaronson",
                "description": "A thought-provoking journey through quantum computing, complexity theory, and the philosophy of computation. It provides unique insights into the theoretical foundations.",
                "level": "Intermediate",
                "year": 2013
            },
            {
                "title": "Principles of Quantum Communication and Cryptography",
                "authors": "Subhash Kak",
                "description": "Explores quantum approaches to communication and cryptography, including DNA-based security techniques and quantum key distribution.",
                "level": "Advanced",
                "year": 2018
            }
        ]
        
        # Display books as expandable sections
        for book in books:
            with st.expander(f"{book['title']} ({book['year']})"):
                st.markdown(f"**Authors:** {book['authors']}")
                st.markdown(f"**Level:** {book['level']}")
                st.markdown(f"**Description:** {book['description']}")
        
        # Key research papers
        st.subheader("Key Research Papers")
        
        # Create a DataFrame of important papers
        papers_data = {
            "Title": [
                "Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer",
                "Quantum Algorithm for Linear Systems of Equations",
                "A DNA Computer for Encryption and Decryption",
                "Quantum Machine Learning",
                "DNA-Based Cryptography",
                "A Quantum-DNA Algorithm for DNA Sequence Analysis",
                "Quantum Secure Direct Communication with Quantum Memory",
                "Quantum Advantage with Noisy Shallow Circuits",
                "Hybrid Quantum-Classical Approach to Quantum Optimal Control",
                "Quantum Supremacy Using a Programmable Superconducting Processor"
            ],
            "Authors": [
                "Shor, P.W.",
                "Harrow, A.W., Hassidim, A., Lloyd, S.",
                "Gehani, A., LaBean, T., Reif, J.",
                "Biamonte, J., et al.",
                "Leier, A., Richter, C.",
                "Pang, T.Y., et al.",
                "Xiang, G.Y., et al.",
                "Bravyi, S., Gosset, D., König, R.",
                "Li, J., et al.",
                "Arute, F., et al."
            ],
            "Year": [
                1997,
                2009,
                2003,
                2017,
                2000,
                2015,
                2012,
                2018,
                2017,
                2019
            ],
            "Focus Area": [
                "Quantum Algorithms",
                "Quantum Algorithms",
                "DNA Computing",
                "Quantum Machine Learning",
                "DNA Cryptography",
                "Quantum-DNA Computing",
                "Quantum Communication",
                "Quantum Advantage",
                "Quantum Control",
                "Quantum Supremacy"
            ]
        }
        
        papers_df = pd.DataFrame(papers_data)
        
        # Add a filter by focus area
        focus_areas = ["All"] + sorted(papers_df["Focus Area"].unique().tolist())
        selected_focus = st.selectbox("Filter by focus area:", focus_areas)
        
        if selected_focus != "All":
            filtered_df = papers_df[papers_df["Focus Area"] == selected_focus]
        else:
            filtered_df = papers_df
        
        # Display the filtered papers
        st.dataframe(filtered_df.sort_values(by=["Year"], ascending=False))
        
        # Recent developments section
        st.subheader("Recent Developments")
        
        st.markdown("""
        ### Recent Breakthroughs in Quantum Computing and DNA Security
        
        **Quantum Advantage Demonstrations:**
        - Google's demonstration of quantum supremacy with the Sycamore processor
        - IBM's eagle processor with 127 qubits
        - Improvements in error correction and noise mitigation
        
        **DNA Computing Advances:**
        - Improved DNA strand displacement computing
        - DNA-based data storage with higher density and retrieval accuracy
        - Novel DNA cryptography methods with quantum-enhanced security
        
        **Quantum-DNA Integration:**
        - Hybrid systems combining quantum computing and DNA techniques
        - Quantum-secured DNA storage systems
        - Quantum ML for analyzing large-scale genomic data
        """)
        
        # Reading recommendations
        st.info("""
        **Reading Recommendation Strategy:**
        
        For those new to the field, we recommend starting with introductory books like "Quantum Computing: A Gentle Introduction" before moving to more advanced texts like Nielsen & Chuang.
        
        When exploring research papers, begin with review articles in your area of interest before diving into specific technical papers. This will provide context and help you understand the significance of specialized research.
        """)
    
    # Online Courses tab
    with tabs[2]:
        st.header("Online Courses and Tutorials")
        
        st.markdown("""
        ### Free Courses and Tutorials
        
        Explore these high-quality free resources to learn quantum computing at your own pace:
        """)
        
        # Create a list of free courses
        free_courses = [
            {
                "title": "Qiskit Textbook",
                "provider": "IBM Quantum",
                "url": "https://qiskit.org/textbook/",
                "description": "A comprehensive introduction to quantum computing using Qiskit, IBM's open-source quantum computing framework.",
                "focus": ["Quantum Computing Basics", "Quantum Algorithms", "Quantum Programming"],
                "level": "Beginner to Intermediate"
            },
            {
                "title": "Quantum Computing for the Very Curious",
                "provider": "Quantum Country",
                "url": "https://quantum.country/",
                "description": "An interactive essay series introducing quantum computing concepts with spaced repetition learning.",
                "focus": ["Quantum Computing Basics", "Quantum Algorithms"],
                "level": "Beginner"
            },
            {
                "title": "Understanding Quantum Computers",
                "provider": "Coursera (Keio University)",
                "url": "https://www.coursera.org/learn/understanding-quantum-computers",
                "description": "An introduction to the world of quantum computing, with minimal mathematics required.",
                "focus": ["Quantum Computing Basics"],
                "level": "Beginner"
            },
            {
                "title": "Quantum Machine Learning",
                "provider": "edX (University of Toronto)",
                "url": "https://www.edx.org/course/quantum-machine-learning",
                "description": "Learn about the emerging field of quantum machine learning and how it relates to classical machine learning.",
                "focus": ["Quantum Machine Learning", "Quantum Algorithms"],
                "level": "Intermediate"
            },
            {
                "title": "Quantum Cryptography",
                "provider": "edX (CalTech)",
                "url": "https://www.edx.org/course/quantum-cryptography",
                "description": "Explore quantum cryptography and quantum key distribution protocols.",
                "focus": ["Quantum Cryptography", "Quantum Security"],
                "level": "Intermediate"
            },
            {
                "title": "Introduction to Quantum Computing for Everyone",
                "provider": "edX (University of Chicago)",
                "url": "https://www.edx.org/course/introduction-to-quantum-computing-for-everyone-2",
                "description": "A non-technical introduction to quantum computing for a general audience.",
                "focus": ["Quantum Computing Basics"],
                "level": "Beginner"
            }
        ]
        
        # Display free courses with expandable sections
        for course in free_courses:
            with st.expander(f"{course['title']} ({course['provider']})"):
                st.markdown(f"**Level:** {course['level']}")
                st.markdown(f"**Focus Areas:** {', '.join(course['focus'])}")
                st.markdown(f"**Description:** {course['description']}")
                st.markdown(f"**URL:** [{course['url']}]({course['url']})")
        
        # Specialized tutorials section
        st.subheader("Specialized Tutorials")
        
        st.markdown("""
        ### DNA Security and Quantum Integration Tutorials
        
        These specialized tutorials focus on the intersection of DNA and quantum technologies:
        """)
        
        specialized_tutorials = [
            {
                "title": "Introduction to DNA Cryptography",
                "provider": "Bioinformatics.org",
                "description": "Learn the basics of using DNA for cryptographic applications, including encoding methods and security considerations.",
                "focus": "DNA Security"
            },
            {
                "title": "Quantum-Enhanced DNA Computing",
                "provider": "Quantum Bio Lab",
                "description": "Explore how quantum computing principles can enhance DNA computing techniques for both security and computational applications.",
                "focus": "Quantum-DNA Integration"
            },
            {
                "title": "Implementing Quantum Random Number Generators",
                "provider": "Qiskit Community",
                "description": "Tutorial on creating quantum random number generators for use in cryptographic applications, including DNA-based systems.",
                "focus": "Quantum Security"
            },
            {
                "title": "DNA Data Storage and Quantum Security",
                "provider": "Synthetic Biology Open Source",
                "description": "Learn about methods for storing data in DNA and securing it with quantum cryptographic techniques.",
                "focus": "DNA-Quantum Storage"
            }
        ]
        
        # Display specialized tutorials
        for tutorial in specialized_tutorials:
            st.markdown(f"**{tutorial['title']}** ({tutorial['provider']})")
            st.markdown(f"*Focus: {tutorial['focus']}*")
            st.markdown(f"{tutorial['description']}")
            st.markdown("---")
        
        # Video resources
        st.subheader("Video Resources")
        
        st.markdown("""
        ### Recommended YouTube Channels and Video Series
        
        Visual learning can enhance understanding of complex quantum concepts:
        
        - **Qiskit YouTube Channel**: Tutorials, lectures, and interviews about quantum computing
        - **PBS Space Time - Quantum Computing Series**: Accessible explanations of quantum physics and computing
        - **Anastasia Marchenkova**: Quantum computing concepts and news
        - **Quantum Computing for Everyone**: Microsoft's series on quantum computing basics
        - **IBM Quantum Experience Guides**: Step-by-step videos for using IBM's quantum computers
        """)
        
        # Hackathons and competitions
        st.subheader("Hackathons and Competitions")
        
        st.markdown("""
        ### Learn by Participating
        
        Enhance your skills by joining quantum computing competitions:
        
        - **IBM Quantum Challenge**: Periodic challenges hosted by IBM Quantum
        - **QHack**: Quantum machine learning hackathon
        - **Quantum Open Source Foundation Challenges**: Community challenges for quantum developers
        - **Quantum Coalition Hack**: Student-focused quantum hackathon
        - **Qiskit Summer Schools**: Intensive quantum computing programs with hands-on projects
        """)
        
        # Learning path recommendation
        st.success("""
        **Recommended Learning Approach:**
        
        1. Start with a general introduction course like "Quantum Computing for the Very Curious"
        2. Follow with the structured Qiskit Textbook to gain hands-on experience
        3. Choose specialized courses based on your interests (algorithms, machine learning, cryptography)
        4. Apply your knowledge through challenges and hackathons
        5. Join quantum computing communities to stay updated on developments
        """)
    
    # Software Tools tab
    with tabs[3]:
        st.header("Software Tools & Frameworks")
        
        st.markdown("""
        ### Quantum Computing Frameworks
        
        These software tools provide the development environment for quantum computing research and applications.
        """)
        
        # Create comparison table of quantum frameworks
        frameworks_data = {
            "Framework": ["Qiskit", "Cirq", "PennyLane", "Q#", "Forest (pyQuil)", "Strawberry Fields", "TensorFlow Quantum"],
            "Developer": ["IBM", "Google", "Xanadu", "Microsoft", "Rigetti", "Xanadu", "Google"],
            "Focus": ["General purpose", "General purpose", "Quantum ML", "Quantum algorithms", "General purpose", "Photonic QC", "Quantum ML"],
            "Language": ["Python", "Python", "Python", "Q# (.NET)", "Python", "Python", "Python/TensorFlow"],
            "Simulator": ["✓", "✓", "✓", "✓", "✓", "✓", "✓"],
            "Hardware Access": ["IBM Q", "Google Quantum", "Various backends", "Azure Quantum", "Rigetti QPUs", "Xanadu hardware", "Various backends"]
        }
        
        frameworks_df = pd.DataFrame(frameworks_data)
        st.dataframe(frameworks_df)
        
        # Installation guide
        st.subheader("Getting Started with Qiskit")
        
        st.markdown("""
        Qiskit is one of the most popular frameworks for quantum computing, developed by IBM.
        Here's how to get started:
        
        ```bash
        # Install Qiskit
        pip install qiskit
        
        # For visualization tools
        pip install matplotlib
        
        # For accessing IBM Quantum hardware (optional)
        pip install qiskit-ibmq-provider
        