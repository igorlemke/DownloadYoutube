#importar a biblioteca necessaria
from pytube import YouTube

#criar um objeto do tipo YouTube
yt = YouTube('https://www.youtube.com/watch?v=dpEjpSx68YI')

#ordena os streams por resolução e faz o download daquele
#que possui a maior resolução
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()