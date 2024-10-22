from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # Для консистентного результату

def TransLate(text: str, scr: str, dest: str) -> str:
    """ Функція повертає текст перекладений на задану мову, або повідомлення про помилку. """
    try:
        translated = GoogleTranslator(source=scr, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str) -> str:
    """ Функція визначає мову для заданого тексту. """
    try:
        language = detect(text)
        return language if set in ["lang", "all"] else None
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

        if out == "screen":
            print(f"N Language ISO-639 code Text")
            print("--------------------------------------------------------")
            for i, (name, code) in enumerate(languages.items(), start=1):
                if text:
                    translated_text = TransLate(text, 'auto', code)
                else:
                    translated_text = "No text provided."
                print(f"{i} {name} {code} {translated_text}")

        # Додати обробку для збереження в файл, якщо потрібно

        return "Ok"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Приклад перекладу
    result = TransLate("Привіт, світ!", "uk", "en")
    print(f"Translated text: {result}")

    # Приклад визначення мови
    detected_lang = LangDetect("Привіт, світ!", "lang")
    print(f"Detected language: {detected_lang}")

    # Приклад виводу списку мов
    LanguageList("screen", "Привіт, світ!")
