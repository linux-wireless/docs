wireless-regdb
--------------

wireless-regdb is regulatory database used by Linux.

License
-------

wireless-regdb is licensed under the `ISC license <https://en.wikipedia.org/wiki/ISC_license>`__ and CRDA is licensed under the `copyleft-next <https://raw.github.com/richardfontana/copyleft-next/master/Releases/copyleft-next-0.3.0>`__ license.

The regulatory database
-----------------------

:doc:`CRDA <crda>` requires a regulatory database (:doc:`Web view <database>` or `gitweb <http://git.kernel.org/?p=linux/kernel/git/wens/wireless-regdb.git;a=blob;f=db.txt;hb=HEAD>`__) to be build and maintained. Our hope is that this database can be used by other platforms (open or proprietary), not just Linux. The database is currently unmaintained, but the latest changes can be found in this git tree:

http://git.kernel.org/?p=linux/kernel/git/wens/wireless-regdb.git

::

   git://git.kernel.org/pub/scm/linux/kernel/git/wens/wireless-regdb.git

The regulatory.bin file there is signed with the current maintainer's RSA private key. We keep the RSA public key embedded as part of CRDA which allows us to verify the authorship and integrity of the regulatory database.

Releases of wireless-regdb
--------------------------

You can find official wireless-regdb releases through the `wireless-regdb archive <http://kernel.org/pub/software/network/wireless-regdb/>`__

ASCII file format
-----------------

Below is an example of a country entry for the db.txt regulatory file for EC (Ecuador)

::

   country EC:
           (2400 - 2483.5 @ 40), (1000 mW)
           (5150 - 5250 @ 80), (50 mW), AUTO-BW, DFS
           (5250 - 5350 @ 80), (125 mW), AUTO-BW, DFS
           (5470 - 5725 @ 160), (125 mW), DFS
           (5725 - 5850 @ 80), (1000 mW)

Note that the frequency range (e.g. ``2400-2483.5``) covers the complete used bandwidth, so this definition allows using the 2 GHz channels 1 through 13 as 40 MHz channels. 5 GHz channels of a bandwidth of 80 or 160 MHz can be used if the frequencies used by the channel fit into the specified frequency ranges.

Binary file format
------------------

We define a new custom binary file format for use with CRDA, to have the data available quickly and as compact as possible as well as allowing to distribute the data along with the digital signature (see below) as easily as possible. The file format is defined in the `regdb.h header file <http://git.kernel.org/?p=linux/kernel/git/mcgrof/crda.git;a=blob;f=regdb.h;hb=HEAD>`__.

RSA Digital Signature
---------------------

Integrity of the binary regulatory file is ensured by digitally signing the regulatory data using a private key and embedding the signature into the binary file. When the file is loaded by the regulatory daemon the signature is checked against a list of public keys built into the regulatory daemon binary or by checking against the list of public keys in a preconfigured directory. This process ensures regulatory.bin file authorship and integrity.

Both CRDA and wireless-regdb allows you to build it without RSA key signature checking, if this is something you find useless then do not use them, but we advise against it. The reason RSA digital signature checks are an option and is what is recommend is that regulatory bodies are highly sensitive towards compliance and the current infrastructure we have gives us best effort on our part of doing the best we can to ensure integrity of the files and also gives us a mechanism to use files from trusted parties on-the-fly. Distribution packaging tends to guarantee file integrity upon installation time and from a specific source but it does not give you on-the-fly file integrity checks. Integrity checks are possible through alternate means such as simple CRC checks but you'd then need a list of all allowed CRCs, by using RSA digital signatures you get both file integrity checks for \_any\_ binary built with the private key by checking for the signature -- and while at it you also can get file authorship protection -- all of this while the file is being read for usage in memory. Distributions do not protect against file corruption after the files are in place, for example.

Chen-Yu Tsai is the default trusted party in CRDA if you enable RSA digital signature checks because he is the maintainer of wireless-regdb. CRDA lets you enable multiple trusted parties by letting you add more public keys into CRDA's source code's pubkeys directory or by adding them into a preconfigured system directory for dynamic reading at runtime.

If your distribution requires you to *build* your own regulatory.bin you can add your own public key into CRDA's source code pubkeys directory or at installation time on the system preconfigured pubkeys directory. CRDA will then run using a regulatory.bin built by Chen-Yu Tsai or your distribution's wirelss-regdb package maintainer's key. The benefit of allowing CRDA to trust either Chen-Yu's key or your own distribution is it allows users to upgrade their regulatory.bin using their own distribution's built regulatory.bin, or simply upgrade to using the binary regulatory.bin provided through wireless-regdb or through releases on this web site.

Sending updates to the regulatory database
------------------------------------------

If you find any errors please send them to the `wireless-regdb <http://lists.infradead.org/mailman/listinfo/wireless-regdb>`__\ (subscribers-only) mailing list and the :doc:`linux-wireless mailing list <../mailinglists>`, either as patches to the `db.txt <http://git.kernel.org/?p=linux/kernel/git/wens/wireless-regdb.git;a=blob;f=db.txt;hb=HEAD>`__ file from the `wireless-regdb git tree <http://git.kernel.org/?p=linux/kernel/git/wens/wireless-regdb.git;a=summary>`__, or just tell us what is wrong in plain English.

Patches sent to the wireless-regdb git tree should be addressed as follows:

::

   To: linux-wireless@vger.kernel.org
   Cc: wireless-regdb@lists.infradead.org
   Subject: wireless-regdb: Update regulatory rules for France (FR) on 5GHz

Mailing list for regulatory updates
-----------------------------------

The goal is to make regulatory data for 802.11 Part 15 rules shared between different 802.11 devices. It may be even possible to share the same regulatory database across different operating systems. Either way since data can potentially be shared we have a mailing list dedicated to discussions and review of just regulatory information. Subscribe to it for review or updates.

http://lists.infradead.org/mailman/listinfo/wireless-regdb (subscribers-only)

Please review `these instructions <http://marc.info/?l=linux-wireless&m=128414096127554&w=2>`__ on details of what is expected from you to make modifications to the regulatory database file.

Changing the database file format
---------------------------------

To change the file format you will need to send patches to both crda (start off with regdb.h) and wireless-regdb/dbparse.py. You should send your patch as an RFC on the linux-wireless mailing list and CC both the wireless-regdb and crda maintainers.
