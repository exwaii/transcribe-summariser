from transcribe import transcribe, clean, translate
from download import get_data


def output(path, og, cleaned=None, summary=None):
    with open(path[:-4] + " original.txt", "w", encoding="utf-8") as f:
        f.write(og)
    if cleaned:
        with open(path[:-4] + " cleaned.txt", "w",  encoding="utf-8") as f:
            f.write(cleaned)
    if summary:
        with open(path[:-4] + " summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)


def main():
    url = input("Enter the url of the video: ")
    title, description, path = get_data(url)

    transcription = transcribe(title, description, path)
    
    
    output(f"transcriptions/{title}/{title}", transcription, *clean(transcription))


if __name__ == "__main__":
    main()

