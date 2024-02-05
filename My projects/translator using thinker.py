import tkinter as tk
from googletrans import Translator
import webbrowser

# Language options
LANGUAGES = {
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


def translate_text():
    text = input_text.get('1.0', 'end-1c')
    source_lang = source_lang_var.get()
    target_lang = target_lang_var.get()

    translator = Translator()
    translated_text = translator.translate(text, src=source_lang, dest=target_lang)

    output_text.delete('1.0', 'end')
    output_text.insert('1.0', translated_text.text)


def open_link():
    link = link_text.get('1.0', 'end-1c')
    webbrowser.open(link)


root = tk.Tk()
root.title("Translator")
root.configure(bg="light blue")  # Set the background color to light blue

# Source Language dropdown
source_lang_label = tk.Label(root, text="Source Language:")
source_lang_label.pack()

source_lang_var = tk.StringVar(root)
source_lang_var.set("en")  # Set default source language

source_lang_dropdown = tk.OptionMenu(root, source_lang_var, *LANGUAGES.values())
source_lang_dropdown.pack()

# Input Text Field
input_label = tk.Label(root, text="Input Text:")
input_label.pack()

input_text = tk.Text(root, height=5, width=50)
input_text.pack()

# Target Language dropdown
target_lang_label = tk.Label(root, text="Target Language:")
target_lang_label.pack()

target_lang_var = tk.StringVar(root)
target_lang_var.set("ar")  # Set default target language

target_lang_dropdown = tk.OptionMenu(root, target_lang_var, *LANGUAGES.values())
target_lang_dropdown.pack()

# Translate button
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Translated Text Field
output_label = tk.Label(root, text="Translated Text:")
output_label.pack()

output_text = tk.Text(root, height=5, width=50)
output_text.pack()

# Link Label
link_label = tk.Label(root, text="My social networking sites :", bg="#e0e0e0")
link_label.pack()

link_text = tk.Text(root, height=1, width=28)
link_text.pack()
link_text.insert('1.0', "https://linktr.ee/mosami7700")

# Open Link Button
open_link_button = tk.Button(root, text="Open Link", command=open_link)
open_link_button.pack()

root.mainloop()
