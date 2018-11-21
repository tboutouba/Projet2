'''On considere que les informations sur les candidats sont stockees sous un format json de la forme de'''

data_test=[
 {
   "id": 1,
   "nom": "nom1",
   "prenom": "prenom1",
   "dateNaissance": 1,
   "lieuNaissance": 1,
   "dateEntretien": 1,
   "lieuEntretien": 1,
   "fichiers": 
   [
     {
       "id" : 1.1,
       "nom": 1.1,
       "contenu": 1,
       "nomTest": 1,
       "contenu_Test": 1,
       "stats": 
       {
         "functionsCount": 1,
         "commentCount": 1,
         "variableNameQuality": 1,
         "duplicate": 
         [
           {
             "id": 1,
             "similarity": 1
           }
         ]
       },
       "compteRendu": 1,
       "dateUpload": 1
     },
     {
       "id" : 1.2,
       "nom": 1.2,
       "contenu": 1,
       "nomTest": 1,
       "contenu_Test": 1,
       "stats": 
       {
         "functionsCount": 1,
         "commentCount": 1,
         "variableNameQuality": 1,
         "duplicate": 
         [
           {
             "id": 1,
             "similarity": 1
           }
         ]
       },
       "compteRendu": 1,
       "dateUpload": 1
     }
   ],
   "metrics":
   {
     "level": 1
   }
 },
 {
   "id": 2,
   "nom": "nom2",
   "prenom": "prenom2",
   "dateNaissance": 2,
   "lieuNaissance": 2,
   "dateEntretien": 2,
   "lieuEntretien": 2,
   "fichiers": 
   [
     {
       "id" : 2,
       "nom": 2,
       "contenu": 2,
       "nomTest": 2,
       "contenu_Test": 2,
       "stats": 
       {
         "functionsCount": 2,
         "commentCount": 2,
         "variableNameQuality": 2,
         "duplicate": 
         [
           {
             "id": 2,
             "similarity": 2
           }
         ]
       },
       "compteRendu": 2,
       "dateUpload": 2
     }
   ],
   "metrics":
   {
     "level": 2
   }
 }
 ]



def liste_candidats(fichier):
    with open(fichier) as data:
        Liste_candidats=[]
        for candidat in data['candidats']:
            informations=[candidat["id"],candidat["nom"],candidat["prenom"]]
            Liste_candidats.append(informations)
        return Liste_candidats




























