"""
Participant:
PADOVAN Dorian
"""


from math import*
from tkinter import Tk
from tkinter import Canvas
from time import time  

G=[
    [0,0,1,1,0,1],
    [0,0,1,0,1,1],
    [1,1,0,1,0,0],
    [1,0,1,0,1,0],
    [0,1,0,1,0,0],
    [1,1,0,0,0,0]  
]

def voir_graphe(graphe):
    """affiche dans la console une représentation du graphe sous forme d'une matrice adjacente

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relié et 1 sinon
    """
    for elt in graphe:
        c=''
        for e in elt:
            c=c+str(e)
        print(c)
        
#voir_graphe(G)

def contient_3_amis_fixes(graphe,i,j,k):
    """regarde si 3 sommets sont amis entre eux

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        i (0<=int<len(graphe)): nom du sommet
        j (0<=int<len(graphe)): nom du sommet
        k (0<=int<len(graphe)): nom du sommet

    Returns:
        bool: True or False
    """
    return graphe[i][j]==1 and graphe[j][k]==1 and graphe[k][i]==1

def contient_3_etrangers_fixes(graphe,i,j,k):
    """regarde si 3 sommets sont étrangers entre eux

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        i (0<=int<len(graphe)): nom du sommet
        j (0<=int<len(graphe)): nom du sommet
        k (0<=int<len(graphe)): nom du sommet

    Returns:
        bool: True or False
    """
    return graphe[i][j]==0 and graphe[j][k]==0 and graphe[k][i]==0

#print(contient_3_amis_fixes(G,0,2,3))
#print(contient_3_etrangers_fixes(G,2,4,5))

def afficher_graphe(graphe):
    """représenation du graphe sous forme d'un cercle depuis le module tkinter

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        
    """
    cords=[]
    n=len(graphe)
    r=250
    for i in range(n):
        x=r*cos(2*i*pi/n)+400
        y=r*sin(2*i*pi/n)+300
        cords.append((x,y))
    
    window = Tk()
    window.geometry("800x800")
    window.configure(background = "grey")
    window.title("Canvas - Draw Shapes")
    window.resizable(False, False)
    
    # setting up the canvas
    canvas = Canvas(width = 800, height = 800, bg = "white")
    canvas.pack(pady = 30)
    
    #canvas.create_text(175, 20, text = "Circle", font = ("Arial", 30))
    n2=len(cords)
    
    for i in range(n):
        for j in range(i,n):
            if graphe[i][j]==1:
                canvas.create_line(cords[i][0],cords[i][1],cords[j][0],cords[j][1],width=5,fill='Blue')
            if graphe[i][j]==0:
                canvas.create_line(cords[i][0],cords[i][1],cords[j][0],cords[j][1],width=5,fill='red',dash=(5))
            if graphe[i][j]==2: # pour mes essaies pour démontrer la dernière question
                canvas.create_line(cords[i][0],cords[i][1],cords[j][0],cords[j][1],width=5,fill='gray')
    
    for i in range(n2):
        canvas.create_oval(cords[i][0]+20, cords[i][1]+20, cords[i][0]-20, cords[i][1]-20, width = 3,fill='black')
        canvas.create_text(cords[i][0],cords[i][1],text=str(i),font = ("Arial", 30),fill='white')
    
    window.mainloop()

#afficher_graphe(G)

def decimal_vers_binaire(p,n):
    """converti un nombre en binaire

    Args:
        p (int=>0):un entier naturel sous base 10
        n (int=>0): un entier naturel sous base 10 

    Returns:
        liste: représentant l'écriture en base 2 du nombre p.La liste est taille n sauf si la représentation de p en base 2 est plus longue que n
    """
    c=[]
    while p!=0:
        c.insert(0,p%2)
        p=p//2
    n2=len(c)
    for i in range(n-n2):
        c.insert(0,0)
    return c
#print(decimal_vers_binaire(37,0))

def sous_ensembles(n):
    """l'ensembles des sous ensembles composés des entiers compris entre 0 et n-1

    Args:
        n (int=>0): un entier naturel

    Returns:
        liste de liste: les sous listes représentent un ensemble possibles d'entiers compris entre 0 et n-1
    """
    e=[]
    n1=2**n
    for i in range(n1):
        l=decimal_vers_binaire(i,n)
        L=[]
        for i in range(n):
            if l[i]==1:
                L.append(i)
        e.append(L)
    return e

#print(sous_ensembles(3))

def sous_ensembles_fixes(n,k):
    """l'ensembles des sous ensembles composés des entiers compris entre 0 et n-1 de taille k

    Args:
        n (int=>0): un entier naturel
        k (int>=0): un entier naturel

    Returns:
        liste de liste: les sous listes représentent un ensemble possible d'entiers compris entre 0 et n-1 de taille k
    """
    e=[]
    n1=2**n
    for i in range(n1):
        l=decimal_vers_binaire(i,n)
        L=[]
        for i in range(n):
            if l[i]==1:
                L.append(i)
        e.append(L)
    t=[]
    for liste in e:
        if len(liste)==k:
            t.append(liste)
    return t

#print(sous_ensembles_fixes(6,3))
#print(sous_ensembles_fixes(6,3))

def graphe_contient_3(graphe,triplet):
    """vérifie si un graphe possède un sous grade d'ordre 3 tel que les 3 n'ont pas de relations ou sont amis. 
    représenté respectivement par des 0 et des 1 

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        triplet (liste): fonction ->sous ensembles_fixes(len(graphe),3)

    Returns:
        bool: True or False
    """
    for i,j,k in triplet:
        if contient_3_amis_fixes(graphe,i,j,k) or contient_3_etrangers_fixes(graphe,i,j,k):
            return True
    return False

assert (graphe_contient_3(G,sous_ensembles_fixes(len(G),3)))==True

def voir_tous_graphes(n):
    """représentation de tous les graphes possibles de taille n sous forme de matrice adjacente dans la console

    Args:
        n (int>=0): un entier naturel
    """
    n2=int((n-1)*n/2)
    n1=2**n2
    for i in range(n1):
        l=decimal_vers_binaire(i,n2)
        graphe=[[0 for iii in range(n)] for j in range(n)]
        for jj in range(0,n):
            for ii in range(jj+1,n):
                b=l.pop()
                graphe[ii][jj]=b
                graphe[jj][ii]=b
        voir_graphe(graphe)
        print('Suivant')
        
#voir_tous_graphes(2)

def test_tous_graphes(n):
    """teste si il existe un sous graphe complet d'odre 3 parmis les graphes de taille n tel que tous ses sommets ont une relation particulière

    Args:
        n (int>=2): un entier naturel strictement supérieur à 1
    """
    triplet=sous_ensembles_fixes(n,3)
    n2=int((n-1)*n/2)
    n1=2**(n2-1) # • Vous pouvez seulement tester les graphes qui correspondent à p entre 0 et 2N/2 (car pour les p suivants cela revient à échanger les segments verts en rouges et inversement)
    for i in range(n1):
        l=decimal_vers_binaire(i,n2)
        graphe=[[0 for iii in range(n)] for j in range(n)]
        for j in range(0,n):
            for ii in range(j+1,n):
                b=l.pop()
                graphe[ii][j]=b
                graphe[j][ii]=b
                
        if not graphe_contient_3(graphe,triplet):
            return graphe
    return True

#print(test_tous_graphes(2))
"""
n=5
G=test_tous_graphes(n)
if G==True:
    print(True)
else:
    print(G)
    afficher_graphe(G)
"""
contre_exemple_pour_4=[[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
#afficher_graphe(contre_exemple_pour_4)   
contre_exemple_pour_5=[[0, 0, 0, 1, 1], [0, 0, 1, 0, 1], [0, 1, 0, 1, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0]]     
#afficher_graphe(contre_exemple_pour_5)
t=time()
assert test_tous_graphes(6)==True
#print(time()-t) # 0.367 seconde sur le pc de la région
t=time()
#assert test_tous_graphes(7)
#print(time()-t) # 25.811 secondes sur le pc de la région
#assert test_tous_graphes(8)
#print(time()-t) # 1h 4minutes et 25.548 secondes sur le pc de la région (en utilisant le pc à côté)


def contient_4_amis_fixes(graphe,i,j,k,o):
    """regarde si 4 sommets sont amis entre eux

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        i (0<=int<len(graphe)): nom du sommet
        j (0<=int<len(graphe)): nom du sommet
        k (0<=int<len(graphe)): nom du sommet
        o (0<=int<len(graphe)): nom du sommet

    Returns:
        bool: True or False
    """
    return graphe[i][j]==1 and graphe[i][k]==1 and graphe[i][o]==1 and graphe[j][k]==1 and graphe[j][o]==1 and graphe[k][o]==1

def graphe_contient_4_ou_3(graphe,quatruplet,triplet):
    """vérifie si un graphe possède un sous graphe complet d'ordre 3 tel que les 3 n'ont pas de relations amicales ou un sous graphe d'ordre 4 tel que les 4 sommets sont amis. 
    Représenté respectivement par des 0 et des 1 

    Args:
        graphe (liste de liste): la matrice adjacente d'un graphe sous forme de liste de liste dont les éléments sont 0 si les deux sommets ne sont pas relier et 1 sinon
        triplet (liste): fonction ->sous ensembles_fixes(len(graphe),3)
        quatruplet(liste): fonction ->sous_ensembles_fixes(len(graphe),4)

    Returns:
        bool: True or False
    """
    for i,j,k,o in quatruplet:
        if contient_4_amis_fixes(graphe,i,j,k,o):
            return True
    for i,j,k in triplet:
        if contient_3_etrangers_fixes(graphe,i,j,k):
            return True
    return False


def test_tous_graphes_4_ou_3(n,t=time()):
    """test si il existe un sous graphe complet d'odre 3 parmis les graphes de taille n tel que tous ses sommets sont étrangers
    ou alors si il existe un sous graphe complet d'ordre 4 parmis les graphes de taille n tel que tous ses sommets soit amis

    Args:
        n (int>=2): un entier naturel strictement supérieur à 1
    """
    triplet=sous_ensembles_fixes(n,3)
    quatruplet=sous_ensembles_fixes(n,4)
    n2=int((n-1)*n/2)
    ctre=[]
    #print(n2)
    n1=2**(n2) # ici la couleur à une importance donc on ne peut pas diviser par 2 
    #test=n1//100 # si n est grand pour voir une avancé 
    #pourcentage=0 # si n est grand pour voir une avancé 
    for i in range(n1):
         # si n est grand pour voir une avancé 
        """if i%test==0:
            print(str(pourcentage)+'%, ',str(time()-t)+' secondes')
            pourcentage=pourcentage+1"""
        l=decimal_vers_binaire(i,n2)
        graphe=[[0 for iii in range(n)] for j in range(n)]
        for j in range(0,n):
            for ii in range(j+1,n):
                b=l.pop()
                graphe[ii][j]=b
                graphe[j][ii]=b 
        if not graphe_contient_4_ou_3(graphe,quatruplet,triplet):
            ctre.append( graphe)
    return ctre

"""
t=time()
n=8
G=test_tous_graphes_4_ou_3(n)
if G==True:
    print(True)
else:
    print(G)
    print(time()-t)
    afficher_graphe(G)
"""
contre_exemple_pour_6=[[0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 0, 1], [0, 0, 0, 1, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 0]]
#afficher_graphe(contre_exemple_pour_6)
contre_exemple_pour_7=[[0, 0, 1, 0, 1, 1, 1], [0, 0, 1, 1, 0, 0, 1], [1, 1, 0, 0, 0, 0, 1], [0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 0, 0, 0, 0]]
#afficher_graphe(contre_exemple_pour_7)
contre_exemple_pour_8=[[0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 0, 1, 1], [1, 0, 0, 1, 0, 1, 0, 1], [0, 1, 1, 0, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 1, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]]
#afficher_graphe(contre_exemple_pour_8) 

"""question 3:
Preuve qu'un graphe d'ordre 6 admet 3 amis ou 3 étrangers

Supposons qu'il existe un graphe complet R d'ordre 6 tel qu'il ne contient aucun sous-graphe d'ordre 3 où toutes les arêtes sont vertes ou rouges.

Soit S un sommet quelconque de R.
Selon le principe des tiroirs (ici 2 tiroirs: vert ou rouge et 5 chaussettes: les voisins de S sachant que R est complet et d'odre 6 ):
S admet au moins 3 voisins d'une même couleur
On note S1,S2 et S3 3 des voisins de S ayant leurs arrêtes avec S qui est de la même couleur.
On remarque alors que:
    comme S-S1 et S-S2 sont d'une même couleur alors S1-S2 est de l'autre couleur 
    comme S-S2 et S-S3 sont d'une même couleur alors S2-S3 est de l'autre couleur 
    comme S-S3 et S-S1 sont d'une même couleur alors S1-S3 est de l'autre couleur 

On a donc une contradiction car le sous graphe de R d'ordre 3 composé de S1, S2 et S3 se voit avoir toutes ses arêtes ayant la même couleur.
Il n'existe donc pas de graphe d'odre 6 tel qu'il n'y ait pas 3 amis ou 3 étrangers

"""

"""question 3:
Preuve qu'un graphe d'ordre 9 admet 4 amis ou 3 étrangers

Supposons qu'il existe un graphe complet R d'ordre 9 tel qu'il ne contient aucun sous-graphe d'ordre 3 où toutes les arêtes sont rouges
et aucun sous-graphe d'odre 4 où toutes les arêtes sont vertes.

Soit S un sommet quelconque de R
Selon le principe des tiroirs (ici 2 tiroirs: vert ou rouge et 8 chaussettes: les voisins de S sachant que R est complet et d'odre 9 ):
S admet au moins 4 voisins d'une même couleur
On note S1,S2,S3 et S4 4 des voisins de S ayant leurs arêtes avec S qui est de la même couleur.

Si les 4 voisins sont rouges: # c'est très abstrait ->ligne 444 il y a une représentation graphique de ce que j'ai fait
    comme S-S1 et S-S2 sont rouges alors S1-S2 est vert
    comme S-S2 et S-S3 sont rouges alors S2-S3 est vert
    comme S-S3 et S-S4 sont rouges alors S3-S4 est vert
    comme S-S3 et S-S1 sont rouges alors S1-S3 est vert
    comme S-S4 et S-S2 sont rouges alors S2-S4 est vert
    comme S-S4 et S-S1 sont rouges alors S1-S4 est vert

On a donc une contradiction car le sous graphe de R d'ordre 4 composé de S1, S2, S3 et S4 se voit avoir toutes ses arêtes de couleurs vertes.

Si les 4 voisins sont verts:
    On cherche maintenant à montrer qu'il y a au minimum un sommet du graphe R tel que au moins 4 de ses arêtes soit rouges
    On suppose donc maintenant que tous les sommets de R ont (au moins) 5 arêtes vertes (pour qu'il n'y en ait pas 4 rouges)
    Toutefois si on représente une arête verte pas une arête et une arête rouge par aucun lien,
    On remarque que c'est impossible que tous les sommets possèdent 5 arêtes vertes car le nombre de sommets de degré impair d’un graphe non orienté est pair.
    On a donc 8 sommets avec au moins 5 arêtes vertes et 1 sommets avec 2,4,6 ou 8 arêtes vertes (ou 6 sommets avec un nombre impair et 3 avec un nombre pair etc)
    On peut éliminer le cas ou il y en as 2 ou 4 car ça impliquerai 4 arêtes rouges et donc un sous graphe complet d'ordre 4 vert comme vu précédement
    
    Si le sommet ayant un degré pair admet pour dégré 6: # c'est très abstrait ->ligne 458 il y a une représentation graphique de ce que j'ai fait
        On note S ce sommet et S1,S2,S3,S4,S5 et S6 les voisins de S ayant leur arêtes avec S de couleurs vertes.
        On note S' un des 6 voisins verts de S
        On constate que S' dans ses (au moins)5 arêtes vertes en admet au moins 3 apartenant aux sommets verts de S(car il n'y a que 2 sommets non relié)
        On note S1',S2' et S3' les voisins cité 
        On remarque alors que:
            comme S-S', S-S1', S-S2', S'-S1' et S'-S2' sont verts alors S1'-S2' est rouge 
            comme S-S', S-S3', S-S2', S'-S3' et S'-S2' sont verts alors S3'-S2' est rouge  
        On remarque alors que:
            comme S1'-S2' et S3'-S2' sont rouges alors S1'-S3' est vert
        
        On a donc une contradiction car le sous graphe de R d'ordre 4 composé de S,S',S1' et S2' se voit avoir toutes ses arêtes de couleurs vertes
    
    Si le sommet ayant un degré pair admet pour dégré 8: # c'est très abstrait ->ligne 458 il y a une représentation graphique de ce que j'ai fait
        On note S ce sommet et S1,S2,S3,S4,S5,S6,S7 et S8 les voisins de S ayant leur arêtes avec S de couleur vertes.
        On note S' un des 8 voisins verts de S
        On constate que S' dans ses (au moins)5 arêtes vertes en admet au moins 5 apartenant aux sommets verts de S(car il n'y a que 0 sommets non relié)
        On note S1',S2' et S3' les voisins cité 
        On remarque alors que:
            comme S-S', S-S1', S-S2', S'-S1' et S'-S2' sont verts alors S1'-S2' est rouge 
            comme S-S', S-S3', S-S2', S'-S3' et S'-S2' sont verts alors S3'-S2' est rouge  
        On remarque alors que:
            comme S1'-S2' et S3'-S2' sont rouges alors S1'-S3' est vert
        
        On a donc une contradiction car le sous graphe de R d'ordre 4 composé de S,S',S1' et S2' se voit avoir toutes ses arrêtes de couleurs vertes  

    
On vient donc de montrer que dans tous les cas le graphe R n'existe pas.
Par conséquent Il n'existe donc pas de graphe complet d'odre 9 tel qu'il n'y ait pas 4 amis ou 3 étrangers
"""
n=9
test9=[[2 for i in range(n)]for j in range(n)]
afficher_graphe(test9)
preuve_pour_9_si_rouge=[
    [2,2,2,2,2,0,0,0,0],#0
    [2,2,2,2,2,2,2,2,2],#1
    [2,2,2,2,2,2,2,2,2],#2
    [2,2,2,2,2,2,2,2,2],#3
    [2,2,2,2,2,2,2,2,2],#4
    [0,2,2,2,2,2,1,1,1],#5
    [0,2,2,2,2,2,2,1,1],#6
    [0,2,2,2,2,2,2,2,1],#7
    [0,2,2,2,2,2,2,2,2]#8
]   #0,1,2,3,4,5,6,7,8

#afficher_graphe(preuve_pour_9_si_rouge)

preuve_pour_9_si_vert=[
    [2,1,1,1,1,1,1,0,2],#0
    [2,2,1,1,2,0,0,1,1],#1
    [2,2,2,0,2,1,1,1,2],#2
    [1,2,2,2,2,2,2,2,2],#3
    [1,2,2,2,2,2,2,2,2],#4
    [1,2,2,2,2,2,1,1,2],#5
    [1,2,2,2,2,2,2,1,2],#6
    [1,2,2,2,2,2,2,2,2],#7
    [1,2,2,2,2,2,2,2,2]#8
]   #0,1,2,3,4,5,6,7,8

#afficher_graphe(preuve_pour_9_si_vert) 