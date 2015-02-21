#################
AKL serverių ūkis
#################

.. contents:: Turinys

Serveris ideja.akl.lt
=====================

:OS: Ubuntu 10.04.4 LTS

   Šiame serveyje šiuo metu veikia tik vienas diskas, kitas nebeveikia.

Apache
------

.. list-table::

   * - http://akl.lt
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     - taps NEAKTUALI, užbaigus naują akl.lt
   * - http://ideja.akl.lt
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     - BEPROBLEMŲ: http://tinyurl.com/newgy5r
   * - http://lietuvybe.org
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     - NEAKTUALI: 2012 m. visa aktuali info perkelta į http://lietuvybe.lt/
   * - http://debian.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - NEAKTUALI: nuo 2006-ųjų neveikia (http://tinyurl.com/q2sxght), 2005-aisiais permesdavo į http://debian.home.lt/
   * - http://gnome.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - NEAKTUALI: svetainė apleista iškart ją įkūrus (http://tinyurl.com/o7tgas4)
   * - http://mokslui.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - Projektas stagnuoja: DVD atvaizdis neatnaujintas nuo 2008 m. Dėl naudingumo ir reikalingumo galėtų pakomentuoti Jurgis. DNS rodo į dogma (tai kad nerodo)
   * - http://pycon.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - Kiek būtų sunku migruoti? Kiek šitoje svetainėje informacijos?
   * - http://plone.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - Labai seniai neatnaujinta, ir panašu, kad vargiai beaktuali svetainė (?)
   * - http://wiki.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - labai menkai naudotas vikis, paskutiniai pakeitimai 2012 m. Gal pavyktų išeksportuoti info ir importuoti kitur?
   * - http://mode.esu.as
     - Zope 2.10
     - ``/srv/zopes/mode``
     - Modesto Liudavičiaus <mode@esu.as> asmeninis fotoalbumas.
   * - http://nariai.akl.lt
     - Zope 2.10
     - ``/srv/zopes/mode``
     -
   * - http://baltix.akl.lt
     - Zope 2.9
     - ``/srv/zopes/baltix``
     - Mantas galėtų pakomentuoti dėl šitos svetainės sudėtingumo ir ar galima ją atnaujinti.
   * - http://planetdjango.org
     -
     - ``/home/adomas/planetdjango/html``
     - BEPROBLEMŲ: projektas pernai užgesintas ir pakeistas dviem statiniais failais: http://tinyurl.com/n8ys6z2
   * - http://vejas.akl.lt
     -
     - ``/srv/vejas/www/``
     - Alberto projektas, gal būtų nesunkiai migruojamas?
   * - http://lists.akl.lt
     - Mailman
     - ``/usr/lib/cgi-bin/mailman``
     - BEPROBLEMŲ: http://packages.ubuntu.com/search?keywords=mailman

Jabber
------

- ``ejabberd``
- ``jabber-pymsn``
- ``pyicqt``

Rimo pastabos:

- Mūsų XMPP servisas neatnaujintas daugybę metų ir veikia nepatikimai. Panašu, kad juo besinaudoja vos keletas žmonių. Galbūt būtų visom prasmėm protinga tiesiog suinstaliuoti naują XMPP serverį ir leisti jame registruotis?
- O gal XMPP paskyros turėtų būti sujungtos su @akl.lt el. pašto paskyromis?
- O gal mums turėti nuosavo XMPP serverio išvis nebereikia?


Mailman
-------
Vargu, ar būtų problemų migruojantis – „Mailman“ per pastaruosius metus nelabai keitėsi, o trečioji jo versija dar neužbaigta ir neišleista.

Named (DNS)
-----------

``/etc/bind``::

    zone akl.lt
    zone baltix.lv
    zone gnome.lt      // sprendžiant iš whois.lt, ši zona dabar gyvena serveriai.lt. NEAKTUALI?
    zone mozilla.lt    // NEAKTUALI – ši zona dabar laikoma „Mozillos“ serveriuose
    zone wonhwado.lt   // sprendžiant iš whois.lt, ši zona dabar gyvena domreg.lt. NEAKTUALI?

Bet kuriuo atveju, „Bind“ atnaujinti nebūtų sunku.

Zope
----

Zope instances::

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

Zope instance prievadai::

  /var/lib/zope2.10/instance/akl/      HTTPPORT 8020
  /var/lib/zope2.8/instance/akl/       HTTPPORT 8020
  /var/lib/zope2.10/instance/mode/     HTTPPORT 8021
  /var/lib/zope2.8/instance/mode/      HTTPPORT 8021
  /var/lib/zope2.9/instance/akl-2.9/   HTTPPORT 8023

Zope prievadai ir Zope versijos::

  18020  Zope 2.12  /srv/zopes/akl-2.12/
   8020  Zope 2.10  /srv/zopes/akl/
   8021  Zope 2.10  /srv/zopes/mode/
   8023  Zope 2.9   /srv/zopes/akl-2.9/, /srv/zopes/baltix/

Apache rewrite rules, prievadai atsakingi servisai iš ``/etc/init.d``::

  akl.lt/          18020   /etc/init.d/zope2.12
  ideja.akl.lt/    18020   /etc/init.d/zope2.12
  lietuvybe.org/   18020   /etc/init.d/zope2.12
  debian.akl.lt/    8020   /etc/init.d/zope2.10
  gnome.akl.lt/     8020   /etc/init.d/zope2.10
  mokslui.akl.lt/   8020   /etc/init.d/zope2.10
  plone.akl.lt/     8020   /etc/init.d/zope2.10
  pycon.akl.lt/     8020   /etc/init.d/zope2.10
  wiki.akl.lt/      8020   /etc/init.d/zope2.10
  mode.esu.as/      8021   /etc/init.d/zope2.10
  nariai.akl.lt/    8021   /etc/init.d/zope2.10
  akl.lt/akl-2.9    8023   /etc/init.d/zope2.9
  baltix.akl.lt/    8023   /etc/init.d/zope2.9
  akl.lt/aklv2      8022   /etc/init.d/zope2.8

Serveris dogma.akl.lt
=====================

:OS: Debian GNU/Linux 6.0

Apache
------

Veikia, naudojama:

- http://autocorr.akl.lt
- http://forumai.akl.lt
- http://gimp.akl.lt
- http://kde.akl.lt
- http://lietuvybe.lt
- http://locost.lt
- http://opensuse.lt
- http://planet.akl.lt
- http://stats.akl.lt
- http://ubuntu.lt
- http://webmail.akl.lt

Veikia, nukreipimai:

- http://atvirasalus.lt
- http://haiku-os.lt

Veikia, nebenaudojama:

- http://blog.akl.lt
- http://coder.akl.lt
- http://coders.akl.lt
- http://ec.akl.lt
- http://guniqueapp.akl.lt
- http://pagalba.akl.lt
- http://slackware.akl.lt

Neveikia:

- http://arkliotakeliai.wonhwado.lt
- http://filezilla.akl.lt
- http://gnome.lt
- http://latex.akl.lt
- http://lekp.akl.lt
- http://linux.akl.lt
- http://lpm.akl.lt
- http://mokslas.akl.lt
- http://mokslui.akl.lt
- http://programos.akl.lt
- http://soft.akl.lt
- http://suse.akl.lt
- http://svietimas.akl.lt
- http://vytis.akl.lt

Serveris faktas.akl.lt [ ? ]
============================

:OS: ?

Serveryje turėjo „suktis“ tik HTTP ir FTP servisas. Serveris užgęso 2012 m., vėliau buvo dalinai, bet tik dalinai prikeltas. Neveikia jau daugiau kaip dvejus metus.

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
