initvals-tool
=============

The initvals-tool is a userspace application used to:

- Get checksums of the initvals for the ath9k_hw driver
- Get checksums of the initvals for the Atheros HAL initvals
- Reformat initval file output
- Synch the initvals from the Atheros HAL to ath9k_hw format

Current checksums
-----------------

The current set of checksums for the latest updated initvals on the
Linux kernel are available and visible on the `ath9k_hw latest initvals
checksums page
<en/users/Drivers/ath9k_hw/initvals-tool/latest-checksums>`__.

Get the initvals-tool code
--------------------------

There's a git tree::

   git://git.kernel.org/pub/scm/linux/kernel/git/mcgrof/initvals-tool.git

Hardware families supported
---------------------------

These are the hardware families supported:

::

     * ar5008 
     * ar9001 
     * ar9002 
     * ar9003 
     * ar9485 
     * ar9580 

Checksumming initvals
---------------------

Say you want to make some silly patch to the initvals and want to ensure
you haven't broken the initvals. An easy way to verify the initvals keep
their integrity is to compute a checksum of the initval arrays. A
checksum will be computed for every array.

By default the checksums for all arrays for all hardware families will
be computed. You can however specify the specific hardware family you
want checksums for by using the -f flag.

Examples::

   # Get the checksums for all arrays for al hardware families
   ./initvals

   # Only get checksums for the AR9002 family
   ./initvals -f ar9002

   # Only get checksums for the AR9003 2p0 family
   ./initvals -f ar9003-2p0

   # Only get checksums for the AR9003 2p2 family
   ./initvals -f ar9003-2p2

   # Only get the checksums for the AR9485 family
   ./initvals -f ar9485

   # Only get the checksusms for the AR9580 1p0 family
   ./initvals -f ar9580-1p0

Now, suppose you want to make some changes to the AR9003 initvals style,
you would read the documentation below about how to do that and then you
can do something like::

   # First get your old checksums
   ./initvals -f ar9003-2p2 | sha1sum

   # Use your new shiny modified print routine
   ./initvals -w -f ar9003-2p2 > ar9003_initvals.h

   # Only get checksums for the AR9003 family, if you get
   # the same sha1sum then the newly generated initvals
   # contain the same data as the old one
   ./initvals -f ar9003-2p2 | sha1sum

You can also compare the initvals against the Atheros HAL by compiling
with 'make ATHEROS=1' and then checking the checksums against the ath9k
ones::

   # get the ath9k checksums for ar9003
   make clean
   make
   ./initvals -f ar9003-2p2 | sha1sum
   # Now compare against the Atheros HAL
   make clean
   make ATHEROS=1
   ./initvals -f ar9003-2p2 | sha1sum

Each row gets its own set of 8 bits for its checksum computation. We use
a u64 for the full checksum allowing us to use arrays of a max column
size of 8. The Atheros initvals currently only use up to 6 columns so we
only use the first 48 bits of the checksum for now.

Reformat initval style
----------------------

Depending on your OS you may or may not need the initvals in a specific
format. The format can be changed by using this tool to read the
original arrays and output the arrays under a new format.

Examples::

   # Generate all the initvals into one large file
   ./initvals -w

   # Generate the initvals for the AR9002 family only
   ./initvals -w -f ar9002

   # Generate the initvals for the AR9003 family only
   ./initvals -w -f ar9003-2p2

Synch initvals from the Atheros HAL
-----------------------------------

If you are an Atheros employee and want to synchronize changes made on
the HAL onto ath9k you can use the initvals tool to generate a new
initvals header for any specific hardware family. You will just need
access to the Atheros .ini files and then compile this program with
ATHEROS=1 as follows::

   make clean
   make ATHEROS=1

You can then synch up the ath9k initvals by doing::

   # To synch the AR5008 initvals
   ./initvals -w -f ar5008 > ar5008_initvals.h

   # To synch the AR9001 initvals
   ./initvals -w -f ar9001 > ar9001_initvals.h

   # To synch the AR9002 initvals
   ./initvals -w -f ar9002 > ar9002_initvals.h

   # To synch the AR9003 2p0 initvals
   ./initvals -w -f ar9003-2p0 > ar9003_2p0_initvals.h

   # To synch the AR9003 2p2 initvals
   ./initvals -w -f ar9003-2p2 > ar9003_2p2_initvals.h

   # To synch the AR9485 initvals
   ./initvals -w -f ar9485 > ar9485_initvals.h

   # To synch the AR9580 1p0 initvals
   ./initvals -w -f ar9580-1p0 > ar9580_1p0_initvals.h

You can then just cp the files into drivers/net/wireless/ath/ath9k/ and
generate a respective patch for upstream inclusion. Note that initval
changes are expected to have a respective equivalent \*good\* commit log
entry, so please don't simply send initval changes without some sort of
explanation, unless you just cannot find one.
