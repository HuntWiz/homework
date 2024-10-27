class WordsFinder:
    file_names = []

    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}

        for i in self.file_names:
            dic = []
            with open(i, encoding='utf-8') as file:
                s = file.read().splitlines()
                for line in s:
                    for l in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        if l in line:
                            line = line.replace(l, ' ')
                    for word in line.split():
                        dic.append(word.lower())

            all_words.update({str(i): dic})

        return all_words

    def find(self, word):
        k = 0
        all_files = {}
        for file in self.file_names:
            for name, words in self.get_all_words().items():
                for i in words:
                    k = k + 1
                    if word == i:
                        all_files.update({name: k})
                        break
                k = 0
        return all_files

    def count(self, word):
        k = 0
        all_files = {}
        for file in self.file_names:
            for name, words in self.get_all_words().items():
                for i in words:
                    if word == i:
                        k = k + 1
                all_files.update({name: k})
                k = 0
        return all_files



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

