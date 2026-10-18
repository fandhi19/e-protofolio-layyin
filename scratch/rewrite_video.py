html_content = '''<!doctype html>
<html lang="id">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Video Praktik Mengajar | Jejak PPL 2 - E-Portofolio PPG PJOK UNY</title>
    <!-- Fonts & Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,700;0,900;1,800&family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" />
    <link rel="stylesheet" href="../CSS/rancangan.css" />
    <link rel="shortcut icon" href="../IMG/logo.png" type="image/x-icon" />
  </head>
  <body>
    <!-- HEADER / NAVBAR DYNAMIC -->
    <header class="navbar" id="navbar">
      <div class="nav-container">
        <a href="../index.html" class="logo">
          <img src="../IMG/logo.png" alt="logo uny" />
          <span>E Portofolio<span class="text-blue"> PPG</span></span>
        </a>

        <div class="hamburger" id="hamburger">
          <span class="bar"></span>
          <span class="bar"></span>
          <span class="bar"></span>
        </div>

        <nav class="nav-links" id="nav-links">
          <a href="../index.html">Beranda</a>
          <a href="../profile.html">Profil</a>

          <div class="dropdown">
            <button class="dropbtn" id="dropdownBtn1">Jejak PPL 1 <i class="fa-solid fa-chevron-down chevron"></i></button>
            <div class="dropdown-content" id="dropdownContent1">
              <a href="../PPL_1/observasi.html"><i class="fa-solid fa-magnifying-glass"></i> Observasi</a>
              <a href="../PPL_1/modulajar.html"><i class="fa-solid fa-book"></i> Modul Ajar</a>
              <a href="../PPL_1/lkpd.html"><i class="fa-solid fa-file-signature"></i> E-LKPD</a>
              <a href="../PPL_1/penilaian.html"><i class="fa-solid fa-clipboard-check"></i> Penilaian</a>
              <a href="../PPL_1/modelguru.html"><i class="fa-solid fa-chalkboard-teacher"></i> Model Guru</a>
            </div>
          </div>

          <div class="dropdown">
            <button class="dropbtn active" id="dropdownBtn2">Jejak PPL 2 <i class="fa-solid fa-chevron-down chevron"></i></button>
            <div class="dropdown-content" id="dropdownContent2">
              <a href="rancangan.html"><i class="fa-solid fa-file-lines"></i> Rancangan Pembelajaran</a>
              <a href="materi.html"><i class="fa-solid fa-book-open"></i> Materi Pembelajaran</a>
              <a href="media.html"><i class="fa-solid fa-photo-film"></i> Media Pembelajaran</a>
              <a href="video.html" class="active"><i class="fa-solid fa-video"></i> Video Praktik Mengajar</a>
              <a href="non-mengajar.html"><i class="fa-solid fa-users-gear"></i> Kegiatan Non-Mengajar</a>
              <a href="instrumen.html"><i class="fa-solid fa-clipboard-check"></i> Instrumen Penilaian</a>
            </div>
          </div>

          <a href="../refleksi.html">Refleksi</a>
          <a href="../filosofi.html">Filosofi</a>
          <a href="../dokumentasi.html">Dokumentasi</a>
        </nav>
      </div>
    </header>

    <main>
      <!-- HERO SECTION -->
      <section class="hero-rancangan">
        <div class="hero-bg-slant"></div>
        <div class="hero-blob"></div>

        <div class="container hero-content">
          <div class="tagline reveal">
            <i class="fa-solid fa-video"></i> Jejak PPL 2 • Dokumentasi Praktik Mengajar
          </div>
          <h1 class="reveal">Video Praktik <span class="text-blue">Mengajar</span></h1>
          <p class="reveal">
            Dokumentasi unjuk kerja pembelajaran nyata Pendidikan Jasmani, Olahraga, dan Kesehatan (PJOK) di SMAN 4 Yogyakarta.
            Menampilkan 2 video praktik unggulan yaitu <strong>Permainan Kasti</strong> dan <strong>Atletik (Lari Jarak Pendek)</strong>,
            lengkap dengan analisis kritis 3 dimensi (Konteks & Tujuan, Kelebihan & Kekurangan, serta Kajian Teori Pedagogis).
          </p>

          <!-- Quick Stats -->
          <div class="quick-stats-bar reveal">
            <div class="stat-pill">
              <i class="fa-solid fa-film"></i>
              <span>2 Video Praktik Terpilih</span>
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-baseball-bat-ball"></i>
              <span>Permainan Kasti</span>
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-person-running"></i>
              <span>Atletik Lari Sprint</span>
            </div>
            <div class="stat-pill">
              <i class="fa-solid fa-microscope"></i>
              <span>Analisis Kritis 3 Poin</span>
            </div>
          </div>
        </div>
      </section>

      <!-- MAIN TABS SECTION (KASTI & ATLETIK CONTROLLER) -->
      <section class="bg-offwhite" style="padding-bottom: 90px; min-height: 80vh;">
        <div class="container">
          <!-- Main Switcher Bar -->
          <div class="main-tabs-wrapper reveal">
            <div class="sub-menu-nav">
              <button class="tab-btn active" id="tabBtnKasti" onclick="switchVideoTab('kasti')">
                <i class="fa-solid fa-baseball-bat-ball"></i>
                <span>Video 1: Permainan Kasti</span>
              </button>
              <button class="tab-btn" id="tabBtnAtletik" onclick="switchVideoTab('atletik')">
                <i class="fa-solid fa-person-running"></i>
                <span>Video 2: Atletik (Lari Sprint)</span>
              </button>
            </div>
          </div>

          <!-- =======================================================
               TAB 1: VIDEO 1 - PERMAINAN KASTI
          ======================================================== -->
          <div class="tab-panel active" id="panelKasti">
            <div class="section-banner reveal">
              <div class="banner-left">
                <h2>Video Praktik Mengajar 1 <span class="text-blue">(Permainan Kasti)</span></h2>
                <p>Pembelajaran Permainan Bola Kecil — Model Tactical Games Approach (TGA) & Pembelajaran Berdiferensiasi</p>
              </div>
              <div class="banner-tags">
                <span class="badge-outline"><i class="fa-solid fa-baseball-bat-ball"></i> Permainan Kasti</span>
                <span class="badge-outline"><i class="fa-solid fa-users"></i> Fase F (Kelas XI)</span>
                <span class="badge-outline"><i class="fa-solid fa-clock"></i> Durasi: ~18 Menit</span>
              </div>
            </div>

            <!-- Video Theater Card Kasti -->
            <div class="video-theater-card reveal">
              <div class="pdf-header">
                <div class="pdf-header-title">
                  <i class="fa-solid fa-clapperboard pdf-icon" style="color: var(--blue-light);"></i>
                  <div class="pdf-header-text">
                    <h3>Praktik Pembelajaran Permainan Kasti: Keterampilan Memukul, Melempar, Menangkap & Taktik Posisi</h3>
                    <span>Pengajar: Muhammad Layyinul Mushthofa, S.Pd • SMAN 4 Yogyakarta • Model Tactical Games Approach (TGA)</span>
                  </div>
                </div>
                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Permainan Kasti')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="https://youtu.be" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-youtube"></i> Tonton di YouTube
                  </a>
                </div>
              </div>

              <!-- Video Player Screen -->
              <div class="video-player-wrapper">
                <div class="video-poster-box" style="background-image: url('../IMG/PPL_2/Praktik Mengajar 1.jpeg');" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Permainan Kasti')">
                  <div class="video-badge-overlay">
                    <span class="video-badge-pill"><i class="fa-solid fa-video"></i> Full HD 1080p</span>
                    <span class="video-badge-pill"><i class="fa-solid fa-baseball-bat-ball"></i> Permainan Kasti</span>
                  </div>
                  <button class="video-play-btn" aria-label="Putar Video Praktik Kasti">
                    <i class="fa-solid fa-play"></i>
                  </button>
                  <div class="video-badge-duration">
                    <i class="fa-solid fa-clock"></i> 18:24 Menit
                  </div>
                </div>
              </div>

              <!-- Skenario Pembelajaran Kasti -->
              <div class="skenario-timeline-box">
                <div class="skenario-timeline-title">
                  <i class="fa-solid fa-list-check text-blue"></i>
                  <span>Alur Skenario Pembelajaran Permainan Kasti</span>
                </div>
                <div class="skenario-grid">
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-pendahuluan">Pendahuluan (15 Menit)</span>
                    <h5>Apersepsi & Pemanasan Dinamis</h5>
                    <p>Pengecekan kesiapan fisik, apersepsi aturan keselamatan bola kecil, pemanasan lempar-tangkap beregu, dan pembagian target capaian belajar.</p>
                  </div>
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-inti">Kegiatan Inti (60 Menit)</span>
                    <h5>Rotasi Stasiun Gerak & Modifikasi Kasti</h5>
                    <p>Pos 1: Lempar-Tangkap Presisi; Pos 2: Akurasi Pukulan Bola Lambung & Datar; Pos 3: Simulasi Kasti modifikasi lapangan dengan aturan taktik posisi regu.</p>
                  </div>
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-penutup">Penutup (15 Menit)</span>
                    <h5>Pendinginan & Refleksi Sportivitas</h5>
                    <p>Pendinginan relaksasi pernapasan, refleksi pemahaman taktis siswa, pengisian lembar asesmen mandiri, dan penutup doa bersama.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Analisis Video Kasti (3 Poin Evaluasi Kritis) -->
            <div class="analisis-section reveal">
              <div class="analisis-header">
                <div class="tagline"><i class="fa-solid fa-microscope"></i> Tinjauan Evaluatif Praktik</div>
                <h3>Analisis Video Praktik Mengajar — Permainan Kasti</h3>
                <p>Refleksi kritis terhadap efektivitas pedagogis, pengelolaan lapangan, diferensiasi alat, dan penguasaan iklim belajar.</p>
              </div>

              <div class="analisis-grid">
                <!-- Poin 1 -->
                <div class="analisis-card point-1">
                  <div class="point-badge"><i class="fa-solid fa-bullseye"></i> Poin 1 • Konteks & Tujuan</div>
                  <div class="card-icon-box"><i class="fa-solid fa-compass"></i></div>
                  <h4>Konteks & Tujuan Praktik</h4>
                  <div class="analisis-body">
                    <p>
                      <strong>Konteks Situasi Pembelajaran:</strong> Praktik dilaksanakan di lapangan terbuka SMAN 4 Yogyakarta bersama 32 peserta didik kelas XI Fase F. Keragaman kemampuan melempar dan memukul peserta didik diakomodasi melalui diferensiasi alat (bola kasti standar dan bola spons lembut untuk pemula) dan variasi jarak pos stasiun.
                    </p>
                    <ul class="analisis-list">
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Tujuan Keterampilan Motorik:</strong> Mengembangkan akurasi gerak manipulatif melempar, menangkap bola melambung/mendatar, serta teknik pukulan berarah.</li>
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Tujuan Kognitif & Taktis:</strong> Mengasah kecerdasan pengambilan keputusan (*tactical decision making*) terkait saat yang tepat berlari antar tiang hinggap (*base*).</li>
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Manajemen Keselamatan:</strong> Menata zonasi ruang pukul steril agar aman dari jangkauan penonton/pemain antrean, mencegah risiko benturan stik kayu.</li>
                    </ul>
                  </div>
                </div>

                <!-- Poin 2 -->
                <div class="analisis-card point-2">
                  <div class="point-badge"><i class="fa-solid fa-scale-balanced"></i> Poin 2 • Kelebihan & Kekurangan</div>
                  <div class="card-icon-box"><i class="fa-solid fa-chart-pie"></i></div>
                  <h4>Kelebihan & Kekurangan Praktik</h4>
                  <div class="analisis-body">
                    <div class="split-box kelebihan">
                      <h5><i class="fa-solid fa-circle-check"></i> Kelebihan / Kekuatan:</h5>
                      <ul>
                        <li><i class="fa-solid fa-check"></i> <strong>Modifikasi Alat Inklusif:</strong> Penggunaan bola spons menurunkan kecemasan (*fear of injury*) bagi siswa pemula, mendongkrak partisipasi aktif hingga 92%.</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Instruksi Suara & Isyarat Peluit:</strong> Kode peluit berjenjang (*whistle signals*) membuat transisi perpindahan pos stasiun berjalan cepat tanpa membuang waktu.</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Umpan Balik Positif & Korektif:</strong> Guru berkeliling secara dinamis memberikan koreksi spesifik pada posisi genggaman pemukul (*grip*) dan ayunan lengan.</li>
                      </ul>
                    </div>
                    <div class="split-box kekurangan">
                      <h5><i class="fa-solid fa-circle-exclamation"></i> Kekurangan & Solusi Perbaikan:</h5>
                      <ul>
                        <li><i class="fa-solid fa-triangle-exclamation"></i> <strong>Pengaruh Angin Terbuka:</strong> Hembusan angin lapangan sesekali membelokkan lintasan bola lambung; solusi berikutnya adalah menyesuaikan sudut lemparan searah angin.</li>
                        <li><i class="fa-solid fa-triangle-exclamation"></i> <strong>Waktu Tunggu Antrean:</strong> Pada awal simulasi, sebagian siswa di tiang tunggu tampak statis; solusi guru menambahkan stasiun *shadow swing* bagi giliran tunggu agar waktu aktif (*ALT-PE*) maksimal.</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <!-- Poin 3 -->
                <div class="analisis-card point-3">
                  <div class="point-badge"><i class="fa-solid fa-book-bookmark"></i> Poin 3 • Landasan Teori</div>
                  <div class="card-icon-box"><i class="fa-solid fa-brain"></i></div>
                  <h4>Kajian Teori Pedagogis Praktik</h4>
                  <div class="analisis-body">
                    <p>
                      <strong>1. Tactical Games Approach (Mitchell, Oslin, & Griffin, 2006):</strong>
                      Pembelajaran mengutamakan pemahaman taktis (*game appreciation*) sebelum teknik tingkat lanjut. Melalui siklus *game-practice-game*, siswa menyadari urgensi penempatan posisi regu jaga untuk mematikan lawan.
                    </p>
                    <div class="teori-quote">
                      "Understanding the tactical problems of games stimulates greater motivation and tactical awareness in student decision making."
                      <strong>— Mitchell et al. (Teaching Sport Concepts and Skills)</strong>
                    </div>
                    <p>
                      <strong>2. Model ALT-PE (Siedentop, 1991):</strong>
                      Pemberian stasiun gerak berulang berhasil menjaga capaian waktu aktif belajar (*Active Learning Time*) kategori *motor-appropriate* sebesar 72%, jauh di atas ambang batas standar efektivitas pembelajaran PJOK.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- =======================================================
               TAB 2: VIDEO 2 - ATLETIK (LARI SPRINT)
          ======================================================== -->
          <div class="tab-panel" id="panelAtletik">
            <div class="section-banner reveal">
              <div class="banner-left">
                <h2>Video Praktik Mengajar 2 <span class="text-blue">(Atletik Lari Jarak Pendek)</span></h2>
                <p>Pembelajaran Nomor Lari Cepat (Sprint) — Penguasaan Start Jongkok, Fase Akselerasi & Dorongan Kaki Maksimal</p>
              </div>
              <div class="banner-tags">
                <span class="badge-outline"><i class="fa-solid fa-person-running"></i> Atletik (Lari Sprint)</span>
                <span class="badge-outline"><i class="fa-solid fa-stopwatch"></i> Teknik Start & Laju Cepat</span>
                <span class="badge-outline"><i class="fa-solid fa-clock"></i> Durasi: ~17 Menit</span>
              </div>
            </div>

            <!-- Video Theater Card Atletik -->
            <div class="video-theater-card reveal">
              <div class="pdf-header">
                <div class="pdf-header-title">
                  <i class="fa-solid fa-clapperboard pdf-icon" style="color: var(--blue-light);"></i>
                  <div class="pdf-header-text">
                    <h3>Praktik Pembelajaran Atletik: Teknik Start Jongkok, Reaksi Aba-aba, & Kecepatan Lari Sprint</h3>
                    <span>Pengajar: Muhammad Layyinul Mushthofa, S.Pd • SMAN 4 Yogyakarta • Model Pembelajaran Berbasis Inkuiri & Demonstrasi</span>
                  </div>
                </div>
                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Atletik Lari Sprint')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="https://youtu.be" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-youtube"></i> Tonton di YouTube
                  </a>
                </div>
              </div>

              <!-- Video Player Screen -->
              <div class="video-player-wrapper">
                <div class="video-poster-box" style="background-image: url('../IMG/PPL_2/Praktik Mengajar 1.jpeg');" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Atletik Lari Sprint')">
                  <div class="video-badge-overlay">
                    <span class="video-badge-pill"><i class="fa-solid fa-video"></i> Full HD 1080p</span>
                    <span class="video-badge-pill"><i class="fa-solid fa-person-running"></i> Atletik Lari Sprint</span>
                  </div>
                  <button class="video-play-btn" aria-label="Putar Video Praktik Atletik">
                    <i class="fa-solid fa-play"></i>
                  </button>
                  <div class="video-badge-duration">
                    <i class="fa-solid fa-clock"></i> 17:10 Menit
                  </div>
                </div>
              </div>

              <!-- Skenario Pembelajaran Atletik -->
              <div class="skenario-timeline-box">
                <div class="skenario-timeline-title">
                  <i class="fa-solid fa-list-check text-blue"></i>
                  <span>Alur Skenario Pembelajaran Atletik Lari Jarak Pendek</span>
                </div>
                <div class="skenario-grid">
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-pendahuluan">Pendahuluan (15 Menit)</span>
                    <h5>Pemeriksaan Fisik & Drill Otot</h5>
                    <p>Skrining kesiapan otot dan persendian, pemanasan dinamis spesifik *hamstring* & *achilles*, serta drill koordinasi langkah kaki (*A-skip*, *B-skip*).</p>
                  </div>
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-inti">Kegiatan Inti (60 Menit)</span>
                    <h5>Teknik Start Jongkok & Akselerasi</h5>
                    <p>Eksplorasi posisi aba-aba (*Bersedia, Siap, Yaa*), latihan reaksi start cepat terhadap rangsang suara, lari akselerasi 30-50m pada 4 jalur paralel, dan perekaman gerak antarteman.</p>
                  </div>
                  <div class="skenario-item">
                    <span class="skenario-step-badge step-penutup">Penutup (15 Menit)</span>
                    <h5>Walking Cool-down & Rekap Catatan Waktu</h5>
                    <p>*Active walking* mencegah penumpukan asam laktat, evaluasi catatan waktu tempuh, refleksi postur dorongan kaki, dan penutup doa.</p>
                  </div>
                </div>
              </div>
            </div>

            <!-- Analisis Video Atletik (3 Poin Evaluasi Kritis) -->
            <div class="analisis-section reveal">
              <div class="analisis-header">
                <div class="tagline"><i class="fa-solid fa-microscope"></i> Tinjauan Evaluatif Praktik</div>
                <h3>Analisis Video Praktik Mengajar — Atletik (Lari Sprint)</h3>
                <p>Refleksi kritis terhadap biomekanika gerak, manajemen keselamatan lintasan lari, dan pemanfaatan asesmen sebaya.</p>
              </div>

              <div class="analisis-grid">
                <!-- Poin 1 -->
                <div class="analisis-card point-1">
                  <div class="point-badge"><i class="fa-solid fa-bullseye"></i> Poin 1 • Konteks & Tujuan</div>
                  <div class="card-icon-box"><i class="fa-solid fa-compass"></i></div>
                  <h4>Konteks & Tujuan Praktik</h4>
                  <div class="analisis-body">
                    <p>
                      <strong>Konteks Situasi Pembelajaran:</strong> Praktik diselenggarakan di lintasan lari datar SMAN 4 Yogyakarta yang ditata menjadi 4 jalur paralel aman. Zona perlambatan deselerasi di belakang garis finish disterilkan secara cermat guna menjamin keselamatan optimal siswa saat melambat.
                    </p>
                    <ul class="analisis-list">
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Tujuan Kinestetik & Teknik:</strong> Menguasai postur start jongkok (*medium start*), sudut lutut 90°-120° pada aba-aba "Siap", dan daya dorong eksplosif saat aba-aba "Yaa".</li>
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Tujuan Akselerasi & Pacing:</strong> Mempertahankan sudut kemiringan badan condong ke depan (*drive phase*) sebelum bertransisi tegak pada kecepatan puncak.</li>
                      <li><i class="fa-solid fa-circle-check"></i> <strong>Diferensiasi Beban:</strong> Penyesuaian jarak tempuh dan repetisi istirahat sesuai kapasitas kebugaran fisik individu siswa untuk mencegah ketegangan otot berlebih (*muscle strain*).</li>
                    </ul>
                  </div>
                </div>

                <!-- Poin 2 -->
                <div class="analisis-card point-2">
                  <div class="point-badge"><i class="fa-solid fa-scale-balanced"></i> Poin 2 • Kelebihan & Kekurangan</div>
                  <div class="card-icon-box"><i class="fa-solid fa-chart-pie"></i></div>
                  <h4>Kelebihan & Kekurangan Praktik</h4>
                  <div class="analisis-body">
                    <div class="split-box kelebihan">
                      <h5><i class="fa-solid fa-circle-check"></i> Kelebihan / Kekuatan:</h5>
                      <ul>
                        <li><i class="fa-solid fa-check"></i> <strong>Demonstrasi Guru Konkret & Presisi:</strong> Guru memperagakan sudut tumpuan tangan berbentuk 'V' terbalik dan penempatan kaki tumpu secara mendalam dan mudah ditiru siswa.</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Rotasi Kelompok Seri Teratur:</strong> Pengelompokan 4 siswa per seri lari membuat lintasan selalu aktif dengan ritme pergantian kelompok yang rapi dan efisien.</li>
                        <li><i class="fa-solid fa-check"></i> <strong>Integrasi Peer-Assessment:</strong> Peserta didik saling mengamati dan mencatat ketepatan postur lutut temannya saat aba-aba "Siap" menggunakan lembar checklist observasi.</li>
                      </ul>
                    </div>
                    <div class="split-box kekurangan">
                      <h5><i class="fa-solid fa-circle-exclamation"></i> Kekurangan & Solusi Perbaikan:</h5>
                      <ul>
                        <li><i class="fa-solid fa-triangle-exclamation"></i> <strong>Fokus Pandangan Garis Finish:</strong> Pada lari bersamaan 4 siswa, pandangan guru sesekali terbagi; solusi berikutnya menugaskan siswa evaluator samping lintasan untuk membantu pencatatan.</li>
                        <li><i class="fa-solid fa-triangle-exclamation"></i> <strong>Kebiasaan Duduk Usai Lari:</strong> Siswa cenderung ingin langsung duduk setelah lari intensitas tinggi; guru secara proaktif mengarahkan siswa untuk tetap berjalan santai sebelum pendinginan statis.</li>
                      </ul>
                    </div>
                  </div>
                </div>

                <!-- Poin 3 -->
                <div class="analisis-card point-3">
                  <div class="point-badge"><i class="fa-solid fa-book-bookmark"></i> Poin 3 • Landasan Teori</div>
                  <div class="card-icon-box"><i class="fa-solid fa-brain"></i></div>
                  <h4>Kajian Teori Pedagogis Praktik</h4>
                  <div class="analisis-body">
                    <p>
                      <strong>1. Tahapan Belajar Motorik (Fitts & Posner, 1967):</strong>
                      Pembelajaran memandu siswa dari tahap kognitif (memahami posisi sendi saat start) menuju tahap asosiatif (penyesuaian irama langkah) hingga otomatisasi gerak dorongan kaki.
                    </p>
                    <div class="teori-quote">
                      "Motor performance improves systematically through cognitive understanding, kinesthetic association, and autonomous neuromuscular execution."
                      <strong>— Fitts & Posner (Human Performance)</strong>
                    </div>
                    <p>
                      <strong>2. Biomekanika Gerak Sprint (Hay, 1993 / Mann, 2011):</strong>
                      Penekanan pada *Ground Reaction Force* (GRF) melalui tolakan telapak kaki bagian depan untuk memaksimalkan efisiensi transfer momentum ke arah horizontal.
                    </p>
                    <p>
                      <strong>3. Feedback Kuantitatif & Kualitatif (Schmidt & Lee, 2011):</strong>
                      Kombinasi *Knowledge of Results* (catatan waktu tempuh) dan *Knowledge of Performance* (koreksi postur lari) mempercepat perbaikan performa gerak siswa secara signifikan.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

        </div>
      </section>
    </main>

    <!-- VIDEO MODAL POPUP -->
    <div class="pdf-modal" id="videoModal">
      <div class="pdf-modal-content" style="max-width: 900px;">
        <div class="pdf-modal-header">
          <h4 id="videoModalTitle"><i class="fa-solid fa-video"></i> Pemutar Video Praktik Mengajar</h4>
          <button class="pdf-close-btn" onclick="closeVideoModal()"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="pdf-modal-body" style="padding: 0; background: #000;">
          <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
            <iframe id="videoModalIframe" src="" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="position: absolute; top:0; left: 0; width: 100%; height: 100%; border:0;"></iframe>
          </div>
        </div>
      </div>
    </div>

    <!-- FOOTER EPIC & MAPS LINK (DENGAN JARAK LUAS) -->
    <footer class="footer">
      <div class="container footer-grid">
        <div class="footer-about">
          <a href="../index.html" class="logo footer-logo">
            <img src="../IMG/logo.png" alt="logo uny" style="width: 40px" />
            <span>E Portofolio<span class="text-blue"> PPG</span></span>
          </a>
          <p>Mendedikasikan diri untuk mencetak generasi yang sehat bugar secara fisik, dan kuat secara mental melalui Pendidikan Jasmani yang inovatif.</p>
          <div class="social-icons">
            <a href="#"><i class="fa-brands fa-instagram"></i></a>
            <a href="#"><i class="fa-brands fa-youtube"></i></a>
            <a href="#"><i class="fa-brands fa-linkedin-in"></i></a>
          </div>
        </div>

        <div class="footer-links">
          <h3>Jejak PPL 1</h3>
          <ul>
            <li><a href="../PPL_1/observasi.html">Observasi</a></li>
            <li><a href="../PPL_1/modulajar.html">Modul Ajar</a></li>
            <li><a href="../PPL_1/lkpd.html">E-LKPD</a></li>
            <li><a href="../PPL_1/penilaian.html">Penilaian</a></li>
            <li><a href="../PPL_1/modelguru.html">Model Guru</a></li>
          </ul>
        </div>

        <div class="footer-links">
          <h3>Jejak PPL 2</h3>
          <ul>
            <li><a href="rancangan.html">Rancangan Pembelajaran</a></li>
            <li><a href="materi.html">Materi Pembelajaran</a></li>
            <li><a href="media.html">Media Pembelajaran</a></li>
            <li><a href="video.html">Video Praktik Mengajar</a></li>
            <li><a href="non-mengajar.html">Kegiatan Non-Mengajar</a></li>
            <li><a href="instrumen.html">Instrumen Penilaian</a></li>
          </ul>
        </div>

        <div class="footer-contact">
          <h3>Info LPTK</h3>
          <p><i class="fa-solid fa-school"></i> Universitas Negeri Yogyakarta (UNY)</p>
          <a href="https://maps.app.goo.gl/uXpXQYgR3v4v5rT46" target="_blank" class="maps-link">
            <i class="fa-solid fa-map-location-dot"></i> Lihat di Google Maps
          </a>
        </div>
      </div>

      <div class="footer-bottom">
        <p>© 2026 Muhammad Layyinul Mushthofa - PPG Prajabatan PJOK. All Rights Reserved.</p>
      </div>
    </footer>

    <!-- SCRIPTS -->
    <script>
      // 1. Navbar Sticky Effect
      window.addEventListener("scroll", () => {
        const navbar = document.getElementById("navbar");
        if (navbar) {
          if (window.scrollY > 50) {
            navbar.classList.add("scrolled");
          } else {
            navbar.classList.remove("scrolled");
          }
        }
      });

      // 2. Hamburger Mobile Nav
      const hamburger = document.getElementById("hamburger");
      const navLinks = document.getElementById("nav-links");
      if (hamburger && navLinks) {
        hamburger.addEventListener("click", () => {
          hamburger.classList.toggle("active");
          navLinks.classList.toggle("active");
        });
      }

      // 3. Dropdown Handling for Mobile
      const dropdownBtns = document.querySelectorAll(".dropbtn");
      dropdownBtns.forEach((btn) => {
        btn.addEventListener("click", function (e) {
          if (window.innerWidth <= 900) {
            e.preventDefault();
            const content = this.nextElementSibling;
            const chevron = this.querySelector(".chevron");

            document.querySelectorAll(".dropdown-content.show").forEach((openContent) => {
              if (openContent !== content) {
                openContent.classList.remove("show");
                const otherChevron = openContent.previousElementSibling?.querySelector(".chevron");
                if (otherChevron) otherChevron.style.transform = "rotate(0deg)";
              }
            });

            content.classList.toggle("show");
            if (chevron) {
              chevron.style.transform = content.classList.contains("show") ? "rotate(180deg)" : "rotate(0deg)";
            }
          }
        });
      });

      document.addEventListener("click", function (e) {
        if (!e.target.closest(".dropdown")) {
          document.querySelectorAll(".dropdown-content.show").forEach((content) => {
            content.classList.remove("show");
            const chevron = content.previousElementSibling?.querySelector(".chevron");
            if (chevron) chevron.style.transform = "rotate(0deg)";
          });
        }
      });

      // 4. Video Tabs Controller (Kasti vs Atletik)
      function switchVideoTab(type) {
        const btnKasti = document.getElementById("tabBtnKasti");
        const btnAtletik = document.getElementById("tabBtnAtletik");
        const panelKasti = document.getElementById("panelKasti");
        const panelAtletik = document.getElementById("panelAtletik");

        if (type === "kasti") {
          btnKasti.classList.add("active");
          btnAtletik.classList.remove("active");
          panelKasti.classList.add("active");
          panelAtletik.classList.remove("active");
        } else {
          btnAtletik.classList.add("active");
          btnKasti.classList.remove("active");
          panelAtletik.classList.add("active");
          panelKasti.classList.remove("active");
        }

        setTimeout(revealOnScroll, 100);
      }

      // 5. Video Modal Controller
      function openVideoModal(videoUrl, title) {
        const modal = document.getElementById("videoModal");
        const iframe = document.getElementById("videoModalIframe");
        const titleEl = document.getElementById("videoModalTitle");

        if (titleEl) {
          titleEl.innerHTML = `<i class="fa-solid fa-video"></i> ${title}`;
        }
        if (iframe) {
          iframe.src = videoUrl;
        }
        if (modal) {
          modal.classList.add("show");
          document.body.style.overflow = "hidden";
        }
      }

      function closeVideoModal() {
        const modal = document.getElementById("videoModal");
        const iframe = document.getElementById("videoModalIframe");

        if (modal) {
          modal.classList.remove("show");
          document.body.style.overflow = "auto";
        }
        if (iframe) {
          iframe.src = "";
        }
      }

      window.addEventListener("keydown", (e) => {
        if (e.key === "Escape") {
          closeVideoModal();
        }
      });

      // Close modal on click outside content
      const videoModalEl = document.getElementById("videoModal");
      if (videoModalEl) {
        videoModalEl.addEventListener("click", (e) => {
          if (e.target === videoModalEl) {
            closeVideoModal();
          }
        });
      }

      // 6. Scroll Reveal Observer
      function revealOnScroll() {
        const reveals = document.querySelectorAll(".reveal");
        const windowHeight = window.innerHeight;
        const revealPoint = 100;

        reveals.forEach((el) => {
          const revealTop = el.getBoundingClientRect().top;
          if (revealTop < windowHeight - revealPoint) {
            el.classList.add("active");
          }
        });
      }

      window.addEventListener("scroll", revealOnScroll);
      window.addEventListener("DOMContentLoaded", revealOnScroll);
    </script>
  </body>
</html>
'''

with open('PPL_2/video.html', 'w', encoding='utf-8') as f:
    f.write(html_content.strip() + '\n')

print('PPL_2/video.html updated successfully with Kasti and Atletik!')

