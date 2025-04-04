---

---


I just came back from GDC 2025, and as always, my head is buzzing with ideas, contacts, and insights from the incredible Audio Summit sessions. While in San Francisco, I recorded numerous personal audio notes after talks like Robin Butel's "Audio with Intent" and Cody Matthew Johnson's session on diegetic music in Star Wars Outlaws.

But we all know what happens to audio recordings - they often sit untouched because reviewing them takes too much time. This year, I decided to solve this problem once and for all.

## The Tools I Already Loved

I've been a fan of OpenAI's Whisper for its impressive transcription capabilities - it handles my voice recordings with remarkable accuracy, even in noisy conference environments. I've also recently discovered Daniel Miessler's Fabric framework, which offers powerful AI patterns for extracting wisdom from content.

Putting these tools together felt like a no-brainer, but I wanted a seamless workflow that would take me from audio file to actionable insights in one step.

## The Solution: A Python Script for Audio Distillation

I created a simple Python script that:

1. Takes any audio file as input
2. Transcribes it using Whisper's base model
3. Pipes the transcript through Fabric's extract_wisdom pattern
4. Saves both the transcript and the distilled wisdom in a timestamped folder

The extract_wisdom pattern is particularly valuable as it organizes the content into sections like key ideas, deeper insights, notable quotes, and practical recommendations - perfect for conference notes.

## How It Works

The script is straightforward - you run it, point it to your audio file, and it handles the rest. Behind the scenes, it uses Whisper for transcription and then leverages Fabric's pattern through a subprocess call.

What I love about this approach is how it transforms rambling audio notes into structured, actionable insights. A 20-minute recording of my thoughts after the Audio Summit becomes a concise document highlighting the most valuable takeaways.

## Try It Yourself

If you're a sound designer, developer, or anyone who records audio notes, this tool might save you hours of review time. I've made the code available on GitHub, so feel free to check out the repository and adapt it to your needs. I also wrote an ollama version because open source always wins, but feel free to use your ollama models through fabric too.

Whether you're processing conference recordings, meeting notes, or creative brainstorming sessions, this approach makes your audio content immediately more valuable and accessible.

What audio recordings are gathering dust in your collection that could benefit from this kind of distillation?