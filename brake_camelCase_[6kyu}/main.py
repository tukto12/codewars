def solution(s):
    my_list = [' ' + letter if letter.isupper() else letter for letter in s]

    result = ''
    for i in my_list:
        result += i
    return result


print(solution('mySuperVariable'))
print(solution('identifer'))
print(solution(''))
