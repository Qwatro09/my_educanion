def single_root_words(root_word, *other_words):
    same_words = []
    my_word = root_word.lower()
    for i_num in range(len(other_words)):
        words_str = str(other_words[i_num]).lower()
        if my_word in words_str or words_str in my_word:
        # if words_str.count(my_word) >= 1 or my_word.count(words_str) >= 1:
            same_words.append(other_words[i_num])

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
