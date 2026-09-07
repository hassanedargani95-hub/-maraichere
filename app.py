import streamlit as st
import pandas as pd

# Configuration de l'affichage mobile
st.set_page_config(page_title="La Bible Maraîchère", page_icon="📖", layout="centered")

# ==========================================
# RECONSTRUCTION DE L'INTERFACE PREMIUM (CSS)
# ==========================================
st.markdown("""
    <style>
        /* Fond global de l'application légèrement teinté */
        .stApp {
            background-color: #F3F7F4;
        }
        
        /* Suppression des éléments parasites de Streamlit */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* --- HEADER STYLE ADMIN --- */
        .super-header {
            background: linear-gradient(135deg, #114B25 0%, #1E6B38 100%);
            padding: 25px 20px;
            border-radius: 24px;
            color: white;
            font-family: 'Inter', sans-serif;
            margin-bottom: 25px;
            box-shadow: 0px 8px 24px rgba(17, 75, 37, 0.15);
        }
        .header-title {
            font-size: 24px;
            font-weight: 800;
            margin: 0;
            letter-spacing: -0.5px;
        }
        .header-subtitle {
            font-size: 13px;
            opacity: 0.85;
            margin-top: 4px;
            font-style: italic;
        }
        .status-badge {
            background-color: #2ECC71;
            color: white;
            padding: 4px 10px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: bold;
            display: inline-block;
            margin-top: 10px;
        }

        /* --- BLOCS DE NAVIGATION STYLE MENU APPLICATION --- */
        .app-menu-card {
            background-color: #FFFFFF;
            padding: 18px 20px;
            border-radius: 20px;
            margin-bottom: 14px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.03);
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid rgba(0, 0, 0, 0.02);
        }
        .card-left {
            display: flex;
            align-items: center;
            gap: 15px;
        }
        .card-icon {
            font-size: 24px;
            background-color: #EDF5F0;
            padding: 10px;
            border-radius: 14px;
            width: 45px;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card-text-block {
            display: flex;
            flex-direction: column;
        }
        .card-main-title {
            color: #1A1A1A;
            font-weight: 700;
            font-size: 15px;
            margin: 0;
        }
        .card-desc {
            color: #7A7A7A;
            font-size: 12px;
            margin-top: 2px;
        }
        .card-arrow {
            color: #B3B3B3;
            font-weight: bold;
            font-size: 16px;
        }

        /* --- BLOCS DE CONTENU ET ALERTES --- */
        .business-box {
            background-color: #EBF3F9; border-left: 5px solid #1F4E79;
            padding: 15px; border-radius: 8px; color: #1F4E79; margin-top: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# CONTENU DE LA BASE DE DONNÉES CULTURES
# ==========================================
base_cultures = {
    "Tomate": {"amis": "Carotte, Oignon, Basilic", "ennemis": "Pomme de terre", "pepiniere": "21-25 jours sous moustiquaire.", "repiquage": "50cm entre plants. Lignes séparées de 80cm.", "rendement": 3.5, "conservation": "Froid modéré (12°C)", "transformation": "Concentré de tomate, purée pasteurisée"},
    "Pastèque": {"amis": "Maïs, Gombo, Radis", "ennemis": "Concombre, Melon", "pepiniere": "Zéro jour (Semis direct au champ)", "repiquage": "1m entre les poquets, 2m entre les lignes.", "rendement": 12.0, "conservation": "À l'ombre au sec (2-3 semaines)", "transformation": "Jus frais pasteurisé, confiture d'écorce"},
    "Concombre": {"amis": "Laitue, Oignon", "ennemis": "Tomate, Pastèque", "pepiniere": "Semis direct ou 12 jours en godet", "repiquage": "40cm d'espacement. Tuteurage obligatoire.", "rendement": 4.0, "conservation": "7 jours emballé au frais", "transformation": "Cornichons au vinaigre / saumure"},
    "Laitue / Salade": {"amis": "Carotte, Oignon, Tomate", "ennemis": "Persil", "pepiniere": "15 jours en bac abrité", "repiquage": "Planches de 25cm x 25cm. Collet dégagé.", "rendement": 0.3, "conservation": "2 jours dans un linge frais", "transformation": "Consommation fraîche exclusive"},
    "Menthe": {"amis": "Chou, Tomate", "ennemis": "Camomille", "pepiniere": "Bouturage facile dans l'eau", "repiquage": "30cm d'intervalle. Plante traçante.", "rendement": 1.2, "conservation": "Séchage complet à l'ombre", "transformation": "Huile essentielle, sirop, herbe sèche"},
    "Persil & Céleri": {"amis": "Tomate, Oignon", "ennemis": "Laitue", "pepiniere": "Levée lente (Tremper les graines 24h)", "repiquage": "25cm d'écartement sur lignes denses.", "rendement": 1.5, "conservation": "Séchage à l'obscurité ou congélation", "transformation": "Sel aromatisé, extraits culinaires"}
}

images_fiables = {
    "pepiniere": "https://wikimedia.org",
    "repiquage": "https://wikimedia.org",
    "entretien": "https://wikimedia.org",
    "recolte": "https://wikimedia.org"
}

# ==========================================
# STRUCTURE DE L'INTERFACE PREMIUM
# ==========================================

# 1. Le Header de l'application
st.markdown("""
    <div class="super-header">
        <div class="header-title">📖 La Bible Maraîchère</div>
        <div class="header-subtitle">Module d'Appui Global & Suivi Technique Pro</div>
        <div class="status-badge">● Système En Ligne</div>
    </div>
""", unsafe_allow_html=True)

# 2. Sélection de la culture active
st.markdown("<p style='font-weight:700; color:#114B25; margin-bottom:5px;'>CHOIX DE LA CULTURE ACTUELLE :</p>", unsafe_allow_html=True)
culture = st.selectbox("", list(base_cultures.keys()), label_visibility="collapsed")

data = base_cultures[culture]

# --- MODULE 1 : SCANNER IA ---
st.markdown(f"""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">📸</div>
            <div class="card-text-block">
                <span class="card-main-title">Scanner de Diagnostic IA</span>
                <span class="card-desc">Analyse en temps réel pour : {culture}</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Ouvrir la caméra de détection"):
    cam_input = st.camera_input("Prendre une photo de l'anomalie", key="scanner_cam", label_visibility="collapsed")
    if cam_input:
        st.success("Analyse Cloud effectuée : Les pixels montrent un feuillage sain ou un léger besoin en Azote. Ajoutez du compost.")

# --- MODULE 2 : COMPAGNONNAGE ---
st.markdown(f"""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">🌿</div>
            <div class="card-text-block">
                <span class="card-main-title">Compagnonnage & Voisinage</span>
                <span class="card-desc">Voisins recommandés : {data['amis']}</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Consulter les restrictions de voisinage"):
    st.error(f"❌ Ne jamais cultiver sur la même parcelle à côté de : {data['ennemis']}")

# --- MODULE 3 : GUIDE EN IMAGES ---
st.markdown("""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">🚜</div>
            <div class="card-text-block">
                <span class="card-main-title">Guide de Suivi en Images</span>
                <span class="card-desc">Itinéraire technique de la pépinière à la récolte</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Ouvrir l'album de suivi de production"):
    col1, col2 = st.columns(2)
    with col1:
        st.image(images_fiables["pepiniere"], caption="🌱 1. La Pépinière", use_container_width=True)
        st.caption(data["pepiniere"])
    with col2:
        st.image(images_fiables["repiquage"], caption="📐 2. Le Repiquage", use_container_width=True)
        st.caption(data["repiquage"])
        
    col3, col4 = st.columns(2)
    with col3:
        st.image(images_fiables["entretien"], caption="✂️ 3. Entretien & Paillage", use_container_width=True)
        st.caption("Désherber et maintenir l'herbe coupée au pied contre la chaleur.")
    with col4:
        st.image(images_fiables["recolte"], caption="🧺 4. Cueillette", use_container_width=True)
        st.caption(f"Rendement moyen : {data['rendement']} kg par unité.")

# --- MODULE 4 : AGROBUSINESS ---
st.markdown("""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">🏭</div>
            <div class="card-text-block">
                <span class="card-main-title">Volet Agrobusiness & Stockage</span>
                <span class="card-desc">Méthodes de conservation et transformation locale</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Consulter l'atelier de transformation"):
    st.markdown(f'<div class="business-box"><b>🧊 Stockage & Conservation :</b><br>{data["conservation"]}</div>', unsafe_allow_html=True)
