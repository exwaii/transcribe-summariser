# import whisper
import time

import openai
from dotenv import load_dotenv
import os
import tiktoken
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

punctuation_tokens = encoding.encode(".!?;:")


def translate(title, description, path):
    start = time.time()
    audio_file = open(path, "rb")
    print("translating title and description")
    prompt = f"""This video's translated english title is "{
            openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are to help translate the title of a video"},            
                    {"role": "user", "content": f"The title of this video is {title}. Please reply with only the translated title in english."},
                ]
            )["choices"][0]["message"]["content"]
    }". It's description is "{
            openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are to help translate the description of a video"},
                    {"role": "user", "content": f"The description of this video is {description}. Please reply with its translation in english. Only return up to any links, hashtags, etc."},
                ])["choices"][0]["message"]["content"]
        }." """
    end_time = time.time() - start
    print(
        f"translating title and description took {end_time // 60} minute(s) and {end_time % 60} second(s)")

    start = time.time()
    print("transcribing")
    transcript = openai.Audio.transcribe("whisper-1", audio_file, prompt=prompt)

    end_time = time.time() - start
    print(
        f"whisper transcription of audio done in {end_time // 60} minute(s) and {end_time % 60} second(s)")

    return transcript["text"]
    # translated = openai.Audio.translate("whisper-1", audio_file, prompt=prompt)


def transcribe(title, description, path, language="en"):
    start = time.time()
    audio_file = open(path, "rb")
    print("transcribing audio")
    transcript = openai.Audio.transcribe(
        "whisper-1", audio_file, prompt=f"This video's title is {title}. It's description is: {description}. ", language=language)

    end_time = time.time() - start
    print(
        f"whisper transcription of audio done in {end_time // 60} minute(s) and {end_time % 60} second(s)")

    return transcript['text']


def fix(summary, text):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": 'You are an assistant to help add line breaks ("paragraph") a trasncript for better readability' +
                ("Here is what the previous part of the transcript is about: \n" + summary) if summary else ""},
            {"role": "user", "content": "Please reply with a form of the following transcript that can be read more easily, using line breaks: \n" + text}
        ]
    )


def summarise(text):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are to return a summary of the user's input. Do not refer explicitly to the user's input, instead only return the summary."},
            {"role": "user", "content": text},
        ]
    )


def clean(text):
    start = time.time()
    transcript = fix("", text)["choices"][0]["message"]["content"]
    prev = summarise(text)["choices"][0]["message"]["content"]
    end_time = time.time() - start
    print(
        f"cleaning transcript took {end_time // 60} minute(s) and {end_time % 60} second(s)")
    return transcript, prev


def main():
    pass


if __name__ == "__main__":
    main()
