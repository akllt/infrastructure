How to use
==========

In order to do full deployment run this command::

  ansible-playbook deploy.yml -K

If you did just insignificant changes and want to do quick deploy run this
command::

  ansible-playbook deploy.yml -K --tags upload



Testing deployment scripts
==========================

Before doing real deployment you may want to try to deploy to a sandbox,
instructions bellow helps you to do that.

Install vagrant, virtualbox and ansible::

    sudo apt install vagrant virtualbox python-pip
    sudo pip install ansible

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
