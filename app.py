import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration de la page mobile Premium
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# ==========================================
# CONNEXION AU CERVEAU DE L'IA CLOUD (CORRECTION ERREUR 404)
# ==========================================
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw" 

if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    # Correction de l'erreur 404 : Retrait du préfixe "models/" pour s'adapter à la passerelle d'analyse
    modele_ia = genai.GenerativeModel("gemini-1.5-flash")
else:
    modele_ia = None

# Styles graphiques professionnels "Vert Nature"
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header {
            background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px;
            color: white; text-align: center; margin-top: -60px; margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Intelligence Artificielle connectée de terrain</p></div>', unsafe_allow_html=True)

# Base de données pour les onglets conseils
base_cultures = {
    "Tomate": {"famille": "Solanacées", "amis": "Carotte, Oignon, Laitue, Basilic", "ennemis": "Pomme de terre, Poivron"},
    "Pastèque": {"famille": "Cucurbitacées", "amis": "Maïs, Gombo, Tournesol", "ennemis": "Concombre, Melon"},
    "Concombre": {"famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon", "ennemis": "Tomate, Pastèque"}
}

# Navigation par onglets
onglets_list = ["📸 VRAI Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles"]
tab1, tab2, tab3 = st.tabs(onglets_list)

# --- ONGLET 1 : RECONNAISSANCE IA DYNAMIQUE ---
with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle Automatique')
    
    fichier_photo = st.file_uploader("Prendre ou charger une photo de votre culture :", type=["jpg", "png", "jpeg"], key="photo_unique_champ")
    
    if fichier_photo is not None:
        st.success("📊 Image reçue avec succès par le terminal.")
        
        # Ouverture immédiate de l'image réelle
        image_pil = Image.open(fichier_photo)
        st.markdown("##### 🎯 Image sélectionnée pour le scan :")
        
        # Correction de l'affichage de l'image (affiche l'image en entier sans la rogner ni l'étirer)
        st.image(image_pil, caption=f"Fichier actif : {fichier_photo.name}", use_container_width=False, width=300)
        
        # BOUTON DÉCLENCHEMENT DU SCANNER IA CONNECTÉ
        if st.button("🚀 LANCER L'ANALYSE AUTOMATIQUE PAR INTERNET", key="bouton_ia"):
            if modele_ia is None:
                st.error("Erreur de configuration : La connexion avec le serveur de vision Google n'est pas activée.")
            else:
                with st.spinner("L'IA Cloud analyse les formes, les couleurs et les symptômes de votre image..."):
                    try:
                        consigne_prompt = """
                        Agis en tant qu'expert en pathologie végétale et maraîchage d'Afrique de l'Ouest.
                        Analyse cette photo de culture maraîchère et fournis OBLIGATOIREMENT une réponse structurée en français exactement comme ceci :
                        
                        1. 🎯 NOM DE LA PLANTE : Dit précisément quelle plante ou fruits sont présents sur la photo (ex: Piment, Betterave, Tomate, Pastèque, feuille d'arbre fruiter).
                        2. 🦠 NOM DE LA MALADIE OU DU SYMPTÔME : Identifie précisément l'attaque visible, la pourriture, le champignon ou la carence.
                        3. ❓ CAUSES PROBABLES : Explique physiquement et environnementalement pourquoi ce problème est apparu sur l'exploitation.
                        4. 🍃 TRAITEMENT NATUREL ET PROTOCOLE (BIO) : Donne une recette claire à base de plantes locales (Neem, Ail, Cendre, Piment) ou bicarbonate pour soigner la plante.
                        5. 🧪 TRAITEMENT CHIMIQUE EN DERNIER RECOURS : Donne un produit chimique homologué pour le maraîchage avec ses consignes de sécurité et le Délai Avant Récolte (DAR).
                        """
                        
                        # Appel direct au modèle Gemini
                        reponse_ia = modele_ia.generate_content([consigne_prompt, image_pil])
                        
                        st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                        st.markdown("<h3 style='color:#0B4619; text-align:center;'>📋 RAPPORT DE DIAGNOSTIC AUTOMATIQUE CLOUD</h3>", unsafe_allow_html=True)
                        st.write(reponse_ia.text)
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error(f"Erreur lors de la connexion au serveur de vision : {str(e)}")

# --- ONGLET 2 : ASSOCIATIONS ---
with tab2:
    st.markdown('### 🌿 Association possible')
    choix_plante = st.selectbox("Sélectionnez une culture :", list(base_cultures.keys()), key="cat_sel")
    if choix_plante:
        c = base_cultures[choix_plante]
        st.success(f"✅ **Bonnes associations (Amis) :** {c['amis']}")
        st.error(f"❌ **À ÉVITER à proximité (Ennemis) :** {c['ennemis']}")

# --- ONGLET 3 : SUIVI CYCLES ---
with tab3:
    st.markdown('### 🚜 Étapes de Production')
    st.write("Suivi technique précis du calendrier cultural de la pépinière à la récolte.")
