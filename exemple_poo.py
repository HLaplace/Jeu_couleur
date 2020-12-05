class joueur:

    def __init__(self,name,points_vie,points_attack):
# ici on definit les atributs du joueur
        self.name = name
        self.points_vie = points_vie
        self.points_attack = points_attack # en repetant le nom de ma varaible je defini le fait la valeur sera défini
        # lors de la creation d une instance
        self.points_bouclier = 2 # du coup ici tous les joueurs auront 2 points de bouclier du coup la variable
        # n est pas dans le def

    def attaque(self,victime):
        # ceci est une methode de la class joueur
        print(self.named + " attaque " + victime.name)
        victime.points_vie = victime.points_vie - (self.points_attack - victime.points_bouclier)
        print(str(victime.name) + " a maintenant " + str(victime.points_vie) + " points de vie.")

    def info(self):
        print("")
        print(self.name + ':')
        print("Point de vie : " + str(self.points_vie))
        print("Point attaque : " + str(self.points_attack))
        print("Point de bouclier : " + str(self.points_bouclier))
        print("")

# creation d un role
# dans le cas present le magicien a toute les carateristiques du joueur avec en plus la capacite de soigner
class magicien(joueur):

    def __init__(self,name,points_vie,points_attack):
    
        super().__init__(name,points_vie,points_attack)

        self.soin = 2

    def soigner(self,personne_soigner):
        personne_soigner.points_vie = personne_soigner.points_vie + 2 #self.soin
        print(str(personne_soigner.name) + " a maintenant " + str(personne_soigner.points_vie) + " points de vie.")

#________________________________________main ________________________________________

hugo = magicien('Hugo',20, 5)
dark_vador = joueur('Dark_vador', 14, 6)

hugo.soigner(dark_vador)

