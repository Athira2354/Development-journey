# write a function called register_check that check how many students are in school the function takes a dictionary as parameter if the student is in school the dictionary says 'yes' .if the student is not in school the dictionary says'no'. your function should return  the no of students in school use the dictionary below your  fuction should return 3.

def register_check(register):
    
    count=0
    for student in register.values():
        if student=='yes':
           count+=1
    return count

print(register_check(register= {
              'Michael':'yes',
              'John':'no',
              'Peter':'yes',
              'Mary':'yes',
              }))
