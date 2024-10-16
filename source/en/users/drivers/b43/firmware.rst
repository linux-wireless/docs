Introduction
============

- Broadcom hardware requires firmware to be uploaded after every reset.
- **b43** expects firmware to be available in the system (usually ``/lib/firmware/b43/``).
- Broadcom didn't publish firmware for most of the cards.
- **b43** community developed **b43-fwcutter** extracting firmware files out of Broadcom Linux binary drivers.
- Distributions are not allowed to redistribute extracted firmware.

This of course causes problems for end-users. They have to download
binary drivers on their own and extract firmware out of it.

Current solutions
-----------------

There are many attempts trying to make end-users life easier:

- Firmware extraction procedure described on `old b43 wiki page <http://linuxwireless.sipsolutions.net/en/users/Drivers/b43/#Device_firmware_installation>`__.
- openSUSE: helper script ``install_bcm43xx_firmware`` as part of ``b43-fwcutter`` package.
- Ubuntu: special ``firmware-b43-installer`` package with some script executed after installation.
- Debian: some ``postinst`` script integrated into **b43-fwcutter** tool.

Problem
-------

While above solutions may seem to work for some (many?) users, they are
not really perfect. Few issues:

- Limitation to users of particular distributions.
- Duplicated work on solving the same problem.
- Maintenance problem, it takes time to propagate firmware updates across all implementations. If firmware API happens to change (used to happen in past), maintainers have to track how/where to place the firmware.
- Lack of one global way for users to install firmware.
- Limitations of particular implementations (extracting old firmware, support for limited chipsets only, no solution for offline installation).

Idea
----

We'd like to write a one common helper script and make it part of the ``b43-fwcutter`` project. This would result in a one common way of installing ``b43`` firmware for all users. Of course distributions still could integrate a proper call to the script e.g. in the ``postinst``.

List of planned requirements for the common script:

- Support for installing ``b43`` and ``b43legacy`` firmware.
- Installing the newest firmware for every API version (so users can freely switch between kernels).
- Allow offline installation by providing a path to downloaded driver (archive). This will require a small list of md5/sha sums but should be easy to maintain.

Our current plan is to share this idea with various distributions (most likely package maintainers) and listen to the feedback. Based on that we may change/extend our script requirements.

Once we get requirements list complete and "Ack" from distributions we'll write the common script and make it part of the ``b43-fwcutter``.
