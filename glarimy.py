import sys
def deduplicate(duplicate):
    words=[]
    string=duplicate.split()
    for i in string:
        if i not in string:
            words.append(i)
    return words

def sort(string_list):
    new_list=sorted(string_list)
    return new_list
    
def parse(string):
    file = open(string,"r")
    info=file.read()
    file.close()
    words=deduplicate(info)
    new=sort(words)
    new_list=" ".join(new)
    print(new_list)
    
parse(sys.argv[1])
