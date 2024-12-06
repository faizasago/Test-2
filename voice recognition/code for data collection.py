#install (pip install datasets pydub librosa) 
from datasets import load_dataset
trust_remote_code=True

# Load CommonVoice dataset (English)
dataset = load_dataset("common_voice", "en")

# Preview dataset structure
print(dataset)

# Collect audio files and their corresponding transcriptions
# You can use the training or validation set
train_data = dataset["train"]

# Example: Print the first 5 entries
for i in range(5):
    print(f"Audio path: {train_data[i]['audio']['path']}, Transcription: {train_data[i]['sentence']}")
