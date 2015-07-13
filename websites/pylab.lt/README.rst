Testing deployment scripts
==========================

Before doing real deployment you may want to try to deploy to a sandbox,
instructions bellow helps you to do that.

Install vagrant and virtualbox::

    sudo apt install vagrant virtualbox

For the vagrant, you will probably need to download it from vagrant.com_,
because at least 1.6 version is required.

.. _vagrant.com: http://www.vagrantup.com/downloads.html

To do deployment run::

    ./runsalt.py vagrant

If everything went well you should see working web page by visiting
http://localhost:8080/ .

How it works?
=============

For deployment masterless SaltStack minion is used. Since SaltStack minion has
to be installed and configured on server first, there is a small ``runsalt.py``
tool.

``runsalt.py`` is responsible for bootstrapping and configuring minion on the
server. It is assumed, that single server possible has more than one project
deploy, to avoid conflicts between projects, each project has separate
SaltStack minion configuration. By default minion configuration is saved in
``/root/salt/{project}`` directory.

When running ``salt-call`` you have to specify project's configuration like
this::

    salt-call --config-dir=/root/salt/myproject

Correct configuration directory is specified automatically if you use
``runsalt.py``. Actually ``runsalt.py`` utility just calls ``salt-call`` with
needed arguments and makes sure, that SaltStack minion is bootstrapped and
configured on the server..

You can configure ``runsalt.py`` tool using ``runsalt.cfg`` configuration file.
Here is example ``runsalt.cfg``:

.. code-block:: cfg

    [runsalt]
    minion-id = production
    project = pydev
    server = example.com
    project-root = /opt/{project}
    salt-config = /root/salt/{project}

    [staging]
    server = staging.example.com

``runsalt.cfg`` file has ``[runsalt]`` section for configuring ``runsalt.py``
parameters. Three required parameters ``minion-id``, ``project`` and ``server``
has to be specified.

All other sections are interpreted ans environments. For example ``[staging]``
section overrides ``[runsalt]`` parameters if ``staging`` environment is
specified. To deploy using an environment you need to pass environment name as
first positional argument to the ``runsalt.py``::

    runsalt.py staging

By default environment automatically sets ``minion-id`` to environment name. If
you wan different ``minion-id`` you have to specify it explicitly.

Since you can control ``minion-id`` from ``runsalt.cfg``, you can use than in
``top.sls`` files, for example, pillar ``top.sls`` file could look like this:

.. code-block:: yaml

    base:
      production:
        - production
      vagrant:
        - vagrant

With this, each environment will be provided with different pillar variables.

``runsalt.py`` automatically adds ``vagrant`` environment and detects server
configuration from ``vagrant ssh-config``. So you can test you configuration
using this command::

    runsalt.py vagrant
