

def pfe(s):
  st = [] 
  for c in s:
    if c.isdigit():
      st.append(int(c))
    else:
      b = st.pop()
      a = st.pop()
      if c == '+':
        st.append(a+b)  
      elif c == '-':
        st.append(a-b)
      elif c == '/':
        st.append(a/b)
      elif c == '*':
        st.append(a*b)
  
  return int(st.pop())
  
s = input().strip()
print(pfe(s))
      