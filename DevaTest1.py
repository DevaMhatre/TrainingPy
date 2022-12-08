

# COMPREHENSIONs Programs
nums = [i for i in range(1, 1001)]
string= "Practice Problems to Drill List Comprehension in Your Head."
# print(nums)

# Q1.
div8= []
for x in nums:
    if x%8==0:
        div8.append(x)
print(div8)

# Q2. num that have 6 in them

inthem =[]
for i in nums:
    if '6' in str(i):
        inthem.append(i) 
    print(inthem)

# Q3. no. of spaces in string

spaces =[]
count=0
for i in string:
    if ' ' in str(i):
        count+=1 
print(count)

# Q4. remove all the vowels


vow=['a','e','i','o','u']
antii=[ i for i in string if i.lower() not in vow]
print(''.join(antii))

# Q.5
testt=string.split()
tittu=[i for i in testt if len(i)> 6 ]
print(' '.join(tittu))
