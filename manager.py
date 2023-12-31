from pytube import YouTube, Playlist
from time import sleep


def download_playlist(p, q):
    # q = 22
    p = Playlist(p)
    print(f'Downloading: {p.title}')
    for video in p.videos:
        print(video.title)
        sleep(1)
        try:
            stream = video.streams.get_by_itag(q)
            stream.download(output_path=f"/vids/{p.title}-{video.author}")
        except:
            print(f"Failed to download {video.title} - {video.author}")


def download_video(v, q):
    # q = 22
    v = YouTube(v)
    print(f'Downloading: {v.title}')
    try:
        stream = v.streams.get_by_itag(q)
        stream.download(output_path=f"/vids/{v.author}/")
    except:
        print(f"Failed to download {v.title} - {v.author}")
