import os
import sys
import datetime
import subprocess
import whisper
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

def extract_wisdom_with_fabric(transcript_path):
    """Use Fabric's extract_wisdom pattern on the transcript."""
    print("Extracting wisdom using Fabric...")
    
    # Create output filename for the wisdom extraction
    wisdom_path = transcript_path.parent / f"{transcript_path.stem}_wisdom.txt"
    
    # Build the command to pipe the file content to fabric
    cmd = f"cat '{transcript_path}' | fabric --stream --pattern extract_wisdom -o '{wisdom_path}'"
    
    try:
        # Execute the command
        process = subprocess.run(cmd, shell=True, check=True, 
                                capture_output=True, text=True)
        print(process.stdout)
        
        if process.stderr:
            print(f"Warning: {process.stderr}")
            
        return wisdom_path
    except subprocess.CalledProcessError as e:
        print(f"Error running Fabric: {e}")
        print(f"Command output: {e.output}")
        print(f"Command stderr: {e.stderr}")
        return None

def create_output_folder(audio_filepath):
    """Create a timestamped output folder in the same directory as the audio file."""
    parent_dir = Path(audio_filepath).parent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_dir = parent_dir / f"audio_summary_{timestamp}"
    output_dir.mkdir(exist_ok=True)
    
    return output_dir

def save_transcript(output_dir, audio_filepath, transcript):
    """Save the transcript to a file."""
    audio_filename = os.path.basename(audio_filepath)
    base_name = os.path.splitext(audio_filename)[0]
    
    # Save transcript
    transcript_path = output_dir / f"{base_name}_transcript.txt"
    with open(transcript_path, 'w', encoding='utf-8') as f:
        f.write(transcript)
    
    return transcript_path

def main():
    # Get audio filepath
    audio_filepath = get_audio_filepath()
    
    # Transcribe audio
    transcript = transcribe_audio(audio_filepath)
    
    # Create output folder and save transcript
    output_dir = create_output_folder(audio_filepath)
    transcript_path = save_transcript(output_dir, audio_filepath, transcript)
    
    print(f"Transcript saved to: {transcript_path}")
    
    # Extract wisdom using Fabric
    wisdom_path = extract_wisdom_with_fabric(transcript_path)
    
    if wisdom_path and os.path.exists(wisdom_path):
        print(f"Wisdom extraction saved to: {wisdom_path}")
        print("\nProcessing complete!")
    else:
        print("Wisdom extraction failed or file not created.")

if __name__ == "__main__":
    main()
