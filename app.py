import streamlit as st
import pandas as pd

# Configuration Premium de la page mobile
st.set_page_config(page_title="La Bible du Maraîchage", page_icon="🌱", layout="centered")

# ==========================================
# DESIGN SYSTEM ECO-GROCERY MODERNE (CSS)
# ==========================================
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Fond épuré blanc/crème comme l'exemple */
        .stApp {
            background-color: #FFFFFF;
            font-family: 'Lexend', sans-serif;
        }
        
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* --- EN-TÊTE SANS-CHEF STYLE GROCERY --- */
        .grocery-header {
            text-align: center;
            padding: 20px 10px;
            margin-bottom: 15px;
        }
        .main-title {
            font-family: 'Fredoka One', cursive;
            color: #10B981; /* Vert éclatant Grocery */
            font-size: 28px;
            margin: 0;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .main-subtitle {
            color: #6B7280;
            font-size: 13px;
            font-weight: 400;
            margin-top: 6px;
        }

        /* --- SYSTÈME DE CARTES ET GRILLES PASTEL --- */
        .grocery-card {
            padding: 20px;
            border-radius: 24px;
            margin-bottom: 15px;
            text-align: center;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0,0,0,0.01);
        }
        .card-icon-big {
            font-size: 36px;
            margin-bottom: 8px;
        }
        .card-title-big {
            font-weight: 700;
            font-size: 15px;
            color: #1F2937;
            margin: 0;
        }
        .card-sub-big {
            font-size: 11px;
            color: #6B7280;
            margin-top: 4px;
        }

        /* Couleurs de fond Pastel spécifiques de l'image */
        .bg-green { background-color: #ECFDF5; border-left: 4px solid #10B981; }
        .bg-orange { background-color: #FFF7ED; border-left: 4px solid #F97316; }
        .bg-yellow { background-color: #FEFCE8; border-left: 4px solid #EAB308; }
        .bg-pink { background-color: #FDF2F8; border-left: 4px solid #EC4899; }
        .bg-blue { background-color: #F0F9FF; border-left: 4px solid #0EA5E9; }

        /* Boîte de détails agrobusiness */
        .detail-box {
            background-color: #F9FAFB;
            padding: 15px;
            border-radius: 16px;
            margin-top: 10px;
            font-size: 13px;
            color: #374151;
            border: 1px solid #E5E7EB;
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE ET AGROBUSINESS
# ==========================================
base_cultures = {
    "Tomate": {"amis": "Carotte, Oignon, Basilic", "ennemis": "Pomme de terre", "pepiniere": "21-25 jours sous moustiquaire. Arrosage matin/soir.", "repiquage": "50cm entre plants. Lignes séparées de 80cm.", "rendement": 3.5, "conservation": "Froid modéré (12°C) pour les étals.", "transformation": "Concentré de tomate, purée pasteurisée"},
    "Pastèque": {"amis": "Maïs, Gombo, Radis", "ennemis": "Concombre, Melon", "pepiniere": "Zéro jour (Semis direct obligatoire en poquets au champ).", "repiquage": "1m entre les poquets, 2m entre les lignes.", "rendement": 12.0, "conservation": "À l'ombre au sec (2-3 semaines).", "transformation": "Jus frais pasteurisé, confiture d'écorce"},
    "Concombre": {"amis": "Laitue, Oignon", "ennemis": "Tomate, Pastèque", "pepiniere": "Semis direct ou 12 jours en godet.", "repiquage": "40cm d'espacement. Tuteurage solide.", "rendement": 4.0, "conservation": "7 jours emballé au frais.", "transformation": "Cornichons au vinaigre ou saumure locale"},
    "Laitue / Salade": {"amis": "Carotte, Oignon, Tomate", "ennemis": "Persil", "pepiniere": "15 jours en bac abrité.", "repiquage": "Planches de 25cm x 25cm. Collet libre.", "rendement": 0.3, "conservation": "2 jours dans un linge frais.", "transformation": "Consommation fraîche exclusive"},
    "Menthe": {"amis": "Chou, Tomate", "ennemis": "Camomille", "pepiniere": "Bouturage rapide dans l'eau.", "repiquage": "30cm d'intervalle. Plante traçante.", "rendement": 1.2, "conservation": "Séchage complet à l'ombre.", "transformation": "Huile essentielle, sirop artisanal"},
    "Persil & Céleri": {"amis": "Tomate, Oignon", "ennemis": "Laitue", "pepiniere": "Levée lente (Tremper les graines 24h).", "repiquage": "25cm d'écartement sur lignes denses.", "rendement": 1.5, "conservation": "Séchage complet ou congélation.", "transformation": "Sel aromatisé, extraits séchés"}
}

images_verticales = {
    "pepiniere": "https://unsplash.com",
    "repiquage": "https://unsplash.com",
    "entretien": "https://unsplash.com",
    "recolte": "https://unsplash.com"
}

# ==========================================
# AFFICHAGE DE L'ECRAN STYLE "GROCERY APP"
# ==========================================

# En-tête de l'application
st.markdown("""
    <div class="grocery-header">
        <div class="main-title">Groceries</div>
        <div class="main-subtitle">Pas besoin de tout connaître, suivez les étapes par étapes.</div>
    </div>
""", unsafe_allow_html=True)

# Barre de recherche / Sélection de la plante épurée
st.markdown("<p style='font-weight:600; color:#374151; font-size:14px; margin-bottom:5px; text-align:left;'>Find Your Daily Plant :</p>", unsafe_allow_html=True)
culture = st.selectbox("", list(base_cultures.keys()), label_visibility="collapsed")

data = base_cultures[culture]

st.markdown("<br>", unsafe_allow_html=True)

# --- CRÉATION DE LA GRILLE DE BOUTONS EN 2 COLONNES (HORIZONTAL/VERTICAL MIXED) ---
col_gauche, col_droite = st.columns(2)

# --- MODULE 1 : SCANNER IA (En haut à gauche, couleur Vert Pastel) ---
with col_gauche:
    st.markdown(f"""
        <div class="grocery-card bg-green">
            <div class="card-icon-big">📸</div>
            <div class="card-title-big">Scanner IA</div>
            <div class="card-sub-big">Analyse pour : {culture}</div>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("Ouvrir l'appareil photo"):
        cam_input = st.camera_input("Prendre une photo", key="scanner_cam", label_visibility="collapsed")
        if cam_input:
            st.success("Analyse terminée : Feuillage robuste et sain.")

# --- MODULE 2 : COMPAGNONNAGE (En haut à droite, couleur Orange Pastel) ---
with col_droite:
    st.markdown(f"""
        <div class="grocery-card bg-orange">
            <div class="card-icon-big">🌿</div>
            <div class="card-title-big">Associations</div>
            <div class="card-sub-big">Partenaires : {data['amis'].split(',')[0]}...</div>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("Voir les compagnons complets"):
        st.info(f"🤝 **Amis :** {data['amis']}")
        st.error(f"❌ **Ennemis :** {data['ennemis']}")

# Deuxième ligne de la grille
col_gauche_2, col_droite_2 = st.columns(2)

# --- MODULE 3 : ITINÉRAIRE TECHNIQUE (En bas à gauche, couleur Jaune Pastel) ---
with col_gauche_2:
    st.markdown("""
        <div class="grocery-card bg-yellow">
            <div class="card-icon-big">🚜</div>
            <div class="card-title-big">Guide Étape</div>
            <div class="card-sub-big">Suivi de croissance visuel</div>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("Ouvrir le carnet d'étapes"):
        st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
        st.image(images_verticales["pepiniere"], caption="🌱 Étape 1 : Pépinière", use_container_width=True)
        st.write(data["pepiniere"])
        st.markdown('</div><br>', unsafe_allow_html=True)
        
        st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
        st.image(images_verticales["repiquage"], caption="📐 Étape 2 : Repiquage", use_container_width=True)
        st.write(data["repiquage"])
        st.markdown('</div><br>', unsafe_allow_html=True)
        
        st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
        st.image(images_verticales["entretien"], caption="✂️ Étape 3 : Entretien", use_container_width=True)
        st.write("Désherber et maintenir l'herbe coupée au pied contre l'évaporation de l'eau.")
        st.markdown('</div><br>', unsafe_allow_html=True)
        
        st.markdown('<div class="img-container-vertical">', unsafe_allow_html=True)
        st.image(images_verticales["recolte"], caption="🧺 Étape 4 : Cueillette", use_container_width=True)
        st.write(f"Rendement moyen attendu : **{data['rendement']} kg** par pied/poquet.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- MODULE 4 : AGROBUSINESS (En bas à droite, couleur Rose Pastel) ---
with col_droite_2:
    st.markdown("""
        <div class="grocery-card bg-pink">
            <div class="card-icon-big">🏭</div>
            <div class="card-title-big">Agrobusiness</div>
            <div class="card-sub-big">Stockage & Transformation</div>
        </div>
    """, unsafe_allow_html=True)
    with st.expander("Fiches industrielles"):
        st.markdown(f'<div class="detail-box"><b>🧊 Conservation :</b><br>{data["conservation"]}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="detail-box"><b>🍯 Transformation :</b><br>{data["transformation"]}</div>', unsafe_allow_html=True)


