import os

filepath = os.path.join(".", "paragraph_2.txt")
Word_count = 0
Sentence_count = 0

with open(filepath) as fh:
# * Approximate word count
    for row in fh:
        words_list = row.split()
        Word_count += len(words_list)
        Word_length = sum(map(len, words_list))/len(words_list) 
        Sentence_list = row.split('.')
        Sentence_count += len(Sentence_list) 
        Sentence_length = sum(map(len, Sentence_list))/len(Sentence_list)
# * Approximate sentence count
#   * Approximate letter count (per word)
#   * Average sentence length (in words)    

print("```")
print("Paragraph Analysis")
print("-----------------")
print(f"Approximate Word Count: {Word_count}")
print(f"Approximate Sentence Count: {Sentence_count}")
print(f"Average Letter Count: {Word_length}")
print(f"I have no idea how many average words in a sentence but there are: {Sentence_length} avg characters per sentence!")
print("```") 

              

