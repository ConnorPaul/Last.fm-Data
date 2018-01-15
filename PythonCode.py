import codecs
from operator import itemgetter
artistsfile = codecs.open("artists.dat", encoding="utf-8")
userartistsfile = codecs.open("user_artists.dat", encoding="utf-8")
user_friendsfile = codecs.open("user_friends.dat", encoding="utf-8")
user_taggedartistsfile = codecs.open("user_taggedartists.dat", encoding="utf-8")

aid2name = {}
uid2numplays = {}
aid2numplays = {}
listenercounts = {}
songplaycounts = {}
averageplays = {}
newaverageplays = {}
bestfriendsforever = {}
fiveormorefriends = {}
lessthanfivefriends = {}
songplaycounts2 = {}
songplaycounts3 = {}

artistsfile.readline() #skip first line of headers
for line in artistsfile: #reads each line in the file
    line = line.strip()
    fields = line.split('\t')
    aid = int(fields[0]) #this tells the dictionary which part is the artist id
    name = fields[1] #this tells the dictionary which part is the artist name
    aid2name[aid] = name #this maps the aids to the artists
artistsfile.close()
 
userartistsfile.readline() #skip first line of headers
for line2 in userartistsfile:
    line2 = line2.strip()
    fields2 = line2.split('\t')
    uid = int(fields2[0]) #this tells the dictionary which part is the user id
    aid2 = int(fields2[1]) #this tells the dictionary which part is the artist id
    numplays = int(fields2[2]) #this tells the dictionary which part is the number of plays
    if uid in uid2numplays:
        uid2numplays[uid] += numplays #if the uid already exists in the dict, add the current numplay to that uid's total numplays
    else:
        uid2numplays[uid] = numplays #if the uid doesn't exist in the dict, make this numplay the starting number
    if aid2 in aid2numplays:
        aid2numplays[aid2] += numplays #if the aid already exists in the dict, add the current numplay to that aid's total numplays
    else:
        aid2numplays[aid2] = numplays #if the aid doesn't exist in the dict, make this numplay the starting number
    if aid2 in listenercounts:
        listenercounts[aid2] += 1 #if the aid already exists in the dict, add one to the existing count
    else:
        listenercounts [aid2] = 1 #if the aid doesn't exist in the dict, start the count at 1
    if uid in songplaycounts:
        songplaycounts[uid] += numplays #if the uid already exists in the dict, add the current numplay to that uid's total numplays
    else:
        songplaycounts[uid] = numplays #if the uid doesn't exist in the dict, make this numplay the starting number
userartistsfile.close()

for key in aid2numplays:
    averageplays[key] = aid2numplays[key]/listenercounts[key] #matches the aids of the two dictionaries and divides their values. Then uses this information to create a new dictionary with the aid and new values
    
for key in aid2numplays:
    if listenercounts[key] > 50: #checks to make sure that the artist has more than 50 listeners
        newaverageplays[key] = aid2numplays[key]/listenercounts[key] #matches the aids of the two dictionaries and divides their values. Then uses this information to create a new dictionary with the aid and new values

user_friendsfile.readline() #skip first line of headers
for line3 in user_friendsfile: #reads each line in the file
    line3 = line3.strip()
    fields3 = line3.split('\t')
    uid2 = int(fields3[0]) #this tells the dictionary which part is the user id
    fid = int(fields3[1]) #this tells the dictionary which part is the friend id
    if uid2 in bestfriendsforever:
        bestfriendsforever[uid2] += 1
    else:
        bestfriendsforever[uid2] = 1


for key in bestfriendsforever:
    if bestfriendsforever[key] >= 5: #checks to make sure that the user has 5 or more friends
        fiveormorefriends[key] = bestfriendsforever[key] #matches the uids of the two dictionaries and only stores users with 5 or more friends.
    else:
        lessthanfivefriends[key] = bestfriendsforever[key] 

for key in fiveormorefriends:
    songplaycounts2[key] = songplaycounts[key]

for key in lessthanfivefriends:
    songplaycounts3[key] = songplaycounts[key]

sorted_uid2numplays = sorted(uid2numplays.items(), key=itemgetter(1), reverse=True) #sort the uid dictionary by highest to lowest numplays
sorted_aid2numplays = sorted(aid2numplays.items(), key=itemgetter(1), reverse=True) #sort the aid dictionary by highest to lowest numplays
sorted_listenercounts = sorted(listenercounts.items(), key=itemgetter(1), reverse=True) #sort the listener dictionary by highest to lowest listeners
sorted_songplaycounts = sorted(songplaycounts.items(), key=itemgetter(1), reverse=True) #sort the songplay dictionary by highest to lowest songplays
sorted_averageplays = sorted(averageplays.items(), key=itemgetter(1), reverse=True) #sort the averageplays dictionary by highest to lowest average plays
sorted_newaverageplays = sorted(newaverageplays.items(), key=itemgetter(1), reverse=True) #sort the newaverageplays dictionary by highest to lowest average plays
sorted_bestfriendsforever = sorted(bestfriendsforever.items(), key=itemgetter(1), reverse =True) #sort the bestfriendsforeverdictionary by highest to lowest amount of friends

print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('1. Who are the top 10 artists in terms of play counts? [Prints a list of the top 10 artists sorted high to low by number of plays. Format is: NAME (AID) NUMBER OF PLAYS].')
print()
i = 0
for (k,v) in sorted_aid2numplays: #prints the top ten artists with the most number of plays.
    if i < 10:
        print(aid2name[k], '(' + str(k) +')', v)
        i += 1
        
print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('2. What artists have the most listeners? [Prints a list of the 10 artists with the highest number of users who have listened to at least one song by that artist. Sorted high to low by number of listeners. Format is: ARTIST NAME, (AID) and the NUMBER OF DISTINCT USERS WHO HAVE LISTENED TO A SONG BY THAT ARTIST].')
print()      
i = 0
for (k,v) in sorted_listenercounts: #prints the top ten artists with the highest number of users
    if i < 10:
        print(aid2name[k], '(' +str(k) + ')', v)
        i += 1

print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('3. Who are the top users in terms of play counts? [Prints the 10 user ids with the most song plays. Sorted high to low by number of song plays. Format is: UID and (TOTAL NUMBER OF SONG PLAYS FOR THAT USER)].')
print()

i = 0
for (k,v) in sorted_songplaycounts: #prints the 10 user ids with the most song plays
    if i < 10:
        print(k, '(' +str(v) + ')')
        i +=1

print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('4. What artists have the highest average number of plays per listener? [Prints a list of the 10 artists with the highest average number of plays per listener. Sorted high to low by average number of plays per listener. Format is: ARTIST NAME, (AID), NUMBER OF PLAYS, NUMBER OF LISTENERS, and AVERAGE NUMBER OF PLAYS PER LISTENER].')
print()

i = 0
for (k,v) in sorted_averageplays: #prints the artists with the highest average number of plays per listener
    if i < 10:
        print(aid2name[k], '(' + str(k)+ ')', aid2numplays.get(k), listenercounts.get(k), v)
        i += 1
        
print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('5. What artists with at least 50 listeners have the highest average number of plays per listener? [Prints a list of the 10 artists (with at least 50 listeners) with the highest average number of plays per listener. Format is: ARTIST NAME, (AID), NUMBER OF PLAYS, NUMBER OF LISTENERS, and AVERAGE NUMBER OF PLAYS PER LISTENER]')
print()

i = 0
for (k,v) in sorted_newaverageplays: #prints the artists (who have over 50 listeners) with the highest average number of plays per listener
    if i < 10:
        print(aid2name[k], '(' + str(k)+ ')', aid2numplays.get(k), listenercounts.get(k), v)
        i += 1

print()
print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
print()
print('6. Do users with five or more friends listen to more songs than users with less than five friends?')
print()
print('Average number of song plays for users with five or more friends:', (sum(songplaycounts2.values())/len(fiveormorefriends))) #adds up all of the values for songplays and divides that by the length of the dictionary of users with five or more friends
print()
print('Average number of song plays for users with less than five friends:', (sum(songplaycounts3.values())/len(lessthanfivefriends))) #adds up all of the values for songplays and divides that by the length of the dictionary of users with less than five friends