def kra(text, pattern):
    hash_prime = 10102

    def hash_value(substring):
        hash_val = 0
        for char in substring:
            hash_val = (hash_val * 256 + ord(char)) % hash_prime
        return hash_val

    pattern_hash = hash_value(pattern)
    text_hash = hash_value(text[:len(pattern)])

    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == text_hash:
            if text[i:i+len(pattern)] == pattern:
                print(f"Pattern at {i}")


        if i < len(text) - len(pattern):
            text_hash = (256 * (text_hash - ord(text[i]) * (256 ** (len(pattern) - 1))) + ord(text[i + len(pattern)])) % hash_prime

# Example usage
text = "AABAACAADAABAAABAA"
pattern = "AABA"
kra(text, pattern)
