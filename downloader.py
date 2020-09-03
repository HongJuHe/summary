from pytube import YouTube
import os
from pydub import AudioSegment
import glob
import moviepy.editor as mp

num = int(input("몇개의 영상 다운?: "))
for i in range(0, num):
    url = input("url 입력: ")
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(os.getcwd())

files = glob.glob("*.mp4")
for x in files:
    if not os.path.isdir(x):
        filename = os.path.splitext(x)
        print(x)
        try:
            clip = mp.VideoFileClip(x)
            clip.audio.write_audiofile(filename[0]+".mp3")
            sound = AudioSegment.from_mp3(os.getcwd()+"/"+filename[0]+".mp3")
            sp = int(input("몇초부터?"))
            temp = sound[sp:sp+10000]
            temp.export(os.getcwd()+"/"+ filename[0] + ".wav", format="wav")
        except:
            pass