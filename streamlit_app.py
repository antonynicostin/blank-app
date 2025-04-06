import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import base64

# --- PAGE CONFIG ---
st.set_page_config(page_title="Ignatius Benisha | Data Analyst Portfolio", page_icon="📊", layout="wide")

# --- CUSTOM LIGHT THEME (via config.toml) ---
# Make sure to have a .streamlit/config.toml with theme set to light:
# [theme]
# base="light"
# primaryColor="#003366"
# backgroundColor="#f8f9fa"
# secondaryBackgroundColor="#ffffff"
# textColor="#212529"
# font="sans serif"

# --- INLINE STYLE OVERRIDES ---
st.markdown("""
<style>
body {
    background-color: #f8f9fa;
    color: #212529;
}
.header-title {
    font-size: 40px;
    font-weight: bold;
    color: #003366;
}
.subheader-text {
    font-size: 20px;
    color: #495057;
}
.section-header {
    font-size: 28px;
    margin-top: 2em;
    color: #1c1c1c;
    border-bottom: 2px solid #dee2e6;
    padding-bottom: 0.3em;
}
.contact-form {
    background-color: #ffffff;
    padding: 1.5em;
    border-radius: 10px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
</style>
""", unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='header-title'>👩‍💼 Ignatius Benisha</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader-text'>Data Analyst | Python • SQL • Power BI • Streamlit</div>", unsafe_allow_html=True)

st.write("""
📍 Chennai, India  
📧 benishac2018@gmail.com | 📞 +91 6385144081  
🔗 [LinkedIn](https://www.linkedin.com/in/ignatius-benisha-c-6b7037223/) | 🌐 [GitHub](https://github.com/benishac)
""")

# --- SUMMARY SECTION ---
st.markdown("<div class='section-header'>📌 Summary</div>", unsafe_allow_html=True)
st.success("""
Support Engineer with 2 years of fintech/payments experience, now pivoting into Data Analytics. Skilled in SQL, Python, Power BI, and Streamlit. Proven ability to analyze large-scale data and deliver impactful insights.
""")

# --- SKILLS SECTION ---
st.markdown("<div class='section-header'>🧠 Skills & Tools</div>", unsafe_allow_html=True)
cols = st.columns(2)
cols[0].markdown("""
- **Languages**: Python, Java, SQL
- **Data Tools**: Pandas, NumPy, Matplotlib, Streamlit
- **Databases**: MySQL, Oracle SQL Plus
""")
cols[1].markdown("""
- **BI & Visualization**: Power BI, Excel
- **Monitoring Tools**: Datadog, Kibana, Control-M
- **Ticketing Tools**: Jira, ServiceNow
""")

# --- PROJECTS SECTION ---
st.markdown("<div class='section-header'>📊 Featured Projects</div>", unsafe_allow_html=True)

with st.expander("📌 Zomato Sales Analysis Dashboard (Power BI)"):
    st.markdown("""
    - Built an interactive dashboard analyzing 5,000+ transactions.
    - KPIs: sales trends, order volume, customer frequency.
    - Utilized DAX, slicers, and drill-throughs for user insights.
    - 📎 [View Report](https://www.novypro.com/project/zomato-sales-analysis-dashboard)  
    """)
    data = pd.DataFrame({
        'City': ['Chennai', 'Mumbai', 'Bangalore', 'Delhi'],
        'Sales': [45000, 62000, 39000, 52000]
    })
    fig = px.bar(data, x='City', y='Sales', color='City', title='Sample Sales Overview by City')
    st.plotly_chart(fig)

with st.expander("📌 Amazon Prime Video Analytics (Power BI)"):
    st.markdown("""
    - Visualized 7 years of user watch behavior by genre, ratings, and time.
    - Built time-based storytelling using filters, slicers, and trend lines.
    - 📎 [View Report](https://www.novypro.com/project/amazon-prime-video-analysis-dashboard)
    """)
    watch_data = pd.DataFrame({
        'Genre': ['Drama', 'Comedy', 'Thriller', 'Documentary'],
        'Average Watch Time (hrs)': [15, 10, 12, 8]
    })
    fig2 = px.pie(watch_data, names='Genre', values='Average Watch Time (hrs)', title='Average Watch Time per Genre')
    st.plotly_chart(fig2)

# --- CERTIFICATIONS ---
st.markdown("<div class='section-header'>📜 Certifications & Awards</div>", unsafe_allow_html=True)
st.markdown("""
- ✅ Power BI – Oranium  
- ✅ MySQL – Oranium  
- ✅ Java – QSpiders  
- ✅ SQL – QSpiders  
- 🏆 Award: "Amazing Addition" – PagoNXT (Performance Excellence)
""")

# --- EDUCATION ---
st.markdown("<div class='section-header'>🎓 Education</div>", unsafe_allow_html=True)
st.markdown("B.Tech – Information Technology | Jeppiaar Engineering College, Chennai (2018–2022) – 80%")

# --- CONTACT ---
st.markdown("<div class='section-header'>📬 Contact Me</div>", unsafe_allow_html=True)
st.markdown("""
<div class='contact-form'>
<form action="https://formsubmit.co/benishac2018@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="width:100%; padding:8px; margin-bottom:10px;"><br>
    <input type="email" name="email" placeholder="Your email" required style="width:100%; padding:8px; margin-bottom:10px;"><br>
    <textarea name="message" placeholder="Your message" required style="width:100%; padding:8px; height:120px;"></textarea><br>
    <button type="submit" style="padding:10px 20px; background-color:#003366; color:white; border:none; border-radius:5px;">Send Message</button>
</form>
</div>
""", unsafe_allow_html=True)

# --- RESUME DOWNLOAD ---
def download_resume(path):
    try:
        with open(path, "rb") as file:
            btn = st.download_button(
                label="📄 Download Resume",
                data=file,
                file_name="Ignatius_Benisha_Resume.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.warning("Resume file not found. Please check the file path.")

st.markdown("<div class='section-header'>📎 Resume</div>", unsafe_allow_html=True)
download_resume("Resume_Igantius Benisha_.pdf")
