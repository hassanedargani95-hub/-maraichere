import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration de la page mobile Premium Haute Performance
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# ==========================================
# CONNEXION AU CERVEAU DE L'IA CLOUD
# ==========================================
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw" 

if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    modele_ia = genai.GenerativeModel("gemini-1.5-flash")
else:
    modele_ia = None

# Styles graphiques professionnels de la maquette UI
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header {
            background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px;
            color: white; text-align: center; margin-top: -60px; margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .category-card {
            background-color: #FFFFFF; padding: 15px; border-radius: 18px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04); margin-bottom: 15px;
            border-left: 6px solid #2CB674;
        }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
        .badge-methode { padding: 6px 14px; border-radius: 20px; font-weight: bold; color: white; display: inline-block; margin-bottom: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Intelligence Artificielle connectée de terrain</p></div>', unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE EXHAUSTIVE
# ==========================================
base_encyclopedie = {
    "Tomate": {
        "famille": "Solanacées",
        "amis": "Carotte, Oignon, Laitue, Basilic, Œillet d'Inde",
        "ennemis": "Pomme de terre, Poivron, Aubergine",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "21 à 25 jours (jusqu'à obtenir 4 vraies feuilles).",
        "cycle_total": "75 à 90 jours après le repiquage pour les premières cueillettes.",
        "entretien": "Installer des tuteurs dès la 2e semaine, pailler le sol, et tailler obligatoirement les gourmands aux aisselles.",
        "conseil": "Arrosage régulier au pied sans jamais mouiller les feuilles pour bloquer le mildiou."
    },
    "Pastèque": {
        "famille": "Cucurbitacées",
        "amis": "Maïs, Gombo, Tournesol, Radis",
        "ennemis": "Concombre, Melon, Courgette",
        "methode": "🎯 SEMIS DIRECT AU CHAMP",
        "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour (Déteste le repiquage car sa racine pivotante se brise).",
        "cycle_total": "80 à 95 jours après le semis direct.",
        "entretien": "Dresser de larges buttes plates en travers de la pente. Mettre 3 graines par poquet, puis ne laisser que le plus fort après 15 jours.",
        "conseil": "Pincer la tige principale après la 4e feuille pour forcer le développement des gros fruits."
    },
    "Gombo": {
        "famille": "Malvacées",
        "amis": "Piment, Aubergine, Niébé, Pastèque",
        "ennemis": "Oignon, Tomate (partagent une forte sensibilité aux nématodes)",
        "methode": "🎯 SEMIS DIRECT AU CHAMP",
        "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour. Semis direct en poquets de 3 graines.",
        "cycle_total": "55 à 65 jours (Croissance très rapide).",
        "entretien": "Buttage des pieds à la houe un mois après le semis pour renforcer l'ancrage contre les vents forts.",
        "conseil": "Cueillir les capsules tous les 2 jours lorsqu'elles sont tendres sous l'ongle."
    },
    "Oignon": {
        "famille": "Alliacées",
        "amis": "Carotte, Laitue, Tomate, Piment",
        "ennemis": "Gombo, Haricot, Pois",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "45 à 50 jours en pépinière meuble (jusqu'à la grosseur d'un crayon).",
        "cycle_total": "100 à 120 jours après le repiquage.",
        "entretien": "Désherbage manuel très fréquent. Couper le tiers supérieur des feuilles (habillage) au repiquage.",
        "conseil": "Éviter absolument le fumier frais juste avant plantation pour empêcher les bulbes de pourrir."
    },
    "Piment / Poivron": {
        "famille": "Solanacées",
        "amis": "Oignon, Ail, Gombo, Carotte",
        "ennemis": "Tomate, Aubergine",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "25 à 30 jours sous abri moustiquaire.",
        "cycle_total": "80 à 100 jours après repiquage.",
        "entretien": "Apport massif de potassium (cendre) à la floraison. Pailler pour protéger les racines du soleil.",
        "conseil": "Très sensible à l'anthracnose (taches noires sur fruits) par temps de pluie humide."
    },
    "Concombre / Melon / Courgette": {
        "famille": "Cucurbitacées",
        "amis": "Salade, Chou, Oignon, Haricot",
        "ennemis": "Tomate, Pomme de terre, Pastèque",
        "methode": "🎯 SEMIS DIRECT (OU GODETS DE 12 JOURS)",
        "badge_couleur": "#C62828",
        "duree_pepiniere": "Semis direct ou 10-12 jours maximum en petits godets individuels.",
        "cycle_total": "50 à 65 jours selon les variétés.",
        "entretien": "Installer des treillages ou tuteurs pour faire grimper les fruits si l'espace au sol est limité.",
        "conseil": "Arrosage quotidien abondant. Le moindre stress hydrique rend le légume très amer au goût."
    },
    "Chou (Pommé ou de Chine)": {
        "famille": "Brassicacées",
        "amis": "Laitue, Oignon, Pomme de terre, Céleri",
        "ennemis": "Fraise, Ail",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "30 jours. Protéger impérativement contre les chenilles avec un filet fin dès la levée.",
        "cycle_total": "85 à 105 jours après repiquage.",
        "entretien": "Plante très gourmande en azote. Demande un apport régulier de fientes de volailles bien sèches.",
        "conseil": "Maintenir le sol humide pour obtenir une pomme tendre, compacte et douce."
    },
    "Laitue / Salade / Amarante": {
        "famille": "Astéracées",
        "amis": "Chou, Carotte, Oignon, Tomate (profite de son ombre)",
        "ennemis": "Persil, Céleri",
        "methode": "🌱 PÉPINIÈRE OU SEMIS EN LIGNE SERRÉE",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "15 à 18 jours. Les graines doivent être à peine couvertes de sable fin.",
        "cycle_total": "30 à 45 jours (Cycle ultra-court, idéal pour intercaler).",
        "entretien": "Sarclage délicat. Demande une terre fraîche et un arrosage fin sous forme de pluie.",
        "conseil": "Récolter tôt le matin pour garder les feuilles craquantes et éviter le flétrissement."
    },
    "Carotte / Betterave / Radis": {
        "famille": "Apiacées",
        "amis": "Oignon, Poireau, Laitue, Tomate",
        "ennemis": "Aneth, Fenouil",
        "methode": "🎯 SEMIS DIRECT EN LIGNES SERRÉES",
        "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour (Le repiquage déforme la racine, la rendant fourchue et invendable).",
        "cycle_total": "70 à 90 jours (25 jours pour les radis roses).",
        "entretien": "Éclaircissage rigoureux 20 jours après levée pour laisser 5 cm d'espace entre les racines.",
        "conseil": "Exige un sol profondément meuble, sableux et totalement débarrassé des cailloux."
    },
    "Menthe / Persil / Céleri": {
        "famille": "Lamiacées & Apiacées (Aromatiques)",
        "amis": "Tomate, Chou, Oignon",
        "ennemis": "Salade, Laitue",
        "methode": "🌱 PÉPINIÈRE OU BOUTURAGE (MENTHE)",
        "badge_couleur": "#2E7D32",
        "duree_pepiniere": "Levée très lente (jusqu'à 21 jours pour le persil). Tremper les graines 24h avant.",
        "cycle_total": "Récolte continue par coupe des tiges dès le 60e jour.",
        "entretien": "La menthe se propage par lianes rampantes (stolons) et peut être plantée pour fixer les bordures.",
        "conseil": "Excellentes cultures pour l'agrobusiness (séchage à l'ombre et revente en herbes sèches)."
    },
    "Haricot vert / Niébé": {
        "famille": "Fabacées (Légumineuses)",
        "amis": "Maïs, Tomate, Aubergine, Pomme de terre",
        "ennemis": "Oignon, Ail, Échalote",
        "methode": "🎯 SEMIS DIRECT AU CHAMP",
        "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour. Semis direct en poquets peu profonds.",
        "cycle_total": "45 à 60 jours.",
        "entretien": "Binage léger. Cette plante fabrique ses propres nodules pour fertiliser la terre en azote.",
        "conseil": "Idéal pour restructurer un sol fatigué après une grosse culture de Solanacées."
    }
}

# Navigation par onglets
onglets_list = ["📸 VRAI Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles"]
tab1, tab2, tab3 = st.tabs(onglets_list)

# --- ONGLET 1 : RECONNAISSANCE IA DYNAMIQUE ---
with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle Automatique')
    
    # Prise de vue unique pour stabiliser le réseau mobile LTE et empêcher le bug de chargement
    fichier_photo = st.file_uploader("Prendre ou charger une photo de votre culture :", type=["jpg", "png", "jpeg"], key="photo_unique_champ")
    
    if fichier_photo is not None:
        st.success("📊 Image reçue avec succès.")
        image_pil = Image.open(fichier_photo)
        st.image(image_pil, caption=f"Fichier prêt : {fichier_photo.name}", width=280)
        
        if st.button("🚀 LANCER L'ANALYSE AUTOMATIQUE PAR INTERNET", key="bouton_ia"):
            if modele_ia is None:
                st.error("Erreur de configuration de la clé API.")
            else:
