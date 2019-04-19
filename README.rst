#################
AKL serverių ūkis
#################

.. contents:: Turinys
    :depth: 2

Serveriai
=========

iv-4.pov.lt
-----------

:OS: Ubuntu 14.04.3 LTS
:Kur: dedikuoti.lt virtualus serveris
:Kas prižiūri: Marius Gedminas
:Servisai: Python, PHP svetainės

Pakeitimų istoriją galima peržiūrėti (tik administratoriams) https://iv-4.pov.lt/changelog

Šį serverį AKL'ui padovanojo `Programuotojų artelė`_.

.. _Programuotojų artelė: http://pov.lt/

Svetainės:

- ubuntu.lt_
- pycon.lt_
- atviriduomenys.lt_
- pylab.lt_
- manopozicija.lt_
- savanoriai.maistobankas.lt_

ideja.akl.lt
------------

:OS: Ubuntu 10.04.4 LTS
:Kur: VU MIF kompiuterių laboratorija, antrame aukšte, Naugarduko g.
:Kas prižiūri: Marius Gedminas
:Servisai: Jabber_, Mailman_, DNS_, svetainės
:Būklė: **šiuo metu veikia tik vienas RAID diskas iš dviejų**

Pakeitimų istoriją galima peržiūrėti https://ideja.akl.lt/changelog

.. note::

    Šiam vidiniam puslapiui pasiekti reikia slaptažodžio.  Jei neturite,
    bet turite root priėjimą prie idėjos, susikurkite::

        ssh -t ideja sudo htpasswd /etc/akl.passwd $yourusername


Svetainės
~~~~~~~~~

``grep -E 'ServerName|ServerAlias' /etc/apache2/sites-enabled/* | column -t``

============ ====================== =========================================
Tipas        Svetainė               Pastabos
------------ ---------------------- -----------------------------------------
ServerName   www.akl.lt             Zope (/srv/zopes/akl-2.12)
ServerAlias  akl.lt_                ^
ServerName   baltix.akl.lt_         Zope + Plone (/srv/zopes/baltix-2.13)
ServerAlias  baltix.lv              ^
ServerAlias  www.baltix.lv          ^
ServerAlias  baltix.lt              ^
ServerAlias  www.baltix.lt          ^
ServerName   ideja.akl.lt_          pov-server-page_
ServerName   lists.akl.lt_          Mailman_
ServerName   mode.esu.as_           Zope (/srv/zopes/mode), **neveikia** [*]_
ServerName   nariai.akl.lt_         Zope (/srv/zopes/mode), **neveikia**
ServerName   pycon.akl.lt_          redirect to pycon.lt
ServerAlias  python.akl.lt          ^
ServerName   vejas.akl.lt_          static (/srv/vejas/www/)
ServerName   wiki.akl.lt_           Zope (/srv/zopes/akl-2.13), **neveikia**
============ ====================== =========================================

.. [*] Sugriuvo upgradinant Ubuntu 8.04 į 10.04, kai buvo išmesti
       zope2.9 ir zope2.10 paketai. Marius pataisys, jei sugebės.

Monitoringas:

- konfigūracija ``/etc/pov/check-web-health``
- patikros kas 15 minučių (``/etc/cron.d/pov-check-health``)
- jei kas neveikia siunčiamas emailas

.. _pov-server-page: https://github.com/ProgrammersOfVilnius/pov-server-page


Zope
~~~~

Ubuntu senesnės versijos turėjo Debian paketus: zope2.8, zope2.9, zope2.10.
Ubuntu 10.04 nebeturi nė vieno, tad visi jie neveikia::

  /var/lib/zope2.10/instance:
      akl ->     /srv/zopes/akl
      mode ->    /srv/zopes/mode

  /var/lib/zope2.8/instance:
      akl ->     /srv/zopes/akl/
      aklv2 ->   /srv/zopes/aklv2/
      mode ->    /srv/zopes/mode

  /var/lib/zope2.9/instance:
      akl-2.9 -> /srv/zopes/akl-2.9

  /var/lib/zope/instance:
      default

Vėliau buvo sukurti keli Zope instance'ai rankomis, naudojant zc.buildout::

  /srv/zopes/akl-2.12
  /srv/zopes/akl-2.13
  /srv/zopes/baltix-2.13

Zope instance prievadai (juos galima pamatyti https://ideja.akl.lt/ports)::

  $ grep 'define HTTPPORT' /srv/zopes/*/etc/zope.conf | sed 's/:%define HTTPPORT//' | column -t | sort -n -k2
  /srv/zopes/akl-2.10/etc/zope.conf     8020
  /srv/zopes/akl/etc/zope.conf          8020
  /srv/zopes/mode/etc/zope.conf         8021
  /srv/zopes/akl-2.9/etc/zope.conf      8023
  /srv/zopes/baltix/etc/zope.conf       8023
  /srv/zopes/akl-2.12/etc/zope.conf     18020
  /srv/zopes/akl-2.13/etc/zope.conf     18022
  /srv/zopes/baltix-2.13/etc/zope.conf  18023

Zope prievadai ir Zope versijos::

  18023  Zope 2.13  /srv/zopes/baltix-2.13/
  18022  Zope 2.13  /srv/zopes/akl-2.13/
  18020  Zope 2.12  /srv/zopes/akl-2.12/
   8020  Zope 2.10  /srv/zopes/akl-2.10/, /srv/zopes/akl/     NEVEIKIA
   8021  Zope 2.10  /srv/zopes/mode/                          NEVEIKIA
   8023  Zope 2.9   /srv/zopes/akl-2.9/, /srv/zopes/baltix/   NEVEIKIA

Apache rewrite rules, prievadai atsakingi servisai iš ``/etc/init.d``::

  baltix.akl.lt/   18023   /etc/init.d/zope2.13-baltix
  akl.lt/          18020   /etc/init.d/zope2.12
  wiki.akl.lt/     18022   /etc/init.d/zope2.13   NEVEIKIA
  mode.esu.as/      8021   /etc/init.d/zope2.10   NEVEIKIA
  nariai.akl.lt/    8021   /etc/init.d/zope2.10   NEVEIKIA


dogma.akl.lt
------------

:OS: Debian GNU/Linux 8.5
:Kur: LMTA virtualus serveris
:Kas prižiūri: Rimas Kudelis

Ėmus gesti fizinio serverio diskams, duomenys iš jų perkelti į laikiną virtualią mašiną Lietuvos muzikos ir teatro akademijos serveryje. Tuo pačiu padarytas atnaujinimas. Dabar serveris laukia nuolatinių namų, tačiau joks pavojus trumpuoju laikotarpiu jam negresia.

faktas.akl.lt
-------------

:OS: 
:Kur: VU MIF kompiuterių laboratorija, antrame aukšte, Naugarduko g.
:Kas prižiūri: niekas
:Būklė: Neveikia nuo 2012 m.

Serveryje turėjo „suktis“ tik HTTP ir FTP servisas. Serveris užgęso 2012 m., vėliau buvo dalinai, bet tik dalinai prikeltas. Neveikia jau daugiau kaip dvejus metus.

diedas.soften.ktu.lt
--------------------

:OS:
:Kur: KTU
:Kas prižiūri: niekas
:Būklė: apleistas, neprižiūrimas

Iki 2016 m. šis serveris aptarnavo AKL el. paštą, tačiau jau mažiausiai keletą metų nebuvo prižiūrimas. 2016 m. rugpjūtį serveris tapo nepasiekiamas.

mail.akl.lt
-----------

:OS: 
:Kur: LMTA virtualus serveris
:Kas prižiūri: Rimas Kudelis

Sugedus diedas.soften.ktu.lt_ serveriui, AKL el. paštas perkeltas į LMTA virtualų serverį, kuriame veikia Rimo asmeninis el. paštas ir keletas interneto svetainių.

Interneto svetainės
===================

akl.lt
------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Naudojamas: taip
:Viduriai: Zope 2.12
:Vieta serveryje: ``/srv/zopes/akl-2.12``
:Kas prižiūri: Mantas Kriaučiūnas

Migruojama ant naujausio Django/Wagtail ir Python 3:
https://github.com/python-dirbtuves/akl.lt

Serveris anksčiau fiziškai gulėjo VU MIF, bet vėliau buvo perduotas Manui
Kriaučiūnui.

atviriduomenys.lt
-----------------

:Serveris: iv-4.pov.lt_
:Adresas: atviriduomenys.lt
:Naudojamas: taip
:Viduriai: Starlette_, Gunicorn_, Python 3.7, PostgreSQL
:Vieta serveryje: ``/opt/atviriduomenys.lt``
:Kas prižiūri: Mantas Zimnickas
:Kodas: https://github.com/atviriduomenys/spinta

.. _Starlette: https://www.starlette.io/
.. _Gunicorn: https://gunicorn.org/

pylab.lt
--------

:Serveris: iv-4.pov.lt_
:Adresas: pylab.lt
:Naudojamas: ne
:Viduriai: Django 1.8, Python 3, PostgreSQL
:Vieta serveryje: ``/opt/pylab.lt``
:Kas prižiūri: Mantas Zimnickas

Šis projektas buvo vienas iš Python dirbtuvių projektų, skirtas vidiniam Python
dirbtuvių naudojimui ir susitikimų organizacimui. Tačiau Python dirbtuvės nuo
2015 metų rudenio nebevyksta ir šis projektas nuo to laiko nebenaudojamas.

manopozicija.lt
---------------

:Serveris: iv-4.pov.lt_
:Adresas: manopozicija.lt
:Naudojamas: taip
:Viduriai: Django 1.8, Python 3, PostgreSQL
:Vieta serveryje: ``/opt/manopozicija.lt``
:Kas prižiūri: Mantas Zimnickas
:Kodas: https://github.com/sirex/manopozicija.lt

savanoriai.maistobankas.lt
--------------------------

:Serveris: iv-4.pov.lt_
:Adresas: savanoriai.maistobankas.lt
:Naudojamas: taip
:Viduriai: Django 1.9, Python 3, PostgreSQL
:Vieta serveryje: ``/opt/savanoriai.maistobankas.lt``
:Kas prižiūri: Mantas Zimnickas
:Kodas: https://github.com/sirex/savanoriai

lietuvybe.org
-------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.12
:Vieta serveryje: ``/srv/zopes/akl-2.12``
:Kas prižiūri:

2012 m. visa aktuali info perkelta į http://lietuvybe.lt/

debian.akl.lt
-------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Nuo 2006-ųjų neveikia (http://tinyurl.com/q2sxght), 2005-aisiais permesdavo į
http://debian.home.lt/.

gnome.akl.lt
------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Svetainė apleista iškart ją įkūrus (http://tinyurl.com/o7tgas4).

mokslui.akl.lt
--------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Projektas stagnuoja: DVD atvaizdis neatnaujintas nuo 2008 m. Dėl naudingumo ir
reikalingumo galėtų pakomentuoti Jurgis.

pycon.akl.lt
------------

:Migravimas: Perkelti
:Naudojamas: taip
:Serveris: ideja.akl.lt_
:Viduriai: apache vhostas
:Vieta serveryje: ``/etc/apache2/sites-available/pycon.akl.lt``
:Kas prižiūri: Marius Gedminas

Redirectina į http://pycon.lt, kuris yra su Pelican darytas statinis saitas
(https://bitbucket.org/sirex/pyconlt/), talpinamas POV serveriuose.

pycon.lt
--------

:Migravimas: Perkelti
:Adresas: pycon.lt
:Naudojamas: taip
:Serveris: iv-4.pov.lt
:Viduriai: Django
:Vieta serveryje: ``/opt/pycon``
:Kas prižiūri: Karina Klinkevičiūtė, Mantas Zimnickas
:Kodas: https://github.com/karina-klinkeviciute/pyconlt

plone.akl.lt
------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Labai seniai neatnaujinta, ir panašu, kad vargiai beaktuali svetainė (?).
Zope 2.10 instance'as net neturi Plone!  Matyt buvo nuspręsta šios svetainės
nemigruoti iš senesnio Zope instance'o.

wiki.akl.lt
-----------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Labai menkai naudotas vikis, paskutiniai pakeitimai 2012 m. Gal pavyktų
išeksportuoti info ir importuoti kitur?

mode.esu.as
-----------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/mode``
:Kas prižiūri:

Modesto Liudavičiaus <mode@esu.as> asmeninis fotoalbumas.

nariai.akl.lt
-------------

:Migravimas: ?
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/mode``
:Kas prižiūri:

baltix.akl.lt
-------------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.13
:Vieta serveryje: ``/srv/zopes/baltix-2.13``
:Kas prižiūri:

Mantas Kriaučiūnas galėtų pakomentuoti dėl šitos svetainės sudėtingumo ir ar
galima ją atnaujinti.

Naujoje akl.lt svetainėje, planuojame padaryti galimybę ant tos pačios TVS
prikabinti kelias skirtingas svetaines. Galbūt, baltix.akl.lt būtų geras
kandidatas perkėlimui.

planetdjango.org
----------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Statiniai failai.
:Vieta serveryje: ``/home/adomas/planetdjango/html``
:Kas prižiūri:

Projektas 2014 m. užgesintas ir pakeistas dviem statiniais failais:
http://tinyurl.com/n8ys6z2.

DNSas rodo nebe į idėją, tad galima ignoruoti.

vejas.akl.lt
------------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: Statiniai failai.
:Vieta serveryje: ``/srv/vejas/www/``
:Kas prižiūri: Albertas Agėjevas

lists.akl.lt
------------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: `Mailman <http://www.gnu.org/software/mailman/>`__
:Vieta serveryje: ``/usr/lib/cgi-bin/mailman``
:Kas prižiūri:


autocorr.akl.lt
---------------

:Migravimas: Perkelti
:Nuoroda: http://autocorr.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: pavienis PHP skriptas
:Vieta serveryje: ``/var/www/autocorr.akl.lt/``
:Kas prižiūri: Rimas Kudelis

forumai.akl.lt
--------------

:Migravimas: Perkelti
:Nuoroda: http://forumai.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: `SMF <http://www.simplemachines.org/>`
:Vieta serveryje: ``/var/www/forumai.akl.lt/``
:Kas prižiūri:

gimp.akl.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://gimp.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: apache vhostas
:Vieta serveryje:
:Kas prižiūri:

Redirectina į http://gimp.lt/ – Giedriaus Naudžiūno ir kompanijos prižiūrimą svetainę apie GIMP. Senoji svetainė, veikusi kaip akl.lt subdomenas, pašalinta su Giedriaus palaiminimu.

kde.akl.lt
----------

:Migravimas: Perkelti
:Nuoroda: http://kde.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: WordPress
:Vieta serveryje: ``/home/dgvirtual/www/kde/``
:Kas prižiūri: Donatas Glodenis

lietuvybe.lt
------------

:Migravimas: Perkelti
:Nuoroda: http://lietuvybe.lt
:Serveris: dogma.akl.lt_
:Viduriai: `CMS Made Simple <http://www.cmsmadesimple.org/>`
:Vieta serveryje: ``/var/www/lietuvybe.kt/``
:Kas prižiūri: Rimas Kudelis

locost.lt
---------

:Migravimas: Perkelti
:Nuoroda: http://locost.lt
:Serveris: dogma.akl.lt_
:Viduriai: `phpBB <https://www.phpbb.com/>`
:Vieta serveryje: ``/home/locost/www/phpBB3/``
:Kas prižiūri: Albertas Agejevas

opensuse.lt
-----------

:Migravimas: Perkelti
:Nuoroda: http://opensuse.lt
:Serveris: dogma.akl.lt_
:Viduriai: `Joomla! <https://www.joomla.org/>`
:Vieta serveryje: ``/home/opensuse/opensuse.lt/``
:Kas prižiūri: Mindaugas Baranauskas

planet.akl.lt
-------------

:Migravimas: Perkelti
:Nuoroda: http://planet.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: `Planet Venus <http://intertwingly.net/code/venus/>`
:Vieta serveryje: ``/var/www/planet.akl.lt/``, ``/etc/planet`` ir kiti `planet-venus` paketo failai
:Kas prižiūri:

stats.akl.lt
------------

:Migravimas: Perkelti?
:Nuoroda: http://stats.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: `PhpMyVisites <http://www.phpmyvisites.us/>`
:Vieta serveryje: ``/var/www/stats.akl.lt/``
:Kas prižiūri:

ubuntu.lt
---------

:Nuoroda: https://ubuntu.lt
:Naudojamas: taip
:Serveris: iv-4.pov.lt_
:Viduriai: phpBB, PHP, Apache, MySQL
:Vieta serveryje:
:Kas prižiūri: Mantas Zimnickas
:Kodas: https://launchpad.net/~ubuntu-lt

Yra planų migruoti serverį nuo PHPBB prie Misago: http://www.ubuntu.lt/forum/viewtopic.php?f=4&t=9544

Naujai kuriamo varianto kodas: https://github.com/python-dirbtuves/ubuntu.lt

webmail.akl.lt
--------------

:Migravimas: Perkelti
:Nuoroda: http://webmail.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

atvirasalus.lt
--------------

:Migravimas: Perkelti
:Nuoroda: http://atvirasalus.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

haiku-os.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://haiku-os.lt
:Serveris: dogma.akl.lt_
:Viduriai: statiniai HTML failai
:Vieta serveryje: /var/www/haiku-os.lt/
:Kas prižiūri:

Svetainė nebereikalinga – už domeną nebemokama, o jokių vertingų duomenų joje nėra.


blog.akl.lt
-----------

:Migravimas: Nereikalingas?
:Nuoroda: http://blog.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai: WordPress
:Vieta serveryje: ``/var/www/blog.akl.lt``
:Kas prižiūri:

coder.akl.lt
------------

:Migravimas: Nereikalingas
:Nuoroda: http://coder.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

coders.akl.lt
-------------

:Migravimas: Nereikalingas
:Nuoroda: http://coders.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

ec.akl.lt
---------

:Migravimas: Nereikalingas
:Nuoroda: http://ec.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

guniqueapp.akl.lt
-----------------

:Migravimas: Nereikalingas
:Nuoroda: http://guniqueapp.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

pagalba.akl.lt
--------------

:Migravimas: Nereikalingas
:Nuoroda: http://pagalba.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

slackware.akl.lt
----------------

:Migravimas: Nereikalingas
:Nuoroda: http://slackware.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

arkliotakeliai.wonhwado.lt
--------------------------

:Migravimas: Nereikalingas
:Nuoroda: http://arkliotakeliai.wonhwado.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

filezilla.akl.lt
----------------

:Migravimas: Nereikalingas
:Nuoroda: http://filezilla.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

gnome.lt
--------

:Migravimas: Nereikalingas
:Nuoroda: http://gnome.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

latex.akl.lt
------------

:Migravimas: Nereikalingas
:Nuoroda: http://latex.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

lekp.akl.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://lekp.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

linux.akl.lt
------------

:Migravimas: Nereikalingas
:Nuoroda: http://linux.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

lpm.akl.lt
----------

:Migravimas: Nereikalingas
:Nuoroda: http://lpm.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

mokslas.akl.lt
--------------

:Migravimas: Nereikalingas
:Nuoroda: http://mokslas.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

mokslui.akl.lt
--------------

:Migravimas: Nereikalingas
:Nuoroda: http://mokslui.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

programos.akl.lt
----------------

:Migravimas: Nereikalingas
:Nuoroda: http://programos.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

soft.akl.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://soft.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

suse.akl.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://suse.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

svietimas.akl.lt
----------------

:Migravimas: Nereikalingas
:Nuoroda: http://svietimas.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

vytis.akl.lt
------------

:Migravimas: Nereikalingas
:Nuoroda: http://vytis.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:


Servisai
========

Jabber
------

:Migravimas: ?
:Serveris: ideja.akl.lt_
:Viduriai: ejabberd_
:Vieta serveryje:
:Kas prižiūri:

.. _ejabberd: https://www.ejabberd.im/

- ``ejabberd``
- ``jabber-pymsn``
- ``pyicqt``

Rimo pastabos:

- Mūsų XMPP servisas neatnaujintas daugybę metų ir veikia nepatikimai. Panašu,
  kad juo besinaudoja vos keletas žmonių. Galbūt būtų visom prasmėm protinga
  tiesiog suinstaliuoti naują XMPP serverį ir leisti jame registruotis?

- O gal XMPP paskyros turėtų būti sujungtos su @akl.lt el. pašto paskyromis?

- O gal mums turėti nuosavo XMPP serverio išvis nebereikia?


Mailman
-------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: Mailman_
:Kas prižiūri:

Vargu, ar būtų problemų migruojantis – „Mailman“ per pastaruosius metus nelabai
keitėsi, o trečioji jo versija dar neužbaigta ir neišleista.

DNS
---

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: `Bind <https://www.isc.org/downloads/bind/>`__
:Kas prižiūri:

``/etc/bind/zone/*.zone``

============= ======================================================================
Domenas       Pastabos
------------- ----------------------------------------------------------------------
akl.lt
baltix.lv
gnome.lt      sprendžiant iš whois.lt, ši zona dabar gyvena serveriai.lt. NEAKTUALI?
mozilla.lt    NEAKTUALI – ši zona dabar laikoma „Mozillos“ serveriuose
wonhwado.lt   sprendžiant iš whois.lt, ši zona dabar gyvena domreg.lt. NEAKTUALI?
============= ======================================================================

Bet kuriuo atveju, „Bind“ atnaujinti nebūtų sunku.

FTP
---

:Migravimas: Perkelti
:Serveris: faktas.akl.lt_
:Viduriai:
:Kas prižiūri:

Neveikia:

- http://ftp.akl.lt
- http://files.akl.lt
- http://mirror.akl.lt


Migravimo planas į virtualius serverius
=======================================

Kadangi šiuo metu yra trys skirtingi serveriai, turintys labai daug skirtingų
projektų, tarp kurių nemaža dalis yra pasenusių, siūlau visus esamus projektus
aprašyti į Dockerfile_ ir talpinti į vieną serverį Docker_ konteineriuose.

Tokiu būdu, viename serveryje bus galima tvarkingai talpinti visus projektus,
nereikės skirtingų serverių Python'ui, PHP'ui ir pan.

Be to Dockerfile_ užtikrins projekto paleidimo atkartojamumą, todėl jei
ateityje reikės kraustytis į kokį nors kitą serverį, arba reikės atnaujinti
sistemą, tai migravimas bus paprastesnis ir vienintelis reikalavimas serveriui
bus Docker_ palaikymas.

Galiausiai visi Dockerfile_'ai bus apjungti naudojant Fig_ ir saugomi vienoje
repozitorijoje, todėl bus aišku, kas vyksta su projektais, kada paskutinį kartą
jie buvo atnaujinti, kas ką naudoja ir pan.

To tarpu host serveris bus iš esmės tuščias, jame suksis tik Docker_
konteineriai ir tvarkingai bus padėti taip vadinamie *docker volumes*.

.. _Dockerfile: https://docs.docker.com/reference/builder/
.. _Docker: https://www.docker.com/
.. _Fig: http://www.fig.sh/
