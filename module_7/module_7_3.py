class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file_name in self.file_names:
                with open(file_name, encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        for char in punctuation:
                            line = line.replace(char, '')
                        words.extend(line.split())
                    all_words[file_name] = words

        return all_words

    def find(self, word):
        find_result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for file_name, words in all_words.items():
            if word_lower in words:
                find_result[file_name] = words.index(word_lower) + 1
        return find_result

    def count(self, word):
        count_result = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for file_name, words in all_words.items():
            count_result[file_name] = words.count(word_lower)
        return count_result


# finder2 = WordsFinder('test_file.txt')
#
# print(finder2.get_all_words())
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))


# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))


# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))


# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
#
# print(finder1.get_all_words())
# print(finder1.find('captain'))
# print(finder1.count('captain'))


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
