Using sparse
============

Sparse is a semantic parser and static analyzer utility we use for Linux
kernel development. We highly recommend using sparse for the wireless
subsystem. Below are some quick instructions how to get this set up and
how to use it.

Get sparse
----------

You can get sparse from::

   git://git.kernel.org/pub/scm/devel/sparse/sparse.git

Version of sparse to use
------------------------

We recommend to use the latest stable release of sparse. As of now this
is v0.5.1, so you can do something as follows::

   git checkout v0.5.1

Or do ``git tag -l`` to see all releases.

Install sparse
--------------

To install::

   make
   make install

Using sparse
------------

To use sparse for kernel development simply pass on the C=2 argument
onto your make command. For example to enable sparse for mac80211
development you would use::

   make C=2 M=net/mac80211/

This will force-check all corresponding source files. To only check
files which will be recompiled you would use the C=1 argument::

   make C=1 M=net/mac80211/

Endian checks
-------------

Most endian complaints are typically valid and reflect design issues.
These should be reviewed carefully. Happily, since v4.10-rc1 these
checks are automatically enabled.
