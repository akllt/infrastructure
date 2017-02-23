How to run deployment scripts
=============================

::

    ansible-playbook -K deploy.yml

If you updated Django or Spirit version, you should run deployment using this command::

    ansible-playbook -K deploy.yml -e upgrade=1
