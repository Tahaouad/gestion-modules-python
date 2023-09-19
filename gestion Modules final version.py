class Formateur:
    cpt=0
    lst=[]
    def __init__(self,Matricule:int=None,Nom:str=None,Prenom:str=None,Echelle:int=None,listeModu=lst):
        while Echelle<1 or Echelle>20:
            Echelle=int(input("Entrer echelle valide"))
        self.Matricule=Matricule
        self.Nom=Nom
        self.Prenom=Prenom
        self.Echelle=Echelle       
        Formateur.lst=listeModu    
        self.listeMod=Formateur.lst
        Formateur.cpt += 1
    def afficher(self):
        for i in self.listeMod:
            print(i)
    def __str__(self):
        return str(self.Matricule)+" "+str(self.Nom)+" "+str(self.Prenom)+" "+str(self.Echelle)+" "+str([i for i in self.listeMod])


class Module:
    cm=0
    ForM=[]
    def __init__(self,Ref=None,Intitulé=None,For=ForM):
        self.Ref=Ref
        self.Intitulé=Intitulé
        Module.ForM=For
        self.For=Module.ForM
        Module.cm += 1
    def __str__(self):
        return str(self.Ref)+" "+str(self.Intitulé)+" "+str(self.For)
    



class Centre:
    lstF=[]
    lstM=[]
    def __init__(self,lstF,lstM):
        Centre.lstF=lstF
        Centre.lstM=lstM
        self.lstF=Centre.lstF
        self.lstM=Centre.lstM
    def afficher(self):
        print("----------liste Formateur-------------")
        for i in self.lstF:
              print(i)
              #i.afficher()
           
        print("----------liste Modules-------------")
        for i in self.lstM:
            print(i)
            
    def AjouterF(self):
        m=int(input("Donner le Matricule"))
        n=input("Donner le Nom")
        p=input("Donner le PNom")
        ech=int(input("Donner l'echelle"))
        for1=Formateur(m,n,p,ech,[])
        self.lstF.append(for1)
    def AjouterM(self):
        R=input("Donner la reference ")
        I=input("Donner l'intitulé")
        mod=Module(R,I,[])
        self.lstM.append(mod)
    def recherche(self):
        pass
    def affecterF(self):
        ref=input("Donner la reférence du Module")
        mat=int(input("Entrer le matricule de formateur concerné par le module"))
        for i in Centre.lstM:
            if ref==i.Ref:
                print("Module existe")
                for j in Centre.lstF:
                    if j.Matricule==mat:
                        print("Formateur existe")
                        i.For.append(j.Matricule)
                        j.listeMod.append(i.Ref)
    def affecterM(self):
        matt=int(input("Entrer le matricule de formateur concerné par le module"))
        for i in self.lstF :
            if matt == i.Matricule :
                print("Formateur existe")
                ref=input("Donner la reférence du Module")
                for j in self.lstM:
                    if ref==j.Ref :
                        print("Module existe")
                        i.listeMod.append(j.Ref)
                        j.For.append(i.Matricule)
    def supprimerL(self):
        ref=str(input("Donner la reférence du Module"))
        mat=int(input("Entrer le matricule de formateur concerné par le module"))
        for i in self.lstM:
            if ref==i.Ref:
                print("Module existe")
                for j in self.lstF:
                    if j.Matricule==mat:
                        print("Formateur existe")
                        for part in i.For:
                            if (part == mat) : 
                                i.For.remove(part)                        
                        for ele in j.listeMod:
                            print(ele,end=" ")
                            if (ele == ref) :
                                j.listeMod.remove(ele)
                                print("Done")
    def supprimer(self):
        print("1- Pour supprimer un Module :\n2- Pour supprimer un Formateur :")
        c=int(input("Entrer votre choix "))
        match c :
            case 1 :
                ref=input("Donner la reférence du Module")
                for i in self.lstM:
                    if ref==i.Ref:
                        for j in self.lstF:
                            for ele in j.listeMod :
                                if ele == ref :
                                    j.listeMod.remove(ele)
                                    print("Module detachee")
                        Centre.lstM.remove(i)
                        print("Module supprimer")
            case 2 :
                mat=int(input("Entrer le matricule de formateur concerné par le module"))
                for i in self.lstF:
                    if i.Matricule==mat:
                        for j in self.lstM:
                            for ele in j.For :
                                if ele == mat :
                                    j.For.remove(ele)
                                    print("Formateur detachee")
                        Centre.lstF.remove(i)
                        print("Formateur supprimer")
            case _ :
                print("Choix invalide")

F1 = Formateur(111,"TATELI","AHMED",12,[])
F2 = Formateur(222,"MEZWAR","HATIM",8,[])
F3 = Formateur(333,"TOUBANI","BADR",13,[])
F4 = Formateur(444,"ELWAZZANI","YAAKOUB",19,[])

M1=Module("M01","Metier et Formation",[])
M2=Module("M02","Programation PYTHON",[])
M3=Module("M03","Les base de donnees",[])
M4=Module("M04","Securite des sys.info",[])
                 
C1=Centre([F1,F2,F3,F4],[M1,M2,M3,M4])

while True:
    print("================Bienvenue=================")
    print("1- Afficher Modules et Formateurs")
    print("2- Ajouter Formateur")
    print("3- Ajouter Module")
    print("4- Affecter Formateur")
    print("5- Affecter Module")
    print("6- Detacher Formateur/Module")
    print("7- Supprimer Module/Formateur")
    print("8- Quitter ")
    ch=int(input("Entrer votre choix ")) 
    match ch:
        case 1:
           C1.afficher()
        case 2:
           C1.AjouterF()
        case 3:
           C1.AjouterM()
        case 4:
           C1.affecterF()
        case 5:
           C1.affecterM()
        case 6:
            C1.supprimerL()
        case 7:
            C1.supprimer()
        case 8:
            break
        case _:
           print("Choix invalide")
        
    
        


        
    
