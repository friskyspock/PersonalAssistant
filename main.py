from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
  print("Say something!")
  audio = r.listen(source)

# recognize speech using whisper
try:
  input_text = r.recognize_whisper(audio, model="base.en")
  print("User: ",input_text)
except sr.UnknownValueError:
  print("Whisper could not understand audio")
except sr.RequestError as e:
  print(f"Could not request results from Whisper; {e}")

llm = Ollama(
    model="gemma", 
    request_timeout=30.0
)


def add_task(task):
  with open("to-do-list.txt","+a") as file:
      file.write(task+'\n')



print("Assistant: ",response['message']['content'])
engine.say(response['message']['content'])
engine.runAndWait()