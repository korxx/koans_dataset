import re
data = ""
def print_koans(data):    
    return re.sub('(----)', '</li><li>', data)
    
def edit_koans(data):
    return re.sub('</li><li>', '(----)', data)