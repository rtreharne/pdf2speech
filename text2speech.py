from gtts import gTTS
import sys

def text_to_mp3(fname):
    with open(fname, 'r') as f:
        data = f.read()
        print(data)
    tts = gTTS(text=data, lang='en')
    tts.save("output.mp3")

if __name__ == "__main__":
    text_to_mp3("elligibility.txt")
