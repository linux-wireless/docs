acx1xx
------

/!\\ There is legal controversy surrounding the development of this driver, see the wireless mailing list for more information. Until that is cleared, we suggest to not use or download this driver. See `kernel inclusion section <http://acx100.sourceforge.net/wiki/History#Kernel_inclusion>`__ for some background information on the previous attempt to include it in the mainline kernel.

`acx100 <http://acx100.sf.net>`__ was a project started by Andreas Mohr to create a free open source driver for the acx100 chipset from Texas Instruments. Later produced acx111 chipsets, which can be found on PCI, PCMCIA or USB devices, are also supported.

Currently, the driver is working quite reliably, but it does not support WPA encryption and uses a home-grown wireless stack. The main focus of development is now the port to the mac80211 kernel stack. This mac80211 port is still in alpha status, but there have even been some success reports of it working.

supported chips
---------------

-  ACX100 (`TNETW1100 <http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?templateId=6116&navigationId=12147&path=templatedata/cm/product/data/acx100>`__)
-  ACX111 (`TNETW1130 <http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?contentId=4039&navigationId=12305&templateId=6116>`__)
-  `TNETW1450 <http://focus.ti.com/general/docs/bcg/bcgprodcontent.tsp?templateId=6116&navigationId=12147&path=templatedata/cm/product/data/tnetw1450>`__ (USB)

available devices
-----------------

A complete list of devices known to work with acx1xx can he found on `the acx100 wiki <http://acx100.sourceforge.net/wiki/Device_list>`__

*If you put lists here like bcm43xx does it's far easier for people to find out about this driver since it'll be listed on* :doc:`en/users/Devices/PCI <../devices/pci>` *and* :doc:`en/users/Devices/USB <../devices/usb>`\ *.*

features
--------

*TODO*

working
~~~~~~~

::

     * //TODO// 

not working yet
~~~~~~~~~~~~~~~

::

       * //TODO// 

not supported
~~~~~~~~~~~~~

::

         * //TODO// 

device firmware
---------------

All devices require propietary firmware images to work. The `wiki <http://acx100.sourceforge.net/wiki/Firmware>`__ should give you a good point to start on which firmware to choose and where to get it. All currently available firmware versions can be found at http://acx100.erley.org/fw/.

external links
--------------

::

           * [[http://acx100.sf.net/|Main development site]] 
           * [[http://acx100.sourceforge.net/wiki/|Wiki]] 
           * [[http://acx100.git.sourceforge.net/git/gitweb.cgi?p=acx100/acx-mac80211|git tree of mac80211 port]] 
