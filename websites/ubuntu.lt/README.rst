How to run deployment scripts
=============================

Note: I switched to Python 3.8, which is installed via pyenv and runs via
gunicorn and gunicorn is proxied via Apache. I tried to  update ansible scripts
to match what is on server, but did not finished it.

So this ansible script no longer works.

I will try to updated it some time later.

::

    ansible-playbook -K deploy.yml

If you updated Django or Spirit version, you should run deployment using this command::

    ansible-playbook -K deploy.yml -e upgrade=1
