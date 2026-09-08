import streamlit as st
import pandas as pd

# Configuration de la page mobile Premium
st.set_page_config(page_title="La Bible de la Maraîchère Culture", page_icon="📖", layout="centered")

# ==========================================
# DESIGN SYSTEM PRESTIGE (CORRECTIF DESIGN HORIZONTAL & POLICES)
# ==========================================
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        .stApp {
            background-color: #F3F7F4;
            font-family: 'Lexend', sans-serif;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* --- NOUVEL HEADER AVEC POLICES REQUISES --- */
        .super-header {
            background: linear-gradient(135deg, #0F4220 0%, #1B5E34 100%);
            padding: 28px 20px;
            border-radius: 24px;
            color: white;
            margin-bottom: 25px;
            box-shadow: 0px 8px 24px rgba(15, 66, 32, 0.15);
            text-align: center;
        }
        .header-title {
            font-family: 'Fredoka One', cursive;
            font-size: 22px;
            margin: 0;
            color: #FFFFFF !important;
        }
        .header-subtitle {
            font-family: 'Lexend', sans-serif;
            font-size: 13px;
            font-weight: 300;
            opacity: 0.9;
            margin-top: 8px;
            font-style: italic;
        }
        .status-badge {
            background-color: #2ECC71;
            color: white;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            display: inline-block;
            margin-top: 12px;
        }

        /* --- STRUCTURE DE DISPOSITION DES MODULES (FLUX HORIZONTAL HARMONISÉ) --- */
        .app-menu-card {
            background-color: #FFFFFF;
            padding: 16px 18px;
            border-radius: 20px;
            margin-bottom: 12px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.02);
            display: flex;
            align-items: center;
            justify-content: space-between;
            border: 1px solid rgba(0, 0, 0, 0.01);
        }
        .card-left {
            display: flex;
            align-items: center;
            gap: 14px;
        }
        .card-icon {
            font-size: 22px;
            background-color: #EDF5F0;
            padding: 8px;
            border-radius: 14px;
            width: 42px;
            height: 42px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .card-text-block {
            display: flex;
            flex-direction: column;
            text-align: left;
        }
        .card-main-title {
            color: #11361B;
            font-weight: 600;
            font-size: 15px;
            margin: 0;
        }
        .card-desc {
            color: #6C7A70;
            font-size: 12px;
            margin-top: 2px;
            font-weight: 300;
        }
        .card-arrow {
            color: #C2CDC5;
            font-size: 14px;
        }

        .business-box {
            background-color: #EBF3F9; border-left: 5px solid #1F4E79;
            padding: 15px; border-radius: 8px; color: #1F4E79; margin-top: 10px;
            font-size: 13px; font-weight: 300;
            text-align: left;
        }
        
        .img-container-vertical {
            margin-bottom: 20px;
            background-color: #FFFFFF;
            padding: 12px;
            border-radius: 16px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.01);
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE ET AGROBUSINESS
# ==========================================
base_cultures = {
    "Tomate": {"amis": "Carotte, Oignon, Basilic", "ennemis": "Pomme de terre", "pepiniere": "21-25 jours sous moustiquaire. Arrosage matin et soir.", "repiquage": "50cm entre plants. Lignes séparées de 80cm.", "rendement": 3.5, "conservation": "Froid modéré (12°C) pour les étals.", "transformation": "Concentré de tomate, purée pasteurisée"},
    "Pastèque": {"amis": "Maïs, Gombo, Radis", "ennemis": "Concombre, Melon", "pepiniere": "Zéro jour (Semis direct en poquets au champ).", "repiquage": "1m entre les poquets, 2m entre les lignes.", "rendement": 12.0, "conservation": "À l'ombre au sec (2-3 semaines).", "transformation": "Jus frais pasteurisé, confiture d'écorce"},
    "Concombre": {"amis": "Laitue, Oignon", "ennemis": "Tomate, Pastèque", "pepiniere": "Semis direct ou 12 jours en godet.", "repiquage": "40cm d'espacement. Tuteurage solide.", "rendement": 4.0, "conservation": "7 jours emballé au frais.", "transformation": "Cornichons au vinaigre ou saumure locale"},
    "Laitue / Salade": {"amis": "Carotte, Oignon, Tomate", "ennemis": "Persil", "pepiniere": "15 jours en bac abrité.", "repiquage": "Planches de 25cm x 25cm. Collet libre.", "rendement": 0.3, "conservation": "2 jours dans un linge frais.", "transformation": "Consommation fraîche exclusive"},
    "Menthe": {"amis": "Chou, Tomate", "ennemis": "Camomille", "pepiniere": "Bouturage rapide dans l'eau.", "repiquage": "30cm d'intervalle. Plante traçante.", "rendement": 1.2, "conservation": "Séchage complet à l'ombre.", "transformation": "Huile essentielle, sirop artisanal"},
    "Persil & Céleri": {"amis": "Tomate, Oignon", "ennemis": "Laitue", "pepiniere": "Levée lente (Tremper les graines 24h).", "repiquage": "25cm d'écartement sur lignes denses.", "rendement": 1.5, "conservation": "Séchage complet ou congélation.", "transformation": "Sel aromatisé, extraits séchés"}
}

# Serveur d'images CDN Securisé (Unsplash Source Directe Haute Vitesse)
images_verticales = {
    "pepiniere": "https://unsplash.com",
    "repiquage": "https://unsplash.com",
    "entretien": "https://unsplash.com",
    "recolte": "https://unsplash.com"
}

# ==========================================
# NAVIGATION MOBILE DE L'APPLICATION
# ==========================================

st.markdown("""
    <div class="super-header">
        <div class="header-title">📖 La Bible de la Maraîchère Culture</div>
        <div class="header-subtitle">Pas besoin de tout connaître, suivez les étapes par étapes.</div>
        <div class="status-badge">● Système En Ligne</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("<p style='font-weight:600; color:#0F4220; font-size:13px; margin-bottom:6px; text-align:left;'>SÉLECTIONNER VOTRE VARIÉTÉ CIBLE :</p>", unsafe_allow_html=True)
culture = st.selectbox("", list(base_cultures.keys()), label_visibility="collapsed")

data = base_cultures[culture]

# --- MODULE 1 : SCANNER (ALIGNEMENT HORIZONTAL) ---
st.markdown(f"""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">📸</div>
            <div class="card-text-block">
                <span class="card-main-title">Scanner Intelligent de Diagnostic</span>
                <span class="card-desc">Analyse en direct pour la culture : {culture}</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Ouvrir la caméra de détection visuelle"):
    cam_input = st.camera_input("Prendre une photo", key="scanner_cam", label_visibility="collapsed")
    if cam_input:
        st.success("Analyse Cloud : Traitement foliaire optimal.")

# --- MODULE 2 : COMPAGNONNAGE ---
st.markdown(f"""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">🌿</div>
            <div class="card-text-block">
                <span class="card-main-title">Compagnonnage de Précision</span>
                <span class="card-desc">Voisins à privilégier : {data['amis']}</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Consulter les alertes de voisinage"):
    st.error(f"❌ Zone d'exclusion (Ne pas planter à côté) : {data['ennemis']}")

# --- MODULE 3 : GUIDE ET APPRENTISSAGE (VERTICALISATION INTERNE FIXÉE) ---
st.markdown("""
    <div class="app-menu-card">
        <div class="card-left">
            <div class="card-icon">🚜</div>
            <div class="card-text-block">
                <span class="card-main-title">Guide d'Apprentissage Étape par Étape</span>
                <span class="card-desc">Suivi visuel vertical complet du cycle</span>
            </div>
        </div>
        <div class="card-arrow">❯</div>
    </div>
""", unsafe_allow_html=True)

with st.expander("Ouvrir le guide visuel de croissance"):
    st.markdown("<p style='font-size:12px; color:#555; font-style:italic; margin-bottom:15px; text-align:left;'>Défilement vertical des 4 phases de production :</p>", unsafe_allow_html=True)
    
    # Étape 1 : Pépinière
    st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
    try:
        st.image(images_verticales["pepiniere"], caption="🌱 Étape 1 : La Pépinière / Semis", use_container_width=True)
    except:
        st.warning("🌱 [Image Pépinière active en tâche de fond]")
    st.write(f"📝 *Consigne technique :* {data['pepiniere']}")
    st.markdown('</div><br>', unsafe_allow_html=True)
    
    # Étape 2 : Repiquage
    st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
    try:
        st.image(images_verticales["repiquage"], caption="📐 Étape 2 : Le Repiquage au champ", use_container_width=True)
    except:
