#################
AKL serverių ūkis
#################

.. contents:: Turinys
    :depth: 2

Serveriai
=========

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

``grep -E 'ServerName|ServerAlias' /etc/apache2/sites-enabled/*``

============ ====================== ===================================
Tipas        Svetainė               Pastabos
------------ ---------------------- -----------------------------------
ServerName   www.akl.lt             Zope (/srv/zopes/akl-2.12)
ServerAlias  akl.lt_                ^
ServerName   baltix.akl.lt_         Zope + Plone (/srv/zopes/baltix-2.13)
ServerAlias  baltix.lv              ^
ServerAlias  www.baltix.lv          ^
ServerAlias  baltix.lt              ^
ServerAlias  www.baltix.lt          ^
ServerName   debian.akl.lt_         **neveikia** [*]_
ServerName   gnome.akl.lt_          **neveikia**
ServerName   ideja.akl.lt_          pov-server-page_
ServerName   lietuvybe.akl.lt       DNS rodo kitur, reiktų išjungti
ServerAlias  lietuvybe.org          DNS rodo kitur, reiktų išjungti
ServerAlias  www.lietuvybe.org      DNS rodo kitur, reiktų išjungti
ServerName   lists.akl.lt_          Mailman_
ServerName   mode.esu.as_           Zope, **neveikia** (/srv/zopes/mode)
ServerName   mokslui.akl.lt         **neveikia**
ServerAlias  mokslas.akl.lt_        ^
ServerName   nariai.akl.lt_         **neveikia**
ServerName   pycon.akl.lt_          **neveikia**
ServerAlias  python.akl.lt          ^
ServerName   planetdjango.org_      DNS rodo kitur, reiktų išjungti
ServerAlias  www.planetdjango.org   DNS rodo kitur, reiktų išjungti
ServerName   plone.akl.lt_          **neveikia**
ServerName   wiki.akl.lt_           **neveikia**
============ ====================== ===================================

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
  /srv/zopes/baltix-2.13

Zope instance prievadai (juos galima pamatyti https://ideja.akl.lt/ports)::

  $ grep 'define HTTPPORT' /srv/zopes/*/etc/zope.conf | sed 's/:%define HTTPPORT//' | column -t | sort -n -k2
  /srv/zopes/akl-2.10/etc/zope.conf     8020
  /srv/zopes/akl/etc/zope.conf          8020
  /srv/zopes/mode/etc/zope.conf         8021
  /srv/zopes/akl-2.9/etc/zope.conf      8023
  /srv/zopes/baltix/etc/zope.conf       8023
  /srv/zopes/akl-2.12/etc/zope.conf     18020
  /srv/zopes/baltix-2.13/etc/zope.conf  127.0.0.1:18023

Zope prievadai ir Zope versijos::

  18023  Zope 2.13  /srv/zopes/baltix-2.13/
  18020  Zope 2.12  /srv/zopes/akl-2.12/
   8020  Zope 2.10  /srv/zopes/akl-2.10/, /srv/zopes/akl/
   8021  Zope 2.10  /srv/zopes/mode/
   8023  Zope 2.9   /srv/zopes/akl-2.9/, /srv/zopes/baltix/

Apache rewrite rules, prievadai atsakingi servisai iš ``/etc/init.d``::

  baltix.akl.lt/   18023   /etc/init.d/zope2.13
  akl.lt/          18020   /etc/init.d/zope2.12
  debian.akl.lt/    8020   /etc/init.d/zope2.10   NEVEIKIA
  gnome.akl.lt/     8020   /etc/init.d/zope2.10   NEVEIKIA
  mokslui.akl.lt/   8020   /etc/init.d/zope2.10   NEVEIKIA
  plone.akl.lt/     8020   /etc/init.d/zope2.10   NEVEIKIA
  pycon.akl.lt/     8020   /etc/init.d/zope2.10   NEVEIKIA
  wiki.akl.lt/      8020   /etc/init.d/zope2.10   NEVEIKIA
  mode.esu.as/      8021   /etc/init.d/zope2.10   NEVEIKIA
  nariai.akl.lt/    8021   /etc/init.d/zope2.10   NEVEIKIA
  akl.lt/akl-2.9    8023   /etc/init.d/zope2.9    NEVEIKIA
  akl.lt/aklv2      8022   /etc/init.d/zope2.8    SENIAI NEVEIKIA


dogma.akl.lt
------------

:OS: Debian GNU/Linux 6.0
:Kur: VU MIF kompiuterių laboratorija, antrame aukšte, Naugarduko g.
:Kas prižiūri: Rimas Kudelis
:Būklė:

faktas.akl.lt
-------------

:OS:
:Kur: VU MIF kompiuterių laboratorija, antrame aukšte, Naugarduko g.
:Kas prižiūri:
:Būklė:

Serveryje turėjo „suktis“ tik HTTP ir FTP servisas. Serveris užgęso 2012 m.,
vėliau buvo dalinai, bet tik dalinai prikeltas. Neveikia jau daugiau kaip
dvejus metus.

diedas.soften.ktu.lt
--------------------

:OS:
:Kur: KTU
:Kas prižiūri:
:Būklė:

Interneto svetainės
===================

akl.lt
------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Naudojamas: taip
:Viduriai: Zope 2.12
:Vieta serveryje: ``/srv/zopes/akl-2.12``
:Kas prižiūri:

Migruojama ant naujausio Django/Wagtail ir Python 3:
https://github.com/python-dirbtuves/akl.lt

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

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Numigruotas į Pelican: https://bitbucket.org/sirex/pyconlt/, talpinamas POV
serveriuose.

plone.akl.lt
------------

:Migravimas: Nereikalingas
:Serveris: ideja.akl.lt_
:Viduriai: Zope 2.10
:Vieta serveryje: ``/srv/zopes/akl``
:Kas prižiūri:

Labai seniai neatnaujinta, ir panašu, kad vargiai beaktuali svetainė (?).

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
:Viduriai: Zope 2.9
:Vieta serveryje: ``/srv/zopes/baltix``
:Kas prižiūri:

Mantas galėtų pakomentuoti dėl šitos svetainės sudėtingumo ir ar galima ją
atnaujinti.

Naujoje akl.lt svetainėje, planuojame padaryti galimybę, ant tos pačios TVS
prikabinti kelias skirtingas svetaines. Gal būt, baltix.akl.lt būtų geras
kandidatas perkėlimui.

planetdjango.org
----------------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: Statiniai failai.
:Vieta serveryje: ``/home/adomas/planetdjango/html``
:Kas prižiūri:

Projektas 2014 m. užgesintas ir pakeistas dviem statiniais failais:
http://tinyurl.com/n8ys6z2.

vejas.akl.lt
------------

:Migravimas: Perkelti
:Serveris: ideja.akl.lt_
:Viduriai: Statiniai failai.
:Vieta serveryje: ``/srv/vejas/www/``
:Kas prižiūri: Albertas Agėjavas

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
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

forumai.akl.lt
--------------

:Migravimas: Perkelti
:Nuoroda: http://forumai.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

gimp.akl.lt
-----------

:Migravimas: Perkelti
:Nuoroda: http://gimp.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

kde.akl.lt
----------

:Migravimas: Perkelti
:Nuoroda: http://kde.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

lietuvybe.lt
------------

:Migravimas: Perkelti
:Nuoroda: http://lietuvybe.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

locost.lt
---------

:Migravimas: Perkelti
:Nuoroda: http://locost.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

opensuse.lt
-----------

:Migravimas: Perkelti
:Nuoroda: http://opensuse.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

planet.akl.lt
-------------

:Migravimas: Perkelti
:Nuoroda: http://planet.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

stats.akl.lt
------------

:Migravimas: Perkelti
:Nuoroda: http://stats.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

ubuntu.lt
---------

:Migravimas: Perkelti
:Nuoroda: http://ubuntu.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:

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

:Migravimas: Perkelti
:Nuoroda: http://haiku-os.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
:Kas prižiūri:


blog.akl.lt
-----------

:Migravimas: Nereikalingas
:Nuoroda: http://blog.akl.lt
:Serveris: dogma.akl.lt_
:Viduriai:
:Vieta serveryje:
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
