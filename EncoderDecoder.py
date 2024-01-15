text=input("Enter text: ")
key=input("Enter key: ")
ed=int(input("Enter 1 for Encode and 2 for Decode: "))
if ed==1:
    t=len(text)
    k=len(key)
    ascii_text=[]
    for a in text:
        ascii_text.append(ord(a))
    ascii_key=[]
    for a in key:
        ascii_key.append(ord(a))
    ascii_code=[]
    for i in range(0,t):
        c=0
        for j in range(0,k):
            c = c + (ascii_text[i] + ascii_key[j])
        code=[c]
        ascii_code.extend(code)
    encode=""
    for i in ascii_code:
        encode+=chr(i)
    r=encode
if ed==2:
    t=len(text)
    k=len(key)
    ascii_text=[]
    for a in text:
        ascii_text.append(ord(a))
    ascii_key=[]
    for a in key:
        ascii_key.append(ord(a))
    b=0
    for i in range(0,k):
        b=b+ascii_key[i]
    ascii_decode=[]
    for i in ascii_text:
        c=(i-b)//k
        code=[c]
        ascii_decode.extend(code)
    decode=""
    for i in ascii_decode:
        decode+=chr(i)
    r=decode
print("\nYour result is:\n",r)
