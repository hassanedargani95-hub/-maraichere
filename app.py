import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration de la page mobile
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# Connection IA Cloud
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw"
if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    modele_ia = genai.GenerativeModel("gemini-1.5-flash")
else:
    modele_ia = None

# Design UI Vert Nature
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header { background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px; color: white; text-align: center; margin-top: -60px; margin-bottom: 20px; }
        .category-card { background-color: #FFFFFF; padding: 15px; border-radius: 18px; margin-bottom: 15px; border-left: 6px solid #2CB674; }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>IA connectée de terrain</p></div>', unsafe_allow_html=True)

# Base de données exhaustive des plantes maraîchères
base_encyclopedie = {
    "Tomate": {"famille": "Solanacées", "amis": "Carotte, Oignon, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron", "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (21-25 jours)", "cycle": "75 à 90 jours", "entretien": "Tuteurage, taille des gourmands, paillage."},
    "Pastèque": {"famille": "Cucurbitacées", "amis": "Maïs, Gombo, Tournesol", "ennemis": "Concombre, Melon", "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "80 à 95 jours", "entretien": "Buttes plates en travers de la pente, pincer la tige après la 4e feuille."},
    "Gombo": {"famille": "Malvacées", "amis": "Piment, Aubergine, Pastèque", "ennemis": "Oignon, Tomate", "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "55 à 65 jours", "entretien": "Buttage des pieds après un mois, cueillette tous les 2 jours."},
    "Oignon": {"famille": "Alliacées", "amis": "Carotte, Laitue, Tomate", "ennemis": "Gombo, Haricot", "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (45-50 jours)", "cycle": "100 à 120 days", "entretien": "Désherbage fréquent, habillage des plants au repiquage."},
    "Piment / Poivron": {"famille": "Solanacées", "amis": "Oignon, Ail, Gombo", "ennemis": "Tomate, Aubergine", "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (25-30 jours)", "cycle": "80 à 100 jours", "entretien": "Apport de cendre (potassium) à la floraison, paillage protecteur."},
    "Concombre / Melon / Courgette": {"famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon", "ennemis": "Tomate, Pastèque", "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "50 à 65 jours", "entretien": "Arrosage abondant et régulier au pied pour éviter l'amertume."},
    "Chou (Pommé / de Chine)": {"famille": "Brassicacées", "amis": "Laitue, Oignon, Céleri", "ennemis": "Ail, Fraise", "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (30 jours)", "cycle": "85 à 105 jours", "entretien": "Forte demande en azote (fientes sèches), filet anti-chenilles."},
    "Laitue / Salade / Amarante": {"famille": "Astéracées", "amis": "Chou, Carotte, Tomate", "ennemis": "Persil, Céleri", "methode": "🌱 PÉPINIÈRE OU SEMIS EN LIGNE", "cycle": "30 à 45 jours", "entretien": "Sarclage délicat, arrosage fin, récolte tôt le matin à la fraîche."},
    "Carotte / Betterave / Radis": {"famille": "Apiacées", "amis": "Oignon, Laitue, Tomate", "ennemis": "Aneth, Fenouil", "methode": "🎯 SEMIS DIRECT EN LIGNES SERRÉES", "cycle": "70 à 90 jours", "entretien": "Éclaircissage à 5 cm, exige un sol profondément meuble et sans cailloux."},
    "Menthe / Persil / Céleri": {"famille": "Lamiacées & Apiacées", "amis": "Tomate, Chou, Oignon", "ennemis": "Salade", "methode": "🌱 PÉPINIÈRE OU BOUTURAGE", "cycle": "Récolte continue dès le 60e jour", "entretien": "Arrosage régulier, parfait pour le séchage agrobusiness."},
    "Haricot vert / Niébé": {"famille": "Fabacées", "amis": "Maïs, Tomate, Aubergine", "ennemis": "Oignon, Ail", "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "45 à 60 jours", "entretien": "Binage léger. Capte l'azote de l'air pour fertiliser naturellement le sol."}
}

# Navigation par Onglets
tab1, tab2, tab3 = st.tabs(["📸 Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles"])

with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle')
    f_photo = st.file_uploader("Prendre ou charger une photo :", type=["jpg", "png", "jpeg"], key="cam")
    if f_photo is not None:
        image_pil = Image.open(f_photo)
        st.image(image_pil, width=280)
        if st.button("🚀 LANCER L'ANALYSE EN DIRECT"):
            consigne = "Analyse cette photo maraîchère. Donne le NOM DE LA PLANTE, la MALADIE, les CAUSES et le TRAITEMENT NATUREL BIO."
            reponse = modele_ia.generate_content([consigne, image_pil])
            st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
            st.write(reponse.text)
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="category-card"><h3>🌿 Association Possible</h3>Sélectionnez votre culture.</div>', unsafe_allow_html=True)
    pl2 = st.selectbox("Plante :", list(base_encyclopedie.keys()), key="p2")
    if pl2:
        st.success(f"✅ **Amis :** {base_encyclopedie[pl2]['amis']}")
        st.error(f"❌ **Ennemis :** {base_encyclopedie[pl2]['ennemis']}")

with tab3:
    st.markdown('<div class="category-card"><h3>🚜 Suivi Technique Évolutif</h3>Découvrez le processus d\'installation.</div>', unsafe_allow_html=True)
    pl3 = st.selectbox("Plante :", list(base_encyclopedie.keys()), key="p3")
    if pl3:
        st.info(f"📋 **Méthode d'installation :** {base_encyclopedie[pl3]['methode']}")
        st.write(f"⏳ **Temps / Cycle total :** {base_encyclopedie[pl3]['cycle']}")
        st.write(f"✂️ **Entretien obligatoire :** {base_encyclopedie[pl3]['entretien']}")
