class WordsFinder:
    all_words={}

    def __init__(self,*file_names):
        self.file_names=file_names


    def get_all_words(self)->dict:
       for key in self.file_names:
            word_list=[]
            with open(key, 'r', encoding='utf-8') as file:
                words=file.read().lower().strip().split()
                for clear in words:
                    for punct in clear:
                        if punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                           clear=clear.replace(punct,'')
                    word_list.append(clear)
            self.all_words[key]=word_list
       print(self.all_words)


    def find(self, word:str)->dict:
        """метод, где word - искомое слово.
        Возвращает словарь, где ключ - название файла,
        значение - позиция первого такого слова в списке слов этого файла.
        """
        find={}
        find_word=word.lower()
        for key,values in self.all_words.items():
                for index, word  in enumerate(values,start=1):
                    if find_word == word:
                        find[key]=index
                        break
        return find

    def count(self, word:str)->dict:
        """метод, где word - искомое слово.
        Возвращает словарь, где ключ - название файла,
        значение - количество слова word в списке слов этого файла
        """
        find = {}
        find_word = word.lower()
        for key, values in self.all_words.items():
            count=0
            for word in (values):
                if find_word == word:
                    count+=1
            find[key] = count
        return find

def main():
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

if __name__ == '__main__':
    main()




