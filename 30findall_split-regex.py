import re

# re.findall

#text = "My scores were 85, 92 and 76"
#numbers = re.findall(r"\d+", text)
#print(numbers)
# output = ['85', '92', '76']
# Here:
# - \d means any digit from 0–9 (and, by default, other Unicode decimal digits).
# - + means one or more.
# So \d+ finds consecutive groups of digits.
# One subtlety: They're returned as strings, not integers!

"""
What about capturing groups?
This is particularly relevant to your Twitter example.
"""
text = "twitter.com/kath twitter.com/nick"
# result = re.findall(r"twitter\.com/(\w+)", text)
#print(result)
# output - ['kath', 'nick']

# Because you've used parentheses, findall() returns just the contents of the capturing group.
# Without the parentheses, it would return the complete matches:
# result = re.findall(r"twitter\.com/\w+", text)
# print(result)
# output = ['twitter.com/kath', 'twitter.com/nick']

# re.split

#text = "apple,banana,cherry"
#print(text.split(",")) # only one split character allowed

#text = "apple, banana;  cherry   orange"
#result = re.split(r"[,;\s]+", text) # this won't create empty strings for the extra spaces
# remember 
# - \s matches whitespace (spaces, tabs, newlines, etc.).
# - + matches one or more consecutive separators.
# output ['apple', 'banana', 'cherry', 'orange']

"""
Function	    Purpose	                            Returns
re.search()	    Find the first match anywhere	    Match object or None
re.match()	    Match at the beginning	            Match object or None
re.fullmatch()	Match the entire string	            Match object or None
re.findall()	Find all non-overlapping matches	List
re.split()	    Split wherever the pattern matches	List

One thing worth remembering: re.findall() and re.split() always return lists, even if no matches are found. 
In the latter case, re.split() generally returns a list containing the original string.
"""

text = "Python123Java456SQL789"
#print(re.findall(r"\d+", text)) # i suspect this will find ['123','456','789'] - correct!
#print(re.findall(r"[A-Za-z]+",text)) # i suspect will find ['Python','Java','SQL] - correct!
#print(re.split(r"\d+",text)) # i suspect this will return the same as above - yes, but i didn't put the last option!
#rint(re.split(r"(\d+)",text)) # this will capture the numbers as groups as well!
# output - ['Python', '123', 'Java', '456', 'SQL', '789', '']
print(re.split(r"(?:\d+)",text)) # this gives the same as "\d+" so why would you bother?
# to clarify:
# # \d+ — match one or more digits.
# (?:\d+) — group one or more digits, but don't capture them.
# (\d+) — group and capture one or more digits.

# Because sometimes you need to group several things together to apply an operator to the whole group.

# r"(?:abc)+" - Matches abc, abcabc, abcabcabc, etc.
# r"abc+" - Matches ab followed by one or more c characters!
# That's the real purpose of non-capturing groups: you get the grouping behaviour without creating a capture.