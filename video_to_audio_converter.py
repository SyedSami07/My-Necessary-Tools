from moviepy.editor import VideoFileClip
import os

video_extensions = (".mp4", ".mov", ".mkv", ".avi")

videos = [f for f in os.listdir() if f.lower().endswith(video_extensions)]

for video in videos:
    audio_name = os.path.splitext(video)[0] + ".mp3"
    
    clip = VideoFileClip(video)
    clip.audio.write_audiofile(audio_name)
    
    print(f"{video} -> {audio_name}")