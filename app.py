import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configuration de la page mobile Premium
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

# Styles graphiques professionnels "Vert Nature"
st.markdown("""
    <style>
        .stApp { background-color: #F3F5F4; }
        .app-header {
            background-color: #2CB674; padding: 25px; border-radius: 0px 0px 25px 25px;
            color: white; text-align: center; margin-top: -60px; margin-bottom: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .diagnostic-box { background-color: #FFFFFF; padding: 20px; border-radius: 15px; box-shadow: 0px 4px 12px rgba(0,0,0,0.05); margin-top: 15px; }
        .doc-section { background-color: #FFFFFF; padding: 15px; border-radius: 12px; margin-bottom: 12px; border-left: 5px solid #2CB674; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="app-header"><h1>📖 La Bible Maraîchère</h1><p>Intelligence Artificielle connectée de terrain</p></div>', unsafe_allow_html=True)

# Base de données pour les onglets conseils
base_cultures = {
    "Tomate": {"famille": "Solanacées", "amis": "Carotte, Oignon, Laitue, Basilic", "ennemis": "Pomme de terre, Poivron"},
    "Pastèque": {"famille": "Cucurbitacées", "amis": "Maïs, Gombo, Tournesol", "ennemis": "Concombre, Melon"},
    "Concombre": {"famille": "Cucurbitacées", "amis": "Salade, Chou, Oignon", "ennemis": "Tomate, Pastèque"}
}

# Navigation par onglets (Ajout du module Documentation)
onglets_list = ["📸 VRAI Scanner IA", "🌿 Association Possible", "🚜 Suivi Cycles", "📚 Documentation"]
tab1, tab2, tab3, tab4 = st.tabs(onglets_list)

# --- ONGLET 1 : RECONNAISSANCE IA ---
with tab1:
    st.markdown('### 📸 Laboratoire de Vision Artificielle Automatique')
    fichier_photo = st.file_uploader("Prendre ou charger une photo de votre culture :", type=["jpg", "png", "jpeg"], key="photo_unique_champ")
    
    if fichier_photo is not None:
        st.success("📊 Image reçue avec succès.")
        image_pil = Image.open(fichier_photo)
        st.markdown("##### 🎯 Image sélectionnée pour le scan :")
        st.image(image_pil, caption=f"Fichier actif : {fichier_photo.name}", width=300)
        
        if st.button("🚀 LANCER L'ANALYSE AUTOMATIQUE PAR INTERNET", key="bouton_ia"):
            if modele_ia is None:
                st.error("Erreur de configuration : Clé API manquante.")
            else:
                with st.spinner("L'IA Cloud analyse les formes et les symptômes de votre image..."):
                    try:
                        consigne_prompt = """
                        Analyse cette photo de culture maraîchère et fournis une réponse structurée :
                        1. 🎯 NOM DE LA PLANTE : Précise quelle plante ou fruits sont présents (ex: Piment, Betterave, Tomate, Pastèque).
                        2. 🦠 NOM DE LA MALADIE OU DU SYMPTÔME : Identifie l'attaque ou la carence visible.
                        3. ❓ CAUSES PROBABLES : Explique pourquoi ce problème est apparu.
                        4. 🍃 TRAITEMENT NATUREL ET PROTOCOLE (BIO) : Donne une recette claire à base de plantes locales (Neem, Ail, Cendre, Piment) ou bicarbonate.
                        5. 🧪 TRAITEMENT CHIMIQUE EN DERNIER RECOURS : Donne un produit homologué avec le Délai Avant Récolte (DAR).
                        """
                        reponse_ia = modele_ia.generate_content([consigne_prompt, image_pil])
                        st.markdown('<div class="diagnostic-box">', unsafe_allow_html=True)
                        st.markdown("<h3 style='color:#0B4619; text-align:center;'>📋 RAPPORT DE DIAGNOSTIC AUTOMATIQUE CLOUD</h3>", unsafe_allow_html=True)
                        st.write(reponse_ia.text)
                        st.markdown('</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Erreur du serveur : {str(e)}")

# --- ONGLET 2 : ASSOCIATIONS ---
with tab2:
    st.markdown('### 🌿 Association possible')
    choix_plante = st.selectbox("Sélectionnez une culture :", list(base_cultures.keys()), key="cat_sel")
    if choix_plante:
        c = base_cultures[choix_plante]
        st.success(f"✅ **Bonnes associations (Amis) :** {c['amis']}")
        st.error(f"❌ **À ÉVITER à proximité (Ennemis) :** {c['ennemis']}")

# --- ONGLET 3 : SUIVI CYCLES ---
with tab3:
    st.markdown('### 🚜 Étapes de Production')
    st.write("Suivi technique précis du calendrier cultural de la pépinière à la récolte.")

# --- ONGLET 4 : EXHAUSTIF - MODULE DOCUMENTATION (NOUVEAU) ---
with tab4:
    st.markdown('### 📚 Encyclopédie Officielle du Maraîchage')
    st.write("Retrouvez ici la classification complète de toutes les plantes cultivées utilisables dans l'application.")
    
    with st.expander("🍅 1. Les Légumes-Fruits (Solanacées & Cucurbitacées)"):
        st.markdown("""
        <div class="doc-section">
            <b>Cultures à haute valeur marchande, exigeantes en eau et compost :</b><br><br>
            • <b>Tomate</b> : Sensible au flétrissement, demande un tuteurage et un paillage rigoureux.<br>
            • <b>Pastèque</b> : Rampe sur le sol, exige de larges buttes plates et beaucoup d'espace.<br>
            • <b>Piment & Poivron</b> : Très sensibles à l'anthracnose par temps de pluie.<br>
            • <b>Aubergine</b> : Variétés locales amères ou grosses violettes, cycle long.<br>
            • <b>Concombre, Melon & Courgette</b> : Demandent un arrosage régulier au pied pour éviter l'amertume.
        </div>
        """, unsafe_allow_html=True)
        
    with st.expander("🥬 2. Les Légumes-Feuilles (Brassicacées & Astéracées)"):
        st.markdown("""
        <div class="doc-section">
            <b>Cultures à cycle court, idéales pour des revenus rapides :</b><br><br>
            • <b>Chou</b> (Pommé ou de Chine) : Très gourmand en azote (fientes de poules de votre poulailler).<br>
            • <b>Laitue / Salade</b> : Préfère un ombrage léger aux heures chaudes.<br>
            • <b>Épinard & Amarante (Boroussou)</b> : Excellente repousse après coupe.<br>
            • <b>Oseille de Guinée (Bissap)</b> : Résistante, cultivée pour ses feuilles vertes.<br>
            • <b>Moringa</b> : Planté en haies denses pour la récolte continue de feuilles riches.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🥕 3. Les Légumes-Racines & Bulbes (Alliacées & Apiacées)"):
        st.markdown("""
        <div class="doc-section">
            <b>Plantes souterraines exigeant un sol très meuble travaillé en profondeur :</b><br><br>
            • <b>Oignon</b> (Violet de Galmi, Prema) : Éviter le fumier frais (risque de pourriture des bulbes).<br>
            • <b>Ail</b> : Excellent répulsif naturel à planter en bordure.<br>
            • <b>Carotte & Betterave</b> : Demandent un sol sableux sans cailloux pour des racines droites.<br>
            • <b>Radis</b> (Rose ou Noir) & <b>Navet</b> : Cycle ultra-rapide (20 à 25 jours).<br>
            • <b>Patate douce</b> : Cultivée pour ses tubercules et ses lianes comestibles.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🌿 4. Les Plantes Aromatiques & Condiments"):
        st.markdown("""
        <div class="doc-section">
            <b>Herbes à forte valeur ajoutée idéales pour la transformation et l'agrobusiness :</b><br><br>
            • <b>Menthe</b> : Plante traçante envahissante, idéale pour fixer la terre des allées de passage.<br>
            • <b>Persil & Céleri</b> : Germination lente (jusqu'à 3 semaines), tremper les graines avant semis.<br>
            • <b>Basilic</b> : Le meilleur protecteur de la tomate contre les mouches piqueuses.<br>
            • <b>Coriandre & Ciboulette</b> : Très demandées sur les marchés urbains.
        </div>
        """, unsafe_allow_html=True)

    with st.expander("🫘 5. Les Légumes-Gousses (Légumineuses)"):
        st.markdown("""
        <div class="doc-section">
            <b>Plantes miracles qui captent l'azote de l'air pour enrichir vos buttes gratuitement :</b><br><br>
            • <b>Haricot vert</b> : Cycle rapide, forte demande commerciale.<br>
            • <b>Niébé (Haricot local)</b> : Très résistant à la sécheresse, excellent précédent cultural.<br>
            • <b>Pois de terre (Voandzou)</b> : S'adapte parfaitement aux sols pauvres.
        </div>
        """, unsafe_allow_html=True)
