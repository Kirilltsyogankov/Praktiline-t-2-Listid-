##vanused=[] 
##for i in range(5):
##    vanus=int(input("Sisesta vanus: "))
##    vanused.append(vanus) #
##maksimum=max(vanused)
##minimum=min(vanused) 
##summa=sum(vanused)
##keskmine=summa/len(vanused) 
###Kuva ekraanile nimi koos vanusega
##for i in range(5):
##    print(nimed[i],"on ", vanused[i],"aastat vana")


##3
#from random import *
#arvud=[] 
#N=int(input("Mitu rida joonistame? "))
#S=input("Siseta sümbol: ")
#for p in range(N):
#    arvud.append(randint(1,100))
##diagrammi loomine
#for p in range(N):
#    print(arvud[p]*S)


##4
#Indeksid=["Tallinn","Narva,Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa,Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa,Põlvamaa,Võrumaa,Valgamaa","Viljandimaa,Järvamaa,Harjumaa,Rapllamaa","Pärnuma","Läänema,Hiiuma,Saaremaa"]
#while True:
#    try:
#        indeks=int(input("Sisesta oma indeks: "))#10000,15478,98564
#        #if 10000<=indeks=<99999:
#        indeks_elemendide_arv=len(str(indeks))
#        if indeks_elemendide_arv==5:
#            print("5numbriline arv (indeks)")
#            break
#        else:
#            print("On vaja 5numbriline arv(indeks)")
#    except:
#        print("Vale andmetüüp!")
#arv1=indeks//10000
#symbolid=list(str(indeks))
#sym1=symbolid[0]
#print(sym1) 


##5
#rida=[] 
#N=randit(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida) 
#kogus=int(input("Mitu elemendi vahetame oma vahel "))
#if len(rida)//2>=kogus: 
#    a=rida[i]
#    rida[i]=rida[len(rida)-i-1] 
#    rida[len(rida)-i-1]=a 
#print(rida)


##6
#def find_and_replace_useless_number(lst):
#    max_number = max(lst)
    
#    if len(lst) != 0:
#        useless_number = max_number / len(lst)
        
#        lst[lst.index(max_number)] = useless_number
        
#        return lst
#    else:
#        return "nimekiri on tühi"

#numbers = [10, 20, 30, 40, 50]
#result = find_and_replace_useless_number(numbers)
#print("Resultat pärast tundi:", result)


##7
#def sort_abs_list(numbers, reverse=False):
#    return sorted(numbers, key=abs, reverse=reverse)

#numbers = [5, -10, 3, -8, 1, -6]
#sorted_ascending = sort_abs_list(numbers)
#sorted_descending = sort_abs_list(numbers, reverse=True)

#print("Originaalne nimekiri:", numbers)
#print("Kasvav absoluutväärtus:", sorted_ascending)
#print("Kahanev absoluutväärtus:", sorted_descending)


##8
#lists = [['крот', 'белка', 'выхухоль'],
#         ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'],
#         ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']]

#for lst in lists:
#    sorted_list = sorted(lst, key=len)
#    print("Sorteeritud loend:", sorted_list)

