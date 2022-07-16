import os
from pathlib import Path

import pdfplumber
from art import tprint
from gtts import gTTS
from playsound import playsound
from loguru import logger


def create_folder(folder):
    """Create res folder."""
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except:
            print(f"Error for create dir: {folder}")


def converter_to_mp3(file_path="", language="en", play_sound=False):
    """
    Get file and convert to mp3.
    Can be choose language for audio.
    """
    is_file = Path(file_path).is_file()
    suffix_file = Path(file_path).suffix
    if is_file and suffix_file == ".pdf":
        with pdfplumber.PDF(open(file_path, mode="rb")) as pdf:
            pages = [page.extract_text() for page in pdf.pages]
        text = "".join(pages)
        text.replace("\n", "")

        my_mp3 = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        create_folder("mp3")
        my_mp3.save(f"mp3\{file_name}.mp3")
        logger.info(f"{file_name}.mp3 created.")
        if play_sound:
            playsound(f"mp3\{file_name}.mp3")
        return f"{file_name}.mp3 created successfully."
    elif is_file and suffix_file == ".txt":
        with open(file_path, encoding="utf-8", mode="r") as txt:
            read_text = txt.read()
        text = "".join(read_text)
        file_name = Path(file_path).stem
        tts = gTTS(text=text, lang=language)
        tts.save(f"mp3\{file_name}.mp3")
        if play_sound:
            playsound(f"mp3\{file_name}.mp3")
        logger.info(f"{file_name}.mp3 created.")
        return f"{file_name}.mp3 created successfully."
    else:
        return "File not pdf, txt."


if __name__ == "__main__":
    tprint("PDF->MP3", font="bulbhead")
    converter_to_mp3(
        file_path=r"path to txt file",
        language="en",
        play_sound=False,
    )
