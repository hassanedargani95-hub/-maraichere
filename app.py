import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration de la page mobile Premium Haute Performance
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# Connexion sécurisée à l'IA Cloud Google
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw"
if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    modele_ia = genai.GenerativeModel("gemini-1.5-flash")
else:
    modele_ia = None

# Design UI Vert Nature Prestige
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header { background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px; color: white; text-align: center; margin-top: -60px; margin-bottom: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); }
        .category-card { background-color: #FFFFFF; padding: 15px; border-radius: 18px; margin-bottom: 15px; border-left: 6px solid #2CB674; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04); }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
        .badge-biz { background-color: #E6F7ED; color: #1E5631; padding: 8px; border-radius: 10px; font-weight: bold; border: 1px solid #2CB674; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>IA connectée et Agrobusiness de terrain</p></div>', unsafe_allow_html=True)

# Base de données encyclopédique et financière exhaustive
base_encyclopedie = {
    "Tomate": {
        "famille": "Solanacées", "amis": "Carotte, Oignon, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron, Aubergine", 
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (21-25 jours)", "cycle": "75 à 90 jours après repiquage", 
        "entretien": "Tuteurage, paillage du sol, taille obligatoire des gourmands aux aisselles.",
        "conservation": "Froid modéré (12°C) pour le frais. Séchage au soleil des tranches pour la longue conservation.",
        "transformation": "Concentré de tomate en boîte, purée pasteurisée artisanale en bouteilles de verre.", "rendement_base": 3.5
    },
    "Pastèque": {
        "famille": "Cucurbitacées", "amis": "Maïs (brise-vent), Gombo, Tournesol, Radis", "ennemis": "Concombre, Melon, Courgette", 
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "80 à 95 jours après semis", 
        "entretien": "Buttes plates en travers de la pente, pincer la tige après la 4e feuille pour calibrer les fruits.",
        "conservation": "Se conserve 2 à 3 semaines à l'ombre dans un abri sec, ventilé et frais.",
        "transformation": "Jus frais pasteurisé conditionné en bouteilles, confiture d'écorces, extraction d'huile des graines séchées.", "rendement_base": 12.0
    },
    "Gombo": {
        "famille": "Malvacées", "amis": "Piment, Aubergine, Niébé, Pastèque", "ennemis": "Oignon, Tomate", 
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "55 à 65 jours", 
        "entretien": "Buttage des pieds à la houe après un mois pour renforcer l'ancrage face au vent fort.",
        "conservation": "Très fragile. Conserver au frais enveloppé 3 à 5 jours maximum.",
        "transformation": "Séchage solaire et broyage des rondelles pour obtenir de la poudre de gombo longue conservation.", "rendement_base": 1.8
    },
    "Oignon": {
        "famille": "Alliacées", "amis": "Carotte, Laitue, Tomate, Piment", "ennemis": "Gombo, Haricot, Pois", 
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (45-50 jours)", "cycle": "100 à 120 jours après repiquage", 
        "entretien": "Désherbage manuel fréquent, habillage des plants (taille des feuilles et racines) au repiquage.",
        "conservation": "Séchage complet du feuillage sur le champ (ressuyage), puis stockage des bulbes suspendus au sec (6 mois).",
        "transformation": "Séchage de lamelles d'oignons en poudre, confit d'oignon pour la restauration.", "rendement_base": 2.5
    },
    "Piment / Poivron": {
        "famille": "Solanacées", "amis": "Oignon, Ail, Gombo, Carotte", "ennemis": "Tomate, Aubergine", 
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (25-30 jours)", "cycle": "80 à 100 jours après repiquage", 
        "entretien": "Apport massif de potassium (cendre de bois) à la floraison, paillage protecteur.",
        "conservation": "Séchage intégral au soleil des fruits rouges pour une conservation sur plusieurs années.",
        "transformation": "Purée de piment fort en pots (pâte de piment), piment en poudre de table.", "rendement_base": 2.0
    },
    "Concombre / Melon / Courgette": {
        "famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon, Haricot", "ennemis": "Tomate, Pastèque", 
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "50 à 65 jours", 
        "entretien": "Arrosage abondant et régulier au pied. Le moindre stress d'eau rend le fruit amer.",
        "conservation": "Conserver emballé dans un endroit frais entre 10 et 12°C pendant 7 à 10 jours.",
        "transformation": "Mise en bocaux de saumure vinaigrée aromatisée pour faire des cornichons.", "rendement_base": 4.5
    },
    "Chou (Pommé / de Chine)": {
        "famille": "Brassicacées", "amis": "Laitue, Oignon, Céleri", "ennemis": "Ail, Fraise", 
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE (30 jours)", "cycle": "85 à 105 jours après repiquage", 
        "entretien": "Forte demande en azote (fientes de poule bien sèches), installation obligatoire d'un filet anti-chenilles.",
        "conservation": "Se conserve au frais en cave ventilée pendant 2 à 3 semaines.",
        "transformation": "Fermentation naturelle salée en bocaux étanches pour faire de la choucroute.", "rendement_base": 3.0
    },
    "Laitue / Salade / Amarante": {
        "famille": "Astéracées", "amis": "Chou, Carotte, Tomate", "ennemis": "Persil, Céleri", 
        "methode": "🌱 PÉPINIÈRE OU SEMIS EN LIGNES", "cycle": "30 à 45 jours", 
        "entretien": "Sarclage très délicat, arrosage fin sous forme de pluie, cueillette à la fraîche le matin.",
        "conservation": "Durée de vie très courte (48h). Conserver enveloppé dans un linge propre humide au frais.",
        "transformation": "Consommation brute exclusive en frais. Pas de transformation industrielle viable.", "rendement_base": 0.4
    },
    "Carotte / Betterave / Radis": {
        "famille": "Apiacées", "amis": "Oignon, Laitue, Tomate", "ennemis": "Aneth, Fenouil", 
        "methode": "🎯 SEMIS DIRECT EN LIGNES SERRÉES", "cycle": "70 à 90 jours", 
        "entretien": "Éclaircissage rigoureux à 5 cm après levée. Exige un sol sableux meuble et sans cailloux.",
        "conservation": "Couper les fanes vertes et stocker les racines dans du sable sec à l'ombre (conservation 2 mois).",
        "transformation": "Jus de carotte/betterave pasteurisé en bouteilles, rondelles de betteraves en conserve de vinaigre.", "rendement_base": 2.2
    },
    "Menthe / Persil / Céleri": {
        "famille": "Lamiacées & Apiacées", "amis": "Tomate, Chou, Oignon", "ennemis": "Salade", 
        "methode": "🌱 PÉPINIÈRE OU BOUTURAGE (MENTHE)", "cycle": "Récolte continue dès le 60e jour", 
        "entretien": "Arrosage régulier. La menthe s'étale d'elle-même, parfaite pour stabiliser les bords de buttes.",
        "conservation": "Séchage complet des feuilles suspendues à l'ombre. Stockage en bocaux hermétiques pendant 1 an.",
        "transformation": "Extraction d'huile essentielle par distillation, fabrication de sirops de menthe artisanaux.", "rendement_base": 1.5
    },
    "Haricot vert / Niébé": {
        "famille": "Fabacées", "amis": "Maïs, Tomate, Aubergine", "ennemis": "Oignon, Ail", 
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "cycle": "45 à 60 jours", 
        "entretien": "Binage léger pour casser la croûte de terre. Fixe l'azote de l'air pour amender le sol.",
        "conservation": "Haricot vert frais : 5 jours au frais. Niébé grain : séchage complet et stockage avec feuilles de neem anti-charançons.",
        "transformation": "Conserves de haricots verts stérilisés en bocaux, ensachage propre des graines de niébé triées.", "rendement_base": 1.6
    }
}

# Navigation par Onglets (Retour de tous les modules demandés)
onglets_app = st.tabs(["📸 Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"])

# --- MODULÉ 1 : SCANNER IA ---
with onglets_app[0]:
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

# --- MODULE 2 : ASSOCIATION POSSIBLE ---
with onglets_app[1]:
    st.markdown('<div class="category-card"><h3>🌿 Association Possible</h3>Découvrez les affinités biologiques pour protéger vos buttes naturellement.</div>', unsafe_allow_html=True)
    pl2 = st.selectbox("Sélectionnez votre culture :", list(base_encyclopedie.keys()), key="p2")
    if pl2:
        st.success(f"🤝 **Bonnes associations (Amis) :** {base_encyclopedie[pl2]['amis']}")
        st.error(f"❌ **À ÉVITER à proximité (Ennemis) :** {base_encyclopedie[pl2]['ennemis']}")

# --- MODULE 3 : SUIVI CYCLES ---
with onglets_app[2]:
    st.markdown('<div class="category-card"><h3>🚜 Suivi Technique Évolutif</h3>Suivez le parcours complet de la pépinière jusqu\'au panier.</div>', unsafe_allow_html=True)
