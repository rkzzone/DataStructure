import streamlit as st
from collections import deque

# Judul aplikasi
st.title("Studi Kasus Struktur Data Queue")

# Deskripsi studi kasus
st.write("""
    Pada studi kasus ini, kita akan mengimplementasikan konsep Struktur Data Queue untuk mencari 
    hasil maksimum dari area yang dapat dicakup oleh histogram dalam array input. Anda dapat memasukkan
    array angka (dipisahkan oleh spasi), dan aplikasi ini akan menghitung hasil maksimum area histogram tersebut.
""")

# Form untuk memasukkan array
array_input = st.text_input("Masukkan array (space-separated):")

# Tombol untuk proses perhitungan
if st.button("Hitung Maksimum Area"):
    if array_input:
        # Parsing input array
        try:
            A = list(map(int, array_input.split()))
            N = len(A)

            # Inisialisasi deque dan variabel hasil maksimum
            Q = deque([-1])  # Deque yang dimulai dengan -1 untuk melacak indeks histogram
            res = 0          # Variabel untuk menyimpan hasil maksimum

            # Proses perhitungan area maksimum menggunakan deque
            for i in range(N):
                x = A[i]
                while Q[-1] != -1 and A[Q[-1]] >= x:
                    y = Q.pop()
                    res = max(res, A[y] * (i - 1 - Q[-1]))
                Q.append(i)

            # Memproses sisa elemen di deque setelah loop
            while Q[-1] != -1:
                y = Q.pop()
                res = max(res, A[y] * (N - 1 - Q[-1]))

            # Menampilkan hasil dengan format yang lebih besar
            st.markdown(f"<h3>Hasil maksimum area: {res}</h3>", unsafe_allow_html=True)
        except ValueError:
            st.error("Pastikan hanya memasukkan angka yang dipisahkan dengan spasi.")

# Dropdown untuk menampilkan kode sumber
with st.expander("Tampilkan Source Code"):
    st.code('''
        from collections import deque

        # Membaca jumlah kasus uji
        t = int(input("Berapa jumlah test case yang akan dilakukan? "))

        # Loop untuk setiap kasus uji
        for _ in range(t):
            # Membaca panjang array A
            N = int(input(f"Berapa Panjang Array A pada test case ke {_ + 1}? "))
            
            # Membaca array A
            A = list(map(int, input("Input array (space-separated): ").split()))
            
            # Inisialisasi deque dan variabel hasil maksimum
            Q = deque([-1])  # Deque yang dimulai dengan -1 untuk melacak indeks histogram
            res = 0          # Variabel untuk menyimpan hasil maksimum
            
            # Iterasi untuk menghitung area maksimum
            for i in range(N):
                x = A[i]
                
                # Memeriksa elemen deque untuk mencari area maksimum
                while Q[-1] != -1 and A[Q[-1]] >= x:
                    y = Q.pop()  # Mengeluarkan dari belakang (seperti stack)
                    res = max(res, A[y] * (i - 1 - Q[-1]))
                
                # Tambahkan indeks saat ini ke deque
                Q.append(i)
            
            # Memproses sisa elemen di deque setelah loop
            while Q[-1] != -1:
                y = Q.pop()  # Mengeluarkan dari belakang
                res = max(res, A[y] * (N - 1 - Q[-1]))
            
            # Cetak hasil maksimum area untuk kasus uji saat ini
            print("Hasil maksimum area:", res)
   ''')