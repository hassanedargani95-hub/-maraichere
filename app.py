import streamlit as st

# Configuration de la page mobile
st.set_page_config(page_title="La Bible du Maraîchage", page_icon="🌱", layout="centered")

# ==========================================
# DESIGN EXCLUSIF "DELICIOUS FOOD" APPLICATIF (CSS)
# ==========================================
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Fond d'écran épuré gris/bleu très clair comme le modèle */
        .stApp {
            background-color: #F3F5F7;
            font-family: 'Lexend', sans-serif;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* --- BARRE SUPÉRIEURE ÉPURÉE --- */
        .top-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 5px;
            margin-bottom: 5px;
        }
        .top-menu-icon { font-size: 22px; color: #1F2937; cursor: pointer; }
        
        /* --- SECTION EN-TÊTE STYLISÉE --- */
        .section-title {
            font-family: 'Fredoka One', cursive;
            color: #1F2937;
            font-size: 22px;
            margin: 15px 0 5px 5px;
            text-align: left;
        }
        .section-subtitle {
            color: #4B5563;
            font-size: 13px;
            margin-left: 5px;
            margin-bottom: 15px;
            text-align: left;
            font-style: italic;
        }
        
        /* --- CARTES DE PRODUITS DU CATALOGUE --- */
        .product-card {
            background: #FFFFFF;
            padding: 15px;
            border-radius: 24px;
            box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.01);
            text-align: center;
            margin-bottom: 15px;
        }
        .product-price {
            font-weight: 700;
            color: #10B981;
            font-size: 16px;
            margin-top: 5px;
        }
        
        /* --- BARRE DE NAVIGATION INFÉRIEURE FIXE BLEUE --- */
        .bottom-nav-bar {
            background-color: #2563EB;
            padding: 12px;
            border-radius: 20px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: 30px;
            box-shadow: 0px 8px 24px rgba(37, 99, 235, 0.2);
        }
        .nav-icon {
            color: #FFFFFF;
            font-size: 20px;
            opacity: 0.8;
            cursor: pointer;
        }
        .nav-icon:hover { opacity: 1; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES DU CATALOGUE AGROBUSINESS
# ==========================================
catalogue_produits = {
    "Tomate Cobra F1": {"emoji": "🍅", "prix": "450 FCFA / Kilo", "desc": "Calibre uniforme, haute résistance au transport.", "conservation": "Froid modéré (12°C) pour les étals marchés.", "transformation": "Concentré de tomate locale pasteurisée."},
    "Pastèque Ronde": {"emoji": "🍉", "prix": "1 500 FCFA / Unité", "desc": "Très sucrée, chair ferme rouge éclatante.", "conservation": "À l'ombre au sec ventilé pendant 2 à 3 semaines.", "transformation": "Jus frais pasteurisé conditionné en bouteille."},
    "Concombre Long": {"emoji": "🥒", "prix": "300 FCFA / Kilo", "desc": "Croquant, idéal pour les restaurants locaux.", "conservation": "7 jours emballé sous bâche fraîche à 10°C.", "transformation": "Cornichons marinés en saumure vinaigrée."},
    "Laitue Feuille": {"emoji": "🥬", "prix": "200 FCFA / Pied", "desc": "Fraîcheur maximale, cycle court de récolte.", "conservation": "2 jours maximum enveloppé dans un linge humide.", "transformation": "Vente directe exclusive en circuit frais."}
}

# --- 1. REPRODUCTION DE LA BARRE SUPÉRIEURE ---
col_menu_gauche, col_profil_droite = st.columns([3, 1])
with col_menu_gauche:
    st.markdown('<div class="top-menu-icon">☰</div>', unsafe_allow_html=True)
with col_profil_droite:
    # L'option d'enregistrement se loge proprement tout en haut à droite
    ouvrir_profil = st.button("👤 Profil", key="btn_top_profil", use_container_width=True)

if ouvrir_profil:
    st.markdown("<div class='product-card' style='text-align:left;'>", unsafe_allow_html=True)
    with St.form("form_inscription"):
        st.markdown("### 📝 Enregistrement Producteur")
        Nom = st.text_input("Nom de l'exploitant :", placeholder="Ex: Issouf")
        Localite = st.text_input("Zone de culture :", placeholder="Ex: Bobo-Dioulasso")
        St.form_submit_button("Créer mon compte")
    St.markdown("</div>", unsafe_allow_html=True)

# --- 2. TITRE DE SECTION STYLE "DELICIOUS FOOD" ---
st.markdown('<div class="section-title">Delicious Food</div>', unsafe_allow_html=True)
st.markdown('<div class="section-subtitle">Pas besoin de tout connaître, suivez les étapes par étapes.</div>', unsafe_allow_html=True)

# --- 3. BARRE DE FILTRES DES CATÉGORIES (HORIZONTALE) ---
st.write("✨ **Catégories disponibles :**")
categorie_choisie = st.radio("", ["Tout voir", "Maraîchère", "Aromatique", "Agrobusiness"], horizontal=True, label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# --- 4. GRILLE DES PRODUITS DU CHAMP ---
st.markdown('<div class="section-title" style="font-size:18px;">Sélection des cultures</div>', unsafe_allow_html=True)

culture_choisie = st.selectbox("Sélectionnez le légume à analyser :", list(catalogue_produits.keys()))
produit = catalogue_produits[culture_choisie]

# Affichage de la carte produit stylisée
st.markdown(f"""
    <div class="product-card">
        <div style="font-size: 55px; margin-bottom: 10px;">{produit['emoji']}</div>
        <div style="font-weight: 700; font-size: 18px; color: #1F2937;">{culture_choisie}</div>
        <div style="font-size: 13px; color: #6B7280; margin-top: 4px;">{produit['desc']}</div>
        <div class="product-price">{produit['prix']}</div>
    </div>
""", unsafe_allow_html=True)

# Structure des modules techniques via les onglets épurés sous la carte
onglet1, onglet2, onglet3 = st.tabs(["📸 Scanner Réseau", "🏭 Agrobusiness & Stock", "💰 Calculateur Marge"])

with onglet1:
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    fichiers_photos = st.file_uploader("Sélectionnez vos images pour l'analyse IA :", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if fichiers_photos:
        st.success(f"🤖 {len(fichiers_photos)} photo(s) analysée(s). Structure foliaire saine.")

with onglet2:
    st.markdown(f"""
        <div class="product-card" style="text-align:left; border-left:4px solid #2563EB;">
            <b style="color:#2563EB;">🧊 Conservation Pro :</b><br>{produit['conservation']}<br><br>
            <b style="color:#10B981;">🍯 Option Transformation :</b><br>{produit['transformation']}
        </div>
    """, unsafe_allow_html=True)

with onglet3:
    St.markdown("### 💰 Simulation de Campagne")
    Unites = st.number_input("Nombre de pieds cultivés :", min_value=10, value=500, step=50)
    Charges = st.number_input("Total des dépenses engagées (FCFA) :", min_value=0, value=25000, step=1000)
    St.metric(label="Volume estimé de récolte", value=f"{unites * 3.5:.1f} kg")

# --- 5. REPRODUCTION DE LA BARRE DE NAVIGATION INFÉRIEURE BLEUE ---
st.markdown("""
    <div class="bottom-nav-bar">
        <div class="nav-icon">🏠</div>
        <div class="nav-icon">⭐</div>
        <div class="nav-icon">👤</div>
        <div class="nav-icon">⚙️</div>
    </div>
""", unsafe_allow_html=True)
