======
tftool
======
.. image:: https://readthedocs.org/projects/tftool/badge/?version=latest
    :target: https://tftool.readthedocs.io/en/latest/
.. image:: https://img.shields.io/pypi/v/tftool?color=success
    :target: https://pypi.org/project/tftool
.. image:: https://img.shields.io/docker/v/barnabyshearer/tftool/latest?color=success&label=docker
    :target: https://hub.docker.com/repository/docker/barnabyshearer/tftool

Ergonomic utilities for the terraform CLI.

Install
-------

::

    python3 -m pip install tftool

Usage
-----

::

    alias tfplan="terraform plan -refresh=false -input=false -out=/tmp/plan && terraform show -json /tmp/plan"
    alias tfapply="xargs -or0 terraform apply"
    tfplan | tftool target --no-updates | tfapply
