#18.12.2024 Andre Meronen
#Harjutus 15 

kuud = [["jaanuar",-4,0,9,-13,-9,-11,13,-19,-19,14,15,-10,7,-7,25,-4,18,16,-11,-8,19,8,-8,-6,-7,-9,14,12,12,-12,10],
["veebruar",5,-14,-7,-18,-1,20,-12,13,5,12,12,9,17,11,-16,8,26,19,17,-2,-12,17,-17,6,6,21,19,-17,0,-13,27],
["märts",10,16,21,-19,21,-17,-16,-19,-20,9,12,21,2,6,-6,23,9,-11,8,7,20,-11,-17,18,16,3,23,24,-20,-3,10],
["aprill",-2,21,21,-14,22,5,1,1,-6,-10,-14,24,17,-8,-11,6,16,-19,-10,27,28,28,23,0,-6,0,-18,16,-3,-19,2],
["mai",0,29,9,-4,14,19,23,20,-5,9,-7,28,4,10,22,-20,16,16,2,-12,6,3,2,2,-19,21,21,-16,17,2,22],
["juuni",12,-13,12,4,1,11,10,-7,-20,-3,26,-10,23,25,3,7,-9,23,8,7,26,-13,-16,-7,-19,13,-20,17,9,5,15],
["juuli",-11,-5,10,-14,7,15,-15,21,17,-13,24,6,18,3,30,22,-11,0,-5,17,0,-10,-16,7,26,-10,18,21,18,12,-15],
["august",11,26,1,2,-16,14,2,6,11,11,14,-2,-1,1,-11,-1,-13,-4,10,-16,17,20,-10,-6,-2,-3,29,17,-19,10,-17],
["september",-2,6,-15,27,13,-17,5,10,9,27,15,-2,26,-2,23,15,-17,-14,23,14,-16,9,-14,22,-13,25,24,-13,28,-20,-10],
["oktoober",-8,-4,15,-18,22,25,25,11,3,-6,9,10,11,23,27,-9,8,-8,-14,13,-7,-9,15,24,-4,19,5,-8,-4,-6,-5],
["november",-6,3,-14,-3,6,6,-20,-2,-12,15,-2,17,-17,24,-10,19,6,-8,-18,2,9,10,-8,10,-14,29,-8,-3,18,-6,30],
["detsember",-3,-19,29,-4,-9,25,-6,-12,-11,29,7,26,-11,3,19,8,17,3,-2,18,21,0,22,19,-4,15,16,11,6,10,14]]

for i in range(len(kuud)):
    print(kuud[i][0])
    k=[]
    for j in range(1,len(kuud[i])):
        k.append(kuud[i][j])
    print(kuud[i].index(max(k)))
