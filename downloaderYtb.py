import os
from yt_dlp import YoutubeDL

def baixar_video(url):
    output_path = "Musicas"
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),  
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Baixando a música: {url}...")
            ydl.download([url])
            print("Download de áudio concluído!")
        except Exception as e:
            print(f"Erro ao tentar baixar o vídeo: {e}")

def baixar_playlist(url):
    output_path = "Playlists"
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(playlist_title)s/%(title)s.%(ext)s'),  
    }

    with YoutubeDL(ydl_opts) as ydl:
        try:
            print(f"Baixando a playlist: {url}")
            ydl.download([url])
            print("Download de áudio da playlist concluído!")
        except Exception as e:
            print(f"Erro ao tentar baixar a playlist: {e}")

escolha = int(input("Digite 1 para Video ou 2 para Playlist:"))

if escolha == 1:
    url = input("Cole o link do seu Video: ")
    baixar_video(url)
elif escolha == 2:
    url = input("Cole o link da sua Playlist: ")
    baixar_playlist(url)
else:
    print("Escolha inválida. Digite 1 para Video ou 2 para Playlist.")
