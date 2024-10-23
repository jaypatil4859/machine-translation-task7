import tkinter as tk
from tkinter import messagebox
import datetime
import tensorflow as tf
import json
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_translations(english_file, hindi_file):
    with open(english_file, 'r', encoding='utf-8') as file:
        english_sentences = file.read().strip().split('\n')
    with open(hindi_file, 'r', encoding='utf-8') as file:
        hindi_sentences = file.read().strip().split('\n')
    return dict(zip(english_sentences, hindi_sentences))

def translate_to_hindi(sentence, english_to_hindi):
    if len(sentence) < 2:
        return "Error: Word length must be at least 2 letters.", ""
    
    current_time = datetime.datetime.now().time()
    start_time = datetime.time(21, 0)
    end_time = datetime.time(22, 0)
    
    if sentence[0].lower() in 'aeiou' and not (start_time <= current_time <= end_time):
        return "", "This word starts with Vowels, provide some other words."

    hindi_translation = english_to_hindi.get(sentence.lower(), "Translation not found.")
    return f"Hindi Translation: {hindi_translation}", ""

def on_translate_click():
    sentence = entry.get()
    english_to_hindi = load_translations("data7/english.txt", "data7/hindi.txt")
    hindi, error = translate_to_hindi(sentence, english_to_hindi)
    if error:
        messagebox.showerror("Error", error)
    else:
        hindi_label.config(text=hindi)

# Load model (example file path)
model = load_model("translation_model.h5")

# GUI setup
root = tk.Tk()
root.title("Translator GUI")
tk.Label(root, text="Enter an English word:").grid(row=0)
entry = tk.Entry(root)
entry.grid(row=0, column=1)
tk.Button(root, text="Translate", command=on_translate_click).grid(row=1, columnspan=2)
hindi_label = tk.Label(root, text="")
hindi_label.grid(row=2, columnspan=2)
root.mainloop()





