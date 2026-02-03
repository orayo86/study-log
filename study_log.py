# Daftar untuk menyimpan semua catatan belajar
catatan = []

# Nama file untuk menyimpan data
FILE_CATATAN = "catatan.json"

import json
import os


def simpan_ke_json():
    """
    Fungsi untuk menyimpan semua catatan ke file JSON.
    File akan tersimpan dengan nama 'catatan.json'.
    """
    try:
        with open(FILE_CATATAN, 'w') as file:
            json.dump(catatan, file, indent=2, ensure_ascii=False)
        print(f"✓ Data berhasil disimpan ke {FILE_CATATAN}\n")
    except Exception as e:
        print(f"❌ Gagal menyimpan data: {e}\n")


def baca_dari_json():
    """
    Fungsi untuk membaca catatan dari file JSON.
    Jika file tidak ada, mulai dengan list kosong.
    """
    global catatan
    
    if os.path.exists(FILE_CATATAN):
        try:
            with open(FILE_CATATAN, 'r') as file:
                catatan = json.load(file)
            print(f"✓ Data berhasil dimuat dari {FILE_CATATAN}")
            print(f"  Total catatan: {len(catatan)}\n")
        except Exception as e:
            print(f"⚠️  Gagal membaca file: {e}")
            print("  Mulai dengan data kosong.\n")
            catatan = []
    else:
        print(f"ℹ️  File {FILE_CATATAN} belum ada. Mulai dengan data kosong.\n")
        catatan = []


def tambah_catatan():
    """
    Fungsi untuk menambahkan catatan belajar baru.
    Meminta input: mapel, topik, dan durasi belajar (menit)
    Data otomatis disimpan ke file JSON.
    """
    print("\n=== Tambah Catatan Belajar ===")
    
    # Meminta input dari pengguna
    mapel = input("Masukkan nama mapel: ")
    topik = input("Masukkan topik yang dipelajari: ")
    durasi = input("Masukkan durasi belajar (menit): ")
    
    # Membuat dictionary untuk satu catatan
    catatan_baru = {
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    }
    
    # Menambahkan catatan ke dalam list
    catatan.append(catatan_baru)
    
    # Simpan ke JSON secara otomatis
    simpan_ke_json()
    print("✓ Catatan berhasil ditambahkan!\n")


def lihat_catatan():
    """
    Fungsi untuk menampilkan semua catatan belajar dengan rapi.
    Jika belum ada data, tampilkan pesan yang sesuai.
    """
    # Cek apakah ada catatan atau tidak
    if len(catatan) == 0:
        print("\n📭 Belum ada catatan belajar. Mulai tambahkan catatan belajar Anda!\n")
        return
    
    # Tampilkan header
    print("\n" + "="*60)
    print("📚 DAFTAR CATATAN BELAJAR")
    print("="*60)
    
    # Tampilkan setiap catatan dengan format rapi
    for i, c in enumerate(catatan, 1):
        print(f"\n{i}. Mapel: {c['mapel']}")
        print(f"   Topik: {c['topik']}")
        print(f"   Durasi: {c['durasi']} menit")
        print("-" * 60)
    
    # Tampilkan statistik
    total_durasi = sum(int(c['durasi']) for c in catatan if c['durasi'].isdigit())
    print(f"\nTotal catatan: {len(catatan)} | Total durasi belajar: {total_durasi} menit\n")


def tampilkan_catatan():
    """Menampilkan semua catatan yang sudah ditambahkan (versi singkat)"""
    if len(catatan) == 0:
        print("\nBelum ada catatan belajar.\n")
        return
    
    print("\n=== Daftar Catatan Belajar ===")
    for i, c in enumerate(catatan, 1):
        print(f"{i}. Mapel: {c['mapel']}")
        print(f"   Topik: {c['topik']}")
        print(f"   Durasi: {c['durasi']} menit\n")


def total_waktu():
    """
    Fungsi untuk menghitung total durasi belajar dari semua catatan.
    Menampilkan hasil dengan format yang mudah dipahami.
    """
    # Jika tidak ada catatan
    if len(catatan) == 0:
        print("\n⏱️  Belum ada catatan belajar. Total waktu belajar: 0 menit\n")
        return 0
    
    # Hitung total durasi dengan cara yang aman
    total = 0
    for c in catatan:
        try:
            # Coba konversi durasi ke integer
            durasi = int(c['durasi'])
            total += durasi
        except ValueError:
            # Jika durasi tidak valid, lewati
            print(f"⚠️  Durasi '{c['durasi']}' pada mapel '{c['mapel']}' tidak valid (lewat)")
    
    # Tampilkan hasil
    jam = total // 60
    menit = total % 60
    
    print("\n" + "="*60)
    print("⏱️  TOTAL WAKTU BELAJAR")
    print("="*60)
    print(f"Total durasi: {total} menit")
    print(f"Atau: {jam} jam {menit} menit")
    print("="*60 + "\n")
    
    return total


def filter_per_mapel():
    """
    Fitur untuk menampilkan catatan belajar berdasarkan mapel tertentu.
    Menampilkan total waktu belajar untuk mapel yang dipilih.
    """
    # Cek apakah ada catatan
    if len(catatan) == 0:
        print("\n📭 Belum ada catatan belajar.\n")
        return
    
    # Dapatkan daftar mapel yang unik
    daftar_mapel = []
    for c in catatan:
        if c['mapel'] not in daftar_mapel:
            daftar_mapel.append(c['mapel'])
    
    # Tampilkan daftar mapel
    print("\n" + "="*60)
    print("🔎 FILTER CATATAN PER MAPEL")
    print("="*60)
    print("\nDaftar mapel yang tersedia:")
    for i, mapel in enumerate(daftar_mapel, 1):
        print(f"{i}. {mapel}")
    
    # Minta input dari pengguna
    try:
        pilihan = int(input("\nPilih nomor mapel (atau 0 untuk batalkan): "))
        
        # Validasi input
        if pilihan == 0:
            print("Dibatalkan.\n")
            return
        
        if pilihan < 1 or pilihan > len(daftar_mapel):
            print("❌ Pilihan tidak valid.\n")
            return
        
        mapel_terpilih = daftar_mapel[pilihan - 1]
        
    except ValueError:
        print("❌ Input harus berupa angka.\n")
        return
    
    # Filter catatan berdasarkan mapel terpilih
    catatan_terfilter = [c for c in catatan if c['mapel'] == mapel_terpilih]
    
    # Tampilkan hasil filter
    print("\n" + "="*60)
    print(f"📖 CATATAN BELAJAR: {mapel_terpilih}")
    print("="*60)
    
    for i, c in enumerate(catatan_terfilter, 1):
        print(f"\n{i}. Topik: {c['topik']}")
        print(f"   Durasi: {c['durasi']} menit")
        print("-" * 60)
    
    # Hitung total durasi untuk mapel ini
    total_mapel = 0
    for c in catatan_terfilter:
        try:
            total_mapel += int(c['durasi'])
        except ValueError:
            pass
    
    jam = total_mapel // 60
    menit = total_mapel % 60
    
    print(f"\nTotal catatan: {len(catatan_terfilter)} | ", end="")
    print(f"Total durasi: {total_mapel} menit ({jam}h {menit}m)\n")


def menu_utama():
    """
    Fungsi untuk menampilkan menu utama dan mengelola navigasi program.
    User bisa memilih fitur yang ingin digunakan.
    """
    while True:
        # Tampilkan menu
        print("\n" + "="*60)
        print("📚 STUDY LOG - MENU UTAMA")
        print("="*60)
        print("1. Tambah Catatan Belajar")
        print("2. Lihat Semua Catatan")
        print("3. Filter Catatan per Mapel")
        print("4. Lihat Total Waktu Belajar")
        print("5. Simpan Data (Backup)")
        print("6. Keluar Program")
        print("="*60)
        
        # Minta input dari user
        pilihan = input("\nPilih menu (1-6): ").strip()
        
        # Proses pilihan
        if pilihan == "1":
            tambah_catatan()
        
        elif pilihan == "2":
            lihat_catatan()
        
        elif pilihan == "3":
            filter_per_mapel()
        
        elif pilihan == "4":
            total_waktu()
        
        elif pilihan == "5":
            simpan_ke_json()
        
        elif pilihan == "6":
            print("\n" + "="*60)
            print("👋 Terima kasih telah menggunakan Study Log!")
            print("   Data Anda telah disimpan secara otomatis.")
            print("="*60 + "\n")
            break
        
        else:
            print("❌ Pilihan tidak valid. Silakan masukkan angka 1-6.\n")


# Contoh penggunaan
if __name__ == "__main__":
    # Muat data dari file JSON saat program dimulai
    baca_dari_json()
    
    # Jalankan menu utama
    menu_utama()
