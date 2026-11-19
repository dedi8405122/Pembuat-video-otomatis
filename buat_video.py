PHYTON
from moviepy.editor import TextClip

# Membuat klip teks berdurasi 5 detik
clip = TextClip("Video Otomatis dari GitHub!", fontsize=50, color='white', size=(1280, 720), bg_color='black')
clip = clip.set_duration(5)

# Menyimpan hasil menjadi file MP4
clip.write_videofile("hasil_video.mp4", fps=24)
