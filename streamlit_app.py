# Save as app.py

import streamlit as st
from PIL import Image

# Page configuration
st.set_page_config(page_title="Shivam Garg | Portfolio", layout="wide")

# Sidebar with icons for better navigation
st.sidebar.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background: #2b2d42;
            color: #ffffff;
        }
        .sidebar .stRadio > label {
            font-size: 1.2em;
            color: #ffffff;
        }
        .stRadio div[role='radiogroup'] > label:hover {
            color: #fca311;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("🔍 Navigation")
sections = [
    "🏠 Home",
    "🎯 Career Objective",
    "📄 Professional Summary",
    "💼 Experience",
    "🎓 Education",
    "🛠️ Skills",
    "📈 Projects",
    "📜 Certifications",
    "🏆 Highlights",
]
selection = st.sidebar.radio("Select a Section", sections)

# Global CSS Styling for enhanced visuals and animations
st.markdown(
    """
    <style>
        /* Page Fade-in Animation */
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .main-content {
            animation: fadeIn 1s ease-in-out;
        }

        /* General Container Styling */
        .container {
            background: #f0f4f8; /* Light background for better readability */
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
            transition: transform 0.2s, box-shadow 0.2s;
            margin: 15px 0;
            color: #2b2d42;
        }

        .container:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 20px rgba(0, 0, 0, 0.2);
            background: #e8eff5;
        }

        /* Section Headers Styling */
        .section-header {
            color: #264653;
            font-size: 2.2em;
            font-weight: bold;
            padding: 0.5em 0;
        }

        /* Text Styling */
        .text-content {
            color: #2b2d42;
            font-size: 1.1em;
        }

        /* Link Styling */
        .container a {
            color: #264653;
            font-weight: 600;
            text-decoration: none;
        }

        .container a:hover {
            color: #fca311;
        }

        /* Header Styling */
        .header {
            text-align: center;
            font-size: 3em;
            color: #2b2d42;
            font-weight: 600;
            margin-bottom: 0.5em;
        }
        .subheader {
            text-align: center;
            font-size: 1.4em;
            color: #5f6368;
        }

        /* Navigation Hover Animation */
        .sidebar .stRadio div[role='radiogroup'] > label:hover {
            font-size: 1.25em;
            transition: font-size 0.2s;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Main Content Wrapper for fade-in effect
st.markdown("<div class='main-content'>", unsafe_allow_html=True)

# Home Section
if selection == "🏠 Home":
    st.markdown("<div style='text-align:center; font-size:3em; color:#2b2d42; font-weight:600;'>Shivam Garg</div>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center; font-size:1.4em; color:#5f6368;'>Data Scientist | Python Developer | Software Engineer</p>",
        unsafe_allow_html=True,
    )
    
    profile_image = "/workspaces/shivamsgarg/image/profile.jpg"  # Update with actual path
    try:
        img = Image.open(profile_image)
        st.image(img, width=150, caption="Shivam Garg", use_container_width=True)  # Adjusted image size and round style
    except:
        st.image("https://via.placeholder.com/150", caption="Shivam Garg", width=150)
    
    st.markdown(
        """
        📍 Ambala, Haryana, India  
        📱 +91 9518082282  
        ✉️ [gargshivam2707@gmail.com](mailto:gargshivam2707@gmail.com)  
        [LinkedIn](http://linkedin.com/in/shivam27071999) | [GitHub](http://github.com/Shivamg27071999)
        """
    )

# Section Template for Reusability
def display_section(title, content_list):
    st.markdown(f"<h2 class='section-header'>{title}</h2>", unsafe_allow_html=True)
    for content in content_list:
        st.markdown(f"<div class='container'><p class='text-content'>{content}</p></div>", unsafe_allow_html=True)

# Career Objective
if selection == "🎯 Career Objective":
    display_section("🚀 Career Objective", [
        "Dynamic Data Scientist and Python Developer, adept at building robust data-driven solutions, with a focus on machine learning and software development."
    ])

# Professional Summary
if selection == "📄 Professional Summary":
    display_section("🔍 Professional Summary", [
        "Experienced in data analysis, machine learning, and Python software development. Skilled in creating efficient algorithms and optimizing model performance."
    ])

# Experience
if selection == "💼 Experience":
    experiences = [
        ("Data Science Intern", "Innomatics Research Labs", "Sep 2024 - Present", [
            "Developed predictive models using ML algorithms.",
            "Built and deployed deep learning models (ANN, CNN) for image classification.",
            "Deployed Python software using Flask for model serving."
        ]),
        ("Freelance Developer", "Remote", "Jul 2021 - Aug 2022", [
            "Designed RESTful APIs using Flask and Django.",
            "Automated data extraction using Python scripts.",
            "Collaborated closely with clients for software delivery."
        ])
    ]
    for title, company, dates, details in experiences:
        st.markdown(f"<div class='container'><strong>{title}</strong> at {company} ({dates})", unsafe_allow_html=True)
        st.markdown("<ul>", unsafe_allow_html=True)
        for detail in details:
            st.markdown(f"<li>{detail}</li>", unsafe_allow_html=True)
        st.markdown("</ul></div>", unsafe_allow_html=True)
# Education Section
if selection == "🎓 Education":
    st.markdown("<h2 class='section-header'>🎓 Education</h2>", unsafe_allow_html=True)
    education_details = [
        "Master of Computer Applications (Data Science) - Lovely Professional University, Punjab (Aug 2022 - Sep 2024)",
        "IBM Certified Data Scientist - Innomatics Research Labs, Hyderabad, India (Sep 2023 – Jun 2024)",
        "Bachelor of Computer Applications - Kurukshetra University, Haryana (Jun 2016 – Jun 2020)"
    ]
    for edu in education_details:
        st.markdown(f"<div class='container'><p class='text-content'>{edu}</p></div>", unsafe_allow_html=True)

# Skills Section
if selection == "🛠️ Skills":
    st.markdown("<h2 class='section-header'>🛠️ Technical Skills</h2>", unsafe_allow_html=True)
    skills = {
        "Programming Languages": "Python, SQL",
        "Frameworks & Tools": "Flask, Django, Streamlit, Git",
        "ML Libraries": "Scikit-Learn, TensorFlow, Keras, Pandas",
        "Data Engineering": "Data Cleaning, ETL Pipelines, Web Scraping",
        "Visualization": "Tableau, Power BI, Matplotlib",
        "Cloud & DevOps": "GitHub Actions, CI/CD, AWS",
        "Software Development": "API Development, Automation",
        "Core ML Concepts": "Neural Networks, NLP, Computer Vision",
        "Languages": "English, Hindi, Punjabi"
    }
    for skill, details in skills.items():
        st.markdown(f"<div class='container'><p class='text-content'><strong>{skill}</strong>: {details}</p></div>", unsafe_allow_html=True)

# Projects Section
if selection == "📈 Projects":
    st.markdown("<h2 class='section-header'>📈 Key Projects</h2>", unsafe_allow_html=True)
    projects = [
        ("Real Estate Data Scraper", "Automated data collection and built a Flask-based visualization app."),
        ("Sales Dashboard", "Created a Tableau dashboard for sales performance analysis."),
        ("Loan Prediction System", "Developed a model and integrated it with a Flask app for real-time predictions."),
        ("Pollution Analysis Tool", "Analyzed vehicle pollution impacts with a ML model and live YouTube data."),
        ("Healthcare Optimization", "Built an ANN model to optimize resource allocation."),
        ("AI Query Assistant", "Developed an AI-powered query assistant integrated with Streamlit."),
        ("Subtitle Search Engine", "Improved search accuracy with a Flask-based application.")
    ]
    for title, description in projects:
        st.markdown(f"<div class='container'><p class='text-content'><strong>{title}</strong>: {description}</p></div>", unsafe_allow_html=True)

# Certifications Section
if selection == "📜 Certifications":
    st.markdown("<h2 class='section-header'>📜 Certifications</h2>", unsafe_allow_html=True)
    certificates = {
        "Advanced Data Analysis Internship Program - Innomatics Research Labs": "path/to/image1.jpg",
        "Machine Learning with Python - Level 1 – IBM": "path/to/image2.jpg",
        "Foundations of Data Science - Coursera": "path/to/image3.jpg"
    }
    for cert, img_path in certificates.items():
        st.markdown(f"<div class='container'><p class='text-content'>{cert}</p><img src='{img_path}' width='100'></div>", unsafe_allow_html=True)

# Additional Highlights Section
if selection == "🏆 Highlights":
    st.markdown("<h2 class='section-header'>🏆 Additional Highlights</h2>", unsafe_allow_html=True)
    highlights = [
        "Hands-on experience in developing full-stack applications and machine learning solutions.",
        "Proven ability to deliver projects efficiently, balancing software development and data science tasks.",
        "Committed to continuous learning, actively improving skills in the latest technologies and frameworks.",
        "Participated in several hackathons and coding challenges, earning top ranks."
    ]
    for highlight in highlights:
        st.markdown(f"<div class='container'><p class='text-content'>{highlight}</p></div>", unsafe_allow_html=True)

# Footer Section
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div style='text-align:center; font-size:0.8em; color:#888;'>", unsafe_allow_html=True)
st.markdown("Made with ❤️ by Shivam Garg | All rights reserved.", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# End of Main Content Wrapper
st.markdown("</div>", unsafe_allow_html=True)
