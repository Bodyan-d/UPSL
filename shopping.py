import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane
@st.cache_data
def load_data():
    return pd.read_csv('shopping_trends.csv')

data = load_data()

# Ustawienia strony
st.title("Shopping Trends Dashboard")
st.sidebar.title("Opcje analizy")

# Filtr ogólny dla wieku
age_filter = st.sidebar.slider("Wiek klienta", int(data["Age"].min()), int(data["Age"].max()), (18, 60))

# Filtry kategorii dla poszczególnych wykresów
category_filter_1 = st.sidebar.multiselect("Zakupy wg kategorii", data["Category"].unique(), data["Category"].unique())
category_filter_2 = st.sidebar.multiselect("Średnia kwota zakupów wg sezonu", data["Season"].unique(), data["Season"].unique())
category_filter_3 = st.sidebar.multiselect("Liczba klientów wg wieku", data["Category"].unique(), data["Category"].unique())
category_filter_4 = st.sidebar.multiselect("rednia kwota zakupów wg wieku", data["Category"].unique(), data["Category"].unique())
category_filter_5 = st.sidebar.multiselect("Procentowy udział kategorii w zakupach", data["Category"].unique(), data["Category"].unique())
category_filter_6 = st.sidebar.multiselect("Średnia kwota zakupów wg dnia tygodnia", data["Category"].unique(), data["Category"].unique())

# Filtruj dane na podstawie wieku i kategorii dla każdego wykresu
filtered_data_1 = data[(data["Age"] >= age_filter[0]) & 
                       (data["Age"] <= age_filter[1]) & 
                       (data["Category"].isin(category_filter_1))]

filtered_data_2 = data[data["Season"].isin(category_filter_2)]

filtered_data_3 = data[(data["Age"] >= age_filter[0]) & 
                       (data["Age"] <= age_filter[1]) & 
                       (data["Category"].isin(category_filter_3))]

filtered_data_4 = data[(data["Age"] >= age_filter[0]) & 
                       (data["Age"] <= age_filter[1]) & 
                       (data["Category"].isin(category_filter_4))]

filtered_data_5 = data[(data["Age"] >= age_filter[0]) & 
                       (data["Age"] <= age_filter[1]) & 
                       (data["Category"].isin(category_filter_5))]

filtered_data_6 = data[(data["Age"] >= age_filter[0]) & 
                       (data["Age"] <= age_filter[1]) & 
                       (data["Category"].isin(category_filter_6))]

# Wyświetlanie danych
st.write("### Filtrowane dane", filtered_data_1)

# Wykresy
st.write("## Analiza wizualna")

# Wykres 1: Zakupy wg kategorii
st.write("### Liczba zakupów wg kategorii")
category_counts = filtered_data_1["Category"].value_counts()
fig, ax = plt.subplots()
category_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Kategoria")
ax.set_ylabel("Liczba zakupów")
st.pyplot(fig)

# Wykres 2: Średnia kwota zakupów wg sezonu
st.write("### Średnia kwota zakupów wg sezonu")
season_mean = filtered_data_2.groupby("Season")["Purchase Amount (USD)"].mean()
fig, ax = plt.subplots()
season_mean.plot(kind="bar", ax=ax)
ax.set_xlabel("Sezon")
ax.set_ylabel("Średnia kwota zakupów (USD)")
st.pyplot(fig)

# Wykres 3: Liczba klientów wg wieku
st.write("### Liczba klientów wg wieku")
fig, ax = plt.subplots()
filtered_data_3["Age"].hist(bins=20, ax=ax)
ax.set_xlabel("Wiek")
ax.set_ylabel("Liczba klientów")
st.pyplot(fig)

# Wykres 4: Średnia kwota zakupów w zależności od wieku klienta
st.write("### Średnia kwota zakupów wg wieku")
age_mean = filtered_data_4.groupby("Age")["Purchase Amount (USD)"].mean()
fig, ax = plt.subplots()
age_mean.plot(kind="line", ax=ax)
ax.set_xlabel("Wiek")
ax.set_ylabel("Średnia kwota zakupów (USD)")
st.pyplot(fig)

# Wykres 5: Procentowy udział każdej kategorii w ogólnej liczbie zakupów
st.write("### Procentowy udział kategorii w zakupach")
category_percentage = (filtered_data_5["Category"].value_counts() / len(filtered_data_5)) * 100
fig, ax = plt.subplots()
category_percentage.plot(kind="pie", ax=ax, autopct='%1.1f%%', startangle=90)
ax.set_ylabel("")  # Ukryj etykietę osi Y
st.pyplot(fig)
