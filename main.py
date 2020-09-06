#!/usr/bin/python
# -*- coding: utf-8 -*-


# import gui
import mode_new as mo_n  # moduł odpowiedzialny za utworzenie nowego konta
import tryby as mo_l  # moduł odpowiedzialny za tryb nauki
import mode_edit as mo_e  # moduł odpowiedzialny za edycję fiszek
import mode_stat_alt as mo_s  # moduł odpowiedzialny za obsługę statystyki


# gui.app.main()  # uruchomienie gui


nick = 'user'
page = '0'
mode = True


def main():
    global nick
    action = input('do you have an account? (Y/N)\n').capitalize()
    if action == 'Y':
        nick = input('enter your name: ')
        menu()
    elif action == 'N':
        nick = input('enter your name: ')
        ans = run_1()
        if ans is True:
            print('your account has been created')
            menu()
        else:
            print('error - account cannot be created')
    else:
        print('you entered inappropriate answer')
    return


def menu():
    global page, mode
    print('available pages:\n2 - learning mode\n3 - edit mode\n4 - stats mode')
    while mode is True:
        page = input('enter page num. or \'exit\' to exit the app: ')
        if page == '2':
            run_2()
        elif page == '3':
            action = input('to add new word type 1\nto edit existing words type 2\n')
            if action == '1':
                run_3(1)
            elif action == '2':
                run_3(2)
            else:
                print('you entered incorrect answer')
        elif page == '4':
            run_4()
        elif page == 'exit':
            page = 0
            mode = False
        else:
            print('you entered wrong command')
    return


def run_1():
    global nick
    ans = mo_n.main(nick)
    return ans


def run_2():
    mo_l.game()
    return


def run_3(f: int = 0):
    with open('all_words.txt', 'r', encoding='utf-8') as all_words:
        new = mo_e.Edward(all_words.read())
    if f == 1:
        new.add_words()
    elif f == 2:
        new.edit_words()
    else:
        pass
    with open('all_words.txt', 'w', encoding='utf-8') as all_words:
        all_words.write(new.ret_list())
    return


def run_4():
    global nick
    with open(f'statistics\\{nick}.txt', 'r', encoding='utf-8') as user_stats:
        new = mo_s.Steve(user_stats.read())
    new.check_day()
    with open(f'statistics\\{nick}.txt', 'w', encoding='utf-8') as user_stats:
        user_stats.write(new.ret_stat())
    return


if __name__ == "__main__":
    main()
