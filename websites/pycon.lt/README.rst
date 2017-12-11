How to use
==========

In order to do full deployment run this command::

  ansible-playbook deploy.yml --ask-vault-pass

If you did just insignificant changes and want to do quick deploy run this
command::

  ansible-playbook deploy.yml --ask-vault-pass --tags upload
