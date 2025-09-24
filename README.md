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

