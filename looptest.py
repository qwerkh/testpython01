target=int(input("Input Number"))
even_sum=0
for number in range(2,target+1,2):
    even_sum+=number

print(f'Total = {even_sum}')
