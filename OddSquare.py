ls = [str(int(i)**2) for i in input('write a sequence: ').split(',') if int(i)%2] #Creating a list of only the odd numbers of given sequence

print(','.join(ls))