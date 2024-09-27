Go back --> :doc:`Atheros Linux wireless drivers <atheros>`

ar6k
----

ar6k is the GPL driver for the Atheros AR6000 mobile 802.11bg chipset used on the `OpenMoko <OpenMoko>`__.

Getting the code
----------------

ar6k never made it upstream but openmoko maintains the driver on their git repository. You can get the latest ar6k code from a branch on their repository:

::

   git clone git://git.openmoko.org/git/kernel.git openmoko
   cd openmkoko
   git checkout -b ar6k origin/andy-tracking

Code on openmoko git
--------------------

You can find the ar6k code under:

::

   drivers/ar6000/

Sharing code upstream
---------------------

It may be possible to share HTC/HIF/WMI code with the :doc:`ar9271 <ar9271>` USB driver. This needs further review.
