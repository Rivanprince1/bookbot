def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    chars = list(text.lower())
    char_counts = {}

    for char in chars:
        if char == " ":  # ✅ Skip spaces
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_char_counts(char_counts):
    sorted_counts = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return sorted_counts