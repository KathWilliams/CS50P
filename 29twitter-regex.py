import re # needed for regular expressions
# get the userID from the twitter profile
# be flexible with the user, we clean it up, lends for a better experience for the user
url = input("URL: ").strip()
# let's say we expect https://twitter.com/KathWilliams
# suggest to ignore anything before the last word
# username = url.replace("https://twitter.com/","")
# what if the user types in just twitter.com. what if they have a ? or / at the end
# what if they type in www or http and not https
# what if they type in 'my username is https://twitter.com/X'

# username = url.removeprefix("https://twitter.com/","") # at least this only removes if it is at the start


# let's use re.sub - substitution
# username = re.sub(r"https://twitter.com/","", url) # our starting point
# the '.' will mean any character will be tolerated!
# username = re.sub(r"^https?://twitter\.com/","", url)
# above - fix the '.' and make the s optional
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/","", url)
# now above make the www optional
# what if they don't type in the http(s) - it https?:// to be optional
# we're nesting optional stuff - hard to read/do, so break it down
# it's all a bit cryptic, so do it baby steps, even expert programmers need to do this
# you could use | as optional
# print(username)
# let's make this conditional to give an error if not
# originally i had the below surrounded by """ to comment out but that doesn't seem to stop python trying to compile it
# so changed to use #
# matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE) # let's assume ends with just the username
# if matches:
#     print(f"Username: ",matches.group(2)) # this won't work as www. will be in matches.group(1)!

# can use the walrus
# if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#   print(f"Username: ",matches.group(2))

# let's change this to ifnore the www!
#if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#   print(f"Username: ",matches.group(1))

# if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#   print(f"Username: ",matches.group(1))

# some other notes from chatgpt:

# we could have used re.match.  match only searches from the beginning so this would not need the ^
# but it still needs the $
# by using re.search with ^ then we have effectively said the same thing as .match
# let's try:
# if matches := re.match(r"(?:https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
#    print(f"Username: ",matches.group(1))
# also re.fullmatch does the whole string so wouldn't need ^ or $

# let's imagine users enter twitter.org or whatever else is possible - could do one of two ways
# if matches := re.match(r"(?:https?://)?(?:www\.)?twitter\.(?:com|org)/(.+)$", url, re.IGNORECASE):
# or
# if matches := re.match(r"(?:https?://)?(?:www\.)?twitter\.(.+)/(.+)$", url, re.IGNORECASE):
# the (.+) means we will accept anything here but will capture it, then we can query matches.group(1) in python in a list?

# one final change.  the username must be in a set of symbols
if matches := re.match(r"(?:https?://)?(?:www\.)?twitter\.com/([0-9A-Za-z_]+)$", url, re.IGNORECASE):
   print(f"Username: ",matches.group(1))
# to clarify
# re.search() with ^ and $ - starts at the beginning and must reach the end
#  looks anywhere in the string
# re.match() with $ - automatically starts at the beginning and must reach the end
#  so ^ is redundant
#  doesn't mean the full string must match
# re.fullmatch() - requires the entire string to match without either anchor
#  neither ^ or $ is needed

# also re.split
# re.findall