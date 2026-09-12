import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration Premium Haute Performance Mobile
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# Connexion sécurisée à l'IA Cloud Google
API_KEY_SECRET = "AQ.Ab8RN6J5BtDax27zI7Iz6-zyRi3Ql2Mg6U19v7ggbcDToXEibw" 
if API_KEY_SECRET:
    genai.configure(api_key=API_KEY_SECRET)
    modele_ia = genai.GenerativeModel("gemini-1.5-flash")
else:
    modele_ia = None

# Styles graphiques professionnels de la maquette UI Vert Nature
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header { background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px; color: white; text-align: center; margin-top: -60px; margin-bottom: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); }
        .category-card { background-color: #FFFFFF; padding: 15px; border-radius: 18px; box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04); margin-bottom: 15px; border-left: 6px solid #2CB674; }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
        .badge-methode { padding: 6px 14px; border-radius: 20px; font-weight: bold; color: white; display: inline-block; margin-bottom: 10px; }
        .badge-biz { background-color: #E6F7ED; color: #1E5631; padding: 8px; border-radius: 10px; font-weight: bold; border: 1px solid #2CB674; display: inline-block; margin-top: 10px; }
        .doc-section { background-color: #FFFFFF; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #2CB674; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Système Intégral Connecté & Agrobusiness</p></div>', unsafe_allow_html=True)

# Base de données exhaustive et solide
base_encyclopedie = {
    "Tomate": {
        "famille": "Solanacées", "amis": "Carotte, Oignon, Laitue, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32", "cycle": "75 à 90 jours",
        "entretien": "Tuteurage, paillage épais, taille obligatoire des gourmands aux aisselles.",
        "conservation": "Froid modéré (12°C). Séchage solaire complet des tranches étalées sur des claies.",
        "transformation": "Concentré de tomate, coulis pasteurisé en bouteilles, tomates séchées confites.", "rendement_base": 3.5
    },
    "Pastèque": {
        "famille": "Cucurbitacées", "amis": "Maïs (brise-vent), Gombo, Tournesol", "ennemis": "Concombre, Melon",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828", "cycle": "80 à 95 jours",
        "entretien": "Buttes très larges et plates en travers de la pente. Ne laisser qu'un plant robuste après 15 jours.",
        "conservation": "Se conserve 2 à 3 semaines à l'ombre sur de la paille sèche dans un abri aéré.",
        "transformation": "Jus frais pasteurisé, confiserie à base d'écorces blanches (pelures), huile de graines.", "rendement_base": 12.0
    },
    "Gombo": {
        "famille": "Malvacées", "amis": "Piment, Aubergine, Pastèque", "ennemis": "Oignon, Tomate",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828", "cycle": "55 à 65 jours",
        "entretien": "Buttage des pieds à la houe un mois après la levée pour consolider la tige contre le vent.",
        "conservation": "Fragile. Se conserve 3 à 4 jours enveloppé à l'abri de la lumière.",
        "transformation": "Déshydratation des rondelles au séchoir solaire et réduction en poudre fine de contre-saison.", "rendement_base": 1.8
    },
    "Oignon": {
        "famille": "Alliacées", "amis": "Carotte, Laitue, Tomate", "ennemis": "Gombo, Haricot",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32", "cycle": "100 à 120 jours",
        "entretien": "Désherbage manuel frequent. Habillage (taille) des feuilles et radicelles au repiquage.",
        "conservation": "Ressuyage de 48h sur le champ, puis tressage et suspension dans un hangar sec.",
        "transformation": "Séchage de fines lamelles et réduction en poudre d'oignon aromatique.", "rendement_base": 2.5
    },
    "Piment / Poivron": {
        "famille": "Solanacées", "amis": "Oignon, Ail, Gombo", "ennemis": "Tomate, Aubergine",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32", "cycle": "80 à 100 jours",
        "entretien": "Apport de cendres de bois (potassium) à la floraison. Pailler le sol.",
        "conservation": "Séchage intégral au soleil sur des nattes propres. Conservation sur plusieurs années.",
        "transformation": "Pâte de piment fort en pots (mélange huile chaude), poudre de piment pur.", "rendement_base": 2.0
    },
    "Concombre / Melon": {
        "famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon", "ennemis": "Tomate, Pastèque",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828", "cycle": "50 à 65 jours",
        "entretien": "Arrosage quotidien abondant au pied. Le moindre manque d'eau rend le fruit amer.",
        "conservation": "Conserver emballé au frais (10-12°C) pendant 7 à 10 jours maximum.",
        "transformation": "Immersion immédiate dans une saumure vinaigrée salée pour la production de cornichons.", "rendement_base": 4.5
    },
    "Chou": {
        "famille": "Brassicacées", "amis": "Laitue, Oignon, Céleri", "ennemis": "Ail, Fraise",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32", "cycle": "85 à 105 jours",
        "entretien": "Exigeant en azote (fientes de poule sèches). Filet anti-chenilles obligatoire.",
        "conservation": "Se conserve au frais en caissettes bois ventilées pendant 2 à 3 semaines.",
        "transformation": "Râpage fin et fermentation lactique naturelle (saumure) pour fabriquer la choucroute.", "rendement_base": 3.0
    },
    "Laitue / Salade": {
        "famille": "Astéracées", "amis": "Chou, Carotte, Tomate", "ennemis": "Persil, Céleri",
        "methode": "🌱 PÉPINIÈRE OU LIGNES", "badge_couleur": "#2E7D32", "cycle": "30 à 45 jours",
        "entretien": "Sarclage délicat, arrosage fin en pluie, récolte obligatoire à l'aube.",
        "conservation": "Très courte (24 à 48h). Envelopper dans un tissu en coton humide au frais.",
        "transformation": "Aucune transformation possible. Consommation brute à l'état frais uniquement.", "rendement_base": 0.4
    },
    "Carotte / Betterave": {
        "famille": "Apiacées", "amis": "Oignon, Laitue, Tomate", "ennemis": "Aneth, Fenouil",
        "methode": "🎯 SEMIS DIRECT EN LIGNES SERRÉES", "badge_couleur": "#C62828", "cycle": "70 à 90 jours",
        "entretien": "Éclaircissage à 5 cm après levée. Exige un sol profondément sableux meuble sans cailloux.",
        "conservation": "Couper les fanes et stocker les racines alignées dans du sable sec à l'ombre (2 mois).",
        "transformation": "Extraction mécanique de jus filtré pasteurisé, conserves de rondelles au vinaigre.", "rendement_base": 2.2
    },
    "Menthe": {
        "famille": "Lamiacées", "amis": "Tomate, Chou, Oignon", "ennemis": "Camomille",
        "methode": "🌱 PÉPINIÈRE OU BOUTURAGE DIRECT", "badge_couleur": "#2E7D32", "cycle": "Continue dès 60 jours",
        "entretien": "Arrosage fréquent. Parfaite pour fixer et stabiliser la terre des bordures d'allées.",
        "conservation": "Séchage complet des tiges suspendues à l'ombre. Stockage en bocaux hermétiques (1 an).",
        "transformation": "Distillation artisanale à la vapeur pour extraire l'huile essentielle, sirops maison.", "rendement_base": 1.5
    },
    "Persil / Céleri": {
        "famille": "Apiacées", "amis": "Tomate, Oignon, Poireau", "ennemis": "Laitue",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32", "cycle": "Continue dès 60 jours",
        "entretien": "Sarclage rigoureux pour éviter l'étouffement. Exige une terre fraîche et humide.",
        "conservation": "Séchage rapide à l'abri de la lumière pour conserver la couleur verte éclatante.",
        "transformation": "Production de sel de céleri (feuilles séchées pulvérisées avec du sel), bouquets garnis.", "rendement_base": 1.4
    },
    "Haricot vert / Niébé": {
        "famille": "Fabacées", "amis": "Maïs, Tomate, Aubergine", "ennemis": "Oignon, Ail",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828", "cycle": "45 à 60 jours",
        "entretien": "Binage léger. Capte l'azote de l'air pour amender le sol naturellement sans engrais.",
        "conservation": "Frais : 5 jours. Grain sec : stocker avec des feuilles de neem anti-charançons.",
        "transformation": "Stérilisation à l'autoclave et mise en conserve des gousses, ensachage étanche.", "rendement_base": 1.6
    }
}

# Configuration sécurisée des 6 onglets
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["📸 Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget", "📚 Documentation"])

# --- MODULE 1 : SCANNER IA ---
with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle')
    f_photo = st.file_uploader("Prendre ou charger une photo :", type=["jpg", "png", "jpeg"], key="cam_unique")
    if f_photo is not None:
        st.image(f_photo, width=280)
        if st.button("🚀 LANCER L'ANALYSE EN DIRECT", key="bouton_scan"):
            if modele_ia is None:
                st.error("L'IA est hors-ligne. Clé d'accès manquante.")
            else:
                consigne = "Analyse cette photo maraîchère. Donne le NOM DE LA PLANTE, la MALADIE, les CAUSES et le TRAITEMENT NATUREL BIO."
                reponse = modele_ia.generate_content([consigne, f_photo])
                st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                st.write(reponse.text)
                st.markdown('</div>', unsafe_allow_html=True)

