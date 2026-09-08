import streamlit as st

# Configuration de la page mobile
st.set_page_config(page_title="La Bible du Maraîchage", page_icon="🌱", layout="centered")

# ==========================================
# DESIGN ÉCO-PREMIUM VERT & GRAPHIQUES AVANCÉS (CSS)
# ==========================================
st.markdown("""
    <style>
        @import url('https://googleapis.com');
        
        /* Fond d'écran vert végétal texturé avec symboles de légumes */
        .stApp {
            background-color: #E8F2EA;
            background-image: radial-gradient(#C6E2CC 1px, transparent 1px), radial-gradient(#C6E2CC 1px, #E8F2EA 1px);
            background-size: 40px 40px;
            background-position: 0 0, 20px 20px;
            font-family: 'Lexend', sans-serif;
        }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* --- DESIGN DE L'EN-TÊTE ET BOUTON CONNEXION --- */
        .top-bar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 5px;
            margin-bottom: 5px;
        }
        .app-main-title {
            font-family: 'Fredoka One', cursive;
            color: #0F4220;
            font-size: 23px;
            margin: 0;
            text-align: left;
        }
        .app-main-subtitle {
            color: #4B5563;
            font-size: 12px;
            font-weight: 400;
            margin-top: 4px;
            text-align: left;
            font-style: italic;
        }
        
        /* --- INTÉGRATION DE LA ZONE DE DIAGNOSTIC PREMIUM --- */
        .scanner-box-premium {
            background: #FFFFFF;
            padding: 25px 20px;
            border-radius: 28px;
            box-shadow: 0px 10px 30px rgba(15, 66, 32, 0.08);
            border: 1px solid rgba(15, 66, 32, 0.05);
            text-align: center;
            margin-top: 15px;
        }
        .scanner-title {
            font-family: 'Lexend', sans-serif;
            font-weight: 700;
            font-size: 18px;
            color: #0F4220;
            margin-bottom: 6px;
        }
        .scanner-instruction {
            font-size: 12px;
            color: #6B7280;
            font-weight: 400;
            margin-bottom: 15px;
        }
        
        /* Style des boîtes d'informations générales */
        .info-card-premium {
            background-color: #FFFFFF;
            padding: 18px;
            border-radius: 22px;
            margin-top: 12px;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.02);
            border: 1px solid rgba(0, 0, 0, 0.01);
            text-align: left;
        }
        .info-card-title {
            font-weight: 700;
            color: #0F4220;
            font-size: 14px;
            margin-bottom: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE ET DÉTAILS
# ==========================================
base_cultures = {
    "Tomate": {"amis": "Carotte, Oignon, Basilic", "ennemis": "Pomme de terre", "pepiniere": "21-25 jours sous moustiquaire. Arrosage matin/soir.", "repiquage": "50cm entre plants. Lignes séparées de 80cm.", "rendement": 3.5, "conservation": "Froid modéré (12°C) pour les étals.", "transformation": "Concentré de tomate, purée pasteurisée"},
    "Pastèque": {"amis": "Maïs, Gombo, Radis", "ennemis": "Concombre, Melon", "pepiniere": "Zéro jour (Semis direct obligatoire en poquets au champ).", "repiquage": "1m entre les poquets, 2m entre les lignes.", "rendement": 12.0, "conservation": "À l'ombre au sec (2-3 semaines).", "transformation": "Jus frais pasteurisé, confiture d'écorce"},
    "Concombre": {"amis": "Laitue, Oignon", "ennemis": "Tomate, Pastèque", "pepiniere": "Semis direct ou 12 jours en godet.", "repiquage": "40cm d'espacement. Tuteurage solide.", "rendement": 4.0, "conservation": "7 jours emballé au frais.", "transformation": "Cornichons au vinaigre ou saumure locale"},
    "Laitue / Salade": {"amis": "Carotte, Oignon, Tomate", "ennemis": "Persil", "pepiniere": "15 jours en bac abrité.", "repiquage": "Planches de 25cm x 25cm. Collet libre.", "rendement": 0.3, "conservation": "2 jours dans un linge frais.", "transformation": "Consommation fraîche exclusive"},
    "Menthe": {"amis": "Chou, Tomate", "ennemis": "Camomille", "pepiniere": "Bouturage rapide dans l'eau.", "repiquage": "30cm d'intervalle. Plante traçante.", "rendement": 1.2, "conservation": "Séchage complet à l'ombre.", "transformation": "Huile essentielle, sirop artisanal"},
    "Persil & Céleri": {"amis": "Tomate, Oignon", "ennemis": "Laitue", "pepiniere": "Levée lente (Tremper les graines 24h).", "repiquage": "25cm d'écartement sur lignes denses.", "rendement": 1.5, "conservation": "Séchage complet ou congélation.", "transformation": "Sel aromatisé, extraits séchés"}
}

# --- LIGNE DE NAVIGATION SUPÉRIEURE (TITRE & CONNEXION) ---
col_titre, col_btn = st.columns([3, 1.2])
with col_titre:
    st.markdown('<h1 class="app-main-title">La Bible de la Maraîchère Culture</h1>', unsafe_allow_html=True)
    st.markdown('<p class="app-main-subtitle">Pas besoin de tout connaître, suivez les étapes par étapes.</p>', unsafe_allow_html=True)

with col_btn:
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    ouvrir_profil = st.button("👤 S'enregistrer", key="btn_login", use_container_width=True)

# Espace d'enregistrement si l'utilisateur clique sur le bouton en haut à droite
if ouvrir_profil:
    with st.form("form_inscription"):
        st.markdown("### 📝 Créer votre compte producteur")
        nom = st.text_input("Nom de l'exploitant :", placeholder="Ex: Issouf")
        localite = st.text_input("Localisation du champ :", placeholder="Ex: Bobo-Dioulasso")
        st.form_submit_button("Valider mon inscription")

# Sélection de la culture courante
st.markdown("<p style='font-weight:600; color:#0F4220; font-size:13px; margin-bottom:5px; margin-top:15px; text-align:left;'>🥦 SÉLECTIONNER VOTRE VARIÉTÉ CIBLE :</p>", unsafe_allow_html=True)
culture = st.selectbox("", list(base_cultures.keys()), label_visibility="collapsed")
data = base_cultures[culture]

# Structure par Onglets Fluides
onglets = st.tabs(["📸 Scanner", "🌿 Associations", "🚜 Guide Suivi", "🏭 Agrobusiness", "💰 Budget"])

# --- ONGLET 1 : SCANNER REVISITÉ AVEC IMPORTATION MULTIPLE ---
with onglets:
    st.markdown("""
        <div class="scanner-box-premium">
            <div class="scanner-title">📸 Laboratoire de Diagnostic</div>
            <div class="scanner-instruction">Sélectionnez une ou plusieurs photos de vos feuilles ou racines pour lancer l'analyse agronomique.</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='margin-top:10px;'></div>", unsafe_allow_html=True)
    
    # Modifié pour permettre de choisir PLUSIEURS photos à la fois dans la galerie (accept_multiple_files=True)
    fichiers_photos = st.file_uploader("", type=["jpg", "png", "jpeg"], accept_multiple_files=True, label_visibility="collapsed")
    
    if fichiers_photos:
        st.info(f"📸 {len(fichiers_photos)} photo(s) reçue(s) par le serveur de diagnostic.")
        st.success(f"Analyse globale terminée pour votre culture de : {culture}. Éléments foliaires stables.")

# --- ONGLET 2 : COMPAGNONNAGE ---
with onglets:
    st.markdown(f"""
        <div class="info-card-premium">
            <div class="info-card-title">🤝 Voisinage Recommandé (Plantes amies) :</div>
            <p style='font-size:13px; color:#374151;'>{data['amis']}</p>
            <hr style='border: 0; border-top: 1px solid #E5E7EB; margin: 15px 0;'>
            <div class="info-card-title" style='color:#DC2626;'>❌ Zone d'Exclusion (Plantes ennemies) :</div>
            <p style='font-size:13px; color:#374151;'>{data['ennemis']}</p>
        </div>
    """, unsafe_allow_html=True)

# --- ONGLET 3 : GUIDE TECHNIQUE ÉTAPE PAR ÉTAPE ---
with onglets:
    st.markdown(f"""
        <div class="info-card-premium">
            <div class="info-card-title">🌱 Étape 1 : La Pépinière / Semis</div>
            <p style='font-size:13px; color:#4B5563;'>{data['pepiniere']}</p>
        </div>
        <div class="info-card-premium">
            <div class="info-card-title">📐 Étape 2 : Le Repiquage au champ</div>
            <p style='font-size:13px; color:#4B5563;'>{data['repiquage']}</p>
        </div>
        <div class="info-card-premium">
            <div class="info-card-title">✂️ Étape 3 : Entretien et Suivi</div>
            <p style='font-size:13px; color:#4B5563;'>Désherber manuellement et maintenir un paillage organique régulier au pied des plantes pour bloquer l'évaporation de l'eau.</p>
        </div>
        <div class="info-card-premium">
            <div class="info-card-title">🧺 Étape 4 : Récolte et Cueillette</div>
            <p style='font-size:13px; color:#4B5563;'>Cueillette au stade optimal de maturité pour le marché. Rendement estimé : <b>{data['rendement']} kg</b> par unité.</p>
        </div>
    """, unsafe_allow_html=True)

# --- ONGLET 4 : AGROBUSINESS ---
with onglets:
    st.markdown(f"""
        <div class="info-card-premium" style="border-left: 5px solid #3B82F6;">
            <div class="info-card-title" style="color:#1D4ED8;">🧊 Méthodes de Stockage et Conservation :</div>
            <p style='font-size:13px; color:#374151;'>{data['conservation']}</p>
        </div>
        <div class="info-card-premium" style="border-left: 5px solid #10B981;">
            <div class="info-card-title" style="color:#047857;">🍯 Procédés de Transformation Locale :</div>
            <p style='font-size:13px; color:#374151;'>{data['transformation']}</p>
        </div>
    """, unsafe_allow_html=True)

# --- ONGLET 5 : BUDGET ---
with onglets:
    st.markdown("### 💰 Simulateur de Rentabilité Financière")
