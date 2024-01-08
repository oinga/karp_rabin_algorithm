# Pattern Searching with Karp-Rabin Algorithm

This Python code implements the Karp-Rabin algorithm for pattern searching in a given text. The algorithm employs a rolling hash function with a prime number to efficiently detect potential matches between the pattern and substrings of the text.

## Usage

1. Clone the repository or copy the code into your Python environment.
2. Modify the `text` and `pattern` variables in the example usage section according to your input.
3. Run the script to see if the specified pattern is present in the given text.

```python
# Example usage
text = "AABAACAADAABAAABAA"
pattern = "AABA"
kra(text, pattern)
