def romanToInt(s: str) -> int:
    roman_dic = {'I': 1, 'V': 5, 'X': 10,
                 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    i = 0

    while i < len(s):
        x = roman_dic[s[i]]

        if i + 1 < len(s):
            y = roman_dic[s[i + 1]]

            if x >= y:
                sum += x
                i += 1
            else:
                sum += y - x
                i += 2

        else:
            sum += x
            i += 1

    return sum


test = "MCMXCIV"

print(romanToInt(test))
