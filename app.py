import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration Premium Mobile Allégée
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# Connexion sécurisée à l'IA Cloud Google
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw" 
if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    # Utilisation du nom de modèle officiel et stable exigé par l'API
    modele_ia = genai.GenerativeModel("models/gemini-1.5-flash")
else:
    modele_ia = None

# Styles graphiques professionnels Vert Nature Maquette UI
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header { background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px; color: white; text-align: center; margin-top: -60px; margin-bottom: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); }
        .category-card { background-color: #FFFFFF; padding: 15px; border-radius: 18px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04); margin-bottom: 15px; border-left: 6px solid #2CB674; }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Intelligence Artificielle de Précision Connectée</p></div>', unsafe_allow_html=True)

# Liste exhaustive des plantes maraîchères
liste_plantes = [
    "Tomate", "Pastèque", "Gombo", "Oignon", "Piment / Poivron", 
    "Concombre / Melon", "Chou", "Laitue / Salade", 
    "Carotte / Betterave", "Menthe", "Persil / Céleri", "Haricot vert / Niébé"
]

# Configuration des 5 Onglets de Navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📸 Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"])

# --- ONGLETS 1 : VRAI SCANNER IA ---
with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle')
    f_photo = st.file_uploader("Prendre ou charger une photo :", type=["jpg", "png", "jpeg"], key="cam_unique")
    if f_photo is not None:
        image_pil = Image.open(f_photo)
        st.image(image_pil, width=280)
        # Changement : L'analyse est strictement bloquée tant qu'on ne clique pas sur le bouton
        if st.button("🚀 LANCER L'ANALYSE AUTOMATIQUE", key="btn_scan_ia"):
            with st.spinner("L'IA examine vos cultures en direct..."):
                try:
                    consigne = "Analyse cette photo maraîchère africaine. Donne le NOM DE LA PLANTE, la MALADIE, les CAUSES et le TRAITEMENT NATUREL BIO."
                    reponse = modele_ia.generate_content([consigne, image_pil])
                    st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                    st.write(reponse.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Erreur d'analyse : {str(e)}")

# --- ONGLET 2 : ASSOCIATION DES PLANTES ---
with tab2:
    st.markdown('<div class="category-card"><h3>🌿 Compagnonnage & Associations</h3>Sélectionnez une plante pour interroger l\'IA sur ses partenaires de champ et ses ennemis.</div>', unsafe_allow_html=True)
    pl2 = st.selectbox("Sélectionnez la culture à associer :", liste_plantes, key="key_asso")
    # Changement : Verrouillage strict du bouton pour empêcher le plantage automatique au chargement
    if st.button("🔍 CONSULTER LES ASSOCIATIONS", key="btn_asso_ia"):
        with st.spinner("Recherche des affinités..."):
            try:
                prompt_asso = f"Donne les plantes amies (bonnes associations) et les plantes ennemies (à éviter à proximité) pour la culture de : {pl2} en Afrique de l'Ouest. Sois court et précis."
                reponse_asso = modele_ia.generate_content(prompt_asso)
                st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                st.write(reponse_asso.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur : {str(e)}")

# --- ONGLET 3 : SUIVI TECHNIQUE ET CYCLES ---
with tab3:
    st.markdown('<div class="category-card"><h3>🚜 Fiche Technique Évolutive</h3>Découvrez le processus complet de mise en place de votre plante.</div>', unsafe_allow_html=True)
    pl3 = st.selectbox("Sélectionnez la culture à étudier :", liste_plantes, key="key_cycle")
    if st.button("📋 AFFICHER LE PROCESSUS TECHNIQUE", key="btn_cycle_ia"):
        with st.spinner("Génération du calendrier cultural..."):
            try:
                prompt_cycle = f"Pour la culture de la plante '{pl3}', indique de manière structurée : 1. Si la PÉPINIÈRE est obligatoire ou s'il faut faire un SEMIS DIRECT au champ. 2. La durée totale du cycle. 3. Les besoins d'entretien (tuteurage, taille, paillage). Reste synthétique."
                reponse_cycle = modele_ia.generate_content(prompt_cycle)
                st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                st.write(reponse_cycle.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur : {str(e)}")

# --- ONGLET 4 : AGROBUSINESS ---
with tab4:
    st.markdown('<div class="category-card"><h3>🏭 Transformation & Conservation</h3>Apprenez à valoriser vos herbes aromatiques, fruits et racines pour maximiser vos gains.</div>', unsafe_allow_html=True)
    pl4 = st.selectbox("Sélectionnez la culture à valoriser :", liste_plantes, key="key_agro")
    if st.button("🏭 CONFIGURER LE PROJET AGROBUSINESS", key="btn_agro_ia"):
        with st.spinner("Calcul des méthodes agro-industrielles..."):
            try:
                prompt_agro = f"Pour la culture maraîchère de : {pl4}, décris brièvement : 1. Les meilleures méthodes de conservation (stockage au sec ou au frais). 2. Les procédés de transformation locale rentables (séchage en poudre, sirops, conserves, huiles)."
                reponse_agro = modele_ia.generate_content(prompt_agro)
                st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                st.write(reponse_agro.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur : {str(e)}")

# --- ONGLET 5 : BUDGET FINANCIER DYNAMIQUE ---
with tab5:
    st.markdown('<div class="category-card"><h3>💰 Simulateur de Profit & Business Plan</h3>Entrez vos données de terrain pour estimer vos revenus réels en FCFA.</div>', unsafe_allow_html=True)
    pl5 = st.selectbox("Sélectionnez la plante pour le calcul financier :", liste_plantes, key="key_budget")
    
    col1, col2 = st.columns(2)
    with col1:
        nbr_pieds = st.number_input("Nombre de poquets plantés :", min_value=1, value=500, step=50)
        prix_kilo = st.number_input("Prix au Kilo sur le marché (FCFA) :", min_value=50, value=400, step=25)
    with col2:
        total_charges = st.number_input("Total de vos dépenses engagées (FCFA) :", min_value=0, value=25000, step=1000)
    
    t1 = st.checkbox("Application d'un système de paillage complet (+30% rendement)")
    t2 = st.checkbox("Fertilisation organique via les fientes de votre poulailler (+30% rendement)")
    
    if st.button("💰 CALCULER LE RENDEMENT FINANCIER", key="btn_budget_ia"):
        bonus = 1.0
        if t1: bonus += 0.3
        if t2: bonus += 0.3
        with st.spinner("Calcul de la rentabilité..."):
            try:
                prompt_budget = f"Calcule le rendement moyen attendu en Kg pour {nbr_pieds} pieds de {pl5} en appliquant un bonus multiplicateur de fertilité de {bonus}. Multiplie ensuite ce poids par {prix_kilo} FCFA pour obtenir le Chiffre d'Affaires Brut. Soustrais {total_charges} FCFA de charges pour afficher clairement le BÉNÉFICE NET prévisionnel en gros caractères FCFA."
                reponse_budget = modele_ia.generate_content(prompt_budget)
                st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                st.write(reponse_budget.text)
                st.markdown('</div>', unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erreur : {str(e)}")
