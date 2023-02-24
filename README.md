# mise_en_route.py

Ce document est destiné aux utilisateurs du programme `mise_en_route.py`.
C'est un programme très utile qui permet d'afficher quatre colonnes de nombres :

- La première affiche les dix premiers nombres entiers commençant par 1.
- La seconde affiche les dix premiers carrés de nombres entiers commençant par 1.
- La troisème affiche la somme des carrés précédents.
- La dernière affiche la même chose que la troisième, ce qui est utile pour plein d'applications que nous n'avons pas la place de citer ici (Nous savons par exemple que l'UCL l'utilise pour ses algorithmes avancés de détection de triche).

## Dépendances

`mise_en_route.py` requiert une installation de Python 3.
Pour l'installer, débrouillez-vous.

## Installation

Sur les machines similaires à ou basées sur Unix (Linux, macOS, *BSD, &c), vous pouvez installer `mise_en_route.py` en le rendant d'abord exécutable, et puis en le déplaçant dans un dossier appartenant à `$PATH` (e.g., `/usr/local/bin/`) :

```sh
% chmod +x src/mise_en_route.py
% cp src/mise_en_route.py /usr/local/bin/
```

Si vous utilisez Windows, n'utilisez pas Windows.

## Contributions

La contribution est le fondement des projets FOSS.
`mise_en_route.py` n'en serait pas là où il en est sans les contributions de sa communauté, et pour celà, on vous remercie.

Un repository git est mis en place sur GitHub en privé sur [obiwac/mise_en_route.py](https://github.com/obiwac/mise_en_route.py). Vous pouvez demander l'accès en envoyant un e-mail à l'adresse obiwac@gmail.com, avec le titre "Demande d'accès à `mise_en_route.py`", et le format suivant :

```
Bonjour,

Je souhaiterais contribuer au projet `mise_en_route.py`.
Je demande donc l'accès au repository git hébergé sur GitHub sur https://github.com/obiwac/mise_en_route.py
Mon identifiant sur GitHub est : <VOTRE IDENTIFIANT GITHUB>

Merci.
```

Notre équipe 24h/24 se fera un plaisir de répondre à votre demande dans les plus brefs délais.
Si celà vous convient mieux, nous avons également un service de support sur Discord au travers l'utilisateur obiwac#7599.
Une fois que vous avez l'accès, mettez en place l'authentification SSH sur GitHub (ce qui est nécessaire pour contribuer à des repositories privées), et clonez le repository :

```sh
% git clone ssh://git@github.com/obiwac/mise_en_route.py
% cd mise_en_route.py/
```

Vous pouvez ensuite créer une nouvelle branche (avec un nom sensible) avant d'effectuer vos changements :

```sh
% git checkout -b <LE NOM DE VOTRE NOUVELLE BRANCHE>
```

Une fois que vous avez terminé vos changements, vous pouvez les commit avec :

```sh
% git add .
% git commit -m "<LE NOM DE VOTRE COMMIT>"
% git push origin <LE NOM DE VOTRE BRANCHE>
```

Notre équipe de première-classe viendra donc vérifier les changements et les merge si jugés adéquats.

## Intégration continue

*Cette section n'est seulement valide pour ceux qui ont l'accès au repository GitHub.*
*Si vous avez envie d'intégrer le repository ~~et je vous assure, vous en avez envie~~, veuillez vous référer à la section "Contributions".*

`mise_en_route.py` vise à être un programme stable et fiable, donc, contrairement à [Google](https://static.googleusercontent.com/media/www.google.com/en//appsstatus/dashboard/ir/fw6156fs1panucr.pdf) et certaines autres entreprises de la Big Tech, nous considérons les procédures d'intégration continue (CI) de la plus haute importance.

C'est pourquoi un workflow GitHub est mis en place sur le repository GitHub qui permet d'installer un environnement Python 3.9 adéquat sur la dernière version de Ubuntu.
Cet environnement sert à tester toutes modifications apportées à `mise_en_route.py`.
Le code est automatiquement passé dans un linter (PyLint, configuré dans `lint.py`), qui retourne un score de qualité sur 10.
Chez `mise_en_route.py`, l'excellence est au premier rang, et nous n'acceptons aucun résultat du linter de moins de la note parfaite de 10/10.

## License

Ce document et le code source de ce projet (appelés le "Software") sont distribuées sous la license MIT :

```
MIT License

Copyright (c) 2021 Aymeric Wibo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# Sponsors

Le projet `mise_en_route.py` est un projet international qui a pour fins d'améliorer le niveau de vie global et de faire avancer la société humaine.
Cependant, il n'a pas encore de sponsors.
Si vous connaissez une organisation qui serait susceptible de sponsoriser le projet, parlez-en leur.
