# Reversing a string

# def rev_string():
#     rev_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
#     let_input = []
#     user_input = input("What word would you like reversed?")
#     user_len = len(user_input)
#     for letter in user_input:
#         let_input.append(letter)
#     for rev_let in rev_list:
#         if rev_let >= -(user_len):
#             print(let_input[rev_let])

# rev_string()

# Capitalize letter

# def cap_words():
#     cap_list = []
#     word_list = input("Please enter a sentence here.")
#     split_list = word_list.split()
#     for word in split_list:
#         word = word.capitalize()
#         cap_list.append(word)
#     cap_sents = ' '.join(cap_list)
#     print(cap_sents)

# cap_words()

# Compress a string of characters

# def dup_removal():
#     num_chars = []
#     str_chars = []
#     num_str = []
#     char_count = 0
#     user_string = input("Please enter a string of random characters")
#     last_char = user_string[0]
#     for char in user_string:
#         if char == last_char:
#             char_count += 1
#             last_char = char
#         else:
#             num_chars.append(char_count)
#             char_count = 1
#             str_chars.append(last_char)
#             last_char = char
#     num_chars.append(char_count)
#     str_chars.append(last_char)
#     for each in range(len(num_chars)):
#         num_str.append(str(num_chars[each]))
#         num_str.append(str_chars[each])
#     result = ''.join(num_str)
#     print(result)

# dup_removal()
    
# Palindrome

def palindrome_check():
    rev_list = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12, -13, -14, -15]
    let_input = []
    user_input = input("Let's see if your word is a palindrome! Please enter a word")
    user_len = len(user_input)
    for letter in user_input:
        let_input.append(letter)
    for rev_let in rev_list:
        if rev_let >= -(user_len):
            rev_word_list = let_input[rev_let]
    rev_word = ''.join(rev_word_list)
    if user_input == rev_word:
        print("Its a Palindrome!")
    else:
        print("Nope!")


palindrome_check()