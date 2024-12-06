from datasets import load_dataset
import librosa
import numpy as np
import os

# Step 1: Load CommonVoice dataset (English)
dataset = load_dataset("common_voice", "en")

# Step 2: Access the 'train' subset of the dataset
train_data = dataset["train"]

# Example: Print the first 5 entries from the train dataset to verify
for i in range(5):
    print(f"Audio path: {train_data[i]['audio']['path']}, Transcription: {train_data[i]['sentence']}")

# Step 3: Preprocess the audio data (convert to mono, resample, and extract MFCCs)
def preprocess_audio(file_path, target_sr=16000):
    """
    Preprocesses an audio file: converts to mono, resamples, and extracts MFCCs.
    """
    # Load the audio file using librosa
    audio, sr = librosa.load(file_path, sr=target_sr)

    # Ensure mono audio (if stereo, convert to mono)
    if len(audio.shape) > 1:
        audio = np.mean(audio, axis=1)

    # Extract MFCCs from the audio
    mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=13)

    # Normalize or standardize features if needed (e.g., normalization)
    mfccs = (mfccs - np.mean(mfccs)) / np.std(mfccs)

    return mfccs

# Example: Preprocess the first audio file in the training data
file_path = train_data[0]['audio']['path']
mfccs = preprocess_audio(file_path)

# Print the shape of the MFCCs
print("MFCC Shape:", mfccs.shape)