## Exercise 6: Shrinking Guest List
#starting with chapter 3 ,excercise 5 code as needed
invitee=['Tayyeb','Mike','Muntazir','jeff bezos']
print('Hi '+invitee[0]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[1]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[2]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[3]+', I am inviting you At My House For Dinner!\n')
print(invitee[3]+' , I Cannot Come To Dinner.\n')
invitee.pop(3)
invitee.append('Umer')
print('new updated list '+str(invitee)+"\n")
print('Hi '+invitee[0]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[1]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[2]+', I am inviting you At My House For Dinner!\n')
print('Hi '+invitee[3]+', I am inviting you At My House For Dinner!\n')

#now beginning with the code requested in excercise 6
print('Hey Guys,I Have Some Bad News; Due To Some Reason We Just Have Place For Two People For Dinner\n')
print(invitee[1]+''' ,I Am Truly Sorry But I Do Not Have A Seat For You Buddy!,
Maybe Next Time?\n''')
invitee.pop(1)
print(invitee)

#new rejection code message
print(invitee[0]+''' ,I Am Truly Sorry But I Do Not Have A Seat For You Buddy!,
Maybe Next Time?\n''')
invitee.pop(0)
print(invitee,"\n") 

#invitees left final notice/message
print(invitee[0]+",You Are Selected To Be Attending The Dinner Table\n")
print(invitee[1]+",You Are Selected To Be Attending The Dinner Table\n")

#to make list empty
del invitee[:]
print('invitee:',invitee)