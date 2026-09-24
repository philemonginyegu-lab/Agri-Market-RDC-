import streamlit as st

st.set_page_config(
    page_title="Agri Market RDC",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Agri Market RDC")
st.subheader("La plateforme qui relie producteurs et acheteurs")

st.write(
    "Trouvez des produits agricoles, publiez vos produits "
    "et consultez les offres disponibles en RDC."
)

st.divider()

st.header("Que voulez-vous faire ?")

choix = st.radio(
    "Sélectionnez une option :",
    [
        "🛒 Acheter un produit",
        "🌱 Vendre un produit",
        "🔎 Rechercher un produit"
    ]
)

if choix == "🛒 Acheter un produit":
    st.info("Vous pourrez rechercher les produits disponibles près de vous.")

elif choix == "🌱 Vendre un produit":
    st.info("Vous pourrez publier votre produit, sa quantité et son prix.")

elif choix == "🔎 Rechercher un produit":
    st.info("Vous pourrez rechercher un produit agricole par nom ou par ville.")

st.divider()

st.caption("Agri Market RDC 🇨🇩")
