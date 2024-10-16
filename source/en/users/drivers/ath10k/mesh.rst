ath10k mesh mode
================

Refer this link for IEEE 802.11s (Mesh Networking) introduction.
https://wireless.wiki.kernel.org/en/developers/Documentation/ieee80211/802.11s

ath10k supports mesh BSS (MBSS) in raw-mode since Sep/2015 (commit id:
b6c7bafa7d4b1398cce93e4af0a48603919fa933) and in native Wi-Fi mode since
Nov/2015 (commit id: bb58b89c5ea1006c93270fd2e667ab72312bf7ab).

Firmware must have “raw-mode” feature flag to use MBSS in raw-mode and
“mfp-support” feature flag to use MBSS with security.

Bring up Mesh Point (MP)
------------------------

There are 2 manners to bring up MP which are using “iw” and “wpa_supplicant”.

iw does MLME in kernelspace while wpa_supplicant does it in userspace.
iw is simple and quick to verify MP working because it doesn't require
any other utilities, but cannot be used for secured mode due to lack of
SAE support.

Contrarily wpa_supplicant may be a bit complex comparing to iw, however
it is good to use with security.

Setup open Mesh Point using iw
------------------------------

In this example we will configure a MP to use an open Mesh network. The
MP will automatically peer with others that are using same configuration
(mesh ID and channel).

Create a new MP interface "mesh0".

::

   iw phy phy0 interface add mesh0 type mp

Confirm that the new interface created as MP.

::

   iw mesh0 info
   Interface mesh0
           type mesh point

Configure channel information.

::

   iw dev mesh0 set freq 5745 80 5775

If you need, you can change interface’s MAC address.

::

   ifconfig mesh0 hw ether $MAC_ADDRESS

Assign an IP and bring up MP.

::

   ifconfig mesh0 192.168.1.10

Join a Mesh network. “mesh-ath10k” is Mesh ID which can be maximum of 32 bytes long.

::

   iw dev mesh0 mesh join mesh-ath10k

Verify peer link status

::

   iw mesh0 station dump
   Station 8c:fd:f0:00:b3:66 (on mesh0)
           inactive time:  30 ms
           rx bytes:       50768
           rx packets:     665
           tx bytes:       1103
           tx packets:     12
           tx retries:     0
           tx failed:      0
           signal:         -11 dBm
           signal avg:     -11 dBm
           Toffset:        25721647444 us
           tx bitrate:     6.0 MBit/s
           rx bitrate:     1170.0 MBit/s VHT-MCS 8 80MHz short GI VHT-NSS 3
           mesh llid:      2393
           mesh plid:      40952
           mesh plink:     ESTAB
           mesh local PS mode:     ACTIVE
           mesh peer PS mode:      ACTIVE
           mesh non-peer PS mode:  ACTIVE
           authorized:     yes
           authenticated:  yes
           preamble:       long
           WMM/WME:        yes
           MFP:            no
           TDLS peer:      no
           connected time: 328 seconds

Setup Mesh Point using wpa_suppliant
------------------------------------

Both of open MP and secured MP can be brought up using wpa_supplicant.
This section will instruct the steps to both of open and secured MP
setup.

Create a new MP interface "mesh0".

::

   iw phy phy0 interface add mesh0 type mp

Assign an IP and bring up MP.

::

   ifconfig mesh0 192.168.1.10

Create a wpa_supplicant.conf file and configure Mesh information.

::

     * ssid: mesh ID
     * mode=5: mesh mode
     * key_mgmt=NONE: open Mesh
     * key_mgmt=SAE: secured Mesh
     * user_mpm=1: MPM on userspace

::

   ctrl_interface=/var/run/wpa_supplicant
   user_mpm=1
   network={
       ssid="mesh-ath10k"
       mode=5
       frequency= 5745
       key_mgmt=NONE 
   }

To configure secured MP, set key_mgmt to SAE and add psk value

::

   …
   key_mgmt=SAE
   psk=”123456789a”
   …

The wpa_supplicant requires the ieee80211w to be set to non-zero value to have secured mesh operating properly if both patches "mac80211: Encrypt "Group addressed privacy" action frames" and "ath10k: fix group privacy action frame decryption for qca4019" are not available.

::

   …
   ieee80211w=1
   …

Run wpa_supplicant

::

   wpa_supplicant -D nl80211 -i mesh0 -c wpa_supplicant.conf –B

Verify peer link status

::

   iw mesh0 station dump
   Station 8c:fd:f0:00:b3:66 (on mesh0)
           inactive time:  120 ms
           rx bytes:       34743
           rx packets:     457
           tx bytes:       958
           tx packets:     11
           tx retries:     0
           tx failed:      0
           signal:         -24 dBm
           signal avg:     -24 dBm
           Toffset:        77320999230 us
           tx bitrate:     6.0 MBit/s
           rx bitrate:     975.0 MBit/s VHT-MCS 7 80MHz short GI VHT-NSS 3
           mesh llid:      0
           mesh plid:      0
           mesh plink:     ESTAB
           mesh local PS mode:     ACTIVE
           mesh peer PS mode:      ACTIVE
           mesh non-peer PS mode:  ACTIVE
           authorized:     yes
           authenticated:  yes
           preamble:       long
           WMM/WME:        yes
           MFP:            no
           TDLS peer:      no
           connected time: 224 seconds
