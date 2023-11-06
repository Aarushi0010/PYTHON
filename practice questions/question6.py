n = int(input("Enter the number of words: "))
word_list = [input("Enter your word") for _ in range(n)]

longest_word = max(word_list, key=len)
print(longest_word)