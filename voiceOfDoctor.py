#setup text to speech -TTS Model - GTTS 
import os
from gtts import gTTS
from dotenv import load_dotenv

load_dotenv()


def text_to_speech_with_gtts_demo(input_text,output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)


input_text = "I am Satyam Singh Who is developing this Project"
# text_to_speech_with_gtts_demo(input_text=input_text,output_filepath="gtts_testing.mp3")


#setup text to speech -TTS Model -  ElevenLabs
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY") 

def text_to_speech_with_elevenlabs_demo(inputtext,output_file_path ):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text = inputtext,
        voice = "Aria",
        output_format="mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_file_path)

# text_to_speech_with_elevenlabs_demo(input_text,output_file_path="gtts_testing_doctor.mp3")

#use model for text output to voice(automatically play the voice)
import subprocess
import platform

def text_to_speech_with_gtts(input_text,output_filepath):
    language = "en"
    audioobj = gTTS(
        text=input_text,
        lang = language,
        slow = False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['start', '', output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")

# text_to_speech_with_gtts(input_text= input_text,output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text,output_filepath ):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text,
        voice = "Aria",
        output_format="mp3_22050_32",
        model = "eleven_turbo_v2"
    )
    elevenlabs.save(audio,output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":  # Windows
            subprocess.run(['powershell', '-c', f'Start-Process "{output_filepath}"'])
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")
    
# text_to_speech_with_elevenlabs(input_text,output_filepath="eleven_lab_autoplay_testing.mp3")