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
                s = file.readlines()
                for k in s:
                    k.lower() #не делает ловер и не убирает знаки, исправить!
                    for l in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        k.replace(l, ' ')
                    dic.append(k.split())
            all_words.update({str(i): dic})

        return all_words

    def find(self, word):
        for name, words in self.get_all_words().items():
            for i in words:
                if word in words:
                    return {name: i} #еще и не ищет!


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('Captain'))
