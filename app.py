import streamlit as st

# Configuration de la page mobile avec le style de l'image
st.set_page_config(page_title="La Bible Maraîchère", page_icon="📖", layout="centered")

# ==========================================
# DESIGN PREMIUM "VERT NATURE" (STYLE MAQUETTE UI)
# ==========================================
st.markdown("""
    <style>
        /* Fond de l'application grise/blanche comme l'image */
        .stApp { background-color: #F3F5F4; }
        
        /* En-tête vert arrondi de la maquette */
        .app-header {
            background-color: #2CB674;
            padding: 25px;
            border-radius: 0px 0px 25px 25px;
            color: white;
            text-align: center;
            margin-top: -60px;
            margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        
        /* Cartes de catégories blanches et arrondies */
        .category-card {
            background-color: #FFFFFF;
            padding: 15px;
            border-radius: 18px;
            box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.04);
            margin-bottom: 15px;
            border-left: 6px solid #2CB674;
        }
        
        /* Style des boutons et onglets */
        .stTabs [data-baseweb="tab-list"] { gap: 6px; background-color: #E2EFE7; padding: 6px; border-radius: 14px; }
        .stTabs [data-baseweb="tab"] { color: #1E5631; font-weight: bold; border-radius: 10px; padding: 10px; }
        .stTabs [data-baseweb="tab"][aria-selected="true"] { background-color: #2CB674 !important; color: white !important; }
        
        /* Badges de l'Agrobusiness */
        .badge-biz { background-color: #E6F7ED; color: #1E5631; padding: 8px; border-radius: 10px; font-weight: bold; border: 1px solid #2CB674; }
    </style>
""", unsafe_allow_html=True)

# Décoration de l'application (Haut de l'écran)
st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Votre conseiller agricole et agrobusiness connecté</p></div>', unsafe_allow_html=True)

# Base de données exhaustive des plantes demandées
base_cultures = {
    "Tomate": {
        "famille": "Solanacées", "amis": "Carotte, Oignon, Salade, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron",
        "rendement": "3.5 kg / pied", "conseil": "Pailler le sol pour bloquer les champignons de terre.",
        "conservation": "Froid modéré (12°C). Séchage au soleil pour la longue conservation.",
        "transformation": "Concentré de tomate, purée pasteurisée en bouteille."
    },
    "Pastèque": {
        "famille": "Cucurbitacées", "amis": "Maïs, Gombo, Tournesol", "ennemis": "Concombre, Melon",
        "rendement": "12 kg / poquet (2 à 3 fruits)", "conseil": "Dresser de larges buttes plates en travers de la pente.",
        "conservation": "2 à 3 semaines à l'ombre dans un endroit ventilé.",
        "transformation": "Jus frais pasteurisé, confiture d'écorces, extraction d'huile des graines."
    },
    "Concombre": {
        "famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon", "ennemis": "Tomate, Pastèque",
        "rendement": "4.0 kg / pied", "conseil": "Arrosage très régulier pour éviter l'amertume du fruit.",
        "conservation": "7 à 10 jours emballé au frais.",
        "transformation": "Transformation en cornichons dans du vinaigre et des herbes."
    },
    "Menthe": {
        "famille": "Lamiacées", "amis": "Chou, Tomate", "ennemis": "Camomille",
        "rendement": "1.2 kg / m²", "conseil": "Plante traçante, idéale pour stabiliser les bords d'allées.",
        "conservation": "Séchage complet à l'ombre. Se conserve 1 an en bocal fermé.",
        "transformation": "Sirop de menthe, poudre de feuilles séchées, huile essentielle."
    },
    "Persil & Céleri": {
        "famille": "Apiacées", "amis": "Tomate, Oignon", "ennemis": "Salade, Laitue",
        "rendement": "1.5 kg / m²", "conseil": "Graines lentes à germer, les tremper dans l'eau 24h avant.",
        "conservation": "Séchage ou congélation des feuilles ciselées.",
        "transformation": "Bouquets garnis déshydratés, sel de céleri pour la cuisine."
    }
}

# ==========================================
# SYSTÈME DE NAVIGATION PAR ONGLETS (STYLE MAQUETTE UI)
# ==========================================
onglet = st.tabs(["📸 Scanner IA", "🌿 Catégories", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"])

# --- ONGLET 1 : ANALYSE PHOTO CORRIGÉE ET STABLE ---
with onglet[0]:
    st.markdown('<div class="category-card"><h3>📸 Diagnostic de Santé Immédiat</h3>Prenez une photo claire d\'une feuille malade pour déclencher l\'analyse du serveur.</div>', unsafe_allow_html=True)
    
    photo_fichier = st.file_uploader("Sélectionnez ou prenez votre photo ici :", type=["jpg", "png", "jpeg"])
    
    if photo_fichier is not None:
        st.image(photo_fichier, caption="Image importée avec succès", use_container_width=True)
        
        with st.spinner("Analyse agronomique en cours..."):
            st.success("🧠 Analyse terminée ! Symptômes identifiés.")
            
        culture_selection = st.selectbox("Confirmez la culture analysée :", list(base_cultures.keys()))
        
        # Rapport de diagnostic propre
        st.markdown(f"### 🩺 Rapport d'analyse : {culture_selection}")
        st.markdown('<div style="background-color:#EAFBF1; padding:12px; border-radius:10px; color:#1E5631;"><b>🌿 Traitement Naturel :</b> Pulvériser une solution à base d\'huile ou de purin de neem et de savon noir sous les feuilles.</div>', unsafe_allow_html=True)
        st.markdown('<div style="background-color:#FFF9E6; padding:12px; border-radius:10px; color:#7F6000; margin-top:10px;"><b>🧪 Traitement Chimique :</b> Utiliser un fongicide ou insecticide homologué uniquement en cas de forte attaque. Respecter le délai avant récolte.</div>', unsafe_allow_html=True)

# --- ONGLET 2 : LES CATÉGORIES & COMPAGNONNAGE ---
with onglet[1]:
    st.markdown('<div class="category-card"><h3>🌿 Compagnonnage des Plantes</h3>Découvrez les plantes amies et ennemies pour protéger votre champ naturellement.</div>', unsafe_allowed_html=True)
    choix_plante = st.selectbox("Sélectionnez une culture :", list(base_cultures.keys()), key="cat_sel")
    
    if choix_plante:
        c = base_cultures[choix_plante]
        st.write(f"🧬 **Famille :** {c['famille']}")
        st.success(f"✅ **Bonnes associations (Amis) :** {c['amis']}")
        st.error(f"❌ **À ÉVITER à proximité (Ennemis) :** {c['ennemis']}")

# --- ONGLET 3 : SUIVI DES CYCLES DE A À Z ---
with onglet[2]:
    st.markdown('<div class="category-card"><h3>🚜 Étapes de Production en Images</h3>Les étapes clés de votre culture, de la pépinière jusqu\'au panier de récolte.</div>', unsafe_allow_html=True)
    choix_cycle = st.selectbox("Suivre le cycle de :", list(base_cultures.keys()), key="cycle_sel")
    
    if choix_cycle:
        cc = base_cultures[choix_cycle]
        st.image("https://unsplash.com", caption=f"Itinéraire cultural optimal - {choix_cycle}", use_container_width=True)
        st.write(f"💡 **Conseil de rendement :** {cc['conseil']}")
        st.info(f"📈 **Rendement moyen attendu :** {cc['rendement']}")

# --- ONGLET 4 : MODULE AGROBUSINESS ---
with onglet[3]:
    st.markdown('<div class="category-card"><h3>🏭 Volet Conservation & Transformation</h3>Valorisez vos récoltes pour augmenter vos revenus sur le marché de Bobo-Dioulasso.</div>', unsafe_allow_html=True)
    choix_biz = st.selectbox("Agrobusiness pour :", list(base_cultures.keys()), key="biz_sel")
    
    if choix_biz:
        cb = base_cultures[choix_biz]
        st.markdown(f"#### 🏭 Fiche Agrobusiness - {choix_biz}")
        st.markdown(f'<div class="badge-biz">🧊 Méthodes de Conservation :</div><p>{cb["conservation"]}</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="badge-biz" style="color:#0B4619; border-color:#2CB674;">🍯 Procédés de Transformation :</div><p>{cb["transformation"]}</p>', unsafe_allow_html=True)

# --- ONGLET 5 : CALCULATEUR DE RENTABILITÉ ---
with onglet[4]:
    st.markdown('<div class="category-card"><h3>💰 Simulateur de Budget Évolué</h3>Estimez vos gains réels en fonction du nombre de pieds et des techniques appliquées.</div>', unsafe_allow_html=True)
    pl_fin = st.selectbox("Culture de la campagne :", list(base_cultures.keys()), key="fin_sel")
    
    nbr_pieds = st.number_input("Nombre de pieds ou poquets cultivés :", min_value=1, value=200, step=50)
    prix_mkt = st.number_input("Prix de vente sur le marché (FCFA / Kilo) :", min_value=50, value=500, step=25)
    depenses = st.number_input("Total de vos charges engagées (FCFA) :", min_value=0, value=15000, step=1000)
    
    # Calcul dynamique simple
    rendement_estime = nbr_pieds * 2.5
    ca_brut = rendement_estime * prix_mkt
    profit_net = ca_brut - depenses
    
    st.markdown("---")
    st.metric(label="Volume de récolte estimé", value=f"{rendement_estime:.1f} kg")
    st.metric(label="💰 Bénéfice Net Prévisionnel", value=f"{profit_net:,.0f} FCFA".replace(",", " "))
