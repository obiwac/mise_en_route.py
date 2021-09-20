# mise_en_route.py

Ce document est destiné aux utilisateurs du programme `mise_en_route.py`.
C'est un programme très utile qui permet de affiche trois colonnes de nombres:

 - La première afficheles dix premiers nombres entiers commençant par 1.
 - La seconde affiche les dix premiers carrés de nombres entiers commençant par 1.
 - La dernière affiche la somme des carrés précédents.

## Dépendances

`mise_en_route.py` requiert une installation de Python 3.
Pour l'installer, débrouillez vous.

## Installation

Sur les machines similaires à ou basées sur Unix (Linux, macOS, *BSD, &c), vous pouvez installer `mise_en_route.py` en le rendant d'abord executable, et puis en le déplaçant dans un dossier appartenant à `$PATH` (e.g., `/usr/local/bin/`) :

```sh
% chmod +x src/mise_en_route.py
% cp src/mise_en_route.py /usr/local/bin/
```

Si vous utilisez Windows, n'utilisez pas Windows.

## Contribution

La contribution est le fondement des projects FOSS.
`mise_en_route.py` ne serait pas là où il en est sans les contributions de sa communauté, et pour celà, on vous remercie.

Un repositoire git est mis en place sur GitHub en privé sur (obiwac/mise_en_route.py)[https://github.com/obiwac/mise_en_route.py]. Vous pouvez demander l'accès en envoyant un e-mail à l'adresse obiwac@gmail.com, avec le titre "Demande d'accès à `mise_en_route.py`", et le format suivant :

```
Bonjour,

Je souhaiterais contribuer au project `mise_en_route.py`.
Je demande donc l'accès au repositoire git hébergé sur GitHub sur https://github.com/obiwac/mise_en_route.py
Mon identifiant sur GitHub est : <VOTRE IDENTIFIANT GITHUB>

Merci.
```

Une fois que vous avez l'accès, mettez en place l'authentication SSH sur GitHub (ce qui est nécessaire pour contribuer à des repositoires privées), et clonez le repositoire :

```sh
% git clone ssh://git@github.com/obiwac/mise_en_route.py
% cd mise_en_route.py/
```

Vous pouvez ensuite créer une nouvelle branche (avec un nom sensible) avant d'éffectuer vos changements :

```sh
% git checkout -b <LE NOM DE VOTRE NOUVELLE BRANCHE>
```

Une fois que vous avez terminé vous changements, vous pouvez commit votre changement avec :

```sh
% git add .
% git commit -m "<LE NOM DE VOTRE COMMIT>"
% git push origin <LE NOM DE VOTRE BRANCHE>
```

Je viendrais donc vérifier les changements et les merge si je les juge adéquats.

## License

Ce document et le code source de ce projet (appelées le "Software") sont distribuées sous la license MIT :

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
Si vous connaissez une organisation qui serait suceptible de sponsoriser le projet, parlez-en leur.
