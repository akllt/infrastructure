{% set home = '/opt/pylab.lt' %}
{% set path = home + '/app' %}
{% set build_env = salt['pillar.get']('build_env', 'production') %}
{% set server_name = salt['pillar.get']('server_name', 'pylab.lt') %}


pylab:
  pkgrepo.managed:
    - name: deb-src http://ubuntu-archive.mirror.serveriai.lt/ trusty main restricted universe

  pkg.installed:
    - pkgs:
      - language-pack-en
      - language-pack-lt
      - build-essential
      - postgresql
      - libpq-dev
      - python-all-dev
      - python3-all-dev
      - python-egenix-mx-base-dev
      - quilt
      - python-pip
      - python-virtualenv
      - apache2
      - libapache2-mod-wsgi-py3
      - git
    - require:
      - pkgrepo: pylab

  user.present:
    - gid: {{ salt['group.info']('www-data').gid }}
    - home: {{ home }}
    - system: yes

  postgres_user.present:
    - require:
      - pkg: pylab
      - user: pylab

  postgres_database.present:
    - owner: pylab
    - require:
      - pkg: pylab
      - postgres_user: pylab

  git.latest:
    - name: https://github.com/python-dirbtuves/vasaros-dirbtuves.git
    - target: {{ path }}
    - user: pylab
    - rev: master
    - require:
      - pkg: pylab
      - user: pylab


init:
  cmd.run:
    - name: python3 scripts/genconfig.py config/env/{{ build_env }}.cfg
    - cwd: {{ path }}
    - user: pylab
    - creates: {{ path }}/buildout.cfg
    - require:
      - git: pylab


make:
  cmd.wait:
    - cwd: {{ path }}
    - user: pylab
    - env:
      - LC_ALL: en_US.UTF-8
    - watch:
      - git: pylab
      - postgres_database: pylab


migrate:
  cmd.wait:
    - name: bin/django migrate --noinput
    - cwd: {{ path }}
    - user: pylab
    - watch:
      - git: pylab
      - postgres_database: pylab
    - require:
      - cmd: make


collectstatic:
  cmd.wait:
    - name: bin/django collectstatic --noinput
    - cwd: {{ path }}
    - user: pylab
    - watch:
      - git: pylab
    - require:
      - cmd: make


reload:
  cmd.wait:
    - name: touch --no-create {{ path }}/bin/django.wsgi
    - user: pylab
    - watch:
      - git: pylab
    - require:
      - cmd: make


apache2:
  pkg.installed:
    - pkgs:
      - apache2
      - libapache2-mod-wsgi-py3
    - require:
      - pkg: pylab

  service.running:
    - enable: yes
    - watch:
      - pkg: apache2
      - file: /var/log/apache2/pylab.lt
      - file: /etc/apache2/sites-enabled/pylab.lt.conf


/var/log/apache2/pylab.lt:
  file.directory:
    - user: pylab
    - group: www-data
    - mode: 066


/etc/apache2/sites-enabled/pylab.lt.conf:
  file.managed:
    - template: jinja
    - source: salt://apache.conf
    - context:
        server_name: {{ server_name }}
        path: {{ path }}
    - require:
      - pkg: apache2


/etc/apache2/sites-enabled/000-default.conf:
  file.absent:
    - require:
      - pkg: apache2
