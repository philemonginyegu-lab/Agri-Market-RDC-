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
        produits = {
            "maïs": {
                "prix": 2500,
                "unite": "kg",
                "quantite": 500
            },
            "manioc": {
                "prix": 1500,
                "unite": "kg",
                "quantite": 800
            },
            "tomate": {
                "prix": 3000,
                "unite": "kg",
                "quantite": 300
            },
            "oignon": {
                "prix": 4000,
                "unite": "kg",
                "quantite": 250
            },
            "banane": {
                "prix": 2000,
                "unite": "kg",
                "quantite": 400
            }
        }

        recherche = produit.lower().strip()

        if recherche in produits:
            p = produits[recherche]

            st.success("✅ Produit disponible !")

            st.subheader(f"🌱 {produit.capitalize()}")

            st.write(f"📍 Ville : {ville}")
            st.write(f"💰 Prix : {p['prix']:,} CDF / {p['unite']}")
            st.write(f"📦 Quantité disponible : {p['quantite']} {p['unite']}")

            st.button("📞 Contacter le producteur")

        else:
            st.info(
                "ℹ️ Aucun produit trouvé pour le moment. "
                "Essayez : maïs, manioc, tomate, oignon ou banane."
)
