1) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)
-> Untuk menyelesaikan checklist tersebut, saya tidak hanya mengandalkan hasil dari tutorial yang sudah diberikan, tetapi juga melengkapinya dengan pencarian informasi dari berbagai sumber resmi lain. Dengan begitu, saya bisa lebih memahami setiap langkah yang dilakukan, tidak sekadar mengikuti instruksi secara mekanis, melainkan juga mengerti konsep di baliknya. Pendekatan ini membantu saya menerapkan setiap poin dalam checklist secara lebih mandiri dan terarah.

2) Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
--> https://www.canva.com/design/DAGyi5tO7-M/FCptzEnYggJKrkdFKBubZQ/edit?utm_content=DAGyi5tO7-M&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

3) Jelaskan peran settings.py dalam proyek Django!
--> File settings.py pada Django berfungsi sebagai pusat konfigurasi utama dari sebuah proyek. Di dalamnya terdapat berbagai pengaturan penting seperti daftar aplikasi yang digunakan (INSTALLED_APPS), konfigurasi basis data (DATABASES), template (TEMPLATES), file statis (STATICFILES), middleware, hingga kunci rahasia (SECRET_KEY) yang menjaga keamanan proyek. Semua aplikasi dan layanan yang berjalan di dalam Django akan mengacu pada konfigurasi yang telah ditetapkan di file ini, sehingga perubahan atau penyesuaian sistem biasanya dilakukan melalui settings.py

4) Bagaimana cara kerja migrasi database di Django?
--> Migrasi pada Django adalah cara untuk mencatat dan menerapkan perubahan pada model ke dalam basis data. Dengan perintah python manage.py makemigrations, Django membuat berkas migrasi berisi perubahan yang terjadi. Selanjutnya, perintah python manage.py migrate digunakan untuk menerapkan perubahan tersebut ke struktur tabel pada basis data agar sesuai dengan model terbaru

5) Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
--> Framework Django dipilih sebagai permulaan pembelajaran karena dibangun menggunakan Python, bahasa pemrograman yang relatif mudah dipahami dan sudah cukup familiar bagi banyak pemula. Selain itu, Django memiliki alur penggunaan yang sederhana dan tidak terlalu rumit, sehingga lebih fokus memahami konsep dasar pengembangan web tanpa terbebani oleh kompleksitas teknis yang berlebihan

6) Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
--> Sangat jelas, tidak rumit 


Tugas 3
1)  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
--> Data delivery penting dalam implementasi platform karena berfungsi sebagai penghubung untuk mengirim, menerima, dan menampilkan data dari server ke pengguna. Tanpa mekanisme ini, data di server tidak dapat diakses maupun dimanfaatkan oleh pengguna

2) Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
--> Menurut saya, pemilihan antara XML dan JSON bergantung pada tujuan dan kebutuhan. JSON sangat cocok untuk aplikasi web karena serialisasinya cepat, ringkas, dan efisien. Namun, fleksibilitasnya membuat JSON kurang ideal untuk transfer data antar sistem berbeda atau data yang dibaca pihak ketiga. Meski begitu, JSON lebih populer karena mudah dibaca dan ditulis, cepat, fleksibel, serta mudah diolah

3) Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
--> Metode is_valid() digunakan untuk mengecek apakah data yang dimasukkan memenuhi aturan atau kriteria yang telah ditetapkan dalam sebuah form. Jika semua data valid, metode ini akan mengembalikan nilai true, sebaliknya, jika terdapat kesalahan, maka akan mengembalikan false. Oleh karena itu, is_valid() membantu developer memastikan bahwa hanya data yang benar dan lengkap yang diproses lebih lanjut

4) Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
--> Django menyediakan fitur yang disebut CSRF token untuk melindungi dari serangan CSRF (cross-site request forgery) yang berpotensi berbahaya. Saat sesi pengguna dimulai di sebuah website, sistem akan membuat token unik. Token ini kemudian dicek setiap kali ada request yang diproses, untuk memastikan request tersebut benar-benar berasal dari pengguna yang sah, bukan dari pihak yang mencoba menyerang. Apabila csrf_token tidak ada, secara umum, Django akan menolak request POST yang tidak menyertakan token CSRF. Selain itu, tanpa token, website menjadi jauh lebih rentan terhadap serangan

5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
--> Berdasarkan alur checklist yang diberikan, untuk membuat 4 fungsi views dalam format XML, JSON, XML by ID dan JSON by ID, suatu hal yang saya pelajari adalah perlunya penggunaan serializers, karena serializers berfungsi untuk mengubah objek model menjadi format XML maupun JSON. Selanjutnya, routing URL dibuat dengan cara melakukan import view yang sudah dibuat, lalu menambahkan masing-masing path di urls.py

Untuk memenuhi poin berikutnya, saya membuat halaman yang menampilkan data objek model dengan menambahkan tombol “Add” yang akan diarahkan ke halaman form, serta tombol “Detail” pada setiap data objek model yang menampilkan detail dari objek tersebut. Implementasinya dilakukan dengan membuat template seperti create_product.html untuk halaman form penambahan data, serta show_product.html untuk menampilkan daftar produk yang sudah dibuat beserta tombol “Detail”-nya

Secara keseluruhan, untuk mengimplementasikan checklist yang ada, saya menggunakan ilmu dan praktek yang telah saya pelajari pada tutorial sebelumnya, sehingga saya tidak asal mengikuti tutorial dengan cara copy & paste, tetapi saya juga mempelajari latar belakang, tujuan dan manfaat, sehingga dalam pengerjaan tugas 3, saya sudah memiliki gambaran alur pengerjaan

6) Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
--> Saya ingin mengapresiasi para asdos karena telah memberikan alur pengerjaan dan penjelasan yang mudah ditangkap dan membuat suatu hal yang kompleks menjadi lebih simple.

7) Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
--> https://drive.google.com/drive/folders/1af0-Q8gaL7uNZWjqOzZ3ivhPJTCbaYkC?usp=share_link


Tugas 4
1.  Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
--> AuthenticationForm merupakan form bawaan yang berfungsi untuk menangani proses login pengguna. Dengan adanya form ini, kita tidak perlu lagi membuat form login dari awal karena sudah langsung terhubung dengan sistem autentikasi Django. Kelebihan dari AuthenticationForm adalah praktis digunakan, aman karena memanfaatkan hashing password bawaan Django, dan mudah untuk dikustomisasi sesuai kebutuhan. Namun, kekurangannya adalah kurang fleksibel jika aplikasi memiliki kebutuhan autentikasi yang lebih kompleks, misalnya login menggunakan nomor telepon atau OTP, serta tampilannya masih sederhana sehingga biasanya memerlukan penyesuaian desain agar sesuai dengan front-end aplikasi

2.  Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
--> Autentikasi (authentication) adalah proses untuk memastikan identitas pengguna yang sedang login, misalnya memverifikasi apakah username dan password cocok dengan data yang tersimpan di database. Sedangkan otorisasi (authorization) adalah proses menentukan hak akses pengguna setelah berhasil login, seperti apakah user tersebut hanya bisa membaca data atau juga bisa menambah, mengedit, bahkan menghapus data. Django mengimplementasikan keduanya melalui sistem bawaan django.contrib.auth, di mana autentikasi ditangani dengan fungsi login/logout serta model User, sementara otorisasi diatur dengan sistem permission dan groups yang bisa dihubungkan dengan masing-masing user

3.  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
--> #Kelebihan Session:
* Data tidak disimpan langsung di browser, melainkan di server, sehingga lebih aman
Bisa menyimpan data lebih banyak tanpa membebani browser

#Kekurangan Session:
*Membebani server karena data user disimpan di sisi server.
*Membutuhkan manajemen ekstra jika aplikasi memiliki banyak pengguna.

#Kelebihan Cookies
* Disimpan di browser user, sehingga tidak membebani server.
* Dapat digunakan untuk menyimpan preferensi user (misalnya bahasa, tema).

#Kekurangan Cookies
* Rentan terhadap pencurian data (misalnya serangan XSS).
* Kapasitas penyimpanan terbatas.

4.  Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
--> Penggunaan cookies tidak sepenuhnya aman karena data yang tersimpan bisa dicuri oleh pihak ketiga, misalnya melalui serangan XSS. Untuk mengurangi risiko ini, Django menyediakan pengaturan keamanan bawaan seperti SESSION_COOKIE_HTTPONLY untuk mencegah akses cookies melalui JavaScript, SESSION_COOKIE_SECURE agar cookies hanya dikirim lewat HTTPS, serta mekanisme CSRF token yang melindungi form dari serangan CSRF. Dengan kombinasi pengaturan ini, penggunaan cookies dalam Django dapat dibuat lebih aman

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
--> Dalam menyelesaikan checklist yang diberikan, saya tidak hanya sekadar mengikuti instruksi dari tutorial, tetapi juga melengkapinya dengan penelusuran tambahan melalui dokumentasi resmi Django maupun referensi lainnya. Hal ini saya lakukan agar setiap proses, mulai dari pembuatan fitur registrasi, login, dan logout, penambahan akun dengan dummy data, penghubungan model Product dengan User, hingga penerapan session dan cookie* seperti last_login, dapat saya pahami secara menyeluruh. Dengan begitu, setiap langkah yang saya kerjakan tidak hanya bersifat meniru, melainkan benar-benar didasari pemahaman mengenai konsep yang melatarbelakanginya. Pendekatan ini membuat saya lebih mandiri dalam menyelesaikan checklist sekaligus lebih siap menghadapi variasi kasus serupa di luar contoh tutorial

Tugas 5 
1) Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
--> Dalam CSS, ketika beberapa selector diterapkan pada elemen HTML yang sama dan terdapat properti yang saling bertentangan, aturan prioritas akan menentukan mana yang diambil oleh browser. Urutan prioritas CSS dimulai dengan inline style, yang memiliki prioritas tertinggi. Inline style adalah gaya yang diterapkan langsung pada elemen HTML melalui atribut style. Gaya ini akan mengesampingkan gaya lainnya, kecuali jika ada penggunaan !important pada gaya lain. Setelah inline style, urutan prioritas berikutnya adalah internal style, yaitu gaya yang dideklarasikan di dalam tag <style> pada bagian <head> dokumen HTML. Internal style memiliki prioritas lebih tinggi dibandingkan dengan eksternal style, tetapi lebih rendah daripada inline style. Gaya internal ini akan mengoverride gaya dari file eksternal, kecuali jika gaya eksternal tersebut menggunakan !important. Terakhir, eksternal style yang dideklarasikan dalam file CSS terpisah dan dipanggil menggunakan tag <link> atau @import memiliki prioritas terendah. Meskipun sangat berguna untuk menerapkan gaya secara global, eksternal style akan diabaikan jika ada inline style atau internal style yang menerapkan aturan yang sama pada elemen tersebut. Namun, jika sebuah aturan dalam eksternal style menggunakan !important, maka gaya tersebut akan mengesampingkan aturan lainnya yang tidak menggunakan !important, meskipun berada pada urutan prioritas yang lebih rendah.

2) Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
--> Responsive design adalah teknik dalam pengembangan aplikasi web yang memungkinkan tampilan situs menyesuaikan diri dengan ukuran layar perangkat yang digunakan. Dengan menggunakan desain responsif, elemen seperti teks, gambar, dan tata letak akan berubah sesuai dengan perangkat, baik itu desktop, tablet, atau ponsel, tanpa memerlukan zoom in atau zoom out. Hal ini membuat pengalaman pengguna lebih nyaman, karena pengunjung dapat mengakses situs dengan mudah dan tanpa kesulitan.

Contoh aplikasi yang sudah menerapkan responsive design adalah Twitter yang memastikan pengguna dapat berbelanja atau membaca tweet dengan nyaman di berbagai perangkat. Sebaliknya, beberapa situs web pemerintah lokal belum menerapkan desain responsif, sehingga user harus zoom in atau scroll horizontal untuk melihat konten dengan jelas

Pentingnya desain responsif terletak pada kenyamanan pengguna dan aksesibilitas. Dengan desain yang responsif aplikasi web bisa digunakan di berbagai perangkat, meningkatkan interaksi pengguna, dan membantu SEO agar lebih mudah ditemukan di mesin pencari.


3) Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
--> Margin, border dan padding adalah properti CSS yang mengatur ruang di sekitar elemen HTML. Meskipun ketiganya berhubungan dengan ruang, mereka bekerja di tempat yang berbeda dalam struktur elemen Padding adalah ruang yang ada di dalam elemen, antara konten dan batas elemen (border). Padding memastikan konten tidak terlalu dekat dengan border, memberi ruang ekstra di dalam elemen. Border adalah garis yang mengelilingi elemen, di sekitar konten dan padding sehingga memberi batas fisik pada elemen dan bisa diubah warnanya, ketebalan, dan jenis garisnya. Margin adalah ruang di luar elemen, antara elemen dengan elemen lain di sekitarnya yang digunakan untuk memberi jarak antar elemen, menghindari elemen saling menempel

.box {
  margin: 100px 20px 50px 370px; / Margin dengan nilai atas, kanan, bawah, kiri /
  width: 350px;
  height: 50px;
  font-size: 50px;
  border: 10px solid red;  -->  Border 10px merah 
  padding: 160px; --> Padding 160px di semua sisi 
}

4) Jelaskan konsep flex box dan grid layout beserta kegunaannya!
--> Untuk membuat layout dengan menggunakan Flexbox, kita menambahkan "display: flex" pada elemen untuk mendefinisikan penggunaan Flexbox. Kemudian, kita bisa menggunakan properti flex-direction untuk menentukan arah elemen, apakah dalam bentuk kolom atau baris. Flexbox sangat berguna untuk mengatur perataan dan posisi elemen-elemen kecil atau detail, dan cocok digunakan pada layout dengan satu dimensi, baik itu kolom atau baris

Sementara itu, untuk membuat layout menggunakan CSS Grid, kita menambahkan "display: grid" pada elemen dan menggunakan properti grid-template-rows dan grid-template-columns untuk mengatur ukuran elemen, serta grid-gap untuk mengatur jarak antar elemen. CSS Grid sangat baik untuk mengatur layout yang melibatkan elemen-elemen besar seperti gambar, dan cocok digunakan untuk layout dengan dua dimensi, yaitu kolom dan baris


5) Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
--> Berdasarkan alur checklist yang diberikan, untuk mengimplementasikan fungsionalitas seperti edit dan hapus produk, saya memulai dengan membuat views yang menangani kedua fungsi tersebut, dengan memanfaatkan form dan metode penghapusan objek produk. Selanjutnya, saya menyesuaikan tampilan halaman login, register, tambah produk, dan detail produk dengan menggunakan Tailwind CSS, untuk memastikan desainnya responsif dan menarik. Pada halaman daftar produk, saya menambahkan logika untuk menampilkan gambar dan pesan jika produk belum tersedia, serta menampilkan produk dalam bentuk card yang dilengkapi dengan tombol edit dan hapus. Saya juga mengimplementasikan navbar responsif yang akan menyesuaikan tampilannya di berbagai perangkat. Dengan demikian, aplikasi menjadi lebih fungsional dan responsif, memberikan pengalaman pengguna yang lebih baik. Saya menerapkan semua ini dengan memanfaatkan pengetahuan yang saya peroleh dari tutorial dan sumber eksternal, yang memungkinkan saya untuk mengembangkan aplikasi ini dengan pemahaman yang lebih mendalam tentang alur pengembangan dan fungsionalitas yang dibutuhkan
