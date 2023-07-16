from pydub.generators import Sine
from pydub import AudioSegment
from tkinter import filedialog, Tk
import time

DIZIONARIO_CODICE_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.',
    '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': ' ',
    'À': '.--.-', 'È': '.-..-', 'É': '..-..', 'Ì': '..--', 'Ò': '---.', 'Ù': '..--'
}

def show_menu():
    print("1. Testo -> morse + audio morse")
    print("0. Exit")

def testo_in_codice_morse(testo):
    codice_morse = ''
    for char in testo:
        char_maiuscolo = char.upper()
        if char_maiuscolo in DIZIONARIO_CODICE_MORSE:
            codice_morse += DIZIONARIO_CODICE_MORSE[char_maiuscolo] + ' '
        else:
            codice_morse += char + ' '  # Preserva i caratteri non alfanumerici così come sono

    return codice_morse.strip()

def genera_audio(codice_morse):
    audio = AudioSegment.silent(duration=200)  # Silenzio iniziale di 200 millisecondi
    frequenza = 440  # Frequenza per l'onda sinusoidale (nota A4)

    for simbolo in codice_morse:
        if simbolo == '.':
            audio += Sine(frequenza).to_audio_segment(duration=100) + AudioSegment.silent(duration=100)
        elif simbolo == '-':
            audio += Sine(frequenza).to_audio_segment(duration=300) + AudioSegment.silent(duration=100)
        elif simbolo == ' ':
            audio += AudioSegment.silent(duration=300)  # Pausa tra le lettere
        elif simbolo == '/':
            audio += AudioSegment.silent(duration=600)  # Pausa tra le parole

    return audio

if __name__ == "__main__":
    show_menu()
    choice = input("Seleziona un'opzione: ")

    if choice == '1':
        testo_input = input("Inserisci il testo da convertire in codice Morse: ")
        codice_morse_output = testo_in_codice_morse(testo_input)
        print("\nCodice Morse:")
        print(codice_morse_output)

        audio_output = genera_audio(codice_morse_output)
        root = Tk()
        root.withdraw()
        file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("Wave Audio", "*.wav")])
        root.destroy()

        if file_path:
            audio_output.export(file_path, format="wav")
            print("File salvato con successo!")
        else:
            print("Operazione di salvataggio annullata.")
        
    elif choice == '0':
        print("Uscita.")
    
    else:
        print("Scelta non valida.")
