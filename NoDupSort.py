st = input('Write few words: ')
st = sorted(list(set(st.split(' '))))
st = ' '.join(st)
print('\n'+st+'\n')