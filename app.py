import streamlit as st
import pandas as pd

# Configuration de la page mobile
st.set_page_config(page_title="La Bible de la Maraîchère Culture", page_icon="🌱", layout="centered")

# INITIALISATION DE LA BASE DE DONNÉES DES INSCRITS AVEC VOS 6 CRITÈRES
if "liste_inscrits" not in st.session_state:
    st.session_state["liste_inscrits"] = [
        {
            "Nom": "DARGANI", 
            "Prénom": "Hassane", 
            "Numéro téléphone": "+226 00 00 00 00", 
            "Mail": "hassane@example.com", 
            "Production": "Tomate & Pastèque", 
            "Localité": "Bobo-Dioulasso"
        }
    ]

# ==========================================
# DESIGN CONFIGURATION ET ADAPTATION (CSS)
# ==========================================
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        .block-container {
            padding-top: 5px !important;
            padding-bottom: 10px !important;
        }
        
        .stApp {
            background-color: #F3F5F7;
            font-family: 'Lexend', sans-serif;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .top-navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 5px 0px;
        }
        .top-menu-icon { font-size: 22px; color: #1F2937; }
        
        /* --- CADRE PROFESSIONNEL DU TITRE DE L'APPLICATION --- */
        .app-title-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 24px;
            box-shadow: 0px 8px 24px rgba(16, 185, 129, 0.06);
            border: 1px solid rgba(16, 185, 129, 0.1);
            text-align: center;
            margin-top: 10px;
            margin-bottom: 15px;
        }
        .app-main-title {
            font-family: 'Fredoka One', cursive;
            color: #10B981 !important;
            font-size: 23px;
            margin: 0;
        }
        .app-main-subtitle {
            color: #6B7280;
            font-size: 12px;
            margin-top: 6px;
            font-style: italic;
        }
        
        /* --- CARTES ET FORMULAIRES --- */
        .product-card {
            background: #FFFFFF;
            padding: 18px;
            border-radius: 24px;
            box-shadow: 0px 6px 18px rgba(0, 0, 0, 0.01);
            border: 1px solid rgba(0, 0, 0, 0.01);
            margin-bottom: 12px;
        }
        .form-title {
            font-weight: 700;
            color: #1F2937;
            font-size: 16px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .product-price {
            font-weight: 700;
            color: #10B981;
            font-size: 16px;
            margin-top: 5px;
        }
        
        /* --- BARRE BLEUE EN BAS --- */
        .bottom-nav-bar {
            background-color: #2563EB;
            padding: 12px;
            border-radius: 20px;
            display: flex;
            justify-content: space-around;
            align-items: center;
            margin-top: 20px;
        }
        .nav-icon { color: #FFFFFF; font-size: 20px; opacity: 0.8; }
    </style>
""", unsafe_allow_html=True)

# --- 1. BARRE SUPÉRIEURE ---
col_menu_gauche, col_profil_droite = st.columns(2)
with col_menu_gauche:
    st.markdown('<div class="top-menu-icon">☰</div>', unsafe_allow_html=True)
with col_profil_droite:
    ouvrir_profil = st.button("👤 Profil", key="btn_top_profil", use_container_width=True)

# Formulaire d'enregistrement structuré selon vos 6 demandes
if ouvrir_profil:
    st.markdown("<div class='product-card'>", unsafe_allow_html=True)
    st.markdown('<div class="form-title">📝 Enregistrement Exploitant</div>', unsafe_allow_html=True)
    
    with st.form("form_inscription", clear_on_submit=True):
        ins_nom = st.text_input("Nom :", placeholder="Dargani")
        ins_prenom = st.text_input("Prénom :", placeholder="Hassane")
        ins_tel = st.text_input("Numéro téléphone :", placeholder="+226 ...")
        ins_mail = st.text_input("Mail :", placeholder="exemple@mail.com")
        ins_prod = st.text_input("Production :", placeholder="Tomate, Pastèque, Oignon...")
        ins_localite = st.text_input("Localité :", placeholder="Bobo-Dioulasso")
        
        bouton_valider = st.form_submit_button("Créer mon compte")
        
        if bouton_valider and ins_nom and ins_prenom:
            st.session_state["liste_inscrits"].append({
                "Nom": ins_nom.upper(),
                "Prénom": ins_prenom.title(),
                "Numéro téléphone": ins_tel,
                "Mail": ins_mail,
                "Production": ins_prod,
                "Localité": ins_localite
            })
            st.success(f"Compte créé avec succès pour {ins_prenom} {ins_nom} !")
    st.markdown("</div>", unsafe_allow_html=True)

# --- 2. CADRE DU TITRE ---
st.markdown("""
    <div class="app-title-card">
        <div class="app-main-title">La Bible de la Maraîchère Culture</div>
        <div class="app-main-subtitle">Pas besoin de tout connaître, suivez les étapes par étapes.</div>
    </div>
""", unsafe_allow_html=True)

# --- 3. CATALOGUE MARAÎCHER ---
catalogue_produits = {
    "Tomate Cobra F1": {"emoji": "🍅", "prix": "450 FCFA / Kilo", "desc": "Calibre uniforme, haute résistance au transport.", "conservation": "Froid modéré (12°C) pour les étals marchés.", "transformation": "Concentré de tomate locale pasteurisée."},
    "Pastèque Ronde": {"emoji": "🍉", "prix": "1 500 FCFA / Unité", "desc": "Très sucrée, chair ferme rouge éclatante.", "conservation": "À l'ombre au sec ventilé pendant 2 à 3 semaines.", "transformation": "Jus frais pasteurisé conditionné en bouteille."},
    "Concombre Long": {"emoji": "🥒", "prix": "300 FCFA / Kilo", "desc": "Croquant, idéal pour les restaurants locaux.", "conservation": "7 jours emballé sous bâche fraîche à 10°C.", "transformation": "Cornichons marinés en saumure vinaigrée."},
    "Laitue Feuille": {"emoji": "🥬", "prix": "200 FCFA / Pied", "desc": "Fraîcheur maximale, cycle court de récolte.", "conservation": "2 jours maximum enveloppé dans un linge humide.", "transformation": "Vente directe exclusive en circuit frais."}
}

st.markdown("<p style='font-weight:600; color:#1F2937; font-size:13px; margin-bottom:5px;'>Sélectionnez le légume à analyser :</p>", unsafe_allow_html=True)
culture_choisie = st.selectbox("", list(catalogue_produits.keys()), label_visibility="collapsed")
produit = catalogue_produits[culture_choisie]

st.markdown(f"""
    <div class="product-card">
        <div style="font-size: 45px; margin-bottom: 5px;">{produit['emoji']}</div>
        <div style="font-weight: 700; font-size: 16px; color: #1F2937;">{culture_choisie}</div>
        <div style="font-size: 12px; color: #6B7280; margin-top: 2px;">{produit['desc']}</div>
        <div class="product-price">{produit['prix']}</div>
    </div>
""", unsafe_allow_html=True)

# Navigation
onglet1, onglet2, onglet3 = st.tabs(["📸 Scanner", "🏭 Agrobusiness", "💰 Simulateur"])

with onglet1:
    st.markdown("<div style='margin-top:5px;'></div>", unsafe_allow_html=True)
    fichiers_photos = st.file_uploader("Sélectionnez vos images pour l'analyse IA :", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    if fichiers_photos:
        st.success(f"🤖 {len(fichiers_photos)} photo(s) reçue(s).")

with onglet2:
    st.markdown(f"""
        <div class="product-card" style="text-align:left; border-left:4px solid #2563EB; margin-top:10px; font-size:13px;">
            <b style="color:#2563EB;">🧊 Conservation :</b> {produit['conservation']}<br><br>
            <b style="color:#10B981;">🍯 Transformation :</b> {produit['transformation']}
        </div>
    """, unsafe_allow_html=True)

with onglet3:
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    unites = st.number_input("Nombre de pieds cultivés :", min_value=10, value=500, step=50)
    st.metric(label="Volume estimé de récolte", value=f"{unites * 3.5:.1f} kg")

# --- 4. PANNEAU DE CONTRÔLE AVEC VOS 6 PARAMÈTRES (HD) ---
st.markdown("---")
st.markdown("<p style='font-size:11px; color:#9CA3AF; text-align:center;'>🔒 Zone Réservée Direction (HD)</p>", unsafe_allow_html=True)
check_admin = st.checkbox("Accéder à la liste des inscrits au champ", key="admin_panel")

if check_admin:
    st.markdown("<div class='product-card' style='text-align:left;'>", unsafe_allow_html=True)
    st.markdown("### 📋 Liste des producteurs enregistrés")
    df_producteurs = pd.DataFrame(st.session_state["liste_inscrits"])
    # Réorganisation précise des colonnes demandées
    df_producteurs = df_producteurs[["Nom", "Prénom", "Numéro téléphone", "Mail", "Production", "Localité"]]
    st.dataframe(df_producteurs, use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Barre en bas
st.markdown("""
    <div class="bottom-nav-bar">
        <div class="nav-icon">🏠</div>
        <div class="nav-icon">⭐</div>
        <div class="nav-icon">👤</div>
        <div class="nav-icon">⚙️</div>
    </div>
""", unsafe_allow_html=True)
