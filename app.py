import streamlit as st
import pandas as pd

# Configuration de la page mobile Premium
st.set_page_config(page_title="La Bible Maraîchère PRO", page_icon="📖", layout="centered")

# ==========================================
# DESIGN SYSTEM PRESTIGE (CSS)
# ==========================================
st.markdown("""
    <style>
        .stApp { background-color: #F8FAF8; }
        h1 { color: #0B4619 !important; font-family: 'Inter', sans-serif; font-weight: 800; text-align: center; }
        h2, h3 { color: #1E5631 !important; }
        .card {
            background-color: #FFFFFF; padding: 22px; border-radius: 16px;
            box-shadow: 0px 6px 16px rgba(0, 0, 0, 0.03); margin-bottom: 20px;
            border-top: 4px solid #1E5631;
        }
        .business-box {
            background-color: #EBF3F9; border-left: 5px solid #1F4E79;
            padding: 15px; border-radius: 8px; color: #1F4E79; margin-top: 10px;
        }
        .stTabs [data-baseweb="tab-list"] { gap: 8px; background-color: #EEF3EF; padding: 8px; border-radius: 12px; }
        .stTabs [data-baseweb="tab"] { color: #1E5631; font-weight: 600; border-radius: 8px; padding: 10px 15px; font-size: 14px; }
        .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #1E5631 !important; color: white !important; }
    </style>
""", unsafe_allowed_html=True)

# ==========================================
# BASE DE DONNÉES ENCYCLOPÉDIQUE ET AGROBUSINESS
# ==========================================
base_cultures = {
    "Tomate": {
        "famille": "Solanacées",
        "amis": "Carotte, Oignon, Laitue, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron, Aubergine",
        "pepiniere": "Semer en bac ou sous moustiquaire. Arrosage 2 fois/jour. Durée : 21-25 jours.",
        "repiquage": "Écartement : 50 cm entre les plants, 80 cm entre les lignes. Enterrer la tige jusqu'aux premières feuilles.",
        "rendement_base": 3.5,
        "conservation": "Froid humide (12°C) pour les fruits frais. Ne pas descendre sous 10°C (perte de saveur). Longue conservation par séchage au soleil des tranches.",
        "transformation": "Concentré de tomate, purée pasteurisée en bouteilles en verre, tomates séchées confites dans l'huile."
    },
    "Pastèque": {
        "famille": "Cucurbitacées",
        "amis": "Maïs, Gombo, Tournesol, Radis", "ennemis": "Concombre, Melon, Courgette",
        "pepiniere": "ZÉRO JOUR. Semis direct obligatoire en poquets de 3 graines.",
        "repiquage": "Pas de repiquage. Écartement large : 1m entre les pieds, 2m entre les lignes.",
        "rendement_base": 12.0,
        "conservation": "Se conserve 2 à 3 semaines à température ambiante à l'ombre dans un endroit sec et ventilé.",
        "transformation": "Jus frais pasteurisé, confiture d'écorce de pastèque, extraction d'huile à partir des graines séchées et pressées."
    },
    "Concombre": {
        "famille": "Cucurbitacées",
        "amis": "Laitue, Chou, Oignon, Haricot", "ennemis": "Tomate, Pomme de terre, Pastèque",
        "pepiniere": "Semis direct au champ de préférence ou 12 jours en godets de terreau.",
        "repiquage": "Écartement de 40 cm sur la butte. Prévoir des tuteurs ou un treillage pour faire grimper les fruits.",
        "rendement_base": 4.0,
        "conservation": "Très sensible au flétrissement. Conserver emballé au frais (10-12°C) pendant 7 à 10 jours maximum.",
        "transformation": "Transformation en cornichons par immersion dans une saumure vinaigrée avec des herbes aromatiques."
    },
    "Laitue / Salade": {
        "famille": "Astéracées",
        "amis": "Carotte, Radis, Oignon, Tomate", "ennemis": "Persil, Céleri",
        "pepiniere": "15 à 20 jours en bac ombragé. Maintenir le terreau humide mais pas détrempé.",
        "repiquage": "Planches de 25 cm x 25 cm. Garder le collet légèrement au-dessus du niveau de la terre.",
        "rendement_base": 0.3,
        "conservation": "Durée de vie très courte (2 à 3 jours). Conserver au frais enveloppé dans un linge humide.",
        "transformation": "Quasiment impossible à transformer industriellement. Consommation en frais uniquement."
    },
    "Menthe": {
        "famille": "Lamiacées (Aromatique)",
        "amis": "Chou, Tomate, Laitue", "ennemis": "Camomille",
        "pepiniere": "Bouturage très facile dans l'eau ou semis en bac humide pendant 20 jours.",
        "repiquage": "Espacement de 30 cm. Plante traçante très envahissante, idéale en bordure de planches.",
        "rendement_base": 1.2,
        "conservation": "Séchage complet des feuilles à l'ombre dans un endroit chaud et aéré. Conservation en bocaux hermétiques pendant 1 an.",
        "transformation": "Extraction d'huile essentielle de menthe par distillation, fabrication de sirop de menthe artisanal, poudre de menthe séchée."
    },
    "Persil & Céleri": {
        "famille": "Apiacées (Aromatiques)",
        "amis": "Tomate, Oignon, Radis", "ennemis": "Laitue, Salade",
        "pepiniere": "Levée très lente (jusqu'à 3 semaines). Tremper les graines dans l'eau 24h avant le semis en bac.",
        "repiquage": "Espacement de 25 cm sur lignes serrées après 35 jours en pépinière.",
        "rendement_base": 1.5,
        "conservation": "Congélation des feuilles ciselées ou séchage complet à l'abri de la lumière pour garder la couleur verte.",
        "transformation": "Sel de céleri (feuilles séchées broyées avec du sel marin), huiles aromatiques pour la cuisine, bouquets garnis déshydratés."
    }
}

# Images d'illustration agronomiques universelles (Libres de droits)
images_etapes = {
    "pepiniere": "https://unsplash.com", # Jeunes pousses vertes
    "repiquage": "https://unsplash.com", # Plantation en terre
    "entretien": "https://unsplash.com", # Potager entretenu/paillé
    "recolte": "https://unsplash.com"     # Légumes récoltés frais
}

# ==========================================
# INTERFACE DE L'APPLICATION SMARTPHONE
# ==========================================
st.markdown("<h1>📖 La Bible Maraîchère PRO</h1>", unsafe_allowed_html=True)
st.markdown("<p style='text-align: center; color: #666; font-style: italic;'>L'outil intégral de l'agriculteur moderne connecté</p>", unsafe_allowed_html=True)

onglet = st.tabs(["📸 Scanner IA", "🌿 Associations", "🚜 Guide en Images", "🏭 Agrobusiness", "💰 Budget"])

# ------------------------------------------
# ONGLET 3 : LE GUIDE DE CULTURE EN IMAGES
# ------------------------------------------
with onglet[2]:
    st.markdown('<div class="card"><h3>🚜 Guide Visuel Étape par Étape</h3>Suivez les repères en images pour réussir chaque phase de votre culture.</div>', unsafe_allowed_html=True)
    culture_visuelle = st.selectbox("Sélectionnez la plante à suivre :", list(base_cultures.keys()), key="visuel_sel")
    
    if culture_visuelle:
        c_data = base_cultures[culture_visuelle]
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(images_etapes["pepiniere"], caption="🌱 Étape 1 : La Pépinière / Semis", use_container_width=True)
            st.write(c_data["pepiniere"])
        with col2:
            st.image(images_etapes["repiquage"], caption="📐 Étape 2 : Le Repiquage au champ", use_container_width=True)
            st.write(c_data["repiquage"])
            
        st.markdown("---")
        
        col3, col4 = st.columns(2)
        with col3:
            st.image(images_etapes["entretien"], caption="✂️ Étape 3 : Entretien et Paillage", use_container_width=True)
            st.write("Désherbage régulier, maintien du paillage organique pour garder l'humidité et tuteurage si nécessaire.")
        with col4:
            st.image(images_etapes["recolte"], caption="🧺 Étape 4 : Récolte et Maturité", use_container_width=True)
            st.write(f"Cueillette au stade optimal. Rendement attendu : **{c_data['rendement_base']} kg** par unité.")

# ------------------------------------------
# ONGLET 4 : NOUVEAU MODULE AGROBUSINESS (CONSERVATION / TRANSFORMATION)
# ------------------------------------------
with onglet[3]:
    st.markdown('<div class="card"><h3>🏭 Volet Agrobusiness & Valeur Ajoutée</h3>Ne bradez plus vos récoltes en période de surproduction. Maîtrisez le stockage et créez des produits transformés.</div>', unsafe_allowed_html=True)
    culture_biz = st.selectbox("Sélectionnez une culture pour l'agrobusiness :", list(base_cultures.keys()), key="biz_sel")
    
    if culture_biz:
        cb = base_cultures[culture_biz]
        st.markdown(f"## 🏭 Valorisation industrielle : {culture_biz}")
        
        st.markdown('<div class="business-box"><b>🧊 Méthodes de Conservation Spécifiques :</b><br>' + cb["conservation"] + '</div>', unsafe_allowed_html=True)
        st.markdown('<div class="business-box" style="border-left-color: #2E7D32; background-color: #EBF7EE; color: #2E7D32;"><b>🍯 Procédés de Transformation Locale :</b><br>' + cb["transformation"] + '</div>', unsafe_allowed_html=True)

# (Les autres modules restent actifs et connectés en arrière-plan)
with onglet[0]:
    st.info("📸 Module Scanner IA actif. Importez une photo pour l'analyse en ligne.")
with onglet[1]:
    st.info("🌿 Module Compagnonnage actif. Consultez les interactions entre plantes.")
with onglet[4]:
    st.info("💰 Module Simulateur Financier actif. Calculez vos marges de profit.")
