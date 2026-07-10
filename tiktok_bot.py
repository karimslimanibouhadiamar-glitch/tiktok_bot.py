import os
from gtts import gTTS
from moviepy.editor import TextClip, ColorClip, CompositeVideoClip

def create_tiktok_video(text, output_filename="tiktok_video.mp4"):
    print("🤖 جاري تحويل النص إلى صوت بالذكاء الاصطناعي...")
    # 1. تحويل النص إلى صوت (Voiceover)
    tts = gTTS(text=text, lang='ar')
    audio_filename = "voice.mp3"
    tts.save(audio_filename)
    
    print("🎬 جاري تصميم الفيديو وكتابة النصوص التلقائية...")
    # 2. إنشاء خلفية فيديو ملونة بمقاسات التيك توك (1080x1920)
    # مدة الفيديو 5 ثوانٍ كمثال
    background = ColorClip(size=(1080, 1920), color=(30, 30, 45), duration=5)
    
    # 3. كتابة النص متحرك على الشاشة (Subtitles)
    text_clip = TextClip(text, fontsize=70, color='white', font='Arial-Bold', 
                         method='caption', size=(900, None))
    text_clip = text_clip.set_position('center').set_duration(5)
    
    # 4. دمج الصوت مع الفيديو والخلفية
    video = CompositeVideoClip([background, text_clip])
    video = video.set_audio(audio_filename)
    
    # 5. حفظ الفيديو النهائي بجودة عالية
    video.write_videofile(output_filename, fps=24, codec="libx264", audio_codec="aac")
    print(f"✅ تم إنشاء الفيديو بنجاح باسم: {output_filename}")

if __name__ == "__main__":
    # اكتب هنا الفكرة أو المعلومة التي تريد أن يحولها البوت إلى فيديو
    idea_text = "هل تعلم أن الذكاء الاصطناعي يمكنه برمجة هذا الفيديو بالكامل؟"
    create_tiktok_video(idea_text)
