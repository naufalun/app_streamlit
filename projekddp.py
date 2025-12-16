import streamlit as st


# DATA MAKANAN
makanan = [
    {"nama": "Oatmeal : tinggi serat larut (beta-glucan) yang membuat kenyang lebih lama.", "kalori": 160},
    {"nama": "Telur Rebus : lebih rendah kalori dan tinggi protein sehingga membantu mencapai target defisit kalori.", "kalori": 63},
    {"nama": "Ayam Panggang : tinggi protein, rendah lemak & protein sehingga cocok untuk diet dan pembentukan otot.", "kalori": 260},
    {"nama": "Nasi Merah : tinggi serat dan kerbohidrat kompleks.", "kalori": 120},
    {"nama": "Alpukat : tinggi lemak sehat (asam oleat) dan serat yang bikin kenyang lebih lama, sehingga mengurangi keinginan makan berlebih.", "kalori": 160},
    {"nama": "Salmon : kaya protein berkualitas tinggi dan mengandung lemak sehat.", "kalori": 200},
    {"nama": "Brokoli : tinggi kandungan serat dan kalsium yang penting untuk diet.", "kalori": 35},
]


# FUNCTION 1: Hitung kebutuhan kalori
def hitung_kebutuhan_kalori(berat, tinggi, usia, aktivitas):
    bmr = 10 * berat + 6.25 * tinggi - 5 * usia + 5
    faktor = {
        "Ringan": 1.375,
        "Sedang": 1.55,
        "Berat": 1.725
    }
    return int(bmr * faktor[aktivitas])



# FUNCTION 2: Susun menu
def susun_menu(target_kalori):
    total = 0
    menu = []
    for item in makanan:
        if total + item["kalori"] <= target_kalori:
            total += item["kalori"]
            menu.append(item["nama"])
    return menu, total


# FUNCTION 3: Simulasi progress
def simulasi_progress(berat_awal, target, defisit):
    hasil = []
    berat = berat_awal
    minggu = 0

    while berat - defisit > target:
        minggu += 1
        berat -= defisit
        hasil.append((minggu, round(berat, 1)))

    minggu += 1
    hasil.append((minggu, target))
        # if minggu > 52:  # batas agar tidak infinite loop
        #     break

    return hasil



# STREAMLIT UI
st.set_page_config(layout="wide")
st.title("Aplikasi Diet & Nutrisi")

# SIDEBAR NAV
menu = st.sidebar.selectbox(
    "Pilih Fitur",
    ["Hitung Kebutuhan Kalori", "Rekomendasi Menu Diet", "Simulasi Progress Berat Badan"]
)

st.sidebar.write("Silahkan pilih jenis aplikasi.")



# FITUR 1: Hitung kebutuhan kalori
if menu == "Hitung Kebutuhan Kalori":
    st.header("🔥 Hitung Kebutuhan Kalori Harian")

    col1, col2 = st.columns(2)
    with col1:
        berat = st.number_input("Berat (kg)", min_value=0, value=60)
        tinggi = st.number_input("Tinggi (cm)", min_value=0, value=165)
    with col2:
        usia = st.number_input("Usia", min_value=0, value=20)
        aktivitas = st.selectbox("Aktivitas", ["Ringan", "Sedang", "Berat"])

    if st.button("Hitung"):
        hasil = hitung_kebutuhan_kalori(berat, tinggi, usia, aktivitas)
        st.success(f"Total kebutuhan kalori harianmu adalah **{hasil} kcal**")



# FITUR 2: Rekomendasi Menu Diet
elif menu == "Rekomendasi Menu Diet":
    st.header("🥗 Rekomendasi Menu Diet")
    st.image('streamlit.png', width=600)

    target_kalori = st.number_input("Target Kalori Harian", min_value=0, value=1500)

    if st.button("Buat Menu"):
        menu_harian, total = susun_menu(target_kalori)

        if menu_harian:
            st.subheader("Menu Cocok:")
            for item in menu_harian:
                st.write(f"• {item}")

            st.success(f"Total kalori: **{total} kcal**")
        else:
            st.warning("Tidak ada makanan yang cocok untuk target ini.")


# FITUR 3: Simulasi Progress Berat Badan
elif menu == "Simulasi Progress Berat Badan":
    st.header("📉 Simulasi Progress Diet")

    berat_awal = st.number_input("Berat awal (kg)", min_value=0, value=70)
    target_berat = st.number_input("Target berat (kg)", min_value=0, value=60)
    defisit = st.number_input("Penurunan per minggu (kg)", min_value=0.0, value=0.5)

    if st.button("Simulasikan"):
        # hasil = simulasi_progress(berat_awal, target_berat, defisit)

        # if len(hasil) == 0:
        #     st.warning("Target harus lebih rendah dari berat awal.")
        # else:
        #     st.subheader("Perjalanan Mingguan:")
        #     for minggu, b in hasil:
        #         st.write(f"Minggu {minggu}: {b} kg")

        #     st.success(f"Mencapai target dalam **{len(hasil)} minggu**")

        if target_berat >=berat_awal :
            st.warning ("target berat harus lebih kecil dari berat awal")
        elif defisit <= 0:
            st.warning ("penurunan per minggu harus lebih dari 0")
        else :
            hasil = simulasi_progress(berat_awal, target_berat, defisit)

            st.subheader("Perjalanan Mingguan:")
            for minggu, b in hasil:
                st.write(f"Minggu {minggu}: {b} kg")

            st.success(f"Mencapai target dalam **{len(hasil)} minggu**")

