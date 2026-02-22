#Dict question
'''
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
marks = student_marks[query_name]
'''

#Accessing values through dict key
'''
query = input('student name: ').lower().strip()
student_marks = {'lucas': [30,40,50], 'emma': [80,90,90]}
marks = student_marks[query]
'''

# name, *line = input().split() 
# name,*line = [1, 4, 6, 3, 4], Basically name = 1, line = [4, 6, 3, 4]

#Exercise requires to set result to 2 decimal places
''' print(f"{Values:.2f})'''
# : -> start formatting
# 2f -> 2 decimal places
# Only use in f-string







#Next