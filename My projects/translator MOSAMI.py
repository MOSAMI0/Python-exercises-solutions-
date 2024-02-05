from translate import Translator

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

def translate_text(text, target_language):
    translator = Translator(to_lang=target_language)
    translation = translator.translate(text)
    return translation

# Prompt the user for input
allow = True  # variable to control correct language code input

while allow:  # checking if language code is valid

    text = input(
        f"Enter the text to translate: ")
    options = input("To see the language code list enter 'options' or press any key to pass : ")
    if options == 'options':  # showing language options
        for key, value in language.items():
            print(key, ":", value)  # Heading of language option menu
    else:
        pass
    target_language = input("Enter the target language: ")


# Call the translate_text function
    translation = translate_text(text, target_language)

    # Display the translation
    print("Translation:", translation)
