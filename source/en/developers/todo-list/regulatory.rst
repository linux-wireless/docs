Regulatory TODO
===============

Regulatory code is maintained on the Linux kernel but a revamp of new
ideas is being considered on a userspace regulatory simulator. The
userspace regulatory simulator is designed to help us create / modify /
simulate software changes easily but at the same time exist as a
template for anyone to use the same software in any other software
environment given that the license of the code is permissively licensed.

-  Port to any other Operating System
-  Use in firmware if needed You can find the regulatory simulator here:

https://github.com/mcgrof/regsim

The following regulatory ideas are being implemented on the regulatory
simulator. References to code where specific changes are being
implemented on the regulatory simulator are documented below as well.

TPC
---

TPC is something we have considered adding but at least as per our
latest review no one seems to have come up with reasons to support this.

Spectral power limits
---------------------

Its believed we may need to allow for spectral power limits (e.g.
10mW/MHz). If this is true the database may need to be adjusted to
account for these. This is relevant for 5/10 MHz channels, where we
currently assume 1/4 and 1/2 TX power respectively (i.e. assume a
spectral power limit being reached exactly for 20 MHz channels) which
doesn't allow using the full power if the spectral power limit isn't
exactly that.

direct database loading
-----------------------

Instead of going through CRDA, we want to load the database directly
into the kernel. Since this means a major change, a `new, extensible,
file format <regdb-file-format>`__ should be used.
