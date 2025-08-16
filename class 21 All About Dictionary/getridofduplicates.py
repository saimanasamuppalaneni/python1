# get rid of duplicates 
student =  {'id1' :
           {'name':'zara',
            'age':'12',
            'subject':['maths','english','science']},
            'id2' :
           {'name':'joy',
            'age':'11',
            'subject':['maths','social','science']},
            'id3' :
           {'name':'zara',
            'age':'12',
            'subject':['maths','english','science']},
            'id4' :
           {'name':'lila',
            'age':'10',
            'subject':['maths','english','sanskrit']}}
result = {}
for key,value in student.items():
    if value not in result.values():
        result[key] = value
print(result)