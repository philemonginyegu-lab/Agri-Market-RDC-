import streamlit as st

st.set_page_config(
    page_title="Agri Market RDC",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Agri Market RDC")
st.subheader("🔎 Rechercher un produit")

st.write("Trouvez les produits agricoles disponibles près de vous.")

# Recherche du produit
produit = st.text_input(
    "Quel produit recherchez-vous ?",
    placeholder="Exemple : maïs, manioc, tomate..."
)

# Choix de la ville
ville = st.selectbox(
    "📍 Dans quelle ville recherchez-vous ?",
    [
        "Kinshasa",
        "Lubumbashi",
        "Kisangani",
        "Mbuji-Mayi",
        "Kananga",
        "Bukavu",
        "Goma",
        "Kolwezi",
        "Matadi",
        "Autre"
    ]
)

# Quantité souhaitée
quantite = st.number_input(
    "📦 Quantité souhaitée",
    min_value=1,
    value=1,
    step=1
)

unite = st.selectbox(
    "Unité",
    ["kg", "sac", "tonne", "pièce", "tas"]
)

if st.button("🔎 Rechercher"):
    if produit.strip() == "":
        st.warning("⚠️ Veuillez entrer le nom du produit.")
    else:
        st.success(
            f"✅ Recherche lancée pour {produit} à {ville}."
        )

        st.info(
            f"Vous recherchez {quantite} {unite} de {produit}."
        )

        st.write("🌱 Les produits disponibles apparaîtront ici.")
