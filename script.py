"""On souhaite réaliser un script qui permet de pixeliser une image en utilisant la méthode de la moyenne
 des couleurs des pixels voisins. Pour cela, on vous demande de réaliser une fonction
 pixeliser_image(image, taille_pixel) qui prend en paramètre une image et un entier taille_pixel
et qui retourne une nouvelle image pixelisée. La nouvelle image doit être une image de même taille
 que l'image d'origine mais où chaque pixel est la moyenne des couleurs des pixels voisins de
 taille taille_pixel. Par exemple, si taille_pixel vaut 2, alors chaque pixel de la nouvelle
 image est la moyenne des couleurs des pixels voisins de 2x2 pixels. Si taille_pixel vaut 3,
 alors chaque pixel de la nouvelle image est la moyenne des couleurs des pixels voisins de 3x3 pixels.
Si la taille de l'image n'est pas un multiple de taille_pixel, alors on ignore les pixels en trop à droite
 et en bas de l'image. Si la taille de l'image est inférieure à taille_pixel, alors on retourne l'image d'origine. 
 Vous pouvez utiliser la librairie PIL pour manipuler les images. Voici un exemple d'utilisation de la fonction
   pixeliser_image :
"""
from PIL import Image

# def pixeliser_image(image, taille_pixel):
#     largeur, hauteur = image.size
#     nouvelle_image = Image.new("RGB", (largeur, hauteur))
#     for y in range(0, hauteur, taille_pixel):
#         for x in range(0, largeur, taille_pixel):
#             r, g, b = 0, 0, 0
#             n = 0
#             for j in range(taille_pixel):
#                 for i in range(taille_pixel):
#                     if x + i < largeur and y + j < hauteur:
#                         pixel = image.getpixel((x + i, y + j))
#                         r += pixel[0]
#                         g += pixel[1]
#                         b += pixel[2]
#                         n += 1
#             r //= n
#             g //= n
#             b //= n
#             for j in range(taille_pixel):
#                 for i in range(taille_pixel):
#                     if x + i < largeur and y + j < hauteur:
#                         nouvelle_image.putpixel((x + i, y + j), (r, g, b))
#     return nouvelle_image

# image = Image.open("image.jpg")

# nouvelle_image = pixeliser_image(image, 3)
# nouvelle_image.save("image_pixelisee.jpg")
# nouvelle_image.show()

"""On souhaite améliorer la qualité de ce filtre.
Pour cela, on vous demande de réaliser une fonction pixeliser_image_amelioree(image, taille_pixel)
qui prend en paramètre une image et un entier taille_pixel et qui retourne une nouvelle image pixelisée.
La nouvelle image doit être une image de même taille que l'image d'origine mais où chaque pixel est la moyenne
des couleurs des pixels voisins de taille taille_pixel. Pour chaque pixel, on calcule la moyenne des couleurs
des pixels voisins de taille taille_pixel et on calcule la distance entre la couleur du pixel et la moyenne des
couleurs des pixels voisins. On garde la couleur du pixel si la distance est inférieure à un seuil donné en paramètre.
Sinon, on remplace la couleur du pixel par la moyenne des couleurs des pixels voisins. Par exemple, si taille_pixel
vaut 2 et seuil vaut 50, alors chaque pixel de la nouvelle image est la moyenne des couleurs des pixels voisins de 2x2 pixels.
Si la distance entre la couleur du pixel et la moyenne des couleurs des pixels voisins est inférieure à 50, alors on garde la couleur du pixel.
Sinon, on remplace la couleur du pixel par la moyenne des couleurs des pixels voisins. Si taille_pixel vaut 3 et seuil vaut 100,
alors chaque pixel de la nouvelle image est la moyenne des couleurs des pixels voisins de 3x3 pixels. Si la distance entre la couleur du pixel
et la moyenne des couleurs des pixels voisins est inférieure à 100, alors on garde la couleur du pixel. Sinon, on remplace la couleur du pixel
par la moyenne des couleurs des pixels voisins. Si la taille de l'image n'est pas un multiple de taille_pixel, alors on ignore les pixels en trop
à droite et en bas de l'image. Si la taille de l'image est inférieure à taille_pixel, alors on retourne l'image d'origine. Voici un exemple d'utilisation
de la fonction pixeliser_image_amelioree :"""

block=6
nb_couleurs=30
nom_image="A.png"
nom_image_retour="Two_More_Steps.png"
nom_rogne="One_More_Step.png"
image_finale="Finish.png"

def pixeliser_image_amelioree(image, taille_pixel, seuil):
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))
    for y in range(0, hauteur, taille_pixel):
        for x in range(0, largeur, taille_pixel):
            r, g, b = 0, 0, 0
            n = 0
            for j in range(taille_pixel):
                for i in range(taille_pixel):
                    if x + i < largeur and y + j < hauteur:
                        pixel = image.getpixel((x + i, y + j))
                        r += pixel[0]
                        g += pixel[1]
                        b += pixel[2]
                        n += 1
            r //= n
            g //= n
            b //= n
            for j in range(taille_pixel):
                for i in range(taille_pixel):
                    if x + i < largeur and y + j < hauteur:
                        pixel = image.getpixel((x + i, y + j))
                        distance = abs(r - pixel[0]) + abs(g - pixel[1]) + abs(b - pixel[2])
                        if distance < seuil:
                            nouvelle_image.putpixel((x + i, y + j), pixel)
                        else:
                            nouvelle_image.putpixel((x + i, y + j), (r, g, b))
    return nouvelle_image

# image = Image.open("image.jpg")

# nouvelle_image = pixeliser_image_amelioree(image, 20,0)
# # Paramètres à garder : (4,10)
# # Paramètres à garder : (6,20)


# nouvelle_image.save("image_pixelisee_amelioree.jpg")
# nouvelle_image.show()

image2=Image.open(nom_image)

nouvelle_image2 = pixeliser_image_amelioree(image2,block,0)
nouvelle_image2.save(nom_image_retour)
# nouvelle_image2.show()


##### Rogner l'image : #####
def rogner_image(image, taille_pixel):
    largeur, hauteur = image.size
    largeur_nouvelle = largeur - (largeur % taille_pixel)
    hauteur_nouvelle = hauteur - (hauteur % taille_pixel)
    nouvelle_image = image.crop((0, 0, largeur_nouvelle, hauteur_nouvelle))
    return nouvelle_image

image_rognée = rogner_image(nouvelle_image2,block)
image_rognée.save(nom_rogne)
# image_rognée.show()

"""On souhaite créer une palette de couleurs pour générer une image avec moins de couleurs.
On créé une fonction 
creer_palette(image, n) qui prend en paramètre une image et un entier n et qui retourne une liste de n couleurs.
Pour cela, on utilise l'algorithme de k-means pour regrouper les couleurs de l'image en n groupes.
On initialise les n groupes avec n couleurs aléatoires de l'image. On attribue chaque pixel de l'image
au groupe dont la couleur est la plus proche. On met à jour les couleurs des groupes en calculant la
moyenne des couleurs des pixels du groupe. On répète cette étape jusqu'à convergence. Voici un exemple
d'utilisation de la fonction creer_palette :"""

from random import randint

def creer_palette(image, n):
    largeur, hauteur = image.size
    couleurs = []
    for i in range(n):
        x = randint(0, largeur - 1)
        y = randint(0, hauteur - 1)
        couleurs.append(image.getpixel((x, y)))
    while True:
        groupes = [[] for _ in range(n)]
        for y in range(hauteur):
            for x in range(largeur):
                pixel = image.getpixel((x, y))
                distance_min = 256 * 3
                groupe_min = 0
                for i in range(n):
                    distance = abs(couleurs[i][0] - pixel[0]) + abs(couleurs[i][1] - pixel[1]) + abs(couleurs[i][2] - pixel[2])
                    if distance < distance_min:
                        distance_min = distance
                        groupe_min = i
                groupes[groupe_min].append(pixel)
        nouvelles_couleurs = []
        for i in range(n):
            r, g, b = 0, 0, 0
            for pixel in groupes[i]:
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
            if len(groupes[i]) > 0:
                r //= len(groupes[i])
                g //= len(groupes[i])
                b //= len(groupes[i])
            nouvelles_couleurs.append((r, g, b))
        if nouvelles_couleurs == couleurs:
            break
        couleurs = nouvelles_couleurs
    return couleurs

# image = Image.open("image.jpg")

# couleurs = creer_palette(image, 10)
# print(couleurs)

"""On souhaite créer une image avec moins de couleurs en utilisant une palette de couleurs.
On créé une fonction generer_image(image, couleurs) qui prend en paramètre une image et une liste de couleurs
et qui retourne une nouvelle image avec les couleurs de la palette. Pour chaque pixel de l'image, on remplace
la couleur du pixel par la couleur de la palette la plus proche. Voici un exemple d'utilisation de la fonction
generer_image :"""

def generer_image(image, couleurs):
    largeur, hauteur = image.size
    nouvelle_image = Image.new("RGB", (largeur, hauteur))
    for y in range(hauteur):
        for x in range(largeur):
            pixel = image.getpixel((x, y))
            distance_min = 256 * 3
            couleur_min = (0, 0, 0)
            for couleur in couleurs:
                distance = abs(couleur[0] - pixel[0]) + abs(couleur[1] - pixel[1]) + abs(couleur[2] - pixel[2])
                if distance < distance_min:
                    distance_min = distance
                    couleur_min = couleur
            nouvelle_image.putpixel((x, y), couleur_min)
    return nouvelle_image

couleurs = creer_palette(image_rognée, nb_couleurs)
nouvelle_image = generer_image(image_rognée, couleurs)
nouvelle_image.save(image_finale)
nouvelle_image.show()



