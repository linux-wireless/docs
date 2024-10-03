Brainstorming for enable Kconfig on compat-wireless
===================================================

Step 1
~~~~~~

Using the existing kernel's config, generate a Kconfig file that contains all the right symbols for that kernel:

::

   cat .config | genkconf.sh > kernel-kconfig

where the script is this:

::

   #!/bin/bash

   while read line ; do
           case "${line:0:7}" in
           "CONFIG_")
                   line="${line:7}"
                   cfg="${line%%=*}"
                   val="${line#*=}"
                   cfgtype="skip"
                   if [ "$val" = "m" ] ; then
                           cfgtype="tristate"
                   elif [ "$val" = "y" ] ; then
                           cfgtype="bool"
                   fi
                   if [ "$cfgtype" != "skip" ] ; then
                           echo "config $cfg"
                           echo "    $cfgtype"
                           echo "    default $val"
                           echo ""
                   fi
                   ;;
           "# CONFI")
                   cfg="${line:9}"
                   cfg="${cfg%% is not set}"
                   echo "config $cfg"
                   echo "    bool"
                   echo "    default n"
                   echo ""
                   ;;
           esac
   done

Step 2
~~~~~~

Collect all Kconfig symbols from compat:

::

   find . -name Kconfig | xargs cat | sed 's/^config //;t;d' > symbols

Step 3
~~~~~~

Instead of patching Makefiles, replaces all CONFIG\_ by CONFIG_COMPAT\_ in all Makefiles:

::

   find . -name Makefile | xargs rpl "CONFIG_" "CONFIG_COMPAT_"

This means that only things that are actually selected in compat will be built.

Step 4
~~~~~~

Replace all "FOO" with "COMPAT_FOO" symbols in Kconfig and code files:

::

   for sym in $(cat symbols) ; do
       find . -name Kconfig |\
           xargs rpl -w "$sym" "COMPAT_$sym"

       find . -name '*.c' -o -name '*.h' |\
           xargs rpl -w "CONFIG_$sym" "CONFIG_COMPAT_$sym"
   done

Step 5
~~~~~~

Build a Kconfig file:

::

   echo 'source "kernel-kconfig"' > Kconfig
   for k in drivers/net/wireless/*/Kconfig ; do echo "source \"$k\"" >> Kconfig ; done

etc. Currently, mac80211/cfg80211/... Kconfig isn't copied. They will need to be copied and potentially modified for dependencies like WEXT.

Step 6
~~~~~~

Run menuconfig:

::

   /lib/modules/$(uname -r)/build/scripts/kconfig/mconf Kconfig

Step 7
~~~~~~

Build the thing.

The generated .config can be parsed with either the existing compat-wireless-2.6/scripts/gen-compat-autoconf.sh script or scripts/kconfig/confdata.c (conf --silentoldconfig). The generated include/linux/compat_autoconf.h is already included as part of the build of compat-wireless.
