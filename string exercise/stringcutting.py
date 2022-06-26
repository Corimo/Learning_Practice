string = "james"

middle = (len(string) + 1)//2
result = string[0] + string[middle] + string[len(string) -1]
print (str(result))

str1 = "JaSonAy"

middy = len(str1) // 2
start = middy - 1
end = middy + 2

print (str1[start:end])

s1 = "Ault"
s2 = "Kelly"

mid = len(s1) // 2

res = s1[:mid:] + s2 + s1[mid::]
print(res)

st1 = "America"
st2 = "Japan"

starts = st1[0] + st2[0]
mids = st1[len(st1)//2] + st2[len(st2)//2]
ends = st1[len(st1) - 1] + st2[len(st2) - 1]

print(starts + mids + ends)