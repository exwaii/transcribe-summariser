import time
from pytube import YouTube

FORBIDDEN_FOLDER_CHARS = '\\/:*?"<>|'


def get_data(url):
    # TODO
    # GET SUBTITLES IF THERE ARE SUBTITLES
    # PUNCTUATE AND PARAGRAPH AND REMOVE REDUNCANCIES IN TRANSCRIPT
    # SUBTITLES HAVE TIMESTAMPS, FIGURE OUT HOW TO MAKE TRANSCRIPTION TIMESTAMPS FROM WHISPER CODE
    # WITH SUMMARY, CAN MAKE LIKE A CONTENTS PAGE (IF THERE ISNT ALREADY)
    # GPT PULL OUT KEY POINTS, AND TIMESTAMPS WHERE

    start = time.time()
    print("getting youtube audio")
    yt = YouTube(url)
    title = yt.title
    description = yt.description
    for char in FORBIDDEN_FOLDER_CHARS:
        title = title.replace(char, "")
        description = description.replace(char, "")
    path = yt.streams.get_audio_only().download(f"transcriptions\\{title}")
    with open(f"transcriptions/{title}/url.txt", "w") as f:
        f.write(url)
    download_time = time.time() - start
    print(f"youtube audio downloaded in {download_time // 60} minute(s) and {download_time % 60} second(s)")
    return title, description, path

def main():
    get_data("https://youtu.be/GfrF25Fg5rs")


if __name__ == "__main__":
    main()