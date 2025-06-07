# UAS-Data-Mining
Sistem Prediksi Mahasiswa Berisiko Tinggi Drop Out (DO)

## Kelompok 11
Nama Anggota Kelompok
1. Atika Oktavianti (G1A022020)
2. Hikmah Hijrayanti (G1A022026)

Sistem yang kami buat ini dirancang bertujuan untuk melakukan prediksi status dropout mahasiswa menggunakan pendekatan data mining. Berikut penjelasan lengkap berdasarkan aspek teknis dan strategis dalam pengembangan sistem ini:

## Metode data Mining
Dalam merancang sistem prediksi ini, kami akan mengimplementasikan dua algoritma utama yaitu **Random Forest** dan **Logistic Regression**. Pemilihan **Random Forest** didasarkan pada kemampuannya menangani dataset dengan fitur yang beragam dan kompleks, serta ketahanannya terhadap overfitting. Algoritma ini sangat cocok untuk kasus prediksi drop out karena kemampuannya untuk menangani outlier dan missing value dengan lebih baik dibandingkan model linear, serta tingkat akurasi yang tinggi berkat ensemble learning, menggabungkan banyak pohon keputusan (decision trees) untuk menghasilkan prediksi yang stabil dan kuat. Model ini juga memberikan fitur penting yang bisa membantu menjelaskan variabel mana yang paling mempengaruhi kemungkinan dropout. Sementara itu, **Logistic Regression** dipilih sebagai baseline model karena sifatnya yang interpretable dan memberikan probabilitas prediksi yang jelas, memungkinkan pihak akademik memahami kontribusi setiap faktor terhadap risiko drop out.

Pemilihan kedua algoritma ini didasarkan pada karakteristik data akademik yang memiliki fitur numerik (GPA, kehadiran, aktivitas LMS) dan kategorikal (area tempat tinggal, status bekerja). Random Forest mampu menangani mixed data types dengan baik, sementara Logistic Regression memberikan baseline yang solid dengan interpretasi koefisien yang mudah dipahami.

## Proses Data Mining Berdasarkan CRISP-DM
Sistem yang kami rancang ini dikembangkan mengikuti tahapan metodologi CRISP-DM (Cross-Industry Standard Process for Data Mining) yang terdiri dari enam tahap sistematis:

1. **Business Understanding :** Tahap ini akan fokus pada pemahaman kebutuhan institusi dalam mengidentifikasi mahasiswa berisiko drop out secara dini. Tujuannya adalah mengurangi tingkat drop out melalui intervensi akademik yang tepat waktu.
2. **Data Understanding :** Pada tahap ini akan dilakukan eksplorasi mendalam terhadap data akademik mahasiswa yang mencakup performa akademik, pola kehadiran, aktivitas pembelajaran daring, dan faktor sosio-ekonomi. Analisis statistik deskriptif dan visualisasi akan digunakan untuk memahami distribusi data dan mengidentifikasi pola awal.
3. **Data Preparation :** Tahap preprocessing akan mencakup pembersihan data, penanganan missing values, encoding variabel kategorikal, normalisasi/standardisasi fitur numerik, dan splitting dataset. Feature engineering juga akan dilakukan untuk menciptakan fitur baru yang lebih informatif, seperti tren penurunan GPA atau rasio aktivitas LMS terhadap kehadiran.
4. **Modeling :** Tahap Modeling akan mengimplementasikan algoritma terpilih dengan fine-tuning parameter untuk optimasi performa. Implementasi dan training model Random Forest dan Logistic Regression dengan hyperparameter tuning.
5. **Evaluation Model :** Tahap evaluasi dengan evaluasi komprehensif menggunakan multiple metrics (accuracy, precision, recall, F1-score, AUC-ROC) dengan focus pada recall untuk meminimalisir false negative (mahasiswa berisiko yang terlewat). Validation akan dilakukan menggunakan stratified k-fold cross-validation.
6. **Deployment :** Tahap Deployment akan melibatkan integrasi model ke dalam sistem, dengan mempertimbangkan aspek keamanan data dan performa sistem real-time.

## Teknik Preprocessing Data
Teknik preprocessing yang akan diimplementasikan meliputi beberapa teknik untuk memastikan kualitas data optimal:

* **Penanganan Missing Values :** Menghapus atau mengisi nilai-nilai kosong (missing) dalam dataset agar tidak mengganggu proses pelatihan model. Model machine learning tidak dapat memproses data yang memiliki nilai kosong. Mengisi nilai kosong dengan mean/median (untuk numerik) atau modus (untuk kategorikal), atau menghapus baris/kolom tergantung kasus, akan membantu menjaga konsistensi dan akurasi model.
* **Mengecek Data Duplikat :** untuk mengidentifikasi dan menghapus baris-baris data yang terduplikasi agar tidak terjadi bias dalam pelatihan model.
* **Encoding Fitur Kategorikal :** Untuk Mengubah data dalam bentuk kategori (seperti jenis kelamin, jurusan, status beasiswa) menjadi format numerik yang dapat dibaca oleh algoritma machine learning. Sebagian besar model machine learning hanya dapat menerima input numerik. Encoding seperti Label Encoding atau One-Hot Encoding memungkinkan fitur kategorikal digunakan dalam pemodelan.
* **Feature selection :** Untuk memilih fitur (kolom) yang paling relevan terhadap target prediksi dan menghilangkan fitur yang tidak informatif. Feature selection meningkatkan efisiensi dan kinerja model dengan mengurangi kompleksitas, menghilangkan noise, serta mempercepat waktu pelatihan. Ini juga membantu menghindari overfitting.
* **Normalisasi data :** Untuk menskalakan nilai-nilai fitur numerik agar berada dalam rentang yang seragam, misalnya antara 0 dan 1 atau dengan distribusi standar (mean = 0, std = 1). Normalisasi membantu mempercepat proses konvergensi dan meningkatkan akurasi model.
* **Data splitting :** Untuk membagi dataset menjadi dua bagian: data latih (training) dan data uji (testing), data splitting diperlukan agar performa model dapat diuji pada data yang belum pernah dilihat sebelumnya. Ini memastikan evaluasi model bersifat objektif dan menghindari overfitting.

## Strategi Evaluasi Model
Evaluasi model menggunakan pendekatan komprehensif dengan multiple metrics. Metrik utamanya adalah **Accuracy score** untuk mengukur persentase ketepatan prediksi yang benar secara keseluruhan. **Classification report** digunakan untuk mendapatkan **precision**, **recall**, dan **f1-score** yang memberikan gambaran detail tentang performa model pada setiap kelas. Dimana **Precision** dan **Recall** akan dievaluasi secara khusus untuk kelas "dropout" karena lebih penting untuk mengidentifikasi mahasiswa berisiko (minimasi false negative) daripada salah mengklasifikasi mahasiswa aman. Dan F1-Score akan digunakan untuk mendapatkan keseimbangan antara precision dan recall. **Confusion matrix** divisualisasikan menggunakan heatmap untuk melihat distribusi true positive, true negative, false positive, dan false negative. Strategi ini memungkinkan pemahaman mendalam tentang dimana model melakukan kesalahan dan seberapa baik model dapat mengidentifikasi mahasiswa berisiko dropout. Kemudian dilakukan Perbandingan antara kedua model untuk memilih yang terbaik, dan hasil prediksi ditampilkan untuk analisis lebih detail.

## Rencana Pengembangan Sistem
Dalam merancang sistem klasifikasi risiko dropout mahasiswa berbasis data mining, kami merencanakan agar model prediksi dapat digunakan secara berkelanjutan tanpa perlu dilatih ulang setiap kali digunakan. Untuk itu, kami akan mengimplementasikan model persistence menggunakan pustaka joblib, yaitu dengan menyimpan model yang telah dilatih ke dalam file .pkl. Langkah ini memungkinkan model untuk dimuat kembali saat deployment, sehingga sistem dapat memberikan prediksi secara instan tanpa perlu melatih ulang setiap saat.

Sistem juga akan dirancang agar dapat memberikan prediksi interaktif berbasis input pengguna. Artinya, pengguna misalnya staf akademik dapat memasukkan data mahasiswa seperti IPK, status keaktifan, jumlah SKS yang diambil, atau indikator keterlibatan kegiatan kampus. Setelah data dimasukkan, sistem akan secara otomatis mengeluarkan prediksi apakah mahasiswa tersebut termasuk kategori berisiko tinggi dropout atau tidak. Ini akan dikembangkan sebagai antarmuka yang sederhana namun efektif, baik berbasis CLI (Command Line Interface) pada tahap awal maupun GUI atau web dashboard di tahap lanjut. Selain itu, sistem juga akan dikembangkan menjadi dashboard web interaktif menggunakan framework seperti Streamlit. Dashboard ini akan menyajikan hasil klasifikasi dalam bentuk visualisasi yang mudah dipahami

Dengan rancangan sistem yang demikian, kami berharap sistem ini tidak hanya menjadi alat bantu analisis, tetapi juga menjadi bagian integral dari proses pengambilan keputusan dalam pembinaan dan pengawasan akademik mahasiswa secara holistik dan berbasis data.
