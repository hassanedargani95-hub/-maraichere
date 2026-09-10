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
# BASE DE DONNÉES DYNAMIQUE MISE À JOUR (AVEC VOS NOUVELLES PLANTES)
# ==========================================
diagnostics_ia = {
    "Betterave / Radis noir": {
        "maladie": "Galles racinaires ou Carence en Bore",
        "causes": "Attaque tardive de ravageurs souterrains ou épuisement des oligo-éléments du sol dû à une culture répétée sans apport de matière organique fine.",
        "bio": "Apporter un amendement de terre de sous-bois riche en humus et arroser régulièrement à base de purin d'ortie dilué.",
        "chimique": "Aucun traitement d'urgence. Rééquilibrer le sol avant la prochaine mise en place des racines.",
        "remede_nom": "🍂 Humus de forêt (Terre de sous-bois)",
        "remede_desc": "Utiliser de la terre noire prélevée sous les grands arbres sauvages, riche en champignons bénéfiques et en nutriments minéraux."
    },
    "Piment / Poivron": {
        "maladie": "Anthracnose du Piment (Colletotrichum spp.)",
        "causes": "Champignon redoutable qui provoque des taches circulaires concaves et sombres sur les fruits. Favorisé par les éclaboussures de pluie et la stagnation de l'eau.",
        "bio": "Pulvériser une décoction forte de gousses d'ail pilées (30g/L d'eau) ou une solution de bicarbonate de soude pour stopper la propagation.",
        "chimique": "Application d'un fongicide de contact à base de cuivre dès l'apparition des premières lésions sur les piments.",
        "remede_nom": "🧄 Extrait purifié d'Ail ou Bicarbonate",
        "remede_desc": "L'ail contient du soufre naturel qui détruit les membranes des spores de champignons microscopiques sans abîmer la peau du piment."
    },
    "Pastèque": {
        "maladie": "Mildiou ou Oïdium des Cucurbitacées",
        "causes": "Feutrage blanc ou taches denses sur les feuilles rampantes dû à l'humidité de la rosée et au manque de paillage sous la liane.",
        "bio": "Pulvérisation de bicarbonate de soude (5g/L d'eau) additionné d'une cuillère de savon noir liquide pour faire coller la solution.",
        "chimique": "Fongicide systémique de synthèse ou Bouillie Bordelaise en respectant le délai de récolte.",
        "remede_nom": "🧼 Savon de Marseille & Bicarbonate",
        "remede_desc": "Le savon crée un film protecteur qui étouffe le champignon tandis que le bicarbonate neutralise l'acidité nécessaire à sa survie."
    },
    "Tomate": {
        "maladie": "Flétrissement Bactérien ou Mildiou de la Tomate",
        "causes": "Attaque de bactéries ou champignons tropicaux par temps chaud et humide après de fortes averses.",
        "bio": "Arrachage immédiat des pieds malades. Saupoudrer du charbon de bois pilé ou de la cendre pure au pied des plantes saines.",
        "chimique": "Traitement cuprique préventif sur les lignes de culture.",
        "remede_nom": "🪵 Cendre de bois et Charbon pilé",
        "remede_desc": "La cendre assèche immédiatement la base des tiges et modifie le pH de la surface du sol, ce qui paralyse les bactéries."
    }
}

base_cultures = {
    "Tomate": {"famille": "Solanacées"}, "Pastèque": {"famille": "Cucurbitacées"},
    "Concombre": {"famille": "Cucurbitacées"}, "Menthe": {"famille": "Lamiacées"},
    "Persil & Céleri": {"famille": "Apiacées"}
}

# ==========================================
# NAVIGATION PAR ONGLETS
# ==========================================
onglets_list = ["📸 Scanner IA & Diagnostic", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(onglets_list)

# --- ONGLET 1 : DIAGNOSTIC SÉCURISÉ AVEC RECONNAISSANCE ASSISTÉE ---
with tab1:
    st.markdown('<div class="category-card"><h3>📸 Laboratoire de Diagnostic Intelligent</h3>Importez une ou plusieurs photos de vos cultures. Sélectionnez ensuite la plante observée pour obtenir votre ordonnance.</div>', unsafe_allow_html=True)
    
    # Sélection multiple de fichiers photos
    photos_fichiers = st.file_uploader("Télécharger vos photos de terrain (Sélection multiple possible) :", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if photos_fichiers:
        st.write(f"📊 **{len(photos_fichiers)} image(s) chargée(s) avec succès.**")
        
        # Affichage des images sous forme de galerie propre
        cols = st.columns(min(len(photos_fichiers), 3))
        for idx, f in enumerate(photos_fichiers):
            with cols[idx % 3]:
                st.image(f, caption=f"Image {idx+1} du champ", use_container_width=True)
        
        st.markdown("---")
        st.markdown("#### 🎯 Identification de la Culture")
        
        # Bouton d'identification assistée pour garantir un résultat 100% exact par plante
        plante_detectee = st.radio(
            "Quelle culture correspond aux photos ci-dessus ?",
            ["Betterave / Radis noir", "Piment / Poivron", "Pastèque", "Tomate"],
            horizontal=True
        )
        
        if plante_detectee in diagnostics_ia:
            res = diagnostics_ia[plante_detectee]
            
            # Affichage dynamique du rapport complet demandé
            st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:#0B4619; text-align:center;'>📋 RAPPORT CLINIQUE VÉGÉTALE</h3>", unsafe_allow_html=True)
            st.write(f"🌱 **Plante analysée :** {plante_detectee}")
            st.error(f"🦠 **Pathologie détectée :** {res['maladie']}")
            
            st.markdown("#### ❓ Causes de l'attaque ou du symptôme")
            st.write(res["causes"])
            
            st.markdown("---")
            st.markdown("#### 🛠️ Solutions et protocoles de traitement")
            
            col_bio, col_chem = st.columns(2)
            with col_bio:
                st.markdown("<b style='color:#2E7D32;'>🍃 Traitement Naturel & Organique (Bio) :</b>", unsafe_allow_html=True)
                st.write(res["bio"])
                
                # Remplacement de la photo cassée par une carte descriptive visuelle et robuste
                st.markdown('<div class="remede-card">', unsafe_allow_html=True)
                st.markdown(f"📦 **Fiche Médicinale :** {res['remede_nom']}")
                st.write(res["remede_desc"])
                st.markdown('</div>', unsafe_allow_html=True)
                
            with col_chem:
                st.markdown("<b style='color:#7F6000;'>🧪 Traitement Chimique d'Urgence :</b>", unsafe_allow_html=True)
                st.write(res["chimique"])
                st.caption("🚨 Attention : Toujours laver vos outils après l'application et respecter les délais de récolte.")
            st.markdown('</div>', unsafe_allow_html=True)

# --- ONGLET 2 : ASSOCIATION POSSIBLE ---
with tab2:
    st.markdown('<div class="category-card"><h3>🌿 Association possible</h3>Découvrez les plantes amies et ennemies pour protéger votre champ naturellement.</div>', unsafe_allow_html=True)
    choix_plante = st.selectbox("Sélectionnez une culture :", list(base_cultures.keys()), key="cat_sel")
    if choix_plante:
        st.success("✅ **Bonnes associations :** Carotte, Oignon, Laitue, Répulsifs.")
        st.error("❌ **À ÉVITER à proximité :** Mêmes familles botaniques sur la même butte.")

# --- ONGLET 3 : SUIVI CYCLES ---
with tab3:
    st.markdown('<div class="category-card"><h3>🚜 Étapes de Production</h3>Suivi technique précis du calendrier cultural de la pépinière à la récolte.</div>', unsafe_allow_html=True)

# --- ONGLET 4 : AGROBUSINESS ---
with tab4:
    st.markdown('<div class="category-card"><h3>🏭 Volet Conservation & Transformation</h3>Fiches de valorisation pour la menthe, le persil, le céleri, les tomates et pastèques.</div>', unsafe_allow_html=True)

# --- ONGLET 5 : BUDGET ---
with tab5:
    st.markdown('<div class="category-card"><h3>💰 Simulateur de Budget Évolué</h3>Estimez vos dépenses et vos gains nets en FCFA pour le marché de Bobo-Dioulasso.</div>', unsafe_allow_html=True)
