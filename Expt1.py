print("Q1 - Write a Python program to calculate the length of a string")
def string_length(s):
    return len(s)


input_string1 = input("Enter string to find length: ")
print(f"The length of the string is: {string_length(input_string1)}")


print("Q2 - Write a Python program to count the number of characters in a string")
def count_characters_without_spaces(s):
    s_no_spaces = s.replace(" ", "")
    return len(s_no_spaces)


input_string2 = input("Enter string to find length w/o spaces: ")
count = count_characters_without_spaces(input_string2)
print(f"The number of characters in '{input_string2}'  is: {count}")


print("Q3 - Write a Python program to get a string made of the first 2 and the last 2 chars from a given string. If the string length is less than 2, return an empty string")
def string_both_ends(str):
    if len(str) < 2:
        return ''
    return str[0:2] + str[-2:]


input_string3 = input("Enter string to get a string made of the first 2 and the last 2 chars: ")
print(string_both_ends(input_string3))
input_string4 = input("Enter string to get a string made of the first 2 and the last 2 chars: ")
print(string_both_ends(input_string4))


print("Q4 - Write a Python program to get a string from a given string where all occurrences of its first  char have been changed to '$', except the first char itself")
def replace_first_char(s):
    if not s:
        return ''
    first_char = s[0]
    s = s.replace(first_char, '$')
    return first_char + s[1:]


input_string5 = input("Enter string to change occurrences of its first char to '$: ")
print(f"After replacing: {replace_first_char(input_string5)}")


print("Q5 - Write a Python program to get a single string from two given strings, separated by a space and  swap the first two characters of each string")
def swap_first_two_characters(str1, str2):
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    combined_string = new_str1 + new_str2

    return combined_string


input_string6 = input("Enter str 1: ")
input_string7 = input("Enter str 2: ")
result = swap_first_two_characters(input_string6, input_string7)
print(f"Resulting string: {result}")


print("Q6 - Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If  the given string already ends with 'ing' then add 'ly' instead. If the string length of the given  string is less than 3, leave it unchanged")
def changeWord(str):
    if len(str) <= 3:
        return str

    if str[-3:] == "ing":
        return (str + "ly")

    else:
        return (str + "ing")


input_string8 = input("Enter string to add ing or ly: ")
input_string9 = input("Enter string to add ing or ly: ")
input_string10 = input("Enter string to add ing or ly: ")

print(changeWord(input_string8))
print(changeWord(input_string9))
print(changeWord(input_string10))


print("Q7 - Write a Python program to find the first appearance of the substring 'not' and 'poor' from a  given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.  Return the resulting string")
def replaceStr(str):
    not_index = str.find("not")
    poor_index = str.find("poor")
    if not_index != -1 and poor_index != -1 and poor_index > not_index:
        return str[:not_index] + "good" + str[poor_index + len("poor"):]
    else:
        return str


input_string11 = input("Enter string to replace not ... poor with good: ")
input_string12 = input("Enter string to replace not ... poor with good: ")
input_string13 = input("Enter string to replace not ... poor with good: ")

print(replaceStr(input_string11))
print(replaceStr(input_string12))
print(replaceStr(input_string13))


print("Q8 - Write a Python function that takes a list of words and returns the length of the longest one")
def lengthStr(list):
    return len(max(list, key=len))


print("Length of str:", lengthStr(["Good", "Bad", "Average", "Excellent"]))


print("Q9 - Write a Python program to remove the nth index character from a nonempty string")
def indexing(s, index):
    new_string = s.replace(s[index], '')
    return new_string


input_string14 = input("Enter string to remove the nth index character: ")
index = int(input("Enter nth index: "))
result = indexing(input_string14, index)
print(f"Original string: {input_string14}")
print(f"New string: {result}")


print("Q10 - Write a Python program to change a given string to a new string where the first and last chars  have been exchanged")
def exchange(s):
    first_char = s[0]
    last_char = s[-1]
    new_string = last_char + s[1:-1] + first_char
    return new_string


input_string15 = input("Enter string to exchange first and last char: ")
result = exchange(input_string15)
print(f"Original string: {input_string15}")
print(f"New string: {result}")


print("Q11 - Write a Python program to remove the characters which have odd index values of a given  string")
def skipOdd(s):
    newString = ""
    for i, ch in enumerate(s):
        if (i % 2 == 0):
            newString += ch
    return newString


input_string16 = input("Enter string to remove the characters which have odd index values: ")
print(f"The new string is: {skipOdd(input_string16)}")


print("Q12 - Write a Python program to count the occurrences of each word in a given sentence")
def word_count(s):
    words = s.split(" ")
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict


input_string17 = input("Enter string to count the occurrences of each word: ")
result = word_count(input_string17)
print(result)

print("Q13 - Write a Python script that takes input from the user and displays that input back in upper and  lower cases")
input_string18 = input("Enter string: ")
upperCaseString = input_string18.upper()
print(upperCaseString)
lowerCaseString = input_string18.lower()
print(lowerCaseString)

print("Q14 - Write a Python program that accepts a comma separated sequence of words as input and prints  the unique words in sorted form (alphanumerically)")
input_string19 = input("Enter string separated by ',' :")
listStr = input_string19.split(",")
listStr.sort()
print(listStr)

print("Q15 - Write a Python program to reverse the words in the string. ")
input_string20 = input("Enter string:")
reversed_string = input_string20[::-1]
print(f"The reversed string is: f{reversed_string}")