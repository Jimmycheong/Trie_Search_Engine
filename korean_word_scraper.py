'''Korean word writer
'''

import re
import csv

INPUT_FILE = "resources/6000koreanwords.txt"
OUTPUT_FILE = "resources/korean_word_list.txt"
REGEX = r"[\!…\\a-zA-z\d (),/~\t0-9.?:;’'-_<>\"|`]+"

new_info = {}
pattern = re.compile(REGEX)

# Read korean word file
with open(INPUT_FILE, 'r') as file:
    raw_content = file.readlines()

# Find everything that matches the korean words
counter = 0
for line in raw_content:
    stripped = str.strip(line)
    subbed = re.sub(REGEX,"",stripped).strip()
    if subbed != "":
        new_info[counter] = subbed
        counter += 1

# Final cleanising of list to remove ""
all_korean_words =  list(filter(lambda x: x != "" , list(new_info.values())))

print("ALL KOREAN WORDS:", all_korean_words)

# Write to file
with open(OUTPUT_FILE, "w") as file:
    for item in all_korean_words:
        file.writelines(item + "\n")

# Logging
print(F'''
Completed writing to {OUTPUT_FILE}

Total words written to file: {len(all_korean_words)}
     ''')

