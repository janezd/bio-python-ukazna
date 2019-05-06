# Zapiski delavnice "Programiranje v Pythonu in uporaba ukazne vrstice"

### Predviden urnik

**Osnove Pythona, delo z datotekami** (torek, 7. maj, 2019)

- Jupyter notebook in markdown
- Osnove Pythona: izrazi, pogoji, zanke
- Branje in pisanje datotek


**Podatkovne strukture in moduli v Pythonu** (sreda, 8. maj, 2019)

- Podatkovne strukture: objekt, slovar, množica
- Definiranje funkcij


**Uporaba ukazne vrstice Linux** (ponedeljek, 13. maj, 2019)

- Osnove datotečne strukture
- Poganjanja programov
- Preusmerjanja vhoda in izhoda ter gradnja procesnih cevovodov


**Procesiranje bioloških podatkov v Pythonu** (sreda, 15. maj, 2019)

- Priprava datotek FASTA, FASTQ, …
- Uporaba modulov v Pythonu
- Branje, procesiranje in zapisovanje datotek v Biopython
- Osnovne analize zaporedij v Biopython


### Poganjanje preko spleta

Okolje lahko poženete v spletni storitvi *mybinder.org*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/janezd/bio-python-ukazna/master) - osnovna uporaba

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/janezd/bio-python-ukazna/master?urlpath=lab) - dostop do ukazne vrstice Linux (terminal)

Vse spremembe datotek bodo izgubljene, ko poteče seja (to je, največ 12 ur, oziroma največ 10 minut, ko zaprete še zadnje okno v brskalniku  z *mybinder.org*). Datoteko lahko prenesete na računalnik tako, da izberete menu "File -> Download as -> Notebook (.ipynb)." Drugi način je, da v oknu "Home" izberete eno datoteko in nato pritisnete gumb "Download." Možno je tudi naložiti datoteke na spletni strežnik (v oknu "Home", gumb "Upload").


### Namestitev okolja na osebni računalnik

Jupyter lahko poženemo z uporabo programa Docker. V spodnjem besedilu del '/pot/do/skript/na/disku' nadomestite s pravo potjo:

    docker run -it --rm -p 8888:8888 -v /pot/do/skript/na/disku:/home/jovyan/work jupyter/minimal-notebook

Za uporabnike Windows: Navodila najdete na [povezavi](https://docs.docker.com/docker-for-windows/). V primeru,
da se nahajate v delovni mapi, lahko trenutno pot pridobite avtomatično. V PowerShell poženite:

    docker run -it --rm -p 8888:8888 -v ${pwd}:/home/jovyan/work jupyter/minimal-notebook

Če se želimo z ukazno vrstico povezati, moramo najprej ugotoviti ID instance:

    $ docker ps
    CONTAINER ID        IMAGE                      COMMAND                  CREATED              STATUS              PORTS                    NAMES
    4d6a546ca880        jupyter/minimal-notebook   "tini -- start-noteb…"   About a minute ago   Up About a minute   0.0.0.0:8888->8888/tcp   eloquent_goodall

Nato izvedemo ukaz, kjer podamo ID:

    $ docker exec -i -t 4d6a546ca880 /bin/bash

Zdaj se nahajamo v ukazni vrstici Linux.


#### Pretvorba jupyter notebooka v navadno skripto python

Če želimo zvezek (notebook) poganjati v ukazni vrstici, jo je potrebno najprej pretvoriti v navadno skripto Python:

    $ jupyter nbconvert --to=python skripta.ipynb

Nato jo lahko poženemo v ukazni vrstici:

    $ python skripta.py


### Namestitev biopython

Modul [biopython](http://biopython.org/wiki/Download) namestimo v anacondi. Še prej je potrebno namestiti nekaj dodatnih modulov:

    conda install cycler
    conda install matplotlib
    conda install reportlab
    conda install biopython

V primeru težav lahko za 64 bitno verzijo Pythona namestite modul tako, da sledite navodilom [na strani](http://www.lfd.uci.edu/%7Egohlke/pythonlibs/) in namestite paket, recimo *biopython‑1.73‑cp37‑cp37m‑win32.whl*.


### Povezave za vajo in poglabljanje

- [Zbirka nalog](https://ucilnica.fri.uni-lj.si/mod/resource/view.php?id=7614). Po prvih predavanjih so primerne naloge iz prvih dveh poglavij. Po drugih bodo vse do rekurzije; s to se ne bomo ukvarjali, ker je ne boste potrebovali.

- [Stran predmeta Programiranje 1 na FRI](https://ucilnica.fri.uni-lj.si/course/view.php?id=166). Na njej so obširnejši zapiski od teh tule (čeprav so, kot boste videli, v žlahti), predvsem pa so tam kupi in kupi nalog. Nekatere so v zbirki, veliko pa je dodatnih.

Vse naloge spremljajo rešitve. Vendar jih ne glejte, dokler naloge sami ne rešite!
