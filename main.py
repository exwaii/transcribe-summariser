from transcribe import transcribe, clean, translate
from download import get_audio_yt


def output(path, og, cleaned=None, summary=None):
    with open(path + " original.txt", "w", encoding="utf-8") as f:
        f.write(og)
    if cleaned:
        with open(path + " cleaned.txt", "w",  encoding="utf-8") as f:
            f.write(cleaned)
    if summary:
        with open(path + " summary.txt", "w", encoding="utf-8") as f:
            f.write(summary)


def main():
    url = input("Enter the url of the video: ")
    title, description, path = get_audio_yt(url)

    transcription = transcribe(title, description, path)
    
    
    output(f"transcriptions/{title}/{title}", transcription, *clean(transcription))


if __name__ == "__main__":
    main()
    # import time

    # import openai
    # from dotenv import load_dotenv
    # import os
    # import tiktoken

    # load_dotenv()

    # openai.api_key = os.getenv("OPENAI_API_KEY")

    # encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

    # punctuation_tokens = encoding.encode(".!?;:")

    # audio_file = open(
    #     "transcriptions/Bo Burnham vs. Jeff Bezos/Bo Burnham vs Jeff Bezos.mp4", "rb"
    # )

    # start = time.time()

    # transcript = openai.Audio.transcribe("whisper-1", audio_file, response_format="srt")

    # end_time = time.time() - start
    # print(
    #     f"whisper transcription of audio done in {end_time // 60} minute(s) and {end_time % 60} second(s)"
    # )

