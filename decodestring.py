def decodeString(s):
    st=[]
    curr_str=''
    curr_num=0
    for ch in s:
        if ch.Isdigit():
            curr_num=curr_num*10+int(ch)
        elif ch=='[':
            st.append[(curr_str,curr_num)]
            curr_sstr=''
            curr_num=0
        elif ch==']': 
            prev,prevn=st.pop()
            curr_str=prev+prevn*curr_str
        else:
            curr_str+=ch
    return curr_str
s='3[a2[b]]'
print(decodeString(s))


