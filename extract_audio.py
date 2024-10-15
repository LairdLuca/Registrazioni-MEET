from moviepy.editor import VideoFileClip

def extract_audio_from_video(video_path, audio_path):
    """
    Estrae l'audio da un video e lo salva come file separato.

    Args:
    video_path (str): Il percorso del file video da cui estrarre l'audio. (.mp4)
    audio_path (str): Il percorso del file audio da salvare. (.mp3)

    Returns:
    None
    """
    # Carica il video
    video_clip = VideoFileClip(video_path)
    
    # Estrai l'audio dal video
    audio_clip = video_clip.audio
    
    # Salva l'audio in un file
    audio_clip.write_audiofile(audio_path)
    
    # Rilascia le risorse
    audio_clip.close()
    video_clip.close()

# Definisci il percorso del video e il percorso del file audio di output
video_path = 'esempio_video.mp4'
audio_path = 'audio_estratto.mp3'

# Chiama la funzione per estrarre l'audio dal video
extract_audio_from_video(video_path, audio_path)

print("L'audio è stato estratto e salvato in:", audio_path)