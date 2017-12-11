import re, urllib

try:
    import urllib.request
except:
    pass

sites = 'google yahoo cnn msn'.split()
pattern = re.compile(r'<title>+.*</title>+',re.I | re.M)

for s in sites:
    print("Searching: " + s)
    try:
        u =urllib.urlopen('http://' + s + '.com')
    except:
        u = urllib.request.urlopen('http://' + s + '.com')

    text = u.read()
    # title = re.findall(r'<title>+.*</title>+',str(text),re.I|re.M)

    # use patterrn
    title = re.findall(pattern, str(text))
    print(title[0])


