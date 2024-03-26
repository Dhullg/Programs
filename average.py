def longest_word(s):
    words=s.split()
    max_length = len(max(words,key=len))
    longest_words = [word for word in words if len(word)==max_length]
    if len(longest_words)==1:
        return longest_words[0]
    else:
        return longest_words
print(longest_words("this is a new file"))
