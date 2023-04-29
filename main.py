def count_words(file_contents) : 
    words = file_contents.split()
    return len(words)

def count_letters(file_contents) : 
    file_contents = file_contents.lower()
    dict = {}
    for i in file_contents : 
        if i.isalpha() : 
            if i in dict : 
                dict[i] += 1
            else : 
                dict[i] = 1
    return dict
with open("books/frankenstein.txt") as f : 
    file_contents = f.read()
    count = count_words(file_contents)
    print(f'{count} words were found in the document')
    dict = count_letters(file_contents)
    alpha = list(dict.keys())
    alpha.sort()
    for i in alpha : 
        print(f"The '{i}' character was found {dict[i]} times")

