tftool
======

Ergonomic utilities for the terraform CLI.

Usage
-----

.. code-block:: bash

    alias tfplan="terraform plan -refresh=false -input=false -out=/tmp/plan && terraform show -json /tmp/plan"
    alias tfapply="xargs -or0 terraform apply"
    tfplan | tftool target --no-updates | tfapply

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   install
   tftool

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
