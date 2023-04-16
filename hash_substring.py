# python3

def read_input():
    text=input()
    if "I" in text[:1]:
        txt_1=input().rstrip()
        txt_2=input().rstrip()
    else:
        with open("./tests/06", "r") as f:
            txt_1=f.readline().rstrip()
            txt_2=f.readline().rstrip()
    return(txt_1, txt_2)
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    
    
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
   # return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurances=[]
    pat_len=len(pattern)
    txt_len=len(text)
    pat_hash=hash(pattern)
    for i in range(txt_len-pat_len+1):
        if hash(text[i:i+pat_len])==pat_hash:
            if text[i:i+pat_len]==pattern:
                occurances.append(i)
    # this function should find the occurances using Rabin Karp alghoritm 

    # and return an iterable variable
    return occurances


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

