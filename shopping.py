import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane
@st.cache
def load_data():
    return pd.read_csv('shopping_trends.csv')

data = load_data()

# Ustawienia strony
st.title("Shopping Trends Dashboard")
st.sidebar.title("Opcje analizy")

# Filtry
age_filter = st.sidebar.slider("Wiek klienta", int(data["Age"].min()), int(data["Age"].max()), (18, 60))
category_filter = st.sidebar.multiselect("Kategorie produktów", data["Category"].unique(), data["Category"].unique())

# Filtruj dane
filtered_data = data[(data["Age"] >= age_filter[0]) & 
                     (data["Age"] <= age_filter[1]) & 
                     (data["Category"].isin(category_filter))]

# Wyświetlanie danych
st.write("### Filtrowane dane", filtered_data)

# Wykresy
st.write("## Analiza wizualna")

# Wybór wykresów do wyświetlenia
show_category_chart = st.sidebar.checkbox("Pokaż wykres: Liczba zakupów wg kategorii", value=True)
show_season_chart = st.sidebar.checkbox("Pokaż wykres: Średnia kwota zakupów wg sezonu", value=True)
show_age_chart = st.sidebar.checkbox("Pokaż wykres: Liczba klientów wg wieku", value=True)
show_pie_chart = st.sidebar.checkbox("Pokaż wykres: Procentowy udział kategorii w zakupach", value=True)
show_amount_dist_chart = st.sidebar.checkbox("Pokaż wykres: Rozkład kwot wydanych na zakupy", value=True)
show_age_purchase_chart = st.sidebar.checkbox("Pokaż wykres: Zależność między wiekiem a średnią kwotą zakupu", value=True)

# Wykres 1: Zakupy wg kategorii
if show_category_chart:
    st.write("### Liczba zakupów wg kategorii")
    category_counts = filtered_data["Category"].value_counts()
    fig, ax = plt.subplots()
    category_counts.plot(kind="bar", ax=ax)
    ax.set_xlabel("Kategoria")
    ax.set_ylabel("Liczba zakupów")
    st.pyplot(fig)

# Wykres 2: Średnia kwota zakupów wg sezonu
if show_season_chart:
    st.write("### Średnia kwota zakupów wg sezonu")
    season_mean = filtered_data.groupby("Season")["Purchase Amount (USD)"].mean()
    fig, ax = plt.subplots()
    season_mean.plot(kind="bar", ax=ax)
    ax.set_xlabel("Sezon")
    ax.set_ylabel("Średnia kwota zakupów (USD)")
    st.pyplot(fig)

# Wykres 3: Liczba klientów wg wieku
if show_age_chart:
    st.write("### Liczba klientów wg wieku")
    fig, ax = plt.subplots()
    filtered_data["Age"].hist(bins=20, ax=ax)
    ax.set_xlabel("Wiek")
    ax.set_ylabel("Liczba klientów")
    st.pyplot(fig)

# Wykres 4: Procentowy udział kategorii w zakupach
if show_pie_chart:
    st.write("### Procentowy udział kategorii w zakupach")
    fig, ax = plt.subplots()
    category_counts.plot(kind="pie", autopct='%1.1f%%', ax=ax)
    ax.set_ylabel("")  # Usuwamy etykietę osi Y dla wykresu kołowego
    st.pyplot(fig)

# Wykres 5: Rozkład kwot wydanych na zakupy
if show_amount_dist_chart:
    st.write("### Rozkład kwot wydanych na zakupy")
    fig, ax = plt.subplots()
    filtered_data["Purchase Amount (USD)"].hist(bins=20, ax=ax)
    ax.set_xlabel("Kwota zakupu (USD)")
    ax.set_ylabel("Liczba zakupów")
    st.pyplot(fig)

# Wykres 6: Zależność między wiekiem a średnią kwotą zakupu
if show_age_purchase_chart:
    st.write("### Zależność między wiekiem a średnią kwotą zakupu")
    age_purchase = filtered_data.groupby("Age")["Purchase Amount (USD)"].mean()
    fig, ax = plt.subplots()
    ax.scatter(age_purchase.index, age_purchase.values)
    ax.set_xlabel("Wiek")
    ax.set_ylabel("Średnia kwota zakupu (USD)")
    st.pyplot(fig)
