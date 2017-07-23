# My wish dinner guest wish list
dinner_guest = ['Pawpaw Red', 'Pawpaw Ed', 'Uncle Luis']
# Let everyone know pawpaw ed cant make it
print(dinner_guest[1] + " Can not make it to dinner.")
# replace pawpaw ed with Momma nobie she can make the dinner
dinner_guest[1] = "Momma Nodie"
# print the  guest list
print(dinner_guest)
# Invitations to everyone
invitation_message = "please join me for dinner at mc donalds."
# send out the invitations to everyon
print(dinner_guest[0] + " " + invitation_message)
print(dinner_guest[1] + " " + invitation_message)
print(dinner_guest[-1] + " " + invitation_message)
# let everyone know that you found a bigger table
new_venue = 'I found more room at sonic everyone can attend!'
print(new_venue)
#invite aunt charles to dinner
dinner_guest.insert(0, 'Aunt Charles')
# invite Uncle Coon
dinner_guest.insert(1, 'Uncle Coon')
# invite aunit lexie
dinner_guest.append('Aunt Lexie')
# the new guest list
print(dinner_guest)
# invite everyone to dinner
print(dinner_guest[0] + " ," + new_venue)
print(dinner_guest[1] + " ," + new_venue)
print(dinner_guest[2] + " ," + new_venue)
print(dinner_guest[3] + " ," + new_venue)
print(dinner_guest[4] + " ," + new_venue)
print(dinner_guest[-1] + " ," + new_venue)

# Message to let guest know dinner is off
no_dinner = " Hey lets reschedule the dinner sorry!"
# remove people from the list and let them know
removed_guest = dinner_guest.pop(0)
print(removed_guest + "," + no_dinner)
removed_guest = dinner_guest.pop(1)
print(removed_guest + "," + no_dinner)
removed_guest = dinner_guest.pop(2)
print(removed_guest + "," + no_dinner)
removed_guest = dinner_guest.pop(3)
print(removed_guest + "," + no_dinner)

print(dinner_guest[4])


