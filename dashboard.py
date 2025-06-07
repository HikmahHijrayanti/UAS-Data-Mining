import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style matplotlib/seaborn agar bagus
sns.set_style('whitegrid')

# Judul Dashboard
st.title("Dashboard Prediksi Risiko Dropout Mahasiswa")

# Load data (sesuaikan path file CSV kamu)
@st.cache_data
def load_data():
    df = pd.read_csv('dropout_dataset.csv')
    return df

data = load_data()

# Menampilkan ringkasan data
total_mahasiswa = len(data)
risiko_tinggi = data['dropout_risk'].sum()
risiko_aman = total_mahasiswa - risiko_tinggi

st.subheader("Ringkasan Risiko Dropout")
st.write(f"Total Mahasiswa: **{total_mahasiswa}**")
st.write(f"Risiko Tinggi Dropout: **{risiko_tinggi}** ({risiko_tinggi/total_mahasiswa*100:.2f}%)")
st.write(f"Risiko Aman: **{risiko_aman}** ({risiko_aman/total_mahasiswa*100:.2f}%)")

# Filter berdasarkan area tempat tinggal
if 'residence_area' in data.columns:
    area_filter = st.selectbox(
        "Filter Berdasarkan Area Tempat Tinggal",
        options=['All'] + list(data['residence_area'].unique())
    )
    if area_filter != 'All':
        data = data[data['residence_area'] == area_filter]

# Visualisasi 1: Risiko Dropout Berdasarkan Status Kerja
st.subheader("Risiko Dropout Berdasarkan Status Kerja")
plt.figure(figsize=(8,4))
sns.countplot(data=data, x='working_status', hue='dropout_risk')
plt.xlabel("Status Kerja (0=Tidak Bekerja, 1=Bekerja)")
plt.ylabel("Jumlah Mahasiswa")
plt.legend(title='Risiko Dropout', labels=['Aman', 'Risiko'])
st.pyplot(plt.gcf())
plt.clf()

# Visualisasi 2: Tren IPK Semester per Risiko Dropout
st.subheader("Rata-rata IPK Semester per Risiko Dropout")
ipk_cols = ['gpa_sem1', 'gpa_sem2', 'gpa_sem3', 'gpa_sem4']
avg_ipk = data.groupby('dropout_risk')[ipk_cols].mean().T
avg_ipk.columns = ['Aman', 'Risiko']
st.line_chart(avg_ipk)

# Tambah visualisasi lain sesuai kebutuhan

st.write("### Informasi tambahan")
st.write("Dashboard ini membantu pihak rektorat memantau risiko dropout dan faktor pendukungnya agar dapat mengambil tindakan yang tepat.")