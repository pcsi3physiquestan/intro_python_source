import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd

# L1 = np.arange(0, 4)
# L2 = L1 * L1
# L3 = np.ones(4)

# """
# Ci-dessous : une méthode pour créer un tableau à partir de 3 vecteurs de même taille.
# Les L1, L2, L3 sont les lignes du tableau.
# """
# M1 = np.array([L1, L2, L3])

# print("Cas 1 :", M1)
# print("Cas 2 :", M1[2, 3])
# print("Cas 3 :", M1[-1, 2])
# print("Cas 4 :", M1[1])
# print("Cas 5 :", M1[2, :])
# print("Cas 6 :", M1[:, -1])
# print("Cas 7 :", M1[:, -2])
# print("Cas 8 :", M1[1:2, 0:1])
# print("Cas 9 :", M1[:-1, 1])  # Un peu plus compliqué...
# print("Cas 10 :", M1[-3:-1, -3:3])  # On se concentre bien...

# L1 = np.array([1, 2, 3])
# L2 = np.array([1, 2])

# f, ax = plt.subplots()
# ax.plot(L1, L2)

# u1 = 1
# u2 = 0.1
# v1 = 15
# v2 = 14
# a = v1 / v2
# ua = a * np.sqrt((u1 / v1) ** 2 + (u2 / v2) ** 2



# print(ua)

# a = {'fruit': "Pomme", 'couleur': "Rouge", 'nombre': 234, 'prix': 3.45}

# print(a['fruit'])  # Pour afficher le contenu du champ "fruit" du dictionnaire a

# for champ in a:
#   print(champ)


# def fonction_morceau(x):
#   if x < 3:  # Si x < 3
#     a = x - 4
#   elif x < 5:  # Si 3 <= x < 5
#     a = x ** 2
#   else:  # Si x >=5
#     b = x + 4
#     a = b ** 3
#   return a

# x = np.linspace(0, 15, 1000)

# y = [fonction_morceau(i) for i in x]

# plt.plot(x, y)
# plt.show()

# N = 1000000  # Nombre de tirages
# u_min = [1, 5, 10]  # 3 valeurs minimales des 3 distributions uniformes
# u_max = [3, 7, 12]  # 3 valeurs amximales des 3 distributions uniformes

# k = len(u_min)

# u_sims = rd.uniform(u_min, u_max, (N, k))  # On demande explicite un tableau de taille N*k

# X1 = u_sims[:, 0]  # Simulation des u1
# X2 = u_sims[:, 1]  # Simulation des u2
# X3 = u_sims[:, 2]  # Simulation des u3

# f, ax = plt.subplots()
# ax.hist(X1, bins='rice', color='r', label='Entre 1 et 3')
# ax.hist(X2, bins='rice', color='b', label='Entre 5 et 7')
# ax.hist(X3, bins='rice', color='k', label='Entre 10 et 12')
# ax.legend()
# plt.show()

# N = 1000000  # Nombre de tirages
# u_mean = [1, 5, 15]  # 3 valeurs minimales des 3 distributions uniformes
# u_u = [1, 2, 3]  # 3 valeurs amximales des 3 distributions uniformes

# k = len(u_min)

# u_sims = rd.normal(u_mean, u_u, (N, k))  # On demande explicite un tableau de taille N*k

# X1 = u_sims[:, 0]  # Simulation des u1
# X2 = u_sims[:, 1]  # Simulation des u2
# X3 = u_sims[:, 2]  # Simulation des u3

# f, ax = plt.subplots()
# ax.hist(X1, bins='rice', color='r', label='m=1, s=1')
# ax.hist(X2, bins='rice', color='b', label='m=5, s=2')
# ax.hist(X3, bins='rice', color='k', label='m=15, s=3')
# ax.legend()
# plt.show()

# xi = np.array([0.2, 0.8, 1.6, 3.4, 4.5, 7.5])
# yi = [2 * x + 4 + rd.normal(0, x / 5) for x in xi]

# print(np.round(yi, 1))

# liste = [1,5,10,15,20,25]
# for i in liste:
#   if i >15 :
#     break
#     print("boucle arrêtée")
#   print(i)


# def somme_carre(n):
#   S = 0
#   for i in range(n):
#     S = S + i**2
#   return S

# print(somme_carre(5))
# L = []
# if not len(L) < 3:
#   print("La longueur de la liste est inférieure à 3")
# else:
#   print("La longueur de la liste est supérieure à 3")


# print(type(range(3)))

# def somme_carre(n):
#   s = 0
#   for i in range(1, n+1):
#     s += i
#   return s

# print("n=0 : ", somme_carre(0))
# print("n=1 : ", somme_carre(1))
# print("n=2 : ", somme_carre(2))
# print("n=5 : ", somme_carre(5))
# print("n=100 : ", somme_carre(100))

# def somme_carre2(n):
#   s = 0
#   i = 0
#   while i <= n:
#     s += i
#     i += 1
#   return s

# print("n=0 : ", somme_carre(0))
# print("n=1 : ", somme_carre(1))
# print("n=2 : ", somme_carre(2))
# print("n=5 : ", somme_carre(5))
# print("n=100 : ", somme_carre(100))


# def somme_ks(n):
#   s = 0
#   i = 0
#   while i + i**2 + i**3 <= n:
#     s += i
#     i += 1
#   return s

# print("n=0 : ", somme_ks(0))
# print("n=1 : ", somme_ks(2))
# print("n=2 : ", somme_ks(5))
# print("n=5 : ", somme_ks(100))
# print("n=100 : ", somme_ks(2000))

# def getDiv(n):
#     # Fonction qui renvoir tout les diviseurs d'un nombre n.
#     L = []
#     for i in range(1, n +1):
#         if n % i == 0:
#             L += [i]
#     return L

# print("n=1 : ", getDiv(1))
# print("n=4 : ", getDiv(4))
# print("n=24 : ", getDiv(24))
# print("n=47: ", getDiv(47))
# print("n=254 : ", getDiv(254))

# k = 11
# m = 0.3
# X0 = 0.1
# l0 = 0.06
# w0 = np.sqrt(11 / 0.3)

# def xM(x):
#   return (X0 - l0) * np.cos(w0 * x) + l0

# def vM(x):
#   return - w0 *(X0 - l0) * np.sin(w0 * x)


# temps = np.linspace(0, 6 * np.pi / w0, 300)
# xMt = xM(temps)
# vMt = vM(temps)
# Ep = 1 / 2 * k * xMt ** 2
# Ec = 1 / 2 * m * vMt ** 2

# f, ax = plt.subplots()
# f.suptitle("Oscillateur harmonique")

# ax.set_xlabel("t(s)")
# ax.set_ylabel("Position(m)")

# ax.plot(temps, xMt, color='red', label='xM(t)')

# ax.legend()

# f, ax = plt.subplots()
# f.suptitle("Oscillateur harmonique")

# ax.set_xlabel("t(s)")
# ax.set_ylabel("Vitesse(m/s)")

# ax.plot(temps, vMt, color='red', label='vM(t)')

# ax.legend()


# f, ax = plt.subplots()
# f.suptitle("Oscillateur harmonique")

# ax.set_xlabel("t(s)")
# ax.set_ylabel("Energie potentielle(J)")

# ax.plot(temps, Ep, color='red', label='Ep(t)')

# ax.legend()

# f, ax = plt.subplots()
# f.suptitle("Oscillateur harmonique")

# ax.set_xlabel("t(s)")
# ax.set_ylabel("Energie cinétique(J)")

# ax.plot(temps, Ec, color='red', label='Ec(t)')

# ax.legend()

# plt.show()

# nom_fichier = "Sf6/sf6.dat"  # Bien penser aux "" car ce doit être une chaine de caractère

# """Importation complète sous forme de tableau"""
# datas1 = np.loadtxt(nom_fichier, skiprows=7, delimiter=',')  # Il y a bien 6 lignes de commentaires et une ligne de titre.
# print(datas1)  # Le tableau étant volumineux, Python n'en affiche qu'une partie.
# print(datas1[:, 0])  # On peut extraire une colonne, ici la colonne des températures.


# """Importation complète avec un vecteur par colonne"""
# T, P, V, Etat = np.loadtxt(nom_fichier, skiprows=7, unpack=True, delimiter=',')  # On récupère ainsi des vecteurs séparés
# print(P)  # Vecteur des données de Pression en bar


# """Importation partielle d'une colonne
# Il est déconseillé, pour des raison d'efficacité d'importer une à une les colonnes si vous les voulez toutes.
# """
# V1 = np.loadtxt(nom_fichier, skiprows=7, usecols=2, delimiter=',')  # On importe la colonne d'indice 2, soit les volumes
# print(V1)  # Vecteur de données de Volume en m^3

# temps, ucb = np.loadtxt('Sf6/circuit_rc.dat', skiprows=7, delimiter=";", unpack=True)  # Importation des données

# def bin_to_volt(u):
#   """Fonction qui transforme une valeur 0-255 en valeur de tension."""
#   B_MAX = 1023
#   U_MAX = 5
#   B_MIN = 0
#   U_MIN = 0
#   tension = (u - B_MIN) / (B_MAX - B_MIN) * (U_MAX - U_MIN) + U_MIN
#   return tension

# uc = bin_to_volt(ucb)


# """Tracé de uc(t)"""
# f, ax = plt.subplots()
# f.suptitle("Etude de la décharge d'un RC")
# ax.set_xlabel('t(microsecondes)')
# ax.set_ylabel('uc(V)')

# ax.plot(temps, uc, label='uc(t)')

# ax.legend()
# plt.show()

# """Détermination de tau"""
# U0 = uc[0]  # Tension initiale
# i = 0
# while uc[i] > 0.37 * U0 and i < len(uc):  # Test des 37%
#     i = i + 1
# print(temps[i])  # Temps juste avant d'invalider la condition
# print(temps[i+1])  # Temps juste après invalidation

# tau = (temps[i] + temps[i+1]) / 2  # On prend la moyenne des deux
# R = 1e5  # Valeur de R
# C = tau / R / 1e6  # (tau était en microsecondes)

# print("Valeur estimée de tau :", tau)
# print("Valeur estimée de C :", C)
# print("Tous les chiffres ne sont pas significatifs...")

# taus = np.loadtxt('Sf6/circuit_rc_auto.dat', skiprows=7, delimiter=",")  # Importation des données


# print("Nombre de mesures :", len(taus))

# f, ax = plt.subplots()
# f.suptitle("Etude de la décharge d'un RC")
# ax.set_xlabel('tau(microsecondes)')
# ax.set_ylabel('Fréquence')

# ax.hist(taus, bins='rice')

# plt.show()

# """Calcul de la moyenne et écart-type"""
# tau_m = np.mean(taus)
# tau_u = np.std(taus, ddof=1)

# print("Tau moyen : ", tau_m)
# print("Ecart-type : ", tau_u)
# print("Tous les chiffres ne sont pas forcément significatifs...")


# import pandas as pd

# Vi = np.array([1, 2.50, 5.00, 7.50, 10.00])
# Ai = np.array([0.138, 0.428, 0.813, 1.367, 1.765])

# donnees = pd.DataFrame(
#     {
#         "Vi(mL)": ["{:.2f}".format(val) for val in Vi],
#         "A(SI)": ["{:.2f}".format(val) for val in Ai],
#     }
# )

# donnees.style

# """Les bibliothèques ont déjà été importées"""
# Vi = np.array([1, 2.50, 5.00, 7.50, 10.00])
# Ai = np.array([0.128, 0.428, 0.833, 1.267, 1.765])

# Vt = 10  # V_T en mL
# C0 = 2.04  # On n'introduit pas la puissance 10^-5
# u1 = 0.1  # Incertitude sur les volumes en mL

# """Calcul des Ci et uCi. On utilise la vectorialisation des vecteurs numpy"""
# Ci = C0 * Vi / Vt  # Calcul des Ci, on n'introduit pas la puissance 10^-5
# uCi = C0 * u1 / Vt * np.sqrt(1 + (Ci / C0) ** 2)  # Calcul des uCi


# """Tracé des points de mesures"""
# f, ax = plt.subplots()
# f.suptitle("Dosage par absorbance")
# ax.set_xlabel("Absorbance à 640nm (SI)")
# ax.set_ylabel("Concentration (10^-5 mol/L)")

# """Version basique"""
# # ax.errorbar(Ai, Ci, yerr=uCi, label="Points de mesure", linestyle='', color='red', linewidth=1)

# """Version plus esthétique
# capsize rajoute les traits haut et bas"""
# ax.errorbar(Ai, Ci, yerr=uCi, label="Points de mesure", linestyle='', color='red', linewidth=1, capsize=1)


# ax.legend()

# # plt.show()

# print("Le tracé précédent rend l'hypothèse linéaire possible.")
# print("On réalise donc l'ajustement.")

# p = np.polyfit(Ai, Ci, 1)  # Réalisation de l'ajustement affine

# print("-------------------")
# print("Le modèle ajusté a pour équation :")
# print(str(p[0]) + " * A " + str(p[1]))
# print("-------------------")

# Ci_adj = p[0] * Ai + p[1]  # On calcule les valeurs ajustées des concentrations.

# ax.plot(Ai, Ci_adj, label="Modèle ajusté", linestyle=':', color='blue')

# ax.legend()  # Il faut réafficher la légende car on l'a modifiée


# f  # Inutile sauf avec un notebook Jupyter
# plt.show()

# Af = 0.665
# Cf = p[0] * Af + p[1]  # Concentration en bleu patenté dans la solution diluée

# Vf = 50e-3  # Volume de la solution diluée (en L)
# M = 582.66e-3  # Masse molaire du bleu patenté (en kg)
# """Pour calculer la masse, on oublier la puissance 10^-5 dans la concentration"""
# mf = Cf * 1e-5 * Vf * M  # Calcul de la masse de bleu patenté dans un bonbon (en kg)


# Mh = 70  # On choisit un humain de 70kg
# m_DJA = 2.5e-6  # DJA donnée par l'énoncé
# m_max = Mh * m_DJA  # Masse maximale de bleu patenté qu'on peut ingérer
# N_max = m_max / mf

# print("---------------")
# print("Le nombre maximal de bonbons qu'on peut manger est :")
# print(N_max)
# print("---------------")


"""Les bibliothèques scientifiques ont déjà été chargées"""

donnees = np.loadtxt('Sf6/vitesse_son_2.dat', skiprows=10, delimiter=",")
distances = donnees[:, 0]  # Liste des distances.

"""Tracé des histogrammes"""
# f, ax = plt.subplots()
# f.suptitle("Analyse des données expérimentales")
# ax.set_xlabel("Temps de vol (ms)")

# for data in donnees:
#     d = data[0]  # Distance d'étude
#     tps = data[1:]  # Les temps de vol
#     ax.hist(tps, bins='rice', label="D = " + str(d) + " cm")  # Tracé de l'histogramme. Observer l'ajout de la légende.

# ax.legend()

# plt.show()


# def selection(u):
#     """Fonction qui sélectionne les valeurs acceptables du vecteur u"""
#     um = np.mean(u)  # Calcul de la moyenne
#     uu = np.std(u, ddof=1)  # Calcul de l'écart-type

#     """Important : On ne connait pas quelle va être la taille de u_sel.
#     L'usage d'un vecteur numpy est donc déconseillé. On va créer une liste classique
#     qu'on transformera à la fin en vecteur numpy.
#     """
#     u_sel = []  # Liste où l'on va stocker les valeurs sélectionnées.
#     for val in u:  # On parcourt les valeurs de la liste.
#         if np.abs(val - um) <= 2 * uu:  # Test d'écart à la valeur moyenne
#             u_sel.append(val)  # On ajoute la valeur
#     return np.array(u_sel)  # On transforme u_sel en vecteur numpy


# """Détermination des valeurs de c"""
# cs = []  # Liste pour les célérités
# for data in donnees:
#     d = data[0]  # Distance
#     t_sel = selection(data[1:])  # Sélection des valeurs acceptables
#     t_moy = np.mean(t_sel)
#     c = 2 * d / t_moy
#     cs.append(c)

# cs = np.array(cs) / 100 * 1000000 # On passe à des m/s

# f, ax = plt.subplots()
# f.suptitle("Valeurs de célérité estimée")
# ax.set_xlabel("d(cm)")
# ax.set_ylabel("c(m/s)")

# ax.plot(distances, cs, label="Célérité", marker='+', linestyle='')  # On ne relie pas les points.

# plt.show()

# print("On observe des valeurs entre 345m/s et 350m/s soit des valeurs peu dispersées.")

# celerite = np.mean(cs)

# print("---------")
# print("Valeur estimée de la célérité :")
# print(str(celerite) + "m/s")
# print("---------")


