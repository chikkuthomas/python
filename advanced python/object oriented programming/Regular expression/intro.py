#used for pattern matching
#operations between two patterns

#validation
#to check whether the input is validated
#eg: email id, password,phone number,username

#whether the rule is satisfied
# we use "re" package for regular expression
# import re package-to use methods in it

#.............................................................................................................
# RULES #

# rule
#1) x="[abc]" ---- # either a,b,c

#2)  x='[^abc]'  # except a,b,c

#3) x='[a-z]' #a to z  -only lower case

#4)x='[A-Z]'  # A to Z only upper case

# 5) x='[0-9]' # to check numbers from 0 to 9

#6) x='[^a-zA-Z0-9]' # to check symbals

#7) x='[\s]' to check space

#8) x='[\d]- to check digits

#9)x='[\D]' - to check whether not digits

#10)x='[\w]'-all words except special charecters

#11) x='[\W]' - words with special characters






# RULES #
#1) rule

import re
#
# x="[abc]"  # either a,b,c
# matcher=re.finditer(x,"abt coskz") # finding x in second string
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# # 2)rule
# x='[^abc]'  # except a,b,c
# matcher=re.finditer(x,"abt coskz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()


#x='[a-z]' #a to z  -only lower case
# matcher=re.finditer(x,"abt coskz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()


# x='[A-Z]'  # A to Z only upper case
# matcher=re.finditer(x,"abt ScUoskz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='[a-zA-Z]' #"BOTH LOWER AND UPPER CASE"
# matcher=re.finditer(x,"abt coskBz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='[0-9]'  # to check numbers
# matcher=re.finditer(x,'Abvc m874BHk')
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     print()

# x='[^a-zA-z0-9]'  # checking for symbols , not is used
# matcher=re.finditer(x,"abt !co@skz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='\s'  # check space
# matcher=re.finditer(x,"abt coskz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='\d'  # to check digits
# matcher=re.finditer(x,"abt co8sk5z")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='\D'  # which are not digits
# matcher=re.finditer(x,"abt coskz")
# for match in matcher:
#     print(match.start())   # position  # position of space is also considered
#     print(match.group()) # which grp/alphabet is matched
#     print()

# x='\w' #all words except special charecters
# x='\W' # for special charecters


# \   Used to drop the special meaning of character
#     following it (discussed below)
# []  Represent a character class
# ^   Matches the beginning
# $   Matches the end
# .   Matches any character except newline
# ?   Matches zero or one occurrence.
# |   Means OR (Matches with any of the characters
#     separated by it.
# *   Any number of occurrences (including 0 occurrences)
# +   One or more occurrences
# {}  Indicate number of occurrences of a preceding RE
#     to match.
# ()  Enclose a group of REs
#
# \d   Matches any decimal digit, this is equivalent
#      to the set class [0-9].
# \D   Matches any non-digit character.
# \s   Matches any whitespace character.
# \S   Matches any non-whitespace character
# \w   Matches any alphanumeric character, this is
#      equivalent to the class [a-zA-Z0-9_].
# \W   Matches any non-alphanumeric character.
