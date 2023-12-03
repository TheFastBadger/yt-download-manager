from pytube import YouTube, Playlist
from time import sleep

while True:
    p = Playlist(str(input("Enter a playlist url: ")))

    print(f'Downloading: {p.title}')
    for video in p.videos:
        print(video.title)
        sleep(1)
        try:
            stream = video.streams.get_by_itag(22)
            stream.download(output_path=f"C:/Users/mfair/Documents/vids/{p.title}-{video.author}")
        except:
            print(f"Failed to download {video.title} - {video.author}")
