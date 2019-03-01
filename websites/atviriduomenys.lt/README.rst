Testing deployment scripts
==========================

Before doing real deployment you may want to try to deploy to a sandbox,
instructions bellow helps you to do that.

Install vagrant, virtualbox and ansible::

    sudo apt install vagrant virtualbox python-pip
    sudo pip install 'ansible>=1.6'

For the vagrant, you will probably need to download it from vagrant.com_,
because at least 1.6 version is required.


.. _vagrant.com: http://www.vagrantup.com/downloads.html

Prepare virtual machine for testing deployment::

    vagrant up
    ssh-copy-id vagrant@10.0.0.42

You already had your ssh key, `didn't you`__?

__ https://help.ubuntu.com/community/SSH/OpenSSH/Keys#Generating_RSA_Keys

And try to deploy::

    ansible-playbook -u vagrant -i 10.0.0.42, -e env=vagrant deploy.yml

Be patient, this last command may take long time to finish, up to 10 minutes.

If everything went well you should see working web page by visiting
http://localhost:8080/ .





::

   cd /opt/atviriduomenys.lt/
   sudo -Hsu atviriduomenys
      git clone https://github.com/pyenv/pyenv.git
      export PYENV_ROOT=/opt/atviriduomenys.lt/pyenv
      pyenv/bin/pyenv install 3.7.2
      pyenv/versions/3.7.2/bin/python -m venv venv
      venv/bin/pip install -r spinta/requirements.txt -e spinta
      git clone https://github.com/atviriduomenys/manifest.git
      vi .env
         SPINTA_DEBUG=true
         SPINTA_MANIFESTS_DEFAULT_PATH=/opt/atviriduomenys.lt/manifest
   sudo -u postgres psql
      create database "spinta" with owner "atviriduomenys" encoding 'UTF8' LC_COLLATE = 'C.UTF-8' LC_CTYPE = 'C.UTF-8' template template0;
      grant all privileges on database "spinta" to "atviriduomenys";
   sudo -Hsu atviriduomenys
      venv/bin/spinta migrate
      venv/bin/spinta pull gov/vrk/rinkejopuslapis.lt/kandidatai
      venv/bin/uvicorn --host 0.0.0.0 spinta.asgi:app --debug
      venv/bin/pip install gunicorn
      venv/bin/gunicorn -b 0.0.0.0:8000 -w 4 -k uvicorn.workers.UvicornWorker spinta.asgi:app
   sudo a2enmod proxy_http
   sudo vi /etc/apache2/sites-enabled/atviriduomenys.lt.conf
      <VirtualHost *:80>
          ServerName ad.sirex.lt
          ServerAlias www.atviriduomenys.lt
          Redirect permanent / https://atviriduomenys.lt/
      </VirtualHost>

      <VirtualHost *:80>
          ServerAdmin sirexas@gmail.com
          ServerName atviriduomenys.lt

          DocumentRoot /opt/atviriduomenys.lt/www
          Alias /data/ /opt/atviriduomenys.lt/app/var/www/data/

          <Directory /opt/atviriduomenys.lt/www>
              Require all granted
              Options -Indexes
          </Directory>

          <Directory /opt/atviriduomenys.lt/www/data>
              Options +Indexes
              IndexOptions FancyIndexing FoldersFirst HTMLTable
              ServerSignature Off
          </Directory>

          ProxyPass /data/ !
          ProxyPass / http://localhost:8000/

          ErrorLog /var/log/apache2/atviriduomenys.lt/error.log
          CustomLog /var/log/apache2/atviriduomenys.lt/access.log combined
      </VirtualHost>
   sudo vi /etc/systemd/system/spinta.service
      [Unit]
      Description=spinta daemon
      Requires=spinta.socket
      After=network.target

      [Service]
      PIDFile=/run/spinta/pid
      User=atviriduomenys
      Group=www-data
      WorkingDirectory=/opt/atviriduomenys.lt
      ExecStart=/opt/atviriduomenys.lt/venv/bin/gunicorn --pid /run/spinta/pid -w 4 -k uvicorn.workers.UvicornWorker spinta.asgi:app
      ExecReload=/bin/kill -s HUP $MAINPID
      ExecStop=/bin/kill -s TERM $MAINPID
      PrivateTmp=true

      [Install]
      WantedBy=multi-user.target
   sudo vi /etc/systemd/system/spinta.socket
      [Unit]
      Description=spinta socket

      [Socket]
      ListenStream=/run/spinta/socket
      ListenStream=127.0.0.1:8000

      [Install]
      WantedBy=sockets.target
   sudo vi /usr/lib/tmpfiles.d/spinta.conf
      d /run/spinta 0755 atviriduomenys www-data -
   sudo systemd-tmpfiles --remove --create /usr/lib/tmpfiles.d/spinta.conf
   sudo systemctl enable spinta.service
   sudo systemctl start spinta.service
