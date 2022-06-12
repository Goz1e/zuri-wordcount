# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,'r') as file:
        var = file.read()
        file.close()
    return var


def count_words():
    finanl_result = {}
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    word_list = text.split(' ')
    
    for x in word_list:
        counted =word_list.count(x)
        result = {x:counted}
        finanl_result.update(result)
    print(finanl_result)
    return finanl_result


read_file_content("./story.txt")

count_words()