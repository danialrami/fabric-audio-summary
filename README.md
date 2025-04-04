# Audio Transcription and Wisdom Extraction

This Python script automates the process of transcribing audio files and extracting key insights. It's perfect for processing recordings from podcasts, journals, or conference talks.

## Features

- Transcribes audio files using OpenAI's Whisper model
- Extracts wisdom and key insights from transcripts using Fabric's extract_wisdom pattern
- Creates timestamped output folders for organized results
- Supports various audio file formats

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7+
- FFmpeg (required for audio processing)
- Go (required for Fabric installation)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/audio-transcription-wisdom.git
   ```

2. Install OpenAI Whisper:
   ```
   pip install openai-whisper
   ```
   
   Alternatively, you can install the latest version directly from GitHub:
   ```
   pip install git+https://github.com/openai/whisper.git
   ```

3. Install FFmpeg (required by Whisper):
   ```
   # On Ubuntu/Debian
   sudo apt update && sudo apt install ffmpeg
   
   # On macOS
   brew install ffmpeg
   
   # On Windows using Chocolatey
   choco install ffmpeg
   ```

4. Install Fabric (GoLang version):
   ```
   # macOS (arm64)
   curl -L https://github.com/danielmiessler/fabric/releases/latest/download/fabric-darwin-arm64 > fabric && chmod +x fabric && ./fabric --version
   
   # Linux
   cd ~/.local/bin
   curl -L https://github.com/danielmiessler/fabric/releases/latest/download/fabric-linux-amd64 > fabric && chmod +x fabric && ./fabric --version
   ```

   Alternatively, if you have Go installed:
   ```
   go install github.com/danielmiessler/fabric@latest
   ```

5. Set up Fabric:
   ```
   fabric --setup
   ```
   
   You'll need to provide your API keys (or ollama models) during setup.

## Usage

Run the script from the command line:

```
python audio-summary_fabric.py
```

Follow the prompts to enter the path to your audio file. The script will then:

1. Transcribe the audio using Whisper
2. Save the transcript in a timestamped folder
3. Extract wisdom from the transcript using Fabric
4. Save the extracted wisdom in the same folder

## Output

The script creates a timestamped folder in the same directory as the input audio file. This folder contains:

- `{original_filename}_transcript.txt`: The full transcript of the audio
- `{original_filename}_wisdom.txt`: Extracted wisdom and insights

## Acknowledgments

- OpenAI for the Whisper model
- Daniel Miessler for the Fabric framework
