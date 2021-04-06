#!/usr/bin/env python
# coding: utf-8

# In[30]:


number=0
def game_core_v3(number):
    min_num = 0 #Минимальное начало отрезка
    max_num = 101 #Миаксимальный конец отрезка
    count = 0
    mid_num = (min_num+max_num)//2 #Середина отрезка
    while number != mid_num:
        count += 1
        mid_num = (min_num+max_num)//2 #Новая середина отрезка
        if number < mid_num:
            max_num = mid_num #Новый конец отрезка
        elif number > mid_num:
            min_num = mid_num #Новое начало отрезка 
            print(number,mid_num)
    #print("Угаданное число ", mid_num)
    return count


# In[31]:


game_core_v3(number)


# In[32]:


import numpy as np
def score_game(game_core):
    #'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core_v3(number))
    score = int(np.mean(count_ls))
    print('Ваш алгоритм угадывает число в среднем за', score, 'попыток')
    return(score)


# In[33]:


score_game(game_core)


# In[ ]:




