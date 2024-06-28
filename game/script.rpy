define gurubahasa = Character("Guru Bahasa")
# Variabel untuk melacak pelajaran yang sudah dipelajari
default learned_bahasa = False
default learned_mtk = False
default learned_ipa = False
default learned_ips = False

# Variabel untuk jumlah hati
default hearts = 3

# Fungsi untuk menampilkan indikator hati
screen heart_indicator():
    hbox:
        xalign 1.0
        yalign 0.0
        for i in range(hearts):
            add "heart.png" # Ganti "heart.png" dengan gambar hati yang sesuai

# Fungsi untuk mengurangi jumlah hati
init python:
    def decrease_hearts():
        global hearts
        hearts -= 1
        if hearts <= 0:
            renpy.jump("game_over")

# The game starts here.
label start:
    # intro
    "Disuatu sekolah."
    show bg 1
    with fade
    "Guru" "Sebelum mulai kelas mari kita berdoa."
    "tiba-tiba"
    show bg 2
    with fade
    "muncul asap hijau misterius dari ventilasi udara."
    show bg 3
    show bg 4
    "Murid" "Asap apa ini? uhuk-uhuk."
    "Para murid berlarian menghindari asap hijau aneh itu."
    show bg 5
    with fade
    "Adudu" "Asap apa ya tadi?"
    "Probe" "Gatau tuh tapi aneh banget warna hijau kayak racun."
    show bg 6
    with fade
    "Adudu" "Biarin deh ga urus yang penting bisa free class gara-gara asap itu hehe."
    show bg 7
    with fade
    "...."
    show bg 8 
    with fade
    show bg 9
    with fade
    "Guru IPS" "Mau cabut kemana kamu, sini masuk kelas."
    show bg 10
    with fade
    "Probe" "Kok tiba-tiba guru itu jadi galak ya? serem."
    show bg 11
    with fade
    show bg 12
    "Adudu" "Saya mau dibawa kemana ini buuu..... aduuhh......"
    show bg 13
    show bg 14
    "Adudu" "Aduh,Ampun ibu saya gatau jawabanya....."
    show bg 15
    with fade
    "Probe" "Waduh Adudu sampe dipukul."
    show bg 16
    with fade
    "Probe" "Lariiii guru-guru jadi galakkk."
    show bg 17
    with fade
    "Probe" "Duh ayo dong ini kenapa susah banget sih."
    show bg 18
    "Probe" "Akkh digembok, aku harus cari kuncinya."
    show bg 19
    with fade
    show bg 20
    with fade
    "Probe" "Cari kemana ya tapi kuncinya?"
    
    # pilih kelas
    # show screen heart_indicator

    "Pilih dimana kamu mau mencari"

label pilihan_pelajaran:
    menu:
        "kelas Bahasa":
            jump belajar_bahasa
        "kelas Matematika":
            jump belajar_mtk
        "kelas IPA":
            jump belajar_ipa
        "kelas IPS":
            jump belajar_ips

label belajar_bahasa:
    show bg bahasa with fade
    "Probe fokus mencari kunci di seluruh ruangan"
    "Tiba-tiba...."
    show indonesia 1
    "Kamu pasti mencari kunci ini yaa, hahaha"
    show indonesia 2
    gurubahasa "Kamu harus jawab pertanyaan dari saya baru akan saya kasih"
    gurubahasa "Pertanyaan pertama"

label pertanyaanb1:
    gurubahasa "apa warna bendera indonesia?"
    menu:
            "A. Merah dan putih":
                    jump pilihan_a
            "B. Hijau dan putih":
                    jump pilihan_b
            "C. Biru dan putih":
                    jump pilihan_c
            "D. Merah dan biru":
                    jump pilihan_d
label pilihan_a:
    $ jawaban = "a"
    jump cek_jawabanbahasa1

label pilihan_b:
    $ jawaban = "b"
    jump cek_jawabanbahasa1

label pilihan_c:
    $ jawaban = "c"
    jump cek_jawabanbahasa1

label pilihan_d:
    $ jawaban = "d"
    jump cek_jawabanbahasa1

label cek_jawabanbahasa1:
    if jawaban == "a":
        $ answered_correctly = True
    else:
        $ answered_correctly = False
    if answered_correctly:
        "Benar!"
        jump pertanyaanb2
    else:
        "Salah!"
        jump pertanyaanb1
        # buat logic kurangin hati
    return

label pertanyaanb2:
    gurubahasa "Apa antonim dari kata cepat?"
    menu:
            "A. Lambat":
                    jump pilihan_a2
            "B. Silau":
                    jump pilihan_b2
            "C. Mudah":
                    jump pilihan_c2
            "D. Kecil":
                    jump pilihan_d2
label pilihan_a2:
    $ jawaban = "a"
    jump cek_jawabanbahasa2

label pilihan_b2:
    $ jawaban = "b"
    jump cek_jawabanbahasa2

label pilihan_c2:
    $ jawaban = "c"
    jump cek_jawabanbahasa2

label pilihan_d2:
    $ jawaban = "d"
    jump cek_jawabanbahasa2

label cek_jawabanbahasa2:
    if jawaban == "a":
        $ answered_correctly = True
    else:
        $ answered_correctly = False
    if answered_correctly:
        "Benar!"
        jump pertanyaanb3
    else:
        "Salah!"
        # buat logic kurangin hati
        jump pertanyaanb2
    return

label pertanyaanb3:
    gurubahasa "Berikut ini termasuk kata benda kecuali?"
    menu:
            "A. Meja":
                    jump pilihan_a3
            "B. Buku":
                    jump pilihan_b3
            "C. Lemari":
                    jump pilihan_c3
            "D. Berlari":
                    jump pilihan_d3
label pilihan_a3:
    $ jawaban = "a"
    jump cek_jawabanbahasa3

label pilihan_b3:
    $ jawaban = "b"
    jump cek_jawabanbahasa3

label pilihan_c3:
    $ jawaban = "c"
    jump cek_jawabanbahasa3

label pilihan_d3:
    $ jawaban = "d"
    jump cek_jawabanbahasa3

label cek_jawabanbahasa3:
    if jawaban == "d":
        $ answered_correctly = True
    else:
        $ answered_correctly = False
    if answered_correctly:
        "Benar!"
        jump pertanyaanb4
    else:
        "Salah!"
        # buat logic kurangin hati
        jump pertanyaanb3
    return

label pertanyaanb4:
    gurubahasa "Apa antonim dari kata 'panas'?"
    menu:
            "A. Dingin":
                    jump pilihan_a4
            "B. Hangat":
                    jump pilihan_b4
            "C. Sejuk":
                    jump pilihan_c4
            "D. Mendidih":
                    jump pilihan_d4
label pilihan_a4:
    $ jawaban = "a"
    jump cek_jawabanbahasa4

label pilihan_b4:
    $ jawaban = "b"
    jump cek_jawabanbahasa4

label pilihan_c4:
    $ jawaban = "c"
    jump cek_jawabanbahasa4

label pilihan_d4:
    $ jawaban = "d"
    jump cek_jawabanbahasa4

label cek_jawabanbahasa4:
    if jawaban == "a":
        $ answered_correctly = True
    else:
        $ answered_correctly = False
    if answered_correctly:
        "Benar!"
        jump sudahdapatkuncibahasa
    else:
        "Salah!"
        # buat logic kurangin hati
        jump pertanyaanb4
    return

label sudahdapatkuncibahasa:
    show bg kunciterbuka1
    $ learned_bahasa = True
    jump cek_learned

label belajar_mtk:
# pertanyaan disini
    $ learned_mtk = True
    jump cek_learned

label belajar_ipa:
    $ learned_ipa = True
    jump cek_learned

label belajar_ips:
    $ learned_ips = True
    jump cek_learned

label cek_learned:
    if learned_bahasa and learned_mtk and learned_ipa and learned_ips:
        jump scene_selanjutnya
    else:
        "Kamu masih membutuhkan kunci, silahkan cari kunci lainnya"

label scene_selanjutnya:
    e "Selamat! Kamu telah menyelesaikan semua pelajaran. Sekarang kita bisa melanjutkan ke scene selanjutnya."
    # Tambahkan konten untuk scene selanjutnya di sini.
    return

# label game_over:
#     e "Maaf, kamu telah kehabisan hati. Permainan berakhir."
#     return
