from pathlib import Path


# base = Path.home()
# print(base)

guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
# guia2 = guia.with_name("La_Pedrera.txt")
# print(guia2)
print(guia)
print(guia.parent)
print(guia.parent.parent)
print(guia.parent.parent.parent)


guia3 = Path("Europa")
for txt in Path(guia3).glob("**/*.txt"):
    print(txt)

guia4 = Path("Europa", "España", "Barcelona")
en_europa = guia4.relative_to(Path("Europa"))
print(en_europa)
