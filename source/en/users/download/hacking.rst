Hacking compat-wireless
-----------------------

This section deals with development details of compat-wireless and the other trees it uses. If you want to make your own compat-wireless tarballs, or if you see something busted with compat-wireless or just want to add something new or an enhancement this is the guide for you.

Git trees you will need
-----------------------

compat-wireless backports both the bluetooth and 802.11 subsystems down to older kernels. To be able to synchronize backporting the latest and greatest the linux-next.git tree is used as its main source for kernel updates. General Linux kernel compatibility is addressed through a general kernel compatibility tree, compat.git. compat-wireless then has its own tree for specific wireless compatibility. You will then need to checkout three trees to start hacking on compat-wireless:

::

   git://git.kernel.org/pub/scm/linux/kernel/git/next/linux-next.git
   git://github.com/mcgrof/compat.git
   git://github.com/mcgrof/compat-wireless.git

Linux next
~~~~~~~~~~

The linux-next.git tree brings all subsystems being worked on for the next kernel release into one tree. So if the current rc kernel is 2.6.33-rc5, this means linux-next will have what people today are working on for the 2.6.34 kernel release.

compat.git
~~~~~~~~~~

The compat git tree is a general kernel compatibility layer which can be shared amongst different compatibility projects, or drivers. compat-wireless is just one of the kernel compatibility projects using compat.git. compat.git builds a general compatibility module, compat, and any additional modules to let you get new general kernel updates from future kernels on your old kernels.

compat.git modules
^^^^^^^^^^^^^^^^^^

compat.git provides a few modules and headers to help with general kernel compatibility.

compat
''''''

Provides all exported symbols implemented in each respective kernel compat-2.6.xy.c files. Upon module load it just initializes the Linux kernel's *power management Quality Of Service* (aka **pm-qos**) Interface interface added as of the 2.6.24 kernel. No other things are initialized, the rest of the compat module just acts as a library of exported symbols.

compat_firmware_class
'''''''''''''''''''''

Another module which compat.git provides is a backport of the firmware_class module which got updated recently newer with a new request_firmware_nowait() to allow better asynchronous firmware uploading. This was added as of the 2.6.33 kernel. The firmware_class module has been backported into a new module called compat_firmware_class. A separate module has been defined instead of a direct replacement for firmware_class since your system may have old drivers which use the old request_firmware_nowait() and would bust if they used the new request_firmware_nowait(). The compat_firmware_class module registers its own sysfs subsystem and as such also gets udev events sent through a separate subsystem. Because of this a new udev rules file is required and provided.

compat-wireless.git
~~~~~~~~~~~~~~~~~~~

Anything that is not general kernel compatibility but instead specific to 802.11 or bluetooth goes into compat-wireless.git. After you've cloned all three trees, linux-next.git, compat.git and compat-wireless.git you need to change into the compat-wireless directory and tell compat-wireless where you linux-next and compat.git trees are. You do this with environment variables GIT_TREE and GIT_COMPAT_TREE. You can do for example:

::

   export GIT_TREE=/home/user/wireless-testing/
   export GIT_COMPAT_TREE=/home/users/compat.git/

Then you can update your local sources based on these linux-next.git and compat.git trees:

::

   scripts/admin-clean.sh   - Cleans the compat-wireless-2.6 tree
   scripts/admin-update.sh  - Updates compat-wireless-2.6 with your git tree
   scripts/admin-refresh.sh - Does the above two

Adding new drivers
^^^^^^^^^^^^^^^^^^

Most new drivers are enabled for compilation. If see a driver you would like enabled try it into the mix, test them and if they work enable them and send the respective patches.

Generating stable releases
--------------------------

You can make stable releases yourself by checking out the specific branch for the target stable kernel release you want on each git tree:

-  linux-2.6-allstable.git
-  compat-wireless.git
-  compat.git You will also want an updated linux-next.git, you want to ensure that the tag for the target kernel you want is present if you want to cherry pick out stable patches from it. So for example if 2.6.38 was released you want to ensure the linux-next.git tree you have is updated with the v2.6.38 tag.

Now, for example if you wanted to make a 2.6.38.y stable release, you would do:

::

   # On linux-next.git:
   mcgrof@tux ~/linux-next (git::master)$ git fetch
   remote: Counting objects: 43056, done.
   ... etc ...
   mcgrof@tux ~/linux-next (git::master)$ git reset --hard origin
   HEAD is now at 74bdbee Add linux-next specific files for 20110329
   # Now get kernel extraversions on linux-next.git, this allows you
   # to extract stable patches from linux-next.git when the linux-2.6-allstable
   # tree moves to a new extraversion release.
   mcgrof@tux ~/linux-next (git::master)$ git fetch  /home/mcgrof/linux-2.6-allstable/.git/
   mcgrof@tux ~/linux-next (git::master)$ git fetch -t /home/mcgrof/linux-2.6-allstable/.git/


   # For compat-wireless.git:
   mcgrof@tux ~/devel/compat-wireless-2.6 (git::master)$ git checkout -b linux-2.6.38.y origin/linux-2.6.38.y
   Branch linux-2.6.38.y set up to track remote branch linux-2.6.38.y from origin.
   Switched to a new branch 'linux-2.6.38.y'
   mcgrof@tux ~/devel/compat-wireless-2.6 (git::linux-2.6.38.y)$

   # For compat.git:
   mcgrof@tux ~/compat (git::master)$ git checkout -b linux-2.6.38.y origin/linux-2.6.38.y
   Branch linux-2.6.38.y set up to track remote branch linux-2.6.38.y from origin.
   Switched to a new branch 'linux-2.6.38.y'
   mcgrof@tux ~/compat (git::linux-2.6.38.y)$ 

   # For linux-2.6-allstable.git:
   mcgrof@tux ~/linux-2.6-allstable (git::master)$ git checkout -b linux-2.6.38.y origin/linux-2.6.38.y
   Branch linux-2.6.38.y set up to track remote branch linux-2.6.38.y from origin.
   Switched to a new branch 'linux-2.6.38.y'

Once you have the appropriate branches checked out, you can use a script designed to let you make a release:

::

   # First tell compat-wireless scripts your target GIT_TREE
   # from where you want to suck out code from is the stable tree:
   mcgrof@tux ~/devel/compat-wireless-2.6 (git::linux-2.6.38.y)$ export GIT_TREE=/home/mcgrof/linux-2.6-allstable/

   # Then generate a stable release:
   mcgrof@tux ~/devel/compat-wireless-2.6 (git::linux-2.6.38.y)$ ./scripts/gen-stable-release.sh -n -s
   Skipping linux-2.6-allstable git tree update checks for branch: linux-2.6.38.y
   On linux-2.6-allstable: linux-2.6.38.y
   You said to use git tree at: /home/mcgrof/linux-2.6-allstable for linux-next
   Copying /home/mcgrof/linux-2.6-allstable/include/linux/ieee80211.h
   Copying /home/mcgrof/linux-2.6-allstable/include/linux/ieee80211.h
   Copying /home/mcgrof/linux-2.6-allstable/include/linux/nl80211.h
   Copying /home/mcgrof/linux-2.6-allstable/include/linux/pci_ids.h
   ...
   Creating compat-wireless-2.6.38-3-ns.tar.bz2 ...

   Compat-wireles release: compat-wireless-2.6.38-3-ns
   Size: 3.9M      compat-wireless-2.6.38-3-ns.tar.bz2
   sha1sum: b0ca93dbda466b22ed76a8e4792c89931090d7b3  compat-wireless-2.6.38-3-ns.tar.bz2

   Release: /tmp/staging/compat-wireless/compat-wireless-2.6.38-3-ns.tar.bz2

Note that if you supplied the -s flag you will want to review the output for the place where it generates the pending-stable patches. If the respective target upstream tag was not found on linux-next.git it will tell you.

If you want to add additional non-upstream patches you can use the crap/ directory and use the -c flag as well. When people review your tarball they can then find your delta easily. If you submit patches upstream you can stuff them into linux-next-pending/ and use -p. If your patch is upstream on linux-next.git you can cherry pick it out and stuff it into linux-next-cherry-picks/ and use -n. The purpose of all this effort is to enable customizations but to also allow reviewers to quickly find deltas and ensure code gets upstream properly. Check each respective directory README for a review of the directories intent and content.

Sending patches
---------------

compat and compat-wireless contributions follow the contribution model implemented by the Linux kernel. Patches or pull requests for compat and compat-wireless must have be signed-offed. If you don't sign off on them they will not accepted. This means adding a line that says "Signed-off-by: Name <email>" at the end of each commit, indicating that you wrote the code and have the right to pass it on as an open source patch. For exact definition of what the Signed-off-by tag is you can read the definition of the "Developer's Certificate of Origin 1.1", which you can read here:

http://gerrit.googlecode.com/svn/documentation/2.0/user-signedoffby.html

Remember there are three trees. linux-next itself is a conglomeration of kernel git trees itself, so patches for linux-next.git should be sent to each respective subsystem for which the patches are targeted for. So for example for 802.11 you will want to send them to John Linville and cc linux-wireless, for further guidelines on this see the :doc:`Submitting Patches guidelines for 802.11 <../../developers/documentation/submittingpatches>`. As another example, for bluetooth you will want to send them to Marcel Holtmann and cc the linux-bluetooth mailing list. If your patch touches on others areas of the kernel refer to the MAINTAINERS file on the kernel.

For compat.git and compat-wireless.git please send patches against to:

::

   To: Luis R. Rodriguez <mcgrof@kernel.org>
   CC: lf_driver_backport@lists.linux-foundation.org, linux-wireless@vger.kernel.org, linux-bluetooth@vger.kernel.org
   Subject: [PATCH] compat-2.6: fix foo

To post to the lf_driver_backport list you need to subscribe:

http://lists.linux-foundation.org/mailman/listinfo/lf_driver_backport

For patches for compat.git please use a subject like the following:

::

   Subject: [PATCH] compat: fix foo

For compat-wireless.git please use a subject like the following:

::

   Subject: [PATCH] compat-wireless: fix foo

Patches are preferred sent with a clear commit log entry, if unfamiliar with how to send patches please refer to :doc:`our git guide <../../developers/documentation/git-guide>`.

TODO
----

::

     * Dialog (make menuconfig) option for this package -- [[en/users/Download/hacking/config-brainstorming|/config-brainstorming]] 

Administrative
--------------

The way compat-wireless releases are made, where they are kept are detailed in the :doc:`compat-wireless admin page <admin>`.
