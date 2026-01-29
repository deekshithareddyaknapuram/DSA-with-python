student_info={
    'deekshitha':{'rollno':401,'age':19,'course':'python'},
    'sathwik':{'rollno':18,'age':12,'course':'basic'}
}
print(student_info['deekshitha'])
student_info['deekshitha']['phone_no']=9902992
print(student_info['deekshitha'])
del student_info['deekshitha']['age']
print(student_info)
