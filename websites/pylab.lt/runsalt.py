#!/usr/bin/env python3

import re
import sys
import shlex
import subprocess
import pathlib
import unittest
import argparse
import shutil
import tempfile
import os.path


def sh(cmd, context=None, render=False):
    context = {k: shlex.quote(v) for k, v in (context or {}).items()}
    cmd = cmd.format(**context)
    if render:
        return cmd
    else:
        subprocess.check_call(cmd, shell=True)


def quote(*args):
    return ' '.join(map(shlex.quote, args))


class Vagrant(object):
    def __init__(self):
        self.set_up_ssh_config()
        self.host = self.get_hostname()

    def set_up_ssh_config(self):
        config = pathlib.Path('.ssh-config')
        if not config.exists():
            output = subprocess.check_output(['vagrant', 'ssh-config'])
            with config.open('w') as f:
                f.write(output.decode('utf-8'))
        self.config = str(config.resolve())

    def get_hostname(self):
        with open(self.config) as f:
            for line in f:
                if line.startswith('Host '):
                    key, value = line.strip().split(None, 1)
                    return value

    def ssh(self, *args):
        subprocess.check_call(filter(None, ['ssh', '-F', self.config, self.host, quote(*args)]))

    def ssh_output(self, *args):
        return subprocess.check_output(filter(None, ['ssh', '-F', self.config, self.host, quote(*args)]))

    def push(self, src, dst):
        sh('tar --directory {path} -cf- {src} | ssh -F {config} {host} {cmd}', {
            'src': src.name,
            'path': str(src.parent),
            'config': self.config,
            'host': self.host,
            'cmd': sh('sudo tar --directory {dest} --no-same-owner -xf-', {'dest': str(dst)}, render=True)
        })


def is_file_exists(paths):
    for path in paths:
        if os.path.exists(path):
            return True
    return False


def bootstrap():
    pass


def main(argv=None):
    argv = argv or sys.argv

    available_environments = ['vagrant', 'tests']

    parser = argparse.ArgumentParser()
    parser.add_argument('environ', nargs='?', choices=available_environments, help='environment')

    args = parser.parse_args()
    print(args.accumulate(args.integers))


# --------------------------------->8----------------------------------

###########
#  Tests  #
###########

# python3 -munittest runsalt.py


class TestCaseMixin(object):

    def assertRegex(self, regex, text):
        text = text.decode('utf-8') if isinstance(text, bytes) else text
        self.assertTrue(re.match(regex, text) is not None, '%r does not match %r' % (text, regex))


class SshTests(unittest.TestCase):

    def test_ssh_call(self):
        vagrant = Vagrant()
        vagrant.ssh('test', '-d', '/home/vagrant')

    def test_ssh_call_error(self):
        vagrant = Vagrant()
        self.assertRaises(subprocess.CalledProcessError, vagrant.ssh, 'test', '-d', '/home/nothere')


class PushTests(unittest.TestCase):

    def setUp(self):
        self.vagrant = Vagrant()
        self.path = pathlib.Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(str(self.path))
        self.vagrant.ssh('sudo', 'rm', '-r', '-f', '/tmp/%s' % self.path.name)

    def test_push(self):
        (self.path / 'runsalt-test-push').mkdir()
        (self.path / 'runsalt-test-push/a.txt').touch()
        self.vagrant.push(self.path / 'runsalt-test-push', '/tmp')
        self.vagrant.ssh('test', '-d', '/tmp/runsalt-test-push')
        self.vagrant.ssh('test', '-f', '/tmp/runsalt-test-push/a.txt')


class CheckSaltTests(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(is_file_exists(['/usr/bin/salt-call']))
