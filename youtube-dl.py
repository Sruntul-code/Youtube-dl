#Coded By Puxonz
#Open Source Project

import youtube_dl
import requests
from bs4 import BeautifulSoup
import sys
import os

c = requests.Session()
os.system("pkg install ffmpeg")
def download_mp3():
   try:
      ydl_opts = {
          'format': 'bestaudio/best',
          'noplaylist': True,
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
          }],
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
           filenames = (["https://m.youtube.com"+link])
           ydl.download(filenames)
   except youtube_dl.utils.DownloadError:
      print ("Your Connection Lost")
      sys.exit()
def download_mp4():
   try:
       ydl_opts = {'format': '18','noplaylist': True}
       with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            filenames = (["https://m.youtube.com"+link])
            ydl.download(filenames)
   except youtube_dl.utils.DownloadError:
       print ("Your Connection Lost")
       sys.exit()
def convert(url):
    print("""
    \033[33m[\033[35m1\033[33m] \033[39mDownload Mp4
    \033[33m[\033[35m2\033[33m] \033[39mDownload Mp3
    """)
    chose = input("\033[33m$puxonz \033[32m>>> \033[39m")
    if chose == "1":
         try:
             ydl_opts = {'format': '18','noplaylist': True}
             with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                   filenames = ([url])
                   ydl.download(filenames)
         except youtube_dl.utils.DownloadError:
             print ("Your Connection Lost")
             sys.exit()
    elif chose == "2":
       try:
           ydl_opts = {
              'format': 'bestaudio/best',
              'noplaylist': True,
              'postprocessors': [{
                  'key': 'FFmpegExtractAudio',
                  'preferredcodec': 'mp3',
                  'preferredquality': '192',
              }],
           }
           with youtube_dl.YoutubeDL(ydl_opts) as ydl:
              filenames = ([url])
              ydl.download(filenames)
       except youtube_dl.utils.DownloadError:
           print ("Your Connection Lost")
           sys.exit()
    print ("\n\033[33m[\033[32m√\033[33m] \033[39mDownload Success")
    inp = input("")
    main()
def cari_lagu():
    try:
         global search
         search = input("\n\033[33mSearch Songs \033[32m>>> \033[39m")
         url = "https://m.youtube.com/results?search_query="+search
         r = c.get(url)
         soup = BeautifulSoup(r.content, "html.parser")
         angka = 0
         for i in soup.find_all("div", class_="yt-lockup-content"):
              for u in i.findChildren("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link"):
                  angka += 1
                  print ("")
                  print ("\033[33m[\033[35m"+str(angka)+"\033[33m]\033[39m", u.text)
         pilih()
    except requests.exceptions.ConnectionError:
         print ("Your Connection Lost")
def get_link(par,x):
    try:
        url = "https://m.youtube.com/results?search_query="+par
        r = c.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        angka = 0
        for i in soup.find_all("div", class_="yt-lockup-content"):
             angka += 1
             if angka == x:
                for u in i.findChildren("a", class_="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link"):
                    global link
                    link = u.get("href")
    except requests.exceptions.ConnectionError:
        print ("Your Connection Lost")
        sys.exit()
def pilih():
    pil = input("\n\033[33m$puxonz \033[32m>>> \033[39m")
    get_link(search,int(pil))
    print ("""
    \033[33m[\033[35m1\033[33m] \033[39mDownload Mp4
    \033[33m[\033[35m2\033[33m] \033[39mDownload Mp3
    """)
    pilih = input("\033[33m$puxonz \033[32m>>> \033[39m")
    if pilih == "1":
        download_mp4()
        print ("\n\033[33m[\033[32m√\033[33m] \033[39mDownload Success")
        inp = input("")
        main()
    elif pilih == "2":
        download_mp3()
        print ("\n\033[33m[\033[32m√\033[33m] \033[39mDownload Success")
        inp = input("")
        main()
def main():
    os.system("clear")
    print("""\033[33m
    __  __            __        __                   ____
    \ \/ /___  __  __/ /___  __/ /_  ___        ____/ / /
     \  / __ \/ / / / __/ / / / __ \/ _ \______/ __  / /
     / / /_/ / /_/ / /_/ /_/ / /_/ /  __/_____/ /_/ / /
    /_/\____/\__,_/\__/\__,_/_.___/\___/      \__,_/_/
  \033[34m******************************************************* 
  \033[32mAuthor     : Puxonz
  Facebook   : -----
  Whatsapp   : 083195027524
  \033[34m*******************************************************
   \033[33m[\033[35m1\033[33m] \033[39mSearch Song's
   \033[33m[\033[35m2\033[33m] \033[39mConvert Video Url to Mp4/Mp3
    """)
    change = input("\033[33m$puxonz \033[32m>>> \033[39m")
    if change == "1":
        cari_lagu()
    elif change == "2":
        celex = input("\n\033[33mEnter Video Url \033[32m>>> \033[39m")
        convert(celex)

main()
