from moviepy import editor

video = editor.VideoFileClip('E:\\vs code\\EX-7\\Music-espanish.mp4')
video.audio.write_audiofile('E:\\vs code\\EX-7\\Music-espanish.mp3')