# reverse a string
"""
str1 = "Tanishq is my name"
print(str1[::-1])
"""

#check if a string is pallindrome

"""str1  = "namat"
if str1[::1] == str1[::-1]:
    print("it is a pallindrome")
else:
    print("it is not")"""

#ignorining all the cases and spaces

"""str1 = "A man a plan a canal Panama"
str1_low = str1.lower()

cleaned = ""
for i in str1_low:
    if i.isalpha():
        cleaned += i

if cleaned[::1] == cleaned[::-1]:
    print("true")
else:
    print("false")
"""

#count vowels in a string
"""str1 = "hello my name is tanishq and i am just 20 years old."
vowels = 0
for i in str1:
    if i in 'aeiou':
        vowels += 1
print(vowels , "are the number of vowels")"""


#Convert string to uppercase without using .upper()
"""
str_low = "Hello Bhai Mei Bihar se hu Kyuki Meh Bihari hu"
str_upp = ""
for ch in str_low:
    if 'a' <= ch <= 'z':
        str_upp += chr(ord(ch) - 32)
    else:
        str_upp += ch
print("uppercase ", str_upp)
"""

#find the most frequent char in string

"""s = "aabbccabcabcaabcaaaacb"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

max_count = 0
max_char = ''

for ch in freq:
    if freq[ch] > max_count:
        max_count = freq[ch]
        max_char = ch
print("most number of char is  : " , max_char , "it is for " , max_count , "times")"""

# remove all duplicate char from the string

"""str1 = "aabbccabcabcaabcaaaacb"
result = ' '
seen = set()

for ch in str1:
    if ch not in seen:
        result += ch
        seen.add(ch)

print("result after removing duplicats is : " ,result)"""


# Check if two strings are anagrams

"""str1 = "listen"
str2 = "silent"
freq1 = {}
freq2 = {}
if len(str1) != len(str2):
    print("not an anagram")

for ch in str1:
    if ch in freq1:
        freq1[ch] += 1
    else:
        freq1[ch] = 1
for ch in str2:
    if ch in freq2:
        freq2[ch] += 1
    else:
        freq2[ch] = 1
if freq1 == freq2:
    print("they are an anagram")
else:
    print("they are not")"""

# Replace spaces with hyphens in a string

"""str1 = "hello world"
result = str1.replace(' ','-')
print(result)

result1 = ' '
for ch in str1:
    if ch == " ":
        result1 += "-"
    else:
        result1 += ch

print(result1)"""
        
        
