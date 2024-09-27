Modularizing code
-----------------

This section is dedicated to teaching developers how to modularize code in an acceptable way upstream for Linux wireless. You will modularize code in drivers for configurable options, or in mac80211 and cfg80211 when you want an option to be available as a configurable option. Whether or not you have the feature available as modular or not can depend on the stability, size, or use overall general usage case of the code in question.

The Linux kernel allows us to specify build time options using the .config configuration file. The .config file is generated once a user configures a kernel. The kernel can be configured through several user interface mechanisms but all parse existing kernel configuration options stored in Kconfig files. Kernel configuration file writing can be an art in itself but for simple additions to the kernel it is easy enough to just read existing Kconfig files.

Given that Kconfig files allow us to define the kernel configuration options to modularize the kernel we then need to rely on Kconfig for addition of new build time options. When building the kernel we can either piggy back object data to be linked into the final vmlinux kernel or to a specific module. When objects are specified to be part of the final kernel image they get linked into their respective directory's built-in.o object. Each directory's built-in.o object eventually gets linked together to build the final kernel image. A module gets its own set of defined objects linked together to build it.

One can then modularize the kernel with Kconfig options.

Modularizing only once
----------------------

Some build systems, typically proprietary driver build systems, allows for defining a configuration option under a slew of different names. Fortunately, the Linux kernel does not do this. If you want to enable a kernel configuration option you do this once and through the kernel's configuration build system. For instance, you can only set CONFIG_ATH9K=m by enabling the ath9k module when configuring the Linux kernel. Although this is true for CONFIG_ATH9K the CONFIG_ATH9K_HW however can be selected for you when you either want the ath9k driver or the ath9k_htc driver, both of which make use of the objects defined under CONFIG_ATH9K_HW. This dependency map, however, is hidden from the user and the dependency map then is kept track of by the kernel's configuration build system. The final decisions of the entire kernel configuration is stored in one file, .config and its respective defines are stored in the include/generated/autoconf.h upon build time.

Modularizing Mesh for mac80211
------------------------------

Lets start off with one example and reasons for why a feature is a configurable option for mac80211. The 802.11s support for mac80211 is defined as a build time kernel configuration option. This is found in the *net/mac80211/Makefile* as follows:

::

   mac80211-$(CONFIG_MAC80211_MESH) += \
           mesh.o \
           mesh_pathtbl.o \
           mesh_plink.o \
           mesh_hwmp.o

At build time then we will only link to mac80211 the respective mesh build objects if and only if CONFIG_MAC80211_MESH has been set when configuring the kernel. Now, you will see a lot of #ifdef CONFIG_MAC80211_MESH conditions on a lot of mac80211 C files sprinkled in between routines. This behavior *should* be avoided to help with code legibility. The more ifdefs we have sprinkled in a C routine the less legible the code becomes. Instead modularized code should have routines in place for the ifdef code which allows the routine to do nothing when the option is not enabled on the kernel configuration. An example would be to have a foo.h file:

::

   struct stuff {
      int counter;
   };

   #ifdef CONFIG_FOO
   static int foo_increment(struct stuff *c);
   #else /* CONFIG_FOO */
   static inline static int foo_increment(struct stuff *c)
   {
     return 0;
   }
   #endif

Then the foo.c file can be a build time option:

::

   obj-$(CONFIG_FOO) += foo.o

And foo.c can contain:

::

   #include "foo.h"

   static int foo_increment(struct stuff *c)
   {
      c->counter++;
      if (c->counter > 1000)
        return -1;
      return 0;
   }

With this then code that has CONFIG_FOO() disabled can simply use foo_increment() without any harm to either the eye by placing unnecessary ifdefs or to runtime code.

When do you modularize
----------------------

You may modularize if the code in question may be a feature not desirable for all builds. For mesh this is the case as Mesh is still a draft through Draft 802.11s. Mesh code also has quite a bit of code which embedded Linux distributions can shave off by removing it. You **do not** want to modularize firmware API, so if you have a device which accepts certain number of commands you do not want to have a build time option for reducing or increasing the number of commands available for the firmware. For example, you do not want to do something like this:

::

   enum WMI_CMD {
       CMD_RX,
       CMD_TX,
   #ifdef CONFIG_WMI_EXT
       CMD_PRIVATE_GET_MAGIC
   #endif
   };

You want to keep the magic command and instead simply return -EOPNOTSUPP when the command is issued.
