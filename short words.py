import keyboard
import mouse
import random as rand
from time import sleep

used_words = []
working_words = []
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
type_time_max = 0.2
type_time_min = 0
terminal_posX = -800
jklm_screen_posX = 800
pos_y = 1000


def rand_float_range(start, end):
    return rand.random() * (end - start) + start


mouse.move(terminal_posX, pos_y)
sleep(0.09)
mouse.press(button='left')
mouse.release(button='left')

while True:
    word_grab_number = 0

    word_list = open('word list.txt', 'r')

    text = input()

    for word in word_list:
        if text in word:
            working_words.append(word.strip())

    word_list.close()
    working_words = sorted(working_words, key=len)

    try:
        word = working_words[word_grab_number]
        while word in used_words:
            word_grab_number += 1
            word = working_words[word_grab_number]

        used_words.append(word)

        print(used_words)
        print(word)
    except:
        continue

    mouse.move(jklm_screen_posX, pos_y)
    sleep(0.09)
    mouse.press(button='left')
    mouse.release(button='left')
    sleep(0.09)
    if rand.randint(1, 10) <= 4:
        starting_char = rand.randint(1, len(word))
        backspace_amount = rand.randint(1, starting_char)
        for character in range(starting_char):
            sleep(rand_float_range(type_time_min, type_time_max))
            keyboard.write(word[character])
        for index in range(backspace_amount):
            sleep(rand_float_range(type_time_min, type_time_max))
            keyboard.write(alphabet[rand.randint(0, len(alphabet)-1)])
        for index2 in range(backspace_amount):
            sleep(rand_float_range(type_time_min, type_time_max))
            keyboard.send('backspace')
        for character2 in range(starting_char, len(word)):
            sleep(rand_float_range(type_time_min, type_time_max))
            keyboard.write(word[character2])
    else:
        for i in word:
            sleep(rand_float_range(type_time_min, type_time_max))
            keyboard.write(i)

    keyboard.send('enter')
    sleep(0.09)
    mouse.move(terminal_posX, pos_y)
    sleep(0.09)
    mouse.press(button='left')
    mouse.release(button='left')

    working_words = []
