# Zapiski delavnice "Programiranje v Pythonu in uporaba ukazne vrstice"

### Predviden urnik


**Osnove Pythona, delo z datotekami** (ponedeljek, 7. maj, 2018)

- Jupyter notebook in markdown
- Osnove Pythona: izrazi, pogoji, zanke
- Branje in pisanje datotek


**Podatkovne strukture in moduli v Pythonu** (torek, 8. maj, 2018)

- Podatkovne strukture: objekt, slovar, množica
- Definiranje funkcij


**Uporaba ukazne vrstice Linux** (ponedeljek, 14. maj, 2018)

- Osnove datotečne strukture
- Poganjanja programov
- Preusmerjanja vhoda in izhoda ter gradnja procesnih cevovodov


**Procesiranje bioloških podatkov v Pythonu** (sreda, 16. maj, 2018)

- Priprava datotek FASTA, FASTQ, …
- Uporaba modulov v Pythonu
- Branje, procesiranje in zapisovanje datotek v Biopython
- Osnovne analize zaporedij v Biopython



### Poganjanje Jupyter z uporabo Docker


Jupyter lahko poženemo z uporabo programa Docker. V spodnjem besedilu del '/pot/do/skript/na/disku' nadomestite s pravo potjo:

    docker run -it --rm -p 8888:8888 -v /pot/do/skript/na/disku:/home/jovyan/work jupyter/minimal-notebook

Za uporabnike Windows: Navodila najdete na [povezavi](https://docs.docker.com/docker-for-windows/). V primeru,
da se nahajate v delovni mapi, lahko trenutno pot pridobite avtomatično. V PowerShell poženite:

    docker run -it --rm -p 8888:8888 -v ${pwd}:/home/jovyan/work jupyter/minimal-notebook

