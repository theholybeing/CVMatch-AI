# PrepPilot 📚

PrepPilot helps Pakistani Matric and Inter students practise for exams
using their own textbook chapters, with Gemma.

## What it does

Upload or paste a chapter. Gemma writes multiple-choice questions, the app
checks each answer against the chapter text, and explains mistakes in
English, Urdu or Roman Urdu.

## Model and license

- Model: Gemma 4 E4B (`gemma4:e4b`) via Ollama, running locally.
  A small language model (under 10B parameters).
- Optional: Gemma 4 via the Gemini API (`gemma-4-26b-a4b-it`).
- Gemma 4 license: Apache 2.0 [add link]
- This project: MIT.

## Run it

pip install streamlit ollama google-genai python-dotenv pypdf
ollama pull gemma4:e4b

# For the Gemini API option, put GEMINI_API_KEY=your_key in .env

streamlit run app.py

## How answers are verified

Each question includes a quote from the chapter. The app checks that the
quote really exists in the uploaded text and warns the student if it doesn't.

## Privacy

With the local option, the chapter never leaves your computer.

## What's next

Past-paper style questions, progress tracking, a weak-topics report.
