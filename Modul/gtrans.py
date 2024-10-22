from googletrans import Translator

def TransLate(text: str, scr: str, dest: str) -> str:
    """ Функція повертає текст перекладений на задану мову, або повідомлення про помилку. """
    try:
        translator = Translator()
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str) -> str:
    """ Функція визначає мову та коефіцієнт довіри для заданого тексту. """
    try:
        translator = Translator()
        detected = translator.detect(text)
        
        if detected is None:
            return "Error: No language detected."

        if set == "lang":
            return detected.lang
        elif set == "confidence":
            return detected.confidence
        else:  # set == "all"
            return detected.lang, detected.confidence
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    """ Функція повертає код мови або назву мови. """
    languages = {
        "uk": "Ukrainian",
        "en": "English",
        "fr": "French",
        "de": "German",
        # Додайте більше мов за потреби
    }
    for code, name in languages.items():
        if lang == code:
            return name
        if lang.lower() == name.lower():
            return code
    return "Language not found."

def LanguageList(out: str, text: str) -> str:
    """ Виводить в файл або на екран таблицю всіх мов, що підтримуються, та їх кодів. """
    try:
        languages = {
            "Ukrainian": "uk",
            "Afrikaans": "af",
            "Albanian": "sq",
            "Amharic": "am",
            "Arabic": "ar",
            "Armenian": "hy",
            # Додайте більше мов за потреби
        }

        print(f"N Language ISO-639 code Text")
        print("--------------------------------------------------------")
        for i, (name, code) in enumerate(languages.items(), start=1):
            if text:
                translated_text = TransLate(text, 'auto', code)
            else:
                translated_text = "No text provided."
            print(f"{i} {name} {code} {translated_text}")

        return "Ok"
    except Exception as e:
        return f"Error: {e}"

# Приклад викликів функцій
if __name__ == "__main__":
    result = TransLate("Привіт, світ!", "uk", "en")
    print(f"Translated text: {result}")

    detected_lang = LangDetect("Привіт, світ!", "lang")
    print(f"Detected language: {detected_lang}")

    LanguageList("output.txt", "Привіт, світ!")
