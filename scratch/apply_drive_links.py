with open('PPL_2/video.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Kasti video links
kasti_preview = "https://drive.google.com/file/d/1BTjEXJnvLIdBH-rhaplu209EO6RBO4ln/preview"
kasti_view = "https://drive.google.com/file/d/1BTjEXJnvLIdBH-rhaplu209EO6RBO4ln/view"

atletik_preview = "https://drive.google.com/file/d/1W6CIFmzNt0lOlV3g2u9IvT0ICph0DPh0/preview"
atletik_view = "https://drive.google.com/file/d/1W6CIFmzNt0lOlV3g2u9IvT0ICph0DPh0/view"

# 1. Update Kasti Header Actions
content = content.replace(
    """                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Permainan Kasti')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="https://youtu.be" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-youtube"></i> Tonton di YouTube
                  </a>
                </div>""",
    f"""                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('{kasti_preview}', 'Video Praktik Mengajar - Permainan Kasti')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="{kasti_view}" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-google-drive"></i> Buka di Google Drive
                  </a>
                </div>"""
)

# 2. Update Kasti Video Player Box
old_kasti_player = """              <!-- Video Player Screen -->
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
              </div>"""

new_kasti_player = f"""              <!-- Video Player Screen -->
              <div class="video-player-wrapper" id="playerWrapperKasti">
                <div class="video-poster-box" style="background-image: url('../IMG/PPL_2/Praktik Mengajar 1.jpeg');" onclick="playInlineVideo('playerWrapperKasti', '{kasti_preview}')">
                  <div class="video-badge-overlay">
                    <span class="video-badge-pill"><i class="fa-brands fa-google-drive"></i> Google Drive Video</span>
                    <span class="video-badge-pill"><i class="fa-solid fa-baseball-bat-ball"></i> Permainan Kasti</span>
                  </div>
                  <button class="video-play-btn" aria-label="Putar Video Praktik Kasti">
                    <i class="fa-solid fa-play"></i>
                  </button>
                  <div class="video-badge-duration">
                    <i class="fa-solid fa-circle-play"></i> Putar Video
                  </div>
                </div>
              </div>"""

content = content.replace(old_kasti_player, new_kasti_player)

# 3. Update Atletik Header Actions
content = content.replace(
    """                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('https://www.youtube.com/embed/dQw4w9WgXcQ', 'Video Praktik Mengajar - Atletik Lari Sprint')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="https://youtu.be" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-youtube"></i> Tonton di YouTube
                  </a>
                </div>""",
    f"""                <div class="pdf-actions">
                  <button class="btn-pdf-action btn-pdf-fullscreen" onclick="openVideoModal('{atletik_preview}', 'Video Praktik Mengajar - Atletik Lari Sprint')">
                    <i class="fa-solid fa-expand"></i> Layar Penuh
                  </button>
                  <a href="{atletik_view}" target="_blank" class="btn-pdf-action btn-pdf-download">
                    <i class="fa-brands fa-google-drive"></i> Buka di Google Drive
                  </a>
                </div>"""
)

# 4. Update Atletik Video Player Box
old_atletik_player = """              <!-- Video Player Screen -->
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
              </div>"""

new_atletik_player = f"""              <!-- Video Player Screen -->
              <div class="video-player-wrapper" id="playerWrapperAtletik">
                <div class="video-poster-box" style="background-image: url('../IMG/PPL_2/Praktik Mengajar 1.jpeg');" onclick="playInlineVideo('playerWrapperAtletik', '{atletik_preview}')">
                  <div class="video-badge-overlay">
                    <span class="video-badge-pill"><i class="fa-brands fa-google-drive"></i> Google Drive Video</span>
                    <span class="video-badge-pill"><i class="fa-solid fa-person-running"></i> Atletik Lari Sprint</span>
                  </div>
                  <button class="video-play-btn" aria-label="Putar Video Praktik Atletik">
                    <i class="fa-solid fa-play"></i>
                  </button>
                  <div class="video-badge-duration">
                    <i class="fa-solid fa-circle-play"></i> Putar Video
                  </div>
                </div>
              </div>"""

content = content.replace(old_atletik_player, new_atletik_player)

# 5. Add playInlineVideo function to script
old_script_start = """      // 5. Video Modal Controller
      function openVideoModal(videoUrl, title) {"""

new_script_start = """      // 5. Inline Video Player Controller
      function playInlineVideo(wrapperId, embedUrl) {
        const wrapper = document.getElementById(wrapperId);
        if (!wrapper) return;
        wrapper.innerHTML = `
          <iframe src="${embedUrl}?autoplay=1" allow="autoplay; fullscreen" allowfullscreen style="width: 100%; height: 100%; border: none;"></iframe>
        `;
      }

      // 6. Video Modal Controller
      function openVideoModal(videoUrl, title) {"""

content = content.replace(old_script_start, new_script_start)

# Save changes
with open('PPL_2/video.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated PPL_2/video.html with Google Drive links successfully!")

