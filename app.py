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

# Styles graphiques professionnels "Vert Nature" (Maquette UI d'origine)
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
        .badge-biz { background-color: #E6F7ED; color: #1E5631; padding: 8px; border-radius: 10px; font-weight: bold; border: 1px solid #2CB674; display: inline-block; margin-top: 10px; }
        .doc-section { background-color: #FFFFFF; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #2CB674; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Système Intégral Connecté & Agrobusiness</p></div>', unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE ET FINANCIÈRE EXHAUSTIVE
# ==========================================
base_encyclopedie = {
    "Tomate": {
        "famille": "Solanacées", "amis": "Carotte, Oignon, Laitue, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron, Aubergine",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "21 à 25 jours (jusqu'à obtenir 4 vraies feuilles).",
        "cycle_total": "75 à 90 jours après le repiquage.",
        "entretien": "Tuteurage rigoureux, paillage épais, taille des gourmands secondaires à l'aisselle des feuilles.",
        "conseil": "Arrosage au pied sans toucher le feuillage pour interdire l'installation du mildiou.",
        "conservation": "Froid humide contrôlé (10 à 12°C). Séchage solaire complet des tranches étalées sur des claies.",
        "transformation": "Concentré de tomate, coulis pasteurisé en bouteilles, tomates séchées macérées dans l'huile.",
        "rendement_base": 3.5
    },
    "Pastèque": {
        "famille": "Cucurbitacées", "amis": "Maïs (brise-vent), Gombo, Tournesol, Radis", "ennemis": "Concombre, Melon, Courgette",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour (La racine pivotante centrale est ultra-fragile et se brise au déplacement).",
        "cycle_total": "80 à 95 jours après le semis.",
        "entretien": "Buttes très larges et plates en travers de la pente. Un seul plant robuste par poquet après 15 jours.",
        "conseil": "Pincer la liane principale au-dessus de la 4e feuille pour faire grossir les fruits.",
        "conservation": "Se conserve 2 à 3 semaines à l'ombre sur des lits de paille sèche dans un abri aéré.",
        "transformation": "Jus frais pasteurisé, confiserie à base d'écorces blanches (pelures), extraction d'huile des graines.",
        "rendement_base": 12.0
    },
    "Gombo": {
        "famille": "Malvacées", "amis": "Piment, Aubergine, Niébé, Pastèque", "ennemis": "Oignon, Tomate",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour. Semis direct en poquets de 3 graines.",
        "cycle_total": "55 à 65 jours.",
        "entretien": "Buttage des pieds à la houe un mois après la levée pour consolider la tige contre le vent.",
        "conseil": "Cueillette obligatoire tous les 2 jours pour éviter qu'il ne devienne dur et fibreux.",
        "conservation": "Fragile. Se conserve seulement 3 à 4 jours enveloppé à l'abri de la lumière.",
        "transformation": "Déshydratation des rondelles au séchoir solaire et réduction en poudre fine de contre-saison.",
        "rendement_base": 1.8
    },
    "Oignon": {
        "famille": "Alliacées", "amis": "Carotte, Laitue, Tomate, Piment", "ennemis": "Gombo, Haricot, Pois",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "45 à 50 jours en pépinière meuble (grosseurs d'un crayon).",
        "cycle_total": "100 à 120 jours après repiquage.",
        "entretien": "Désherbage manuel frequent. Taille des feuilles et des radicelles lors du repiquage (habillage).",
        "conservation": "Ressuyage obligatoire sur le champ pendant 48h, puis tressage et suspension au sec.",
        "transformation": "Séchage de fines lamelles et réduction en poudre fine d'oignon.",
        "rendement_base": 2.5
    },
    "Piment / Poivron": {
        "famille": "Solanacées", "amis": "Oignon, Ail, Gombo, Carotte", "ennemis": "Tomate, Aubergine",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "25 à 30 jours sous abri moustiquaire.",
        "cycle_total": "80 à 100 jours après le repiquage.",
        "entretien": "Apport de cendres de bois riches en potassium pendant la floraison. Pailler le sol.",
        "conseil": "Surveiller l'anthracnose (taches noires sur fruits) lors des pluies denses.",
        "conservation": "Séchage intégral au soleil sur des nattes. Se conserve plusieurs années au sec.",
        "transformation": "Pâte de piment fort en pots (mélange huile chaude), piment écrasé en poudre.",
        "rendement_base": 2.0
    },
    "Concombre / Melon / Courgette": {
        "famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon, Haricot", "ennemis": "Tomate, Pastèque",
        "methode": "🎯 SEMIS DIRECT AU CHAMP", "badge_couleur": "#C62828",
        "cycle_total": "50 à 65 jours.",
        "duree_pepiniere": "Semis direct ou 10 jours maximum en godets individuels.",
        "entretien": "Arrosage abondant quotidien. Tuteurs solides pour maintenir les fruits hors du sol.",
        "conseil": "Le moindre manque d'eau déclenche immédiatement l'amertume du fruit.",
        "conservation": "Conserver emballé au frais entre 10 et 12°C pendant 7 à 10 jours maximum.",
        "transformation": "Immersion immédiate dans une saumure vinaigrée salée pour la production de cornichons.",
        "rendement_base": 4.5
    },
    "Chou (Pommé / de Chine)": {
        "famille": "Brassicacées", "amis": "Laitue, Oignon, Céleri", "ennemis": "Ail, Fraise",
        "methode": "🌱 PÉPINIÈRE OBLIGATOIRE", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "30 jours. Utiliser un voile anti-insectes dès le premier jour contre les chenilles.",
        "cycle_total": "85 à 105 jours après repiquage.",
        "entretien": "Très exigeant en azote. Apports réguliers de fientes de volailles bien sèches.",
        "conseil": "Maintenir un arrosage constant pour forcer la formation d'une pomme serrée.",
        "conservation": "Se conserve au frais en caissettes bois ventilées pendant 2 à 3 semaines.",
        "transformation": "Râpage fin et fermentation lactique naturelle (saumure) pour fabriquer la choucroute.",
        "rendement_base": 3.0
    },
    "Laitue / Salade / Amarante": {
        "famille": "Astéracées", "amis": "Chou, Carotte, Oignon, Tomate", "ennemis": "Persil, Céleri",
        "methode": "🌱 PÉPINIÈRE OU SEMIS EN LIGNES", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "15 à 18 jours. Couvrir à peine la graine fine.",
        "cycle_total": "30 à 45 jours (Revenus rapides à cycle court).",
        "entretien": "Sarclage manuel délicat. Arrosage fin en pluie pour ne pas abîmer le feuillage.",
        "conseil": "Récolter exclusivement à l'aube pour garder les feuilles craquantes.",
        "conservation": "Critique (24 à 48 heures). Envelopper dans un tissu en coton humide au frais.",
        "transformation": "Aucune transformation connue. Consommation brute à l'état frais uniquement.",
        "rendement_base": 0.4
    },
    "Carotte / Betterave / Radis": {
        "famille": "Apiacées", "amis": "Oignon, Laitue, Tomate", "ennemis": "Aneth, Fenouil",
        "methode": "🎯 SEMIS DIRECT EN LIGNES SERRÉES", "badge_couleur": "#C62828",
        "duree_pepiniere": "Zéro jour (Le repiquage déforme la racine et la rend invendable).",
        "cycle_total": "70 à 90 jours (25 jours pour les radis).",
        "entretien": "Éclaircissage après 20 jours pour laisser 5 cm d'écartement entre les plantes.",
        "conseil": "Exige un sol profondément meuble, sableux et totalement débarrassé des cailloux.",
        "conservation": "Couper les fanes et stocker les racines dans du sable sec à l'ombre (durée 2 mois).",
        "transformation": "Extraction mécanique de jus filtré pasteurisé, betteraves cuites en conserve de vinaigre.",
        "rendement_base": 2.2
    },
    "Menthe": {
        "famille": "Lamiacées (Aromatique)", "amis": "Tomate, Chou, Oignon", "ennemis": "Camomille",
        "methode": "🌱 PÉPINIÈRE OU BOUTURAGE DIRECT", "badge_couleur": "#2E7D32",
        "duree_pepiniere": "15 à 20 jours ou bouturage immédiat de tiges de 10 cm dans de l'eau.",
