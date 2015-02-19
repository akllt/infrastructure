Ko gero, ansčiau ar vėliau, teks kraustyti AKL serverius iš fizinių dėžių į
virtualius serverius.

Mykolas kaip tik tarasi dėl to su VU.

Kad kraustymąsis būtų sklandesnis, noriu padaryti AKL serverių ūkio
inventorizaciją, kab būtų aišku ką kraustyti, ko ne.

.. contents::

Serveris ideja.akl.lt [ Ubuntu 10.04.4 LTS ]
============================================

.. note::

   Šiame serveyje šiuo metu veikia tik vienas diskas, kitas nebeveikia.

Apache
------

.. list-table::

   * - http://akl.lt
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     -
   * - http://ideja.akl.lt
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     -
   * - http://lietuvybe.org
     - Zope 2.12
     - ``/srv/zopes/akl-2.12``
     - (Matyt reikėtų nukreipti į lietuvybe.lt)
   * - http://debian.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     -
   * - http://gnome.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     -
   * - http://mokslui.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     - (DNS rodo į dogma)
   * - http://pycon.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     -
   * - http://plone.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     -
   * - http://wiki.akl.lt
     - Zope 2.10
     - ``/srv/zopes/akl``
     -
   * - http://mode.esu.as
     - Zope 2.10
     - ``/srv/zopes/mode``
     -
   * - http://nariai.akl.lt
     - Zope 2.10
     - ``/srv/zopes/mode``
     -
   * - http://baltix.akl.lt
     - Zope 2.9
     - ``/srv/zopes/baltix``
     -
   * - http://planetdjango.org
     -
     - ``/home/adomas/planetdjango/html``
     -
   * - http://vejas.akl.lt
     -
     - ``/srv/vejas/www/``
     -
   * - http://lists.akl.lt
     - Mailmain
     - ``/usr/lib/cgi-bin/mailman``
     -

Jabber
------

- ``ejabberd``
- ``jabber-pymsn``
- ``pyicqt``

Mailman
-------

Named (DNS)
-----------

``/etc/bind``::

    zone akl.lt
    zone baltix.lv
    zone gnome.lt
    zone mozilla.lt
    zone wonhwado.lt

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

Serveris dogma.akl.lt [ Debian GNU/Linux 6.0 ]
==============================================

Apache
------

Veikia, naudojama:

- http://autocorr.akl.lt
- http://forumai.akl.lt
- http://gimp.akl.lt
- http://kde.akl.lt
- http://locost.lt
- http://mozilla.lt
- http://opensuse.lt
- http://planet.akl.lt
- http://stats.akl.lt
- http://ubuntu.lt
- http://webmail.akl.lt

Veikia, nukreipimai:

- http://atvirasalus.lt
- http://haiku-os.lt
- http://lietuvybe.lt

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

Neveikia:

- http://ftp.akl.lt
- http://files.akl.lt
- http://mirror.akl.lt
