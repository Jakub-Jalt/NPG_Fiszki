#!/usr/bin/python
# -*- coding: utf-8 -*-


class Edward:

    def __init__(self, words_list: str):
        self.words_list = words_list.replace('\n', '-').split('-')
        if self.words_list[-1] == '\n':
            self.words_list = self.words_list[:-1]
        self.list_length = len(self.words_list)

    def add_words(self):
        cur_mode = True
        while cur_mode is True:
            action = input('').capitalize()
            if action == 'Y':
                ang_word = input('enter english word: ')
                pol_word = input('enter polish word: ')
                new_list = [ang_word, pol_word]
                self.words_list.extend(new_list)
                self.list_length += 2
                print(f'pair \"{ang_word}-{pol_word}\" added, do you want do add another pair? (Y/N)')
            elif action == 'N':
                cur_mode = False
            else:
                print('enter appropriate answer (Y/N)')
        return

    def edit_words(self):

        def search(word: str):
            i = 0
            while i < self.list_length:
                if word == self.words_list[i]:
                    break
                i += 1
            return i

        cur_mode = True
        while cur_mode is True:
            action = input('').capitalize()
            if action == 'Y':
                wanted = input('enter word: ')
                idx = search(wanted)
                if idx >= self.list_length:
                    print('your pair has not been found')
                elif idx % 2 == 0:
                    print(f'found pair: {self.words_list[idx]}-{self.words_list[idx+1]}')
                    wanted = input('enter new pair:\n').split('-')
                    self.words_list[idx] = wanted[0]
                    self.words_list[idx + 1] = wanted[1]
                elif idx % 2 == 1:
                    print(f'found pair: {self.words_list[idx - 1]}-{self.words_list[idx]}')
                    wanted = input('enter new pair:\n').split('-')
                    self.words_list[idx - 1] = wanted[0]
                    self.words_list[idx] = wanted[1]
                else:
                    print('search error\n')
            elif action == 'N':
                cur_mode = False
            else:
                print('enter appropriate answer (Y/N)')
        return

    def ret_list(self):
        res = ''
        idx = 0
        while idx < self.list_length:
            res += f'{self.words_list[idx]}-{self.words_list[idx+1]}\n'
            idx += 2
        res = res[:-1]
        return res


if __name__ == "__main__":
    with open('all_words.txt', 'r', encoding='utf-8') as all_words:
        new = Edward(all_words.read())
    new.add_words()
    new.edit_words()
    with open('all_words.txt', 'w', encoding='utf-8') as all_words:
        all_words.write(new.ret_list())
