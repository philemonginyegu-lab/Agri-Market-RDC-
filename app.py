import streamlit as st

st.set_page_config(
    page_title="Agri Market RDC",
    page_icon="🌾",
    layout="centered"
)

st.title("🌾 Agri Market RDC")
st.subheader("🔎 Rechercher un produit")

st.write(
    "Trouvez des produits agricoles et contactez "
    "directement les producteurs."
)

# Villes disponibles
villes = [
    "Kinshasa",
    "Lubumbashi",
    "Matadi",
    "Mbuji-Mayi",
    "Kananga",
    "Kisangani",
    "Goma",
    "Bukavu"
    "Kikwit"
]

# Données fictives pour tester l'application
produits = [
    {
        "nom": "Manioc",
        "ville": "Kinshasa",
        "quantite": 200,
        "prix": 1000,
        "producteur": "Producteur Démo 1",
        "telephone": ""
    },
    {
        "nom": "Maïs",
        "ville": "Kinshasa",
        "quantite": 150,
        "prix": 1800,
        "producteur": "Producteur Démo 2",
        "telephone": ""
    },
    {
        "nom": "Haricots",
        "ville": "Kinshasa",
        "quantite": 80,
        "prix": 2500,
        "producteur": "Producteur Démo 3",
        "telephone": ""
    },
    {
        "nom": "Tomate",
        "ville": "Lubumbashi",
        "quantite": 100,
        "prix": 2000,
        "producteur": "Producteur Démo 4",
        "telephone": ""
    }
]

st.info(
    "Les offres affichées ci-dessous sont fictives. "
    "Elles servent uniquement à tester l'application."
)

with st.form("recherche_produit"):

    recherche = st.text_input(
        "Quel produit recherchez-vous ?",
        placeholder="Ex. : manioc, maïs, tomate..."
    )

    ville = st.selectbox(
        "Dans quelle ville ?",
        villes
    )

    quantite = st.number_input(
        "Quantité souhaitée (kg)",
        min_value=1,
        value=1,
        step=1
    )

    rechercher = st.form_submit_button(
        "🔎 Rechercher"
    )

if rechercher:

    if not recherche.strip():
        st.warning("Veuillez saisir le nom du produit.")

    else:
        resultats = [
            p for p in produits
            if recherche.strip().casefold()
            in p["nom"].casefold()
            and p["ville"] == ville
            and p["quantite"] >= quantite
        ]

        if resultats:
            st.success(
                f"{len(resultats)} offre(s) trouvée(s)."
            )

            for p in resultats:

                st.markdown("---")
                st.subheader(f"🌱 {p['nom']}")

                st.write(f"📍 Ville : {p['ville']}")
                st.write(
                    f"📦 Quantité disponible : "
                    f"{p['quantite']} kg"
                )
                st.write(
                    f"💰 Prix au kg : "
                    f"{p['prix']:,} CDF".replace(",", " ")
                )
                st.write(
                    f"👨‍🌾 {p['producteur']}"
                )

                total = quantite * p["prix"]

                st.write(
                    f"🧾 Coût estimé : "
                    f"{total:,} CDF".replace(",", " ")
                )

                if p["telephone"]:
                    st.link_button(
                        "📞 Contacter le producteur",
                        "https://wa.me/"
                        + p["telephone"]
                    )
                else:
                    st.caption(
                        "Contact à enregistrer lors "
                        "de l'inscription du producteur."
                    )

        else:
            st.warning(
                "Aucune offre correspondant à votre "
                "recherche n'a été trouvée."
)
