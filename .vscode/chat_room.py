str1=input()
def check(string):
    str2=["e","l","l","o"]
    set1=set(string)
    if not (set("hello")<= set1) or string.count("l")<2:
        return "NO"
    firs=string.index("h")
    i=firs+1
    while i<len(string) and len(str2)>0 :

        if str2[0] not in string[i:]:
            return "NO"
        else:
            curr=string[i:].index(str2[0])
            del str2[0]
            i+=curr+1
    return "YES" if len(str2)==0 else "NO"
print(check(str1))

