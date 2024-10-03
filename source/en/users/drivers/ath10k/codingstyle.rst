ath10k/ath11k/ath12k Coding Style
=================================

Introduction
~~~~~~~~~~~~

This is the coding style document for :doc:`ath10k <../ath10k>`,
:doc:`ath11k <../ath11k>` and :doc:`ath12k <../ath12k>` drivers. Read
this before writing any code.

Tools
~~~~~

Use latest GCC which you can download from `crosstool
<https://mirrors.edge.kernel.org/pub/tools/crosstool/>`__. Setting it up
is easy, unpack it to a directory and create a GNUmakefile in Linux
sources top-level directory::

   ARCH=x86
   CROSS_COMPILE=/opt/cross/gcc-13.2.0-nolibc/x86_64-linux/bin/x86_64-linux-

   export ARCH
   export CROSS_COMPILE
   include Makefile

You will need `the latest sparse from git
<https://docs.kernel.org/dev-tools/sparse.html#getting-sparse>`__. Linux
distros usually have too old sparse and you will see wrong errors!

Checking code
~~~~~~~~~~~~~

For checking the code we have dedicated scripts for each driver:

-  `ath10k-check <https://github.com/qca/qca-swiss-army-knife/blob/master/tools/scripts/ath10k/ath10k-check>`__
-  `ath11k-check <https://github.com/qca/qca-swiss-army-knife/blob/master/tools/scripts/ath11k/ath11k-check>`__
-  `ath12k-check <https://github.com/qca/qca-swiss-army-knife/blob/master/tools/scripts/ath12k/ath12k-check>`__

They run various tests, including sparse and checkpatch. Run the script
with ``--help`` to see the installation and usage instructions.
``--version`` shows version information for all dependencies, include
that when reporting a problem.

It is required to run the check script before submitting patches as it
can catch common problems. There must not be any warnings!

An example how to run the script::

   ~$ cd ~/ath
   ~/ath$ ls
   arch/    debian/         include/  lib/                               Module.symvers  sound/
   block/   Documentation/  init/     localversion-wireless-testing      net/            tools/
   certs/   drivers/        ipc/      localversion-wireless-testing-ath  README          usr/
   COPYING  firmware/       Kbuild    MAINTAINERS                        samples/        virt/
   CREDITS  fs/             Kconfig   Makefile                           scripts/        vmlinux-gdb.py@
   crypto/  GNUmakefile     kernel/   mm/                                security/
   ~/ath$ ath10k-check
   drivers/net/wireless/ath/ath10k/debug.h:207: return is not a function, parentheses are not required
   drivers/net/wireless/ath/ath10k/debug.h:209: return is not a function, parentheses are not required
   drivers/net/wireless/ath/ath10k/debug.h:210: return is not a function, parentheses are not required
   drivers/net/wireless/ath/ath10k/debug.h:214: Alignment should match open parenthesis
   drivers/net/wireless/ath/ath10k/debug.h:218: Alignment should match open parenthesis
   drivers/net/wireless/ath/ath10k/debug.c:2430: code indent should use tabs where possible
   drivers/net/wireless/ath/ath10k/debug.c:2430: please, no spaces at the start of a line
   drivers/net/wireless/ath/ath10k/debug.c:2431: code indent should use tabs where possible
   drivers/net/wireless/ath/ath10k/debug.c:2431: please, no spaces at the start of a line
   drivers/net/wireless/ath/ath10k/debug.c:2464: code indent should use tabs where possible
   drivers/net/wireless/ath/ath10k/debug.c:2464: please, no spaces at the start of a line
   drivers/net/wireless/ath/ath10k/debug.c:2465: code indent should use tabs where possible
   drivers/net/wireless/ath/ath10k/debug.c:2465: please, no spaces at the start of a line
   drivers/net/wireless/ath/ath10k/debug.c:2493: Please don't use multiple blank lines
   drivers/net/wireless/ath/ath10k/debug.c:2525: Symbolic permissions 'S_IRUSR' are not preferred. Consider using octal permissions '0400'.
   drivers/net/wireless/ath/ath10k/debug.c:2527: Symbolic permissions 'S_IRUSR' are not preferred. Consider using octal permissions '0400'.
   drivers/net/wireless/ath/ath10k/debug.c:2620: Alignment should match open parenthesis
   drivers/net/wireless/ath/ath10k/debug.c:2640: Alignment should match open parenthesis
   ~/ath$

Linux coding style
~~~~~~~~~~~~~~~~~~

ath10k/ath11k/ath12k mostly follows `Linux Coding Style
<https://docs.kernel.org/process/coding-style.html>`__, so read that
first.

Status/error variables
~~~~~~~~~~~~~~~~~~~~~~

Use a variable named "ret" to store return values or status codes. Also
propagate the error code to upper levels.

Example:

.. code-block:: c

   int ret;

   ret = request_firmware(&fw_entry, filename, ar->dev);
   if (ret) {
           ath10k_warn("Failed to request firmware '%s': %d\n",
                       filename, ret);
           return ret;
   }

   return 0;

Name context variables either "ar" or "ar\_<hifname>". Use
ath10k\_<hifname>_priv() to get access to hif specific context.

Examples:

.. code-block:: c

   struct ath10k *ar = ptr;
   struct ath10k_pci *ar_pci = ath10k_pci_priv(ar);

For consistency always use the main context (struct ath10k \*ar) as
function parameter, don't use hif specific context.

Error path
~~~~~~~~~~

Use goto labels err\_<action> for handing error path, with <action>
giving a clear idea what the label does.

Example:

.. code-block:: c

   ret = ath10k_hif_power_on(ar);
   if (ret)
           return ret;

   ret = ath10k_target_start(ar);
   if (ret)
           goto err_power_off;

   ret = ath10k_init_upload(ar);
   if (ret)
           goto err_target_stop;

   return 0;

   err_target_stop:
           ath10k_target_stop(ar);

   err_power_off:
           ath10k_hif_power_off(ar);

   return ret;

Print error codes after a colon:

.. code-block:: c

   ath10k_warn("failed to associate peer STA %pM: %d\n",
               sta->addr, ret);

Try to start the warning messages with the verb "failed" if possible.
Warning and error messages start with lower case.

ath10k_warn() is used for errors where it might be possible to recover
and ath10k_err() for errors when it's not possible to recover in any
way.

Dan Carpenter's post about error paths:
https://staticthinking.wordpress.com/2022/04/28/free-the-last-thing-style/

Locking
~~~~~~~

Always document what spinlock/mutex/rcu actually protects. Locks should
always protect data, not code flow.

Naming
~~~~~~

Name of symbols and functions follow style
<drivername>\_<filename>\_<symbolname>.

Example:

.. code-block:: c

   int ath10k_mac_start(struct ath10k *ar)

For each component use function names create/destroy for allocating and
freeing something, register/unregister for initializing and cleaning up
them afterwards and start/stop to temporarily pause something.

Example:

.. code-block:: c

   int ath10k_cfg80211_create(struct ath10k *ar)
   int ath10k_cfg80211_register(struct ath10k *ar)
   int ath10k_cfg80211_start(struct ath10k *ar)
   void ath10k_cfg80211_stop(struct ath10k *ar)
   int ath10k_cfg80211_unregister(struct ath10k *ar)
   void ath10k_cfg80211_destroy(struct ath10k *ar)

Comments
~~~~~~~~

Multiline comment style is:

.. code-block:: c

   /* Foo
    * Bar
    */

Error messages
~~~~~~~~~~~~~~

For warning and error messages we have ath10k_warn() and ath10k_err().

ath10k_warn() should be used when ath10k still continues to work, for
example then some limit has been reached or an unknown event has been
received. It's also rate limited.

ath10k_err() should be used when a fatal error has been detected and
ath10k will shut itself down, for example during driver initialization
or firmware recover fails. It is NOT rate limited.

Examples:

.. code-block:: c

   ath10k_warn(ar, "failed to submit frame %d: %d\n", frame_index, ret);
   ath10k_err(ar, "failed to wake up the device from sleep: %d\n", ret);

Debug messages
~~~~~~~~~~~~~~

Use ath10k_dbg() or ath10k_dbg_dump().

The format string for ath10k_dbg() should start with debug level
followed by name of the command or event and then parameters. All
lowercase and no commas, colons or periods.

Examples:

.. code-block:: c

   ath10k_dbg(ar, ATH10K_DBG_BOOT, "boot suspend complete\n");

   ath10k_dbg(ar, ATH10K_DBG_WMI, "wmi mgmt tx skb %pK len %d ftype %02x stype %02x\n",
          msdu, skb->len, fc & IEEE80211_FCTL_FTYPE,
          fc & IEEE80211_FCTL_STYPE);

   ath10k_dbg(ar, ATH10K_DBG_MAC, "mac update sta %pM peer bw %d\n",
          sta->addr, bw);

Things NOT to do
~~~~~~~~~~~~~~~~

Don't use void pointers.

Don't use typedef.
