# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here

  str1 = input('first_word')
  str2 = input('second_word')
first_word = 'astronomer'
second_word = 'moonstarer'
# sorting

if(sorted(first_word) == sorted(second_word)):
    print("True")
else:
    print('False')