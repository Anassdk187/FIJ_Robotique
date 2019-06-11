import ledArduino
import dicoMatrice2D
import comMorse

print("tape un code morse")
lettre = input()
reponseMorse = comMorse.encode(lettre)
print("le code morse est :",reponseMorse)

reponse = comMorse.decode(reponseMorse)
ledArduino.envoiCaractere(reponse)