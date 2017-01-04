# -*- coding: utf-8 -*-
"""
Ce programe en Python analyse les fichiers aoda (S0000000.txt)
qui sont placés dans le dossier où il se trouve.
Il détermine la présence d'éléments fautifs
dans chacun des fichiers.
Il dresse également la liste
des étiquettes dans le fichier, de manière
à pouvoir facilement vérifier leur cohérence.

Éléments fautifs repérés:

- Ligne trop longue (>39 caractères)
- Espace superflu à la fin des lignes
- Doubles espaces entre des mots
- Présence d'un astérisque
- Présence d'un tiret
- Autant de crochets ouverts que de fermés par paragraphe
- Chaque paragraphe doit débuter par une étiquette (un corchet ouvert)
- Plusieurs retours de ligne de suite

Instructions:
1- Placer le fichier AODA_verificateur.exe dans le dossier
où se trouvent les fichiers à vérifier.
2- Double cliquer sur le fichier AODA_verificateur.exe.
3- Consulter le rapport sur la console.


###
À faire:
- Etiquette avec des minuscules
- Option pour apporter des corrections automatiques au texte
###


********EXEMPLE******

***********************
ANALYSE DU FICHIER : S9999999.txt
***********************
PROBLÈMES DÉTECTÉS :

- Espace superflu à la fin de la ligne 11: 
[CHOEUR D'ENFANTS:] 

- Deux lignes vides de suite à la ligne 43

- Deux lignes vides de suite à la ligne 44

- Espace superflu à la fin de la ligne 54: 
[CHOEUR D'ENFANTS:] 

- Manque crochet ou etiquette au debut de la ligne 502: 
ÉMILIE lève une main.]

- Manque un crochet au paragraphe ligne 503: 
ÉMILIE lève une main.]

- Manque crochet ou etiquette au debut de la ligne 527: 
C'est mon dernier bloc.

- Ligne trop longue à la ligne 697: 
[DIMINOU donne des boîtes de raisins secs à TIMMY et TOMMY.

- Ligne trop longue à la ligne 941: 
des personnes présentes dans la pièce.]

- Présence d'un double espace à la ligne 952: 
On peut le  caresser,

- Manque crochet ou etiquette au debut de la ligne 964: 
NOtes: asdfasd* 19:34

- Présence d'un astérisque à la ligne 964: 
NOtes: asdfasd* 19:34

- Présence d'un tiret à la ligne 969: 
- Oh...


LISTE DES ÉTIQUETTES : 

['[AMANDA:]', '[ARTHRU:]', '[ARTHUR:]', '[BUSTER:]', "[CHOEUR D'ENFANTS:]", '[DIMINOU et ÉMILIE:]', '[DIMINOU:]', '[ENFANTS:]', '[JANE:]', '[KAMBLE:]', '[M. RATBURN:]', '[MME MORGAN:]', '[TIMMY:]', '[TOMMY:]', '[Titre:]', '[VOIX MASCULINE:]', '[ÉLÈVE1:]', '[ÉLÈVE2:]', '[ÉMILIE:]']


RÉSUMÉ DES PROBLÈMES DÉTECTÉS :
Espaces superflus en fin de ligne : 2
Doubles lignes vides : 2
Crochets manquants : 1
Étiquettes/crochets manquants début paragraphe : 3
Astérisques : 1
Tirets : 1
Doubles espaces : 1
Lignes trop longues : 2

********FIN EXEMPLE******

"""

import os, re

path = ".\\"

listing = os.listdir(path)


def main():
    
    for infile in listing:        
     
        if re.search('S\d\d\d\d\d\d\d\.txt$', infile):
            print ("\n***********************\nANALYSE DU FICHIER :", infile)
            print ("***********************\nPROBLÈMES DÉTECTÉS :\n")
            file = open(os.path.join(path,infile),'r', encoding='utf-8')
            
            verification(file,infile)

def verification(texte,infile):    
    #   new_file = open(os.path.join(path,infile+"_propre.txt"),'w')   
    
    espace_superflu = 0
    double_espace = 0
    double_retour = 0
    crochet_manquant = 0
    crochet_depart = 0
    asterisque = 0
    tiret = 0
    ligne_longue = 0    
    
    etiquettes = []

    no_ligne = 0
    ligne_vide = 0
    double_ligne_vide = 0

    paragraphe = ""    
    
    
    for line in texte:
        no_ligne += 1
        
        if re.search("^$", line):   #LIGNE VIDE
            ligne_vide = ligne_vide + 1
                        
            if paragraphe.count("[") != paragraphe.count("]"):
                crochet_manquant += 1
                print("- Manque un crochet au paragraphe ligne " + str(no_ligne)
                + ": \n" + paragraphe)
            
            paragraphe = ""
            
            if ligne_vide > 1:  #DEUX LIGNES VIDES

                print("- Deux lignes vides de suite à la ligne " + str(no_ligne)
                + "\n")                
                
                double_retour += 1
                double_ligne_vide += 1
                ligne_vide = 1
                
                
        else:
            
            if len(line) > 39:
                ligne_longue += 1
                print("- Ligne trop longue à la ligne " + str(no_ligne)
                + ": \n" + line)
            
            if ligne_vide > 0:
                if not re.search("^\[", line):
                    crochet_depart += 1
                    print("- Manque crochet ou etiquette au debut de la ligne "
                    + str(no_ligne) + ": \n" + line)
            
            if re.search(" $", line):
                espace_superflu += 1
                print("- Espace superflu à la fin de la ligne " + str(no_ligne)
                + ": \n" + line)
                
            if re.search("\*", line):
                asterisque += 1
                print("- Présence d'un astérisque à la ligne " + str(no_ligne)
                + ": \n" + line)
                
            if re.search("^\-", line):
                tiret += 1
                print("- Présence d'un tiret à la ligne " + str(no_ligne)
                + ": \n" + line)
            
            if re.search("  ", line):
                double_espace += 1
                print("- Présence d'un double espace à la ligne " + str(no_ligne)
                + ": \n" + line)            
            
            etiquette = re.search("^\[(.*)\:\]$", line)
            if etiquette:
                if etiquette.group(0) not in etiquettes:
                    etiquettes.append(etiquette.group(0))
            
            ligne_vide = 0
            
            paragraphe = paragraphe + line
   
    print("\nLISTE DES ÉTIQUETTES : \n")
    print(sorted(etiquettes))
    
    print("\n\nRÉSUMÉ DES PROBLÈMES DÉTECTÉS :")
    if espace_superflu:
        print("Espaces superflus en fin de ligne : " + str(espace_superflu))
    if double_retour:
        print("Doubles lignes vides : " + str(double_retour))
    if crochet_manquant:
        print("Crochets manquants : " + str(crochet_manquant))
    if crochet_depart:
        print("Étiquettes/crochets manquants début paragraphe : " + str(crochet_depart))
    if asterisque:
        print("Astérisques : " + str(asterisque))
    if tiret:
        print("Tirets : " + str(tiret))
    if double_espace:
        print("Doubles espaces : " + str(double_espace))
    if ligne_longue:
        print("Lignes trop longues : " + str(ligne_longue))
      
    
    
main()

input("Press Enter to continue...")