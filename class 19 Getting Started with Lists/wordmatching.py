# word matching
def match_words(list1):
    new_list = []
    count=0
    for i in list1:
        if i [0]==i[-1]and len(i)>2:
            count+=1
            new_list.append(i)
    print(new_list)
    print("the words which has first and last character same are ",count)
list1 = ['aarathi','bob','john','civic','amma']
match_words(list1)