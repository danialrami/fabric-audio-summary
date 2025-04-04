import os
import sys
import datetime
import argparse
import whisper
import ollama
from pathlib import Path

def get_audio_filepath():
    """Prompt the user for the filepath to an audio file."""
    filepath = input("Enter the path to your audio file: ").strip()
    
    # Remove single quotes if present
    if filepath.startswith("'") and filepath.endswith("'"):
        filepath = filepath[1:-1]
    
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)
    
    return filepath

def transcribe_audio(audio_filepath):
    """Transcribe the audio file using Whisper base model."""
    print("Loading Whisper model...")
    model = whisper.load_model("base")
    
    print(f"Transcribing {audio_filepath}...")
    result = model.transcribe(audio_filepath)
    
    return result["text"]

def summarize_with_gemma(transcript):
    """Summarize the transcript using Gemma 3 via Ollama."""
    print("Generating summary with Gemma 3...")
    
    prompt = f"""
    Please analyze the following transcript and provide:
    1. A concise summary of the main points
    2. Key takeaways and insights
    3. Important themes or topics discussed
    
    Transcript:
    {transcript}
    """
    
    response = ollama.chat(
        model='gemma3:12b',
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    return response['message']['content']

def create_output_folder():
    """Create a timestamped output folder."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = Path(f"audio_summary_{timestamp}")
    output_dir.mkdir(exist_ok=True)
    
    return output_dir

def save_results(output_dir, audio_filepath, transcript, summary):
    """Save the transcript and summary to files."""
    audio_filename = os.path.basename(audio_filepath)
    base_name = os.path.splitext(audio_filename)[0]
    
    # Save transcript
    transcript_path = output_dir / f"{base_name}_transcript.txt"
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(transcript)
    
    # Save summary
    summary_path = output_dir / f"{base_name}_summary.txt"
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary)
    
    return transcript_path, summary_path

def main():
    # Get audio filepath
    audio_filepath = get_audio_filepath()
    
    # Transcribe audio
    transcript = transcribe_audio(audio_filepath)
    
    # Summarize transcript
    summary = summarize_with_gemma(transcript)
    
    # Create output folder and save results
    output_dir = create_output_folder()
    transcript_path, summary_path = save_results(output_dir, audio_filepath, transcript, summary)
    
    print(f"\nProcessing complete!")
    print(f"Transcript saved to: {transcript_path}")
    print(f"Summary saved to: {summary_path}")

if __name__ == "__main__":
    main()
