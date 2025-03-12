#setting audiorecoder (ffmpeg & portaudio)
import logging
import os
# from langchain_groq import ChatGroq
import sounddevice as sd
import numpy as np
import wave
import time
from groq import Groq
from dotenv import load_dotenv
load_dotenv()


logging.basicConfig(level = logging.INFO,format= '%(asctime)s - %(levelname)s - %(message)s')



def record_audio(file_path, sample_rate=44100, silence_threshold=500, silence_duration=15):
    print("Recording started... Speak now!")
    
    audio_chunks = []
    silence_start = None
    is_speaking = False
    
    while True:
        # Record small chunks (1 second)
        chunk = sd.rec(int(sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
        sd.wait()
        
        # Convert chunk to numpy array and check volume level
        volume_level = np.abs(chunk).mean()
        
        if volume_level > silence_threshold:
            is_speaking = True
            silence_start = None  # Reset silence timer
            audio_chunks.append(chunk)
        else:
            if is_speaking:
                if silence_start is None:
                    silence_start = time.time()  # Start silence timer
                elif time.time() - silence_start >= silence_duration:
                    print("No speech detected for 15 seconds. Stopping recording...")
                    break
    
    # Combine all recorded chunks
    if audio_chunks:
        audio_data = np.concatenate(audio_chunks, axis=0)
        
        # Save as WAV file
        with wave.open(file_path, 'wb') as wf:
            wf.setnchannels(1)  # Mono
            wf.setsampwidth(2)  # 16-bit
            wf.setframerate(sample_rate)
            wf.writeframes(audio_data.tobytes())
        
        print(f"Audio saved to {file_path}")
    else:
        print("No audio recorded.")

# Set file path where you want to save the recorded audio
# audio_filepath="patient_voice_test_for_patient.mp3"

# record_audio(audio_filepath, duration=10)


def transcribe_with_groq(stt_model, audio_filepath, GROQ_API_KEY):
    client=Groq(api_key=GROQ_API_KEY)
    
    audio_file=open(audio_filepath, "rb")
    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en"
    )

    return transcription.text

#setup speech to text-STT-model for transcription
# GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
# model = "whisper-large-v3"
# client = Groq(
#     api_key= GROQ_API_KEY
# )
# audio_file = open(audio_filepath,"rb") 
# transcription=client.audio.transcriptions.create(
#         model=model,
#         file=audio_file,
#         language="en"
#     )
