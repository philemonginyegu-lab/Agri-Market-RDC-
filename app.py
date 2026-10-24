
import streamlit as st
from supabase import create_client

st.set_page_config(
    page_title="Agri Market RDC",
    page_icon="🌾",
    layout="centered"
)

# Connexion à Supabase
try:
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    supabase = create_client(url, key)
except Exception:
    st.error(
        "Connexion Supabase impossible. "
        "Vérifiez les secrets SUPABASE_URL et SUPABASE_KEY."
    )
    st.stop()

st.title("🌾 Agri Market RDC")
st.write(
    "La plateforme qui relie les producteurs agricoles "
    "aux acheteurs en République démocratique du Congo."
)

# --------------------------------------------------
# 1. ENREGISTRER UN PRODUCTEUR
# --------------------------------------------------

st.header("👨‍🌾 Enregistrer un producteur")

with st.form("form_producteur"):
    nom_producteur = st.text_input("Nom du producteur")
    ville_producteur = st.selectbox(
        "Ville du producteur",
        ["Kinshasa", "Lubumbashi", "Matadi",
         "Mbuji-Mayi", "Kananga", "Kisangani", "Autre"]
    )
    contact_producteur = st.text_input(
        "Téléphone ou contact"
    )

    autre_ville = ""
    if ville_producteur == "Autre":
        autre_ville = st.text_input("Précisez la ville")

    enregistrer_producteur = st.form_submit_button(
        "Enregistrer le producteur"
    )

if enregistrer_producteur:
    ville = autre_ville.strip() if ville_producteur == "Autre" else ville_producteur

    if not nom_producteur.strip() or not contact_producteur.strip() or not ville:
        st.warning("Remplissez le nom, la ville et le contact.")
    else:
        try:
            resultat = supabase.table("producteurs").insert({
                "nom_producteur": nom_producteur.strip(),
                "ville": ville,
                "contact": contact_producteur.strip()
            }).execute()

            st.success("Producteur enregistré avec succès.")
            st.write("Identifiant du producteur :")
            st.code(str(resultat.data[0]["id_producteurs"]))

        except Exception as e:
            st.error("Erreur lors de l'enregistrement du producteur.")
            st.caption(str(e))

# --------------------------------------------------
# 2. ENREGISTRER UN PRODUIT
# --------------------------------------------------

st.divider()
st.header("📦 Enregistrer un produit")

try:
    producteurs = (
        supabase.table("producteurs")
        .select("id_producteurs, nom_producteur, ville, contact")
        .order("nom_producteur")
        .execute()
        .data
    )
except Exception as e:
    producteurs = []
    st.error("Impossible de charger les producteurs.")
    st.caption(str(e))

if producteurs:
    choix_producteur = st.selectbox(
        "Choisissez le producteur",
        producteurs,
        format_func=lambda p: (
            f'{p["nom_producteur"]} — {p["ville"]}'
        ),
        key="choix_producteur"
    )

    with st.form("form_produit"):
        nom_produit = st.text_input(
            "Nom du produit",
            placeholder="Ex. : Haricots blancs"
        )
        quantite = st.number_input(
            "Quantité disponible",
            min_value=1,
            value=20,
            step=1
        )
        unite = st.selectbox(
            "Unité",
            ["sac", "kg", "tonne", "pièce", "tas"]
        )
        prix = st.number_input(
            "Prix unitaire en CDF",
            min_value=0,
            value=0,
            step=500
        )

        enregistrer_produit = st.form_submit_button(
            "Enregistrer le produit"
        )

    if enregistrer_produit:
        if not nom_produit.strip():
            st.warning("Indiquez le nom du produit.")
        else:
            try:
                supabase.table("produits").insert({
                    "nom_produit": nom_produit.strip(),
                    "quantite": int(quantite),
                    "unite": unite,
                    "prix": int(prix),
                    "ville": choix_producteur["ville"],
                    "id_producteur": choix_producteur["id_producteurs"]
                }).execute()

                st.success("Produit enregistré avec succès.")

            except Exception as e:
                st.error("Erreur lors de l'enregistrement du produit.")
                st.caption(str(e))
else:
    st.info(
        "Enregistrez d'abord un producteur pour pouvoir "
        "associer ses produits à son identifiant."
    )

# --------------------------------------------------
# 3. RECHERCHER LES PRODUITS
# --------------------------------------------------

st.divider()
st.header("🔎 Rechercher un produit")

with st.form("form_recherche"):
    recherche = st.text_input(
        "Nom du produit",
        placeholder="Ex. : Haricots blancs"
    )
    ville_recherche = st.selectbox(
        "Ville de recherche",
        ["Toutes les villes", "Kinshasa", "Lubumbashi",
         "Matadi", "Mbuji-Mayi", "Kananga",
         "Kisangani", "Autre"],
        key="ville_recherche"
    )

    ville_autre_recherche = ""
    if ville_recherche == "Autre":
        ville_autre_recherche = st.text_input(
            "Précisez la ville",
            key="autre_recherche"
        )

    rechercher = st.form_submit_button("🔎 Rechercher")

if rechercher:
    try:
        requete = (
            supabase.table("produits")
            .select(
                "*, producteurs!inner("
                "id_producteurs, nom_producteur, contact, ville)"
            )
        )

        if recherche.strip():
            requete = requete.ilike(
                "nom_produit",
                f"%{recherche.strip()}%"
            )

        ville_finale = (
            ville_autre_recherche.strip()
            if ville_recherche == "Autre"
            else ville_recherche
        )

        if ville_finale != "Toutes les villes":
            requete = requete.ilike("ville", ville_finale)

        resultats = requete.execute().data

        if resultats:
            st.success(
                f"{len(resultats)} produit(s) trouvé(s)"
            )

            for produit in resultats:
                producteur = produit.get("producteurs") or {}

                with st.container(border=True):
                    st.subheader(
                        f'🌾 {produit.get("nom_produit", "Produit")}'
                    )
                    st.write(
                        f'📍 Ville : {produit.get("ville", "Non précisée")}'
                    )
                    st.write(
                        f'📦 Quantité : {produit.get("quantite", "Non précisée")} '
                        f'{produit.get("unite", "")}'
                    )

                    prix = produit.get("prix")
                    if prix is not None:
                        st.write(f"💰 Prix unitaire : {prix:,} CDF")

                    st.write(
                        "👨‍🌾 Producteur : "
                        + str(producteur.get(
                            "nom_producteur", "Non renseigné"
                        ))
                    )
                    st.write(
                        "🆔 Identifiant producteur : "
                        + str(produit.get("id_producteur", "Non renseigné"))
                    )
                    st.write(
                        "📞 Contact : "
                        + str(producteur.get(
                            "contact", "Non renseigné"
                        ))
                    )
        else:
            st.info(
                "Aucun produit correspondant. "
                "Vérifiez le nom et la ville."
            )

    except Exception as e:
        st.error(
            "La recherche a échoué. Vérifiez les colonnes "
            "et la relation entre produits et producteurs."
        )
        st.caption(str(e))

st.divider()
st.caption("Agri Market RDC — Du producteur au consommateur 🇨🇩")
