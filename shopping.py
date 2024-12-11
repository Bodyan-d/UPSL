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

# Wykres 1: Zakupy wg kategorii
st.write("### Liczba zakupów wg kategorii")
category_counts = filtered_data["Category"].value_counts()
fig, ax = plt.subplots()
category_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Kategoria")
ax.set_ylabel("Liczba zakupów")
st.pyplot(fig)

# Wykres 2: Średnia kwota zakupów wg sezonu
st.write("### Średnia kwota zakupów wg sezonu")
season_mean = filtered_data.groupby("Season")["Purchase Amount (USD)"].mean()
fig, ax = plt.subplots()
season_mean.plot(kind="bar", ax=ax)
ax.set_xlabel("Sezon")
ax.set_ylabel("Średnia kwota zakupów (USD)")
st.pyplot(fig)

# Wykres 3: Liczba klientów wg wieku
st.write("### Liczba klientów wg wieku")
fig, ax = plt.subplots()
filtered_data["Age"].hist(bins=20, ax=ax)
ax.set_xlabel("Wiek")
ax.set_ylabel("Liczba klientów")
st.pyplot(fig)

# Wykres 4: Suma zakupów wg kategorii
st.write("### Suma zakupów wg kategorii")
category_sum = filtered_data.groupby("Category")["Purchase Amount (USD)"].sum()
fig, ax = plt.subplots()
category_sum.plot(kind="bar", ax=ax, color="green")
ax.set_xlabel("Kategoria")
ax.set_ylabel("Suma zakupów (USD)")
st.pyplot(fig)

# Wykres 5: Rozkład kwot zakupów
st.write("### Rozkład kwot zakupów")
fig, ax = plt.subplots()
filtered_data.boxplot(column="Purchase Amount (USD)", ax=ax, vert=False, patch_artist=True, boxprops=dict(facecolor="orange"))
ax.set_xlabel("Kwota zakupów (USD)")
ax.set_ylabel("Rozkład")
st.pyplot(fig)

# Wykres 6: Średnia kwota zakupów wg wieku
st.write("### Średnia kwota zakupów wg wieku")
age_mean = filtered_data.groupby("Age")["Purchase Amount (USD)"].mean()
fig, ax = plt.subplots()
age_mean.plot(ax=ax, color="red")
ax.set_xlabel("Wiek")
ax.set_ylabel("Średnia kwota zakupów (USD)")
st.pyplot(fig)
