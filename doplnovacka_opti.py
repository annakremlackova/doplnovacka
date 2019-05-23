"""
Proveďte optimalizaci kódu programu "doplnovacka.py" tak,
abys problém řešila s využitím vlastní funkce (vstupními
parametry bude vložený text či název souboru, který se má
načíst, a celé číslo představující, kolikáté slovo textu se
má zaměnit za hvězdičky). Tuto optimalizovanou verzi nahraj
do existujícího projektu na GitHubu. 
"""

s = 0

def funkce (soubor, n):

	with open(soubor) as f:
		text = f.read()
	f.closed
	text = text.replace("  ", " ")
	text = text.replace("\n", "# ")

	seznam = []
	seznam = text.split(" ")
	vysledek = []
	interpunkce = ".,?!-;\""

	for i in range(0, len(seznam)):
		slovo = seznam[i]
		slovoUpraveno = ""
		if ((i + 1) % n == 0):
			for pismeno in slovo:
				if pismeno not in interpunkce:
					slovoUpraveno += "*"
				else:
					slovoUpraveno += pismeno
			vysledek.append(slovoUpraveno)
		else:
			vysledek.append(slovo)

	s = " ".join(vysledek)
	s = s.replace("#", "\n")
	print(s)



n = int(input("Kolikáte slovo mám změnit na hvězdičky? "))
soubor = input("Jaký soubor mám načíst?")
funkce (soubor, n)
