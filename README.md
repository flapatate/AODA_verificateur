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
3- Consulter le rapport.txt.


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
