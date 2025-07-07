import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        label_var.set("Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            label_var.set("Recognizing...")
            window.update()
            text = recognizer.recognize_google(audio)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            speak_text(text)
        except sr.UnknownValueError:
            text_box.insert(tk.END, "Could not understand.")
            speak_text("Sorry, I didn't catch that.")
        except sr.RequestError:
            text_box.insert(tk.END, "Service is down.")
            speak_text("Speech service is not available.")

# GUI setup
window = tk.Tk()
window.title("Voice Recognition System")
window.attributes('-fullscreen', True)
window.configure(bg='black')

label_var = tk.StringVar()
label_var.set("Press the button and speak")

label = tk.Label(window, textvariable=label_var, font=("Arial", 30), fg="white", bg="black")
label.pack(pady=20)

text_box = tk.Text(window, font=("Arial", 20), height=10, wrap="word")
text_box.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(window, bg='black')
btn_frame.pack(pady=20)

listen_btn = tk.Button(btn_frame, text="🎤 Speak Now", font=("Arial", 20), command=recognize_speech, bg="green", fg="white")
listen_btn.pack(side=tk.LEFT, padx=20)

exit_btn = tk.Button(btn_frame, text="❌ Exit", font=("Arial", 20), command=window.quit, bg="red", fg="white")
exit_btn.pack(side=tk.LEFT, padx=20)

# Exit on ESC key
window.bind("<Escape>", lambda e: window.destroy())

window.mainloop()
import tkinter as tk
import speech_recognition as sr
import pyttsx3

# Initialize recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    with sr.Microphone() as source:
        label_var.set("Listening...")
        window.update()
        try:
            audio = recognizer.listen(source, timeout=5)
            label_var.set("Recognizing...")
            window.update()
            text = recognizer.recognize_google(audio)
            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, text)
            speak_text(text)
        except sr.UnknownValueError:
            text_box.insert(tk.END, "Could not understand.")
            speak_text("Sorry, I didn't catch that.")
        except sr.RequestError:
            text_box.insert(tk.END, "Service is down.")
            speak_text("Speech service is not available.")

# GUI setup
window = tk.Tk()
window.title("Voice Recognition System")
window.attributes('-fullscreen', True)
window.configure(bg='black')

label_var = tk.StringVar()
label_var.set("Press the button and speak")

label = tk.Label(window, textvariable=label_var, font=("Arial", 30), fg="white", bg="black")
label.pack(pady=20)

text_box = tk.Text(window, font=("Arial", 20), height=10, wrap="word")
text_box.pack(padx=50, pady=20, fill=tk.BOTH, expand=True)

btn_frame = tk.Frame(window, bg='black')
btn_frame.pack(pady=20)

listen_btn = tk.Button(btn_frame, text="🎤 Speak Now", font=("Arial", 20), command=recognize_speech, bg="green", fg="white")
listen_btn.pack(side=tk.LEFT, padx=20)

exit_btn = tk.Button(btn_frame, text="❌ Exit", font=("Arial", 20), command=window.quit, bg="red", fg="white")
exit_btn.pack(side=tk.LEFT, padx=20)

# Exit on ESC key
window.bind("<Escape>", lambda e: window.destroy())

window.mainloop()
