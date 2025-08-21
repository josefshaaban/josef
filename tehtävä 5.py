leiviska = int(input("Anna leiviskät: "))
naula = int(input("Anna naulat: "))
luoti = int(input("Anna luodit: "))

luodit_yht = leiviska * 20 * 32 + naula * 32 + luoti

grammat = luodit_yht * 13.3

kilogrammat = int(grammat // 1000)
grammat_jaljella = grammat % 1000

print("Massa nykymittojen mukaan on:", kilogrammat, "kilogrammaa ja", round(grammat_jaljella, 2), "grammaa")