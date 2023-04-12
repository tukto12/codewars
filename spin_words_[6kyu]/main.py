def spin_words(sentence):
    my_list = list(sentence.split(' '))

    for i in range(len(my_list)):
        if len(my_list[i]) >= 5:
            my_list[i] = my_list[i][::-1]

    return ' '.join(my_list)
