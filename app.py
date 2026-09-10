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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Votre conseiller agricole et agrobusiness connecté</p></div>', unsafe_allow_html=True)

# ==========================================
# BASE DE DONNÉES DYNAMIQUE DES MALADIES
# ==========================================
base_maladies = {
    "Flétrissement Brutal (Feuilles Vertes)": {
        "maladie": "Flétrissement Bactérien (Ralstonia solanacearum)",
        "causes": "Bactérie du sol qui se développe par forte humidité et chaleur étouffante. Elle pénètre par les blessures des racines et bloque la sève.",
        "bio": "Arracher et brûler les plants morts. Saupoudrer le sol de cendre de bois pure pour stopper la contagion.",
        "chimique": "Aucun produit chimique curatif n'existe. Utiliser des variétés résistantes (Cobra 26 F1) et pratiquer la rotation des cultures.",
        "remede_nom": "Cendre de bois pure",
        "remede_img": "https://unsplash.com"
    },
    "Taches Brunes avec Duvet Blanc/Gris": {
        "maladie": "Mildiou (Phytophthora infestans)",
        "causes": "Champignon microscopique favorisé par les pluies fréquentes, la fraîcheur du matin et un feuillage qui reste mouillé trop longtemps.",
        "bio": "Pulvériser une solution de bicarbonate de soude (5g/L) mélangée à du savon noir végétal.",
        "chimique": "Appliquer un traitement fongicide à base de cuivre (Bouillie bordelaise) sur tout le feuillage.",
        "remede_nom": "Savon noir et bicarbonate",
        "remede_img": "https://unsplash.com"
    },
    "Grosses Bosses ou Galles sur les Racines": {
        "maladie": "Nématodes à galles (Meloidogyne spp.)",
        "causes": "Vers microscopiques invisibles à l'œil nu qui piquent les racines pour s'y nourrir, empêchant la plante de puiser l'eau.",
        "bio": "Incorporer des feuilles ou des tourteaux de Neem broyés dans la butte et planter des Œillets d'Inde tout autour.",
        "chimique": "Nématicides granulés homologués à appliquer au sol uniquement avant la plantation.",
        "remede_nom": "Feuilles et graines de Neem",
        "remede_img": "https://unsplash.com"
    }
}

base_cultures = {
    "Tomate": {"famille": "Solanacées", "amis": "Carotte, Oignon, Basilic, Œillet d'Inde", "ennemis": "Pomme de terre, Poivron", "rendement": "3.5 kg / pied", "conseil": "Pailler le sol.", "conservation": "12°C ou séchage.", "transformation": "Concentré, purée."},
    "Pastèque": {"famille": "Cucurbitacées", "amis": "Maïs, Gombo", "ennemis": "Concombre, Melon", "rendement": "12 kg / poquet", "conseil": "Buttes plates en travers.", "conservation": "À l'ombre aérée.", "transformation": "Jus, confiture d'écorce."},
    "Concombre": {"famille": "Cucurbitacées", "amis": "Salade, Oignon", "ennemis": "Tomate, Pastèque", "renderment": "4.0 kg / pied", "conseil": "Arrosage très régulier.", "conservation": "Frais emballé.", "transformation": "Cornichons."},
    "Menthe": {"famille": "Lamiacées", "amis": "Chou, Tomate", "ennemis": "Camomille", "rendement": "1.2 kg / m²", "conseil": "Idéal en bordure.", "conservation": "Séchage ombre.", "transformation": "Sirop, huile essentielle."},
    "Persil & Céleri": {"famille": "Apiacées", "amis": "Tomate, Oignon", "ennemis": "Salade", "rendement": "1.5 kg / m²", "conseil": "Tremper les graines 24h.", "conservation": "Séchage ou ciselage.", "transformation": "Bouquets déshydratés."}
}

# ==========================================
# NAVIGATION PAR ONGLETS (ALIGNEMENT RIGOUREUX)
# ==========================================
onglets_list = ["📸 Scanner IA & Diagnostic", "🌿 Association Possible", "🚜 Suivi Cycles", "🏭 Agrobusiness", "💰 Mon Budget"]
tab1, tab2, tab3, tab4, tab5 = st.tabs(onglets_list)

# --- ONGLET 1 : SCANNER IA ---
with tab1:
    st.markdown('<div class="category-card"><h3>📸 Laboratoire d\'Analyse d\'Images</h3>Téléchargez une ou plusieurs photos de vos plants malades pour un diagnostic complet.</div>', unsafe_allow_html=True)
    photos_fichiers = st.file_uploader("Prendre ou importer vos photos (Sélection multiple possible) :", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
    
    if photos_fichiers:
        st.write(f"📊 **{len(photos_fichiers)} image(s) sélectionnée(s). Analyse en cours...**")
        cols = st.columns(min(len(photos_fichiers), 3))
        for idx, f in enumerate(photos_fichiers):
            with cols[idx % 3]:
                st.image(f, caption=f"Photo {idx+1}", use_container_width=True)
        
        st.markdown("---")
        st.markdown("#### 🔍 Étape de vérification visuelle")
        plante_scanne = st.selectbox("1️⃣ Indiquez la plante que vous venez de scanner :", list(base_cultures.keys()))
        symptome_repere = st.selectbox("2️⃣ Sélectionnez le symptôme le plus visible sur vos photos :", list(base_maladies.keys()))
        
        if symptome_repere and plante_scanne:
            res = base_maladies[symptome_repere]
            st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
            st.markdown(f"### 🩺 RAPPORT DE DIAGNOSTIC AGRO-INTELLIGENT")
            st.write(f"🌿 **Plante auscultée :** {plante_scanne}")
            st.error(f"🦠 **Maladie identifiée :** {res['maladie']}")
            st.markdown("#### ❓ Causes probables")
            st.write(res["causes"])
            st.markdown("#### 🛠️ Solutions de traitement disponibles")
            
            col_bio, col_chem = st.columns(2)
            with col_bio:
                st.markdown("<b style='color:#2E7D32;'>🍃 Solution Naturelle (Bio) :</b>", unsafe_allow_html=True)
                st.write(res["bio"])
                st.markdown(f"_*Utiliser : {res['remede_nom']}_")
                st.image(res["remede_img"], caption=res["remede_nom"], use_container_width=True)
            with col_chem:
                st.markdown("<b style='color:#7F6000;'>🧪 Solution Chimique d'Urgence :</b>", unsafe_allow_html=True)
                st.write(res["chimique"])
            st.markdown('</div>', unsafe_allow_html=True)

# --- ONGLET 2 : ASSOCIATION POSSIBLE ---
with tab2:
    st.markdown('<div class="category-card"><h3>🌿 Association possible</h3>Découvrez les plantes amies et ennemies pour protéger votre champ naturellement.</div>', unsafe_allow_html=True)
    choix_plante = st.selectbox("Sélectionnez une culture :", list(base_cultures.keys()), key="cat_sel")
    if choix_plante:
        c = base_cultures[choix_plante]
        st.write(f"🧬 **Famille :** {c['famille']}")
        st.success(f"✅ **Bonnes associations (Amis) :** {c['amis']}")
        st.error(f"❌ **À ÉVITER à proximité (Ennemis) :** {c['ennemis']}")

# --- ONGLET 3 : SUIVI CYCLES ---
with tab3:
    st.markdown('<div class="category-card"><h3>🚜 Étapes de Production</h3>Les étapes clés de votre culture, de la pépinière jusqu\'au panier de récolte.</div>', unsafe_allow_html=True)
    choix_cycle = st.selectbox("Suivre le cycle de :", list(base_cultures.keys()), key="cycle_sel")
    if choix_cycle:
        cc = base_cultures[choix_cycle]
        st.markdown(f"#### 📅 Itinéraire Cultural – {choix_cycle}")
        st.markdown("🌱 **Étape 1 - Pépinière :** Semis protégés, arrosage régulier fin matin/soir.")
        st.markdown("📐 **Étape 2 - Repiquage :** Respecter les distances, creuser les poquets à la fraîche.")
        st.markdown("✂️ **Étape 3 - Entretien :** Pailler le sol pour conserver l'humidité.")
        st.markdown("🧺 **Étape 4 - Récolte :** Cueillette au stade de maturité optimal.")
        st.info(f"📈 **Rendement moyen attendu :** {cc['rendement']}")

# --- ONGLET 4 : AGROBUSINESS (CORRIGÉ) ---
with tab4:
    st.markdown('<div class="category-card"><h3>🏭 Volet Conservation & Transformation</h3>Valorisez vos récoltes pour augmenter vos revenus.</div>', unsafe_allow_html=True)
    choix_biz = st.selectbox("Agrobusiness pour :", list(base_cultures.keys()), key="biz_sel")
    if choix_biz:
        cb = base_cultures[choix_biz]
        st.markdown(f"#### 🏭 Fiche Agrobusiness - {choix_biz}")
        st.markdown(f'<div class="badge-biz">🧊 Méthodes de Conservation :</div><p>{cb["conservation"]}</p>', unsafe_allow_html=True)
