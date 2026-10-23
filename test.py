import ollama

text = "Photosynthesis is the process by which plants make food using sunlight, water and carbon dioxide."
r = ollama.chat(model="gemma4:e4b", messages=[{
       "role": "user",
       "content": f"Write 2 multiple-choice questions from this text only:\n{text}",
}])
print(r["message"]["content"])