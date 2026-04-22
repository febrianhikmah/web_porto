import streamlit as st

st.set_page_config(
    page_title="Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

/* background */
.stApp{
    background:#00112A;
}

/* text umum */
h1,h2,h3,h4,h5,h6,p,label,span,div{
    color:white;
}

/* =========================
LINK BUTTON OUTER
========================= */
div[data-testid="stLinkButton"]{
    width:100% !important;
}

/* tombol asli di dalamnya */
div[data-testid="stLinkButton"] a{
    width:100% !important;
    display:flex !important;
    justify-content:center !important;
    align-items:center !important;

    background:#122B3C !important;
    color:Blue !important;

    border:none !important;
    border-radius:10px !important;

    padding:0.70rem 1rem !important;
    text-decoration:none !important;
}

/* semua isi teks */
div[data-testid="stLinkButton"] a *{
    color:white !important;
}

/* hover */
div[data-testid="stLinkButton"] a:hover{
    background:#1b4058 !important;
    color:Blue !important;
}

/* visited */
div[data-testid="stLinkButton"] a:visited{
    color:Blue !important;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# LAYOUT
# ===============================
left, right = st.columns([1, 1.6], gap="large")


# ===============================
# KIRI
# ===============================
with left:
    st.title("Febrian Hikmah Nur Rohim")
    st.title("Data Engineer")

    st.write("""Saya seorang mahasiswa semester 6, Memiliki minat besar dalam bidang Data Engineering, dengan fokus pada bagaimana data dikumpulkan, diproses, dan 
             diubah menjadi informasi yang bernilai. Saya tertarik membangun pipeline data yang efisien, scalable, dan andal untuk mendukung kebutuhan analisis dan 
             pengambilan keputusan.""")

    
    # ===============================
    # GANTI BAGIAN CONNECT JADI INI
    # ===============================
    st.subheader("Connect")

    st.link_button(
        "LinkedIn",
        "https://linkedin.com/in/febrian-nurrohim",
        use_container_width=True
    )

    c3, c4 = st.columns(2)

    with c3:
        st.link_button(
            "Instagram",
            "https://www.instagram.com/rohimm.02/",
            use_container_width=True
        )

    with c4:
        st.link_button(
            "Email",
            "mailto:febriannurrohim12@gmail.com",
            use_container_width=True
        )


# ===============================
# KANAN
# ===============================
with right:
    st.title("Projects")

    projects = [
        {
            "title": "Data Pipeline StreamCart Real-Time E-Commerce",
            "desc": """StreamCart adalah simulasi pipeline data real-time yang mengintegrasikan Apache Kafka dan Python untuk mengelola 
            transaksi e-commerce secara efisien. Proyek ini mentransformasi data mentah ke dalam PostgreSQL sebagai database, 
            menghasilkan sistem penyimpanan yang terstruktur dan optimal untuk kebutuhan analitik bisnis yang cepat dan akurat.""",
            "tags": ["Event Streaming", "Apache Kafka", "ETL", "Python", "PostgreSQL"],
            "doc": "https://github.com/febrianhikmah/StreamCart_Real-Time_E-Commerce_Transactions_Data_Pipeline"
        },
        {
            "title": "Data Pipeline End-to-End YouTube Comment",
            "desc": """YouTube Comment Pipeline adalah proyek end-to-end yang mengotomatisasi pengambilan data komentar dari 
            YouTube API hanya dengan memasukan URL. Menggunakan aplikasi web streamlit sederhana serta proses ETL sebagai proses penunjangnya, data kemudian diproses dan 
            disimpan ke dalam PostgreSQL dengan skema stars skema yang terstruktur.""",
            "tags": ["YouTube API", "ETL", "Python", "PostgreSQL", "Streamlit"],
            "doc": "https://github.com/febrianhikmah/DATA_PIPELINE_YOUTUBE_COMMENT_-END-TO-END-"
        }
    ]

    for p in projects:
        with st.container(border=True):
            st.subheader(p["title"])
            st.write(p["desc"])

            cols = st.columns(len(p["tags"]))
            for i, tag in enumerate(p["tags"]):
                cols[i].info(tag)

            st.link_button(
                "Dokumentasi Project",
                p["doc"],
                use_container_width=True
            )

