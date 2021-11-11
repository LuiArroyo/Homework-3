# Luis Arroyo
# PSID: 2037081
# CIS 2348

players={}
f=1
while(f<6):
    print("Enter player %s's jersey number:" % f)
    jersey=int(input())
    print("Enter player %s's rating:" % f)
    rating=int(input())
    print()
    if((jersey>=0 and jersey<=99) and(rating>=1 and rating<=9)):
        players.update({jersey:rating})
        f = f + 1
    else:
        pass
print('ROSTER')
for key in sorted(players.keys()):
    print("Jersey number: %s, Rating: %s" % (key, players[key]))

def add():
   print("Enter a new player's jersey number:")
   jersey = int(input())
   print("Enter the player's rating:")
   rating=int(input())
   if((jersey>=0 and jersey<=99) and(rating>=1 and rating<=9)):
       players.update({jersey:rating})
   else:
       pass
def remove():
       print('Enter player jersey number:')
       jersey=int(input())
       del players[jersey]
def update():
       print('Enter player jersey number:')
       jersey=int(input())
       print('Enter player rating:')
       rating=int(input())
       players[jersey]=rating
def above():
    print('Enter a rating:')
    rat=int(input())
    for key in sorted(players.keys()):
        if(players[key]>rat):
           print("Jersey number: %s, Rating: %s\n" % (key, players[key]))
        else:
            pass
def output():
   for key in sorted(players.keys()):
       print("jersey number:%s,rating:%s" % (key, players[key]))
store="z"
while(store!="q"):
    print()#given on zybooks
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit')
    print()
    print('Choose an option:')
    store=input()
    if(store=='a'):
        add()
    elif(store=='d'):
        remove()
    elif(store=='u'):
        update()
    elif(store=='r'):
        above()
    elif(store=='o'):
        output()
    else:
        pass