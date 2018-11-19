# If we list all the natural numbers below 10 that
# are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

three = 3
five = 5
three_multiples = [3]
five_multiples = [5]

while three < 999:
    three = three + 3
    three_multiples.append(three)
while five < 995:
    five = five + 5
    five_multiples.append(five)


merged_list = five_multiples + three_multiples
#print(set(merged_list))
print(sum(set(merged_list)))

#this ended up being a very round about way to solve this problem...I kept ending up with the wrong
#answer and had to manually compare my final sum to the correct answer online in order to trouble shoot
#where I was going wrong
#originally I had line 10 and 13 set to 1000 which was throwing off the final sum with extra digits.
#then set them to 999 but realize it was still add an extra 1000 to the list because 995 is less than
#999 and the function appended 1000 (the final multiple of 5) to the list as it was written originally.




