#Each new term in the Fibonacci sequence is generated by adding the previous two terms.
## By starting with 1 and 2, the first 10 terms will be:

#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

#By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

fibb_seq = [1, 2, ]
x = 0
y = 1


while fibb_seq[y] < 4000000:
    z = fibb_seq[x] + fibb_seq[y]
    fibb_seq.append(z)
    x = x + 1
    y = y + 1

#print(fibb_seq)
#print(len(fibb_seq))


i = 0
even_fibb = []
while i < len(fibb_seq):
    if fibb_seq[i] % 2 == 0:
        even_fibb.append(fibb_seq[i])
        i = i + 1
    else:
        i = i + 1

print(sum(even_fibb))

#not the prettiest thing in the world...but I'm learning. this is the first script I've written outside of
#an IDE. I wrote it at work in notepad. I ended up having to tweak a little bit before I could get it to run
#originally i was trying to use sum() in line 15 which was returning ""'int' object is not iterable"" error
#once I fixed that I realized on line 27 I was using regular division and not the modulus operator (%)
#last but not least I was originally using .append[i] on line 28 and couldn't figure out why I was
#getting the wrong answer. After checking the output solution on google and debugging the code a fair bit
#I was able to iron out the issues and print the correct solution.