Calibration Information and Board Data
======================================

This page should help clear up how calibration and board data files
work, as well as document any platform weirdnesses / custom board data
files that are required for various platforms.

Overview
^^^^^^^^

The ath10k NICs require calibration data to be supplied in order to
function correctly.

The calibration data includes:

-  Configuration information (MAC address, 2G/5G, 11n capabilities, 11ac capabilities, number of antennas, etc)
-  Regulatory information
-  Calibration information (crystal offset calibration, TX/RX Gain table, spur information, etc)
-  Power table information (band edges, power levels per channel/rate, etc)

Without it, the NIC will likely not function correctly.

There are a few pieces to the puzzle here.

Calibration Data
^^^^^^^^^^^^^^^^

Firstly - there are a number of sources of calibration data.

-  Sometimes it's in OTP (one time programmable ROM.) It's on-chip, there's a small amount of it, and it's one time programmable.
-  Sometimes it's in serial attached EEPROM (highly unlikely, but it indeed is a possibility).
-  Sometimes it's in some section in flash (NOR, NAND) with the rest of the running system.
-  Sometimes (during initial calibration) it's just a file on a filesystem.

The OTP and EEPROM is typically found on discrete NICs. The flash (NOR,
NAND) calibration sections are typically found in access points and
embedded devices, primarily to cut down manufacturing overhead (no need
to program OTP.)

Now, things are also a little more complicated. The calibration data is
typically a few to tens of kilobytes in size; but OTP is definitely not
that big. So starting with AR9380 NICs (which were the first to support
OTP), calibration data can be stored as a delta against a template board
data file.

Board data
^^^^^^^^^^

So, what's board data? When manufacturers make wireless boards, they
start with one of the reference designs from QCA. These reference
designs have a defined set of parts (LNAs, FEMs, power supply behavior,
etc) which they determine "good" values for. Then people typically tweak
things like channel sets, limit maximum transmit power, limit number of
antennas, regulatory domain selection, etc. Most of these parameters
don't have to change - only the board-to-board variation and some
parameters like regulatory domain and maximum transmit power.

So instead of storing the whole calibration data set in each chip, it's
typically a three stage process:

- The calibration data in OTP says "I'm a board of type X!", which the driver can use to find a template board data file to use;
- The driver loads the template board data file and OTP file into firmware;
- The firmware creates a single large calibration data section, and uses that for operation.

Now, some of the methods don't require it. Notably, in-flash calibration
(NOR, NAND) has an entire copy of the calibration data, so the firmware
just consumes all of that. However! The initial boot-up sequence may use
parameters in the board data file to find out some capabilities, so
typically the board data files are still required.

(TODO: go dig into exactly this order and write it out so people understand what's going on.)

Then there's the source of the board data files. In the ath9k world, the
board data files are header files in the driver. That meant that unless
the vendor wanted to change those templates, they'd have to work against
one of the handful of templates that the driver supported. However, in
the ath10k world, the board data files are a file rather than included
in the firmware/driver - so, vendors occasionally will customize board
data files as part of their calibration work. This means that the
default templates that you're using aren't the ones that ship from QCA
and thus your NIC may not work.

Determining calibration and board data sources
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ath10k supports all of the combinations of the above. The challenge is
picking the right calibration data source and when needed, the right
board data source.

In the early days (and in the reference driver), the board data file was
just a binary image containing the board data for that particular board.
For multi-NIC APs, you could have one file per physical interface name.

This meant that if your vendor used a different reference design, or
customized it too much, your base board data (with all the "defaults"
for calibration) isn't going to be right, and the board will behave very
badly.

For later NICs there are plenty of variants of calibration files, so
ath10k supports a multi-file board data file (the board-2.bin) . There's
an open source tool to unpack and repack the board data files -
https://github.com/qca/qca-swiss-army-knife/blob/master/tools/scripts/ath10k/ath10k-bdencoder
. You can use this on a board-2.bin file to see what the matching
strings are for each board data.

So, when the driver starts up, it will:

- Determine which calibration section to check - file, flash, OTP - this is where you can really use you own calibration data in a file.
- Read the board data information out and check board data files
- if a per-NIC board.bin file exists, use that. This is your general "I really want to use my own per-NIC board data file."
- Assemble a search string to search for board data files - typically that includes the BMI ID out of OTP, PCI ID, PCI subdivide ID, etc
- Use the search string(s) to find a suitable calibration file in a board-2.bin file
- If nothing is found, use the global board.bin file
- If that isn't found, abort

Then the driver will feed the calibration data and the OTP data to the
firmware and .. well, magic happens.

What's BMI ID?
''''''''''''''

The BMI ID field showed up later on (Cascade? Dakota?.) It's supposed to
be a field describing which calibration information to use. The firmware
on Dakota also uses it as a magical field to know if the first radio
(which can do 2g or 5g, boot switchable) is using 2G or 5G calibration
data. It's only a 5 bit field though, which means vendors likely won't
add lots of new IDs for their own boards - they'll just ship custom
board data files.

List of NICs, and board data / calibration data hilarity
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(TBD)
