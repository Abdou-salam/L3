# Exemple d'utilisation
import time
import random
#Pour mesurer le temps d'exécution nous avons à notre disposition 
#la fonction perf_counter()
n = 10000000
#Récupération du temps système et démarrage du chronomètre
start_pc = time.perf_counter()
for i in range(n):
 #on ne fait rien…
 None
end_pc = time.perf_counter()
elapsed_time_pc = end_pc-start_pc
print("Temps écoulé entre les deux mesures : ",elapsed_time_pc)
print("Temps estimé pour une instruction",elapsed_time_pc/n)
random.sample
