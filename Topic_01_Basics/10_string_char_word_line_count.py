# Question 10:
# Take a multi-line string as input (use input() multiple times or
# triple quotes) and print the number of characters, words, and lines
# in it.

print("Enter your text. Type 'END' on a new line to finish:")
lines = []
while True:
    line = input()
    if line == "END":
        break
    lines.append(line)

text = "\n".join(lines)

char_count = len(text)
word_count = len(text.split())
line_count = len(lines)

print(f"Characters: {char_count}")
print(f"Words: {word_count}")
print(f"Lines: {line_count}")

# Time Complexity: O(n) 
# Space Complexity: O(n) 
