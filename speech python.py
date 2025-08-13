import tkinter as tk
import speech_recognition as sr

# Speech recognition function without try/except
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        output_label.config(text="Listening...")
        root.update()
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio)  # Will crash if there's an error
    output_label.config(text=f"You said: {text}")

# Tkinter GUI setup
root = tk.Tk()
root.title("Speech Recognition App")
root.geometry("400x250")
root.config(bg="#f0f0f0")

title_label = tk.Label(root, text="Speech Recognition Project", font=("Arial", 16), bg="#f0f0f0")
title_label.pack(pady=10)

output_label = tk.Label(root, text="Click the button and speak", font=("Arial", 12), wraplength=350, bg="#f0f0f0")
output_label.pack(pady=20)

listen_button = tk.Button(root, text="Start Listening", font=("Arial", 12), command=recognize_speech, bg="#4CAF50", fg="white")
listen_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), command=root.quit, bg="#f44336", fg="white")
exit_button.pack(pady=10)

root.mainloop()
