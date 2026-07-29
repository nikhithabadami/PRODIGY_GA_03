import markovify

with open("dataset/dataset.txt", "r", encoding="utf-8") as f:
    text = f.read()

model = markovify.Text(text, state_size=2)

print("\nGenerated Sentences:\n")

generated = []

for i in range(5):
    sentence = model.make_short_sentence(140)
    if sentence:
        print(f"{i+1}. {sentence}")
        generated.append(sentence)

with open("output/generated_text.txt", "w", encoding="utf-8") as f:
    for sentence in generated:
        f.write(sentence + "\n")

print("\nGenerated text saved to output/generated_text.txt")