## Exercise 7: Seeing the World
#let places i want to visit be noted as bucket_list
bucket_list=['Saudia Arabia','America','Bahrain','Austrailia','Kashmir','london',"Japan"]
print(bucket_list)
print('\n')

# using sorted printing here (A-Z FORM) Alphabetical order
print('Using sorted here:')
print(sorted(bucket_list))
print('\n')

# using reverse printing. "list order in reversed"
print('Using reverse here:')
bucket_list.reverse()
print(bucket_list)
print('\n')

# to undo reverse ande have the original list order using reverse() again.
print('Using reverse here again:')
bucket_list.reverse()
print(bucket_list)
print('\n')

# Sorting the unordered list which was just reversed
print('Using sorted here again:')
print(sorted(bucket_list))
print('\n')

#reversing the .sort() to put the list in order of (Z-A) Alphabetical order reversed
print('list sorted but reversed version:')
bucket_list.sort(reverse=True)
print(bucket_list)
print('\n')