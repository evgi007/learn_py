import re
import operator

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

# print(re.findall(r"\d{1,5}\s\w+\s\w+\.","hjfqwdh234 main st.ashjgj"))

frequencies = [43, 16, 46, 33, 30, 13, 25, 7, 27, 5,
               17, 10, 24, 31, 37, 6, 47, 29, 2, 15,
               12, 32, 51, 9, 26, 22, 49, 39, 42, 44,
               1, 69, 21, 57, 75, 35, 3, 41, 50, 36,
               45, 28, 48, 23, 72, 34, 14, 4, 0, 38, 11,
               40, 73, 66, 54, 18, 64, 68, 58, 74, 60,
               61, 71, 63, 56, 65, 53, 67, 19, 55, 70,
               62, 20, 52, 59, 8]

frequencies_sorted = (sorted(frequencies, key=int))

# print (frequencies.sorted)

for fr in frequencies:
    print ("2433." + str(fr))

# Corey Schafer:
# https://www.youtube.com/watch?v=K8L6KVGG-7o
# text_to_search = '' \
#                  '' \
#                  'sfwefwe' \
#                  'fwefw' \
# 'qergtqergtqerg' \
# 'qqrgqrgqerabcgqer' \
# '.[][]'
#
#
# pattern = re.compile(r'\.')
#
# matches = pattern.finditer(text_to_search)
#
# for match in matches:
#     print(match)
#
# print(text_to_search[5:8])