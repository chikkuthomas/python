import re

# to check whether a is included in the given string, at which all groups and positions

# x='a+'
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     print()
#...................................................................................................................

#x='a*' --- count including zero number of a(only a and space considered, no other elements)
# x='a*'
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())
#     print()
#...................................................................................................................

#x='a?' --- count a as each including zero no of a
# (instead of chrecking as group,it check as each element)

# x='a?'
# r='aaa abc aaaa cga'
# matcher=re.finditer(x,r)
# for match in matcher:
#     print("match found at position: ",match.start())
#     print("matching elemenst: ",match.group())
#     print()
#....................................................................................................................

#x='a{2}' #positions where  aa is matched

# x='a{3}'
# r='aaa abc aaaa cgaa'
# match=re.finditer(x,r)
# for i in match:
#     print(i.start())
#     print()
#....................................................................................................................

# x='a{2,3}' # where minimum 2 or maximum 3 'a' are found
# r='aa aabca aaaa cgaa'
# match=re.finditer(x,r)
# for i in match:
#     print(i.start())
#     print(i.group())
#     print()

#....................................................................................................................
#
# x='^a' #check whether the whole string is starting with 'a'
# r='aa abc cga baac'
# match=re.finditer(x,r)
# for i in match:
#     print("yes starting with a")
#     print(i.start())
#     print(i.group())
#..................................................................................................................

x='a$' #ending with a
r='aa abc cga baaa'
match=re.finditer(x,r)
for i in match:
    print("yes ending with a")
    print(i.start())
    print(i.group())




