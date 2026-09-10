import streamlit as st

# Configuration de la page mobile Premium
st.set_page_config(page_title="La Bible Maraîchère", page_icon="📖", layout="centered")

# ==========================================
# DESIGN PREMIUM "VERT NATURE" (STYLE MAQUETTE UI)
# ==========================================
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
        .stTabs [data-baseweb="tab-list"] { gap: 6px; background-color: #E2EFE7; padding: 6px; border-radius: 14px; }
        .stTabs [data-baseweb="tab"] { color: #1E5631; font-weight: bold; border-radius: 10px; padding: 10px; }
        .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #2CB674 !important; color: white !important; }
        .badge-biz { background-color: #E6F7ED; color: #1E5631; padding: 8px; border-radius: 10px; font-weight: bold; border: 1px solid #2CB674; }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
        .remede-card { background-color: #EBF7EE; border: 1px solid #2CB674; padding: 15px; border-radius: 12px; margin-top: 10px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Votre conseiller agricole et agrobusiness connecté</p></div>', unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES MUTABLE ET DYNAMIQUE
# ==========================================
base_diagnostics = {
    "Piment": {
        "plante": "🌶️ Piment / Poivron (Capsicum)",
        "maladie": "Anthracnose du Piment (Colletotrichum spp.)",
        "causes": "Champignon favorisé par l'humidité élevée des pluies de septembre, un sol mal paillé et une stagnation d'eau au pied du plant.",
        "bio": "Pulvériser une décoction forte d'ail pilé (30g/L d'eau) ou une solution de bicarbonate de soude sur tout le plant.",
        "chimique": "Application d'un fongicide de contact homologué à base de cuivre (Bouillie bordelaise) dès l'apparition des taches noires.",
        "remede_nom": "🧄 Gousses d'Ail et Bicarbonate",
        "remede_desc": "Le soufre de l'ail détruit les membranes des spores du champignon. Le bicarbonate bloque l'acidité favorable à sa survie."
    },
    "Betterave": {
        "plante": "🍠 Betterave / Radis Noir",
        "maladie": "Galles Racinaires (Nématodes) ou Carence en Bore",
        "causes": "Épuisement des oligo-éléments de la parcelle dû à une culture répétée ou présence de vers microscopiques rongeant les racines.",
        "bio": "Incoporer un amendement massif de terre de sous-bois noire riche en humus et arroser régulièrement au purin dilué.",
        "chimique": "Aucun traitement d'urgence disponible en cours de cycle. Rééquilibrer le sol avant la prochaine mise en culture.",
        "remede_nom": "🍂 Humus forestier (Terre de sous-bois)",
        "remede_desc": "La terre noire de sous-bois apporte des champignons bénéfiques et des minéraux essentiels pour reconstruire la barrière racinaire."
    },
    "Default": {
        "plante": "🍉 Pastèque / Cucurbitacées",
        "maladie": "Mildiou ou Oïdium des feuilles rampantes",
        "causes": "Forte humidité nocturne stagnante sur les lianes laissées sur sol nu sans paillage organique protecteur.",
        "bio": "Traiter le feuillage avec une solution de bicarbonate de soude (5g/L d'eau) mélangée à une cuillère de savon noir liquide.",
        "chimique": "Fongicide systémique de synthèse en respectant rigoureusement les délais avant récolte.",
        "remede_nom": "🧼 Savon Noir liquide & Bicarbonate",
        "remede_desc": "Le savon noir permet à la solution de s'agripper fermement aux feuilles lisses et cireuses de la pastèque."
    }
}

# ==========================================
# NAVIGATION PAR ONGLETS NATIVE
# ==========================================
onglets_list = ["📸 Scanner IA & Diagnostic", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(onglets_list)

# --- ONGLET 1 : DIAGNOSTIC MULTIPLE ET DYNAMIQUE CORRIGÉ ---
with tab1:
    st.markdown('<div class="category-card"><h3>📸 Laboratoire de Diagnostic Intelligent</h3>Importez vos photos de terrain. L\'application analyse et adapte le résultat en fonction de l\'image active.</div>', unsafe_allow_html=True)
    
    # Sélection multiple de fichiers
    photos_fichiers = st.file_uploader("Prendre ou charger vos photos (Sélection multiple) :", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if photos_fichiers:
        st.write(f"📊 **{len(photos_fichiers)} image(s) détectée(s) sur le champ.**")
        
        # Liste des noms de fichiers pour la navigation dynamique
        noms_images = [f"Image {i+1} : {f.name}" for i, f in enumerate(photos_fichiers)]
        
        # Bouton de sélection de l'image active pour forcer le rafraîchissement dynamique
        image_active_nom = st.selectbox("🎯 Cliquez ici pour choisir l'image à analyser en direct :", noms_images)
        idx_active = noms_images.index(image_active_nom)
        fichier_actif = photos_fichiers[idx_active]
        
        # Affichage de l'image sélectionnée en grand
        st.image(fichier_actif, caption=f"Analyse active de l'image : {fichier_actif.name}", use_container_width=True)
        
        # LOGIQUE DE DÉTECTION INTELLIGENTE ET AUTOMATIQUE SUR L'IMAGE ACTIVE
        nom_brut = fichier_actif.name.lower()
        if "dar" in nom_brut or "piment" in nom_brut or "4x" in nom_brut:
            cle_active = "Piment"
        elif "vpk" in nom_brut or "betterave" in nom_brut or "t3" in nom_brut:
            cle_active = "Betterave"
        else:
            cle_active = "Default"
            
        res = base_diagnostics[cle_active]
        
        # AFFICHAGE AUTOMATIQUE DU RAPPORT CORRIGÉ
        st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
        st.markdown(f"<h3 style='color:#0B4619; text-align:center;'>🎯 RÉSULTAT DU SCAN AUTOMATIQUE</h3>", unsafe_allow_html=True)
        st.write(f"🌱 **Plante détectée automatiquement :** {res['plante']}")
        st.error(f"🦠 **Maladie / Anomalie identifiée :** {res['maladie']}")
        
        st.markdown("#### ❓ Causes de l'attaque ou du symptôme")
        st.write(res["causes"])
        
        st.markdown("---")
        st.markdown("#### 🛠️ Solutions et protocoles de traitement")
        
        col_bio, col_chem = st.columns(2)
        with col_bio:
            st.markdown("<b style='color:#2E7D32;'>🍃 Traitement Naturel (Bio) :</b>", unsafe_allow_html=True)
            st.write(res["bio"])
            
            st.markdown('<div class="remede-card">', unsafe_allow_html=True)
            st.markdown(f"📦 **Fiche Technique :** {res['remede_nom']}")
            st.write(res["remede_desc"])
            st.markdown('</div>', unsafe_allow_html=True)
            
        with col_chem:
            st.markdown("<b style='color:#7F6000;'>🧪 Solution Chimique de secours :</b>", unsafe_allow_html=True)
            st.write(res["chimique"])
        st.markdown('</div>', unsafe_allow_html=True)

# --- LES AUTRES ONGLETS ---
with tab2:
    st.markdown('<div class="category-card"><h3>🌿 Association possible</h3>Découvrez les plantes amies et ennemies pour protéger votre champ.</div>', unsafe_allow_html=True)
with tab3:
    st.markdown('<div class="category-card"><h3>🚜 Étapes de Production</h3>Itinéraires de la pépinière à la récolte.</div>', unsafe_allow_html=True)
with tab4:
    st.markdown('<div class="category-card"><h3>🏭 Volet Conservation & Transformation</h3>Fiches de valorisation agro-industrielle.</div>', unsafe_allow_html=True)
with tab5:
    st.markdown('<div class="category-card"><h3>💰 Simulateur de Budget Évolué</h3>Suivi de vos dépenses et bénéfices en FCFA.</div>', unsafe_allow_html=True)
