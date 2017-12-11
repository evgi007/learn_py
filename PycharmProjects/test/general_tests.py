import re

# "\s" = space
# print(re.split(r"\s*","here are some words"))

# ()= used for grouping or including
# print(re.split(r"(\s*)","here are some words"))

# Remove "\" character = now "s" is regular character
# print(re.split(r"(s*)","here are some words"))

# [a-f] range of characters to lookin for split based on
# re.I = Ignorecase
# re.M = Multiline
# print(re.split(r"[a-fA-F0-9p-q]","cgwgcoiwegcoqegJHPJHPHnkkl",re.IGNORECASE | re.MULTILINE))

# [a-f][a-f] combination of characters (example "cd"
#print(re.split(r"[a-f][a-f]","cgwgcoiwegcoqegcdJHPJHPHnkkl",re.IGNORECASE | re.MULTILINE))

# Addresses:

# "\d" = digits
# "\D" = non-digits
# "\S" = non-Space
# "\s" = space
# "\w" = alphanumeric
# "\." = "."
# "." = anythingS
# "*" = 0 or more
# "+" = 1 or more
# "?" = 0 or 1 of ....
# {5} = exact number of...
# {1,60} = range on number of..

# "re.split" - split to banch of chuncks
# "re.findall" - only instances
# print(re.findall(r"\d","hjfqwdh234 main st.ashjgj"))

# print(re.findall(r"\d{1,5}","hjfqwdh234 main st.ashjgj"))

print(re.findall(r"\d{1,5}\s\w+\s\w+\.","hjfqwdh234 main st.ashjgj"))