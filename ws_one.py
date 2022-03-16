# 
# 
# 
# 1. Reverse a string
# a. Write code that takes a string as input and returns the string reversed
# b. i.e. “Hello” will be returned as “olleH”


def backward_word(drow):
    challenge_word = 'Hello'
    reverse_word = ''.join(reversed(challenge_word))
    print(reverse_word)
    return challenge_word

challenge_word = 'Hello'
backward_word(challenge_word)


#  2. Capitalize letter
# a. Write code that takes a string as input and capitalize the first letter of 
# each word. Words will be separated by only one space. i.e. “hello 
# world” should be outputted as “Hello World”



def upper_title(title_string_phrase):
    challenge_string = str.title(string_phrase)
    print(challenge_string)
    return title_string_phrase

string_phrase = 'hello world'
upper_title(string_phrase)

#  3. Compress a string of characters
# a. For example, an input of "aaabbbbbccccaacccbbbaaabbbaaa" would 
# compress to "3a5b4c2a3c3b3a3b3a"


def compress_str_loop(string):
    new_string = ""
    string = "aaabbbbbccccaacccbbbaaabbbaaa"
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count = count + 1
        else:
            new_string = new_string + string[1] + str(count)
            count = 1
    new_string = new_string + string[i+1] + str(count)
    print(new_string)
    return string_loop

string_loop = len("aaabbbbbccccaacccbbbaaabbbaaa")
print(f'total characters = {compress_str_loop(string_loop)}')

# 4. BONUS CHALLENGE: Palindrome
# a. A word, phrase, or sequence that reads the same backward as forward i.e. madam

a_string = input('IS THIS A PALINDROME?: ')

def palindrome(string):
    string = string.lower().replace(' ', '')
    return string == string[::-1]

print(palindrome(a_string))

# b. Write code that takes a user input and checks to see if it is a Palindrome and reports the resul