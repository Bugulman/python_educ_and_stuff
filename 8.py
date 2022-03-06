import re

def to_underscope(string):
    """Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.
    """
    
    try:
	    m = re.findall('[A-Z]', string)
	    for word in m:
	        new_w = '_'+ word.lower()
	        string = string.replace(word, new_w)
	    return string[1:]
    except Exception as e:
        return str(string)

print(to_underscope('SomeFrase'))
print(to_underscope(1))
# stri = 'SomeFrase'
# print(stri.lower())
