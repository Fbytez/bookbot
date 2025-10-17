def sort_on(items):
    return items["num"]

def get_report(d):
    l = []
    
    for k, v in d.items():
        if k.isalpha():
            l.append({"char": k, "num": v})
    l.sort(reverse=True, key=sort_on)
    
    return l

def print_report(d):
    sorted_list = get_report(d)
    for d in sorted_list:
        ch = d["char"]
        n = d["num"]
        print(f"{ch}: {n}")

def count_chars(s):
    d = {}
    for c in s:
        c = c.lower()
        if c in d:
            d[c]+=1
        else:
            d[c]=1
    return d

def get_char_count(s):
    return count_chars(s)

def countWords(s):
    return len(s.split()) 

def get_num_words(s):
    num_words = countWords(s)
    print(f"Found {num_words} total words")

def read_book(path_to_file):
    with open(path_to_file) as f:
        s = f.read()
    return s
        
