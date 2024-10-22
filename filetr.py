# filetr.py
import json
import os
from Modul.gtrans import TransLate, LangDetect

def read_config(config_file):
    """ Читає конфігураційний файл. """
    with open(config_file, 'r') as file:
        return json.load(file)

def process_text(file_name, target_lang, output, max_chars, max_words, max_sentences):
    """ Обробляє текстовий файл і виконує переклад. """
    if not os.path.exists(file_name):
        return "File not found."

    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        words = content.split()
        sentences = content.split('.')

        # Перевірка умов
        if len(content) > max_chars or len(words) > max_words or len(sentences) > max_sentences:
            content = " ".join(words[:max_words])
            content += '. '.join(sentences[:max_sentences])

        translated_text = TransLate(content, 'auto', target_lang)

        if output == "screen":
            print(f"Translated to {target_lang}: {translated_text}")
        elif output == "file":
            output_file = f"{os.path.splitext(file_name)[0]}_{target_lang}.txt"
            with open(output_file, 'w', encoding='utf-8') as out_file:
                out_file.write(translated_text)
            return "Ok"
    return "Error"

if __name__ == "__main__":
    config = read_config('config.json')
    process_text(config['file_name'], config['target_lang'], config['output'], 
                 config['max_chars'], config['max_words'], config['max_sentences'])
