import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
from googletrans import Translator, constants
from pprint import pprint
from gtts import gTTS 
import pyaudio
import sys
import wave

class support:

  def __init__(self):
    super().__init__()

  def audio_transcription(self,path, lang):
    r = sr.Recognizer()

    sound = AudioSegment.from_wav(path)  
    # split audio sound where silence is 700 miliseconds or more and get chunks
    chunks = split_on_silence(sound,
        # experiment with this value for your target audio file
        min_silence_len = 500,
        # adjust this per requirement
        silence_thresh = sound.dBFS-22,
        # keep the silence for 1 second, adjustable as well
        keep_silence=100,
    )
    folder_name = "audio-chunks"
    # create a directory to store the audio chunks
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    whole_text = ""
    # process each chunk 
    for i, audio_chunk in enumerate(chunks, start=1):
        # export audio chunk and save it in
        # the `folder_name` directory.
        chunk_filename = os.path.join(folder_name, f"chunk{i}.wav")
        audio_chunk.export(chunk_filename, format="wav")
        # recognize the chunk
        with sr.AudioFile(chunk_filename) as source:
            audio_listened = r.record(source)
            # try converting it to text
            try:
                text = r.recognize_google(audio_listened, language = lang)
            except sr.UnknownValueError as e:
                print("Error:", str(e))
            else:
                text = f"{text.capitalize()}. "
                #print(chunk_filename, ":", text)
                whole_text += text
    # return the text for all chunks detected
    return whole_text.replace(".","")





  def Speach_conversion(self,txt, lang):
    splt_txt=txt.split('.')
    translator = Translator()
    translations = translator.translate(splt_txt, dest=lang)
    C=''
    for translation in translations:
        C=C + ' ' + translation.text + '.'
    return C


  def Text_to_speach(self,conversion_to_Lang2,lang_to):
    speak = gTTS(text=conversion_to_Lang2, lang=lang_to, slow= False) 
    # Using save() method to save the translated  
    # speech in capture_voice.mp3 
    speak.save("static/captured_voice.mp3")      
    # Using OS module to run the translated voice. 
    #os.system("start captured_voice.mp3") static\captured_voice.mp3






