# Zapiski delavnice "Programiranje v Pythonu (in uporaba ukazne vrstice)"

### Predviden urnik

**Osnove Pythona, delo z datotekami** (ponedeljek, 6. maj 2024 ob 15.15)

- Jupyter notebook in markdown
- Osnove Pythona: izrazi, pogoji, zanke
- Branje in pisanje datotek


**Podatkovne strukture in moduli v Pythonu** (torek, 7. maj, 2024 ob 16.00)

- Podatkovne strukture: objekt, slovar, množica
- Definiranje funkcij


### Ostale teme

**Procesiranje bioloških podatkov v Pythonu** (torek, 14. maj 2024 ob 16.00)

- Priprava datotek FASTA, FASTQ, …
- Uporaba modulov v Pythonu
- Branje, procesiranje in zapisovanje datotek v Biopython
- Osnovne analize zaporedij v Biopython


**Uporaba ukazne vrstice Linux** (???)

- Osnove datotečne strukture
- Poganjanja programov
- Preusmerjanja vhoda in izhoda ter gradnja procesnih cevovodov


## Programersko okolje


### Opcija 1: Namestitev Pythona in knjižnic na svoj računalnik

Conda je program za nameščanje Pythona in dodatnih knjižnic zanj ter za ustvarjanje navideznih okolij. Pri tem predmetu ne potrebujemo Anaconde, temveč bo zadoščala Miniconda.

Najprej namestimo [minicondo](https://docs.conda.io/en/latest/miniconda.html).

Odpremo ukazno vrstico (shell, term, cmd, v Windows pa vam bo za tole najboljše služil Anaconda Prompt).

Sestavimo novo navidezno okolje (zamenjajte `ime` z imenom, ki vam bo kaj povedalo):

```
conda create -n ime
```

(Na MS Windows utegnete imeti težave s šumniki v imenih poti -- conda bo slabo delovala, če bo postavljala okolje v mapo `c:\Users\ŠtefanČiželj\miniconda\envs\prog`. V primeru težav poskusite `conda create -p c:\mojiProgrami\ime` ali kaj takega, pri čemer prej naredite mapo c:\mojiProgrami).

Nato aktiviramo novo okolje s `conda activate ime` (ali `conda activate c:\mojiProgrami\ime`, če ste Štefan Čiželj).

Potem namestimo v to okolje python in vse drugo, kar bi še potrebovali.

```
conda install python jupyter
```

Kasneje lahko dodajamo nove stvari; primeri so spodaj.

Za naslednja poganjanja moramo odpreti ukazni pozivnik (npr. Anaconda prompt na Windows) in napisati

```
conda activate ime
jupyter notebook
```


### Opcija 2: Namestitev okolja Docker na osebni računalnik

Jupyter lahko poženemo z uporabo programa Docker. Najprej namestimo program `docker`. Nato v ukazni vrstici poženemo naslednje ('/pot/do/skript/na/disku' nadomestite s pravo potjo):

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

### Opcija 3: Spletno okolje

Okolje lahko poženete v spletni storitvi *mybinder.org*:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/janezd/bio-python-ukazna/HEAD?urlpath=/tree/) - osnovna uporaba

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/janezd/bio-python-ukazna/master?urlpath=lab) - dostop do ukazne vrstice Linux (terminal)

**Vse spremembe datotek bodo izgubljene, ko poteče seja** (to je, največ 12 ur, oziroma največ 10 minut, ko zaprete še zadnje okno v brskalniku  z *mybinder.org*). Datoteko lahko prenesete na računalnik tako, da izberete menu "File -> Download as -> Notebook (.ipynb)." Drugi način je, da v oknu "Home" izberete eno datoteko in nato pritisnete gumb "Download." Možno je tudi naložiti datoteke na spletni strežnik (v oknu "Home", gumb "Upload").

Poganjati je možno tudi v Googlovem [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/janezd/bio-python-ukazna).

### Pretvorba jupyter notebooka v navadno skripto python

Če želimo zvezek (notebook) poganjati v ukazni vrstici, jo je potrebno najprej pretvoriti v navadno skripto Python:

    $ jupyter nbconvert --to=python skripta.ipynb

Nato jo lahko poženemo v ukazni vrstici:

    $ python skripta.py


### Namestitev biopython

Modul [biopython](http://biopython.org/wiki/Download) namestimo v anacondi. Še prej moramo namestiti nekaj dodatnih modulov:

    conda install cycler
    conda install matplotlib
    conda install reportlab
    conda install biopython

V primeru težav lahko za 64 bitno verzijo Pythona namestite modul tako, da sledite navodilom [na strani](http://www.lfd.uci.edu/%7Egohlke/pythonlibs/) in namestite paket, recimo *biopython‑1.79‑cp39‑cp39‑win32.whl*.


## Povezave za vajo in poglabljanje

- [Zbirka nalog](https://ucilnica.fri.uni-lj.si/mod/resource/view.php?id=7614) (vstopite lahko kot gost). Po prvih predavanjih so primerne naloge iz prvih dveh poglavij. Po drugih bodo vse do rekurzije; s to se ne bomo ukvarjali, ker je ne boste potrebovali.

- [Stran predmeta Programiranje 1 na FRI](https://ucilnica.fri.uni-lj.si/course/view.php?id=166). Na njej so obširnejši zapiski od teh tule (čeprav so, kot boste videli, v žlahti), predvsem pa so tam kupi in kupi nalog. Nekatere so v zbirki, veliko pa je dodatnih.

Vse naloge spremljajo rešitve. Vendar jih ne glejte, dokler naloge sami ne rešite!
