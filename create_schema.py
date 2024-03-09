def create_schema(wordle_word, guess):
    schema = ""
    for i in range(0, 5):
        if wordle_word[i] == guess[i]:
            schema += "🟩"
        elif guess[i] in wordle_word:
            schema += "🟨"
        else:
            schema += "⬛️"
    return schema
