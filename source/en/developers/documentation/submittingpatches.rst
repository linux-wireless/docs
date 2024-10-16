Submitting Patches
==================

This guide is designed to give you an idea of how to write patches for
the Linux wireless (Wi-Fi) subsystem. Before reading this guide, read
`the kernel submitting patches guide
<https://docs.kernel.org/process/submitting-patches.html>`__.

Subscribe to this page
----------------------

We would like to ask Linux-wireless developers to subscribe to this page
on the wiki. Any new policies and best practices on patching to
linux-wireless will be posted here.

Prior to sending patches
------------------------

Please **DO NOT** PGP sign patches sent to public lists. The reason is
that signing patches will encapsulate them into MIME and thereby mangle
the patch. Also, please note that we prefer patches inline rather than
attachments. And no HTML mail, our lists reject those automatically.

And carefully read `our email etiquette
<http://www.infradead.org/~dwmw2/email.html>`__, that saves everyone's
time.

Who to address
--------------

Send mac80211, cfg80211 and mac80211_hwsim patches as follows::

   To: Johannes Berg <johannes@sipsolutions.net>
   CC: linux-wireless@vger.kernel.org, Other Developers

For wireless drivers patches (except mac80211_hwsim) send patches as::

   To: linux-wireless@vger.kernel.org
   Cc: Driver maintainers, Other Developers

Where :doc:`Maintainers <../maintainers>` contains the list of
maintainers and mailing lists for the piece of code you are patching.
*Other Developers* in this case can be a list of developers (or mailing
lists) who you think may like to review this patch or who changed the
code you are working on recently.

Do note that drivers might have special requirements, the best is to
check them from the corresponding wiki page. Here's a list for a few of
them:

-  :doc:`ath10k <../../users/drivers/ath10k/submittingpatches>`
-  :doc:`ath11k <../../users/drivers/ath11k/submittingpatches>`
-  :doc:`ath12k <../../users/drivers/ath11k/submittingpatches>`

Checking state of patches from patchwork
----------------------------------------

All wireless patches are tracked in `linux-wireless patchwork project
<https://patchwork.kernel.org/project/linux-wireless/list/>`__. From
patchwork you can check the state of the patch and to whom it is
assigned. Here's a quick link to see all the patches, no matter what's
the state:

* https://patchwork.kernel.org/project/linux-wireless/list/?state=*

Always avoid contacting maintainers directly, they get way too much
email already. Instead use the link above to find your patch and see the
status. Only in last resort contact the maintainers, and do that by
replying to your own patch and ask for status. Do not top post!

Different patchwork states and their meanings:

- **New**: No action haven't taken yet, expect maybe assigned to a
  correct maintainer.
- **Under Review**: The maintainer is waiting review comments from
  others.
- **Accepted**: The maintainer has applied the patch to his/her tree.
- **Rejected**: The maintainer rejected the patch, reasons stated in an
  email.
- **Changes Requested**: Either the maintainer or a reviewer requested
  changes in the patch. The maintainer expects the patch author to
  submit a new version.
- **Deferred**: The maintainer has postponed the review of the patch for
  some reason, for example due to lack of time, patch being to
  controversial or something else. Patch author doesn't need to take any
  action, the maintainer will revisit the patch in a later time.
- **Awaiting Upstream**: The patch depends on an another patch from a
  different tree, for example a wireless driver needing a specific
  mac80211 patch to implement a new feature.
- **RFC**: The patch is sent as Request For Comments. The maintainer
  expects the patch author to submit a new version.
- **Superseded**: There's a new version of the patch available, the
  maintainer has skipped this version.
- **Not Applicable**: The patch is either not part of wireless subsystem
  or it will be applied via different trees (for example net-next or
  driver maintainer trees). The patch is considered as dropped from now
  on and needs to be resubmitted for the maintainer to reconsider it.

Subject
-------

If what you are sending is a patch you should use a subject as follows::

   [PATCH] wifi: subsystem: fix foo and optimize bar

Starting from 2022 we prefix all wireless patch titles with "wifi: ".

In case of wireless patches the subsystem can for example be
``mac80211``, ``cfg80211`` or the name of the driver, for example
``ath9k``. There's an easy way to check with git what prefix you should
use::

   $ git log --oneline --no-merges -10 drivers/net/wireless/ath/ath9k/ar9003_mac.c
   8b537686a116 ath9k: add TPC capability to TX descriptor path
   315dd1149b60 ath9k: fix getting tx duration for dynack
   36678b2b67d7 ath9k: add duration field to ath_tx_status
   3ae351abf15f ath9k: set up tx power into the MRR
   6a4d05dc0c01 ath9k: move ath9k_debug_sync_cause out of ath9k_hw
   e45e91d8812c ath9k: add support for reporting per-chain signal strength
   009af8fb69c9 ath9k: Identify first subframe in an A-MPDU
   ab2761033576 ath9k: remove useless flag conversation.
   ff9bd2d8d95a ath9k_hw: Handle AR_INTR_SYNC_HOST1_(FATAL|PERR) on AR9003
   a4a2954ff49e ath9k_hw: Add AR9565 HW support

If your patch is just a proposal you can mark the patch as RFC in the subject::

   [RFC] wifi: subsystem: add a new way to do foo

If you need to make changes to the patch add a version number inside the brackets::

   [PATCH v2] wifi: subsystem: fix foo and optimize bar
   [PATCH v3] wifi: subsystem: fix foo and optimize bar
   [PATCH v4] wifi: subsystem: fix foo and optimize bar

**Always** increase the version number, no matter how small the change
is. The maintainers focus on the latest version and ignore the older
versions. Make sure that the maintainers don't need to guess what
version he should take, that just creates problems.

Then sending a new version of the patch **always** add a change log,
either after the ``---`` line (three dashes) or in the cover letter.

If a patch in a bigger patchset changes resubmit the whole patchset,
even the patches which have not changes. The maintainers look at
patchsets as a complete unit, usually they do not want to take patches
individually from a patchset.

Subject lines, like commit messages (see below) should be written in
imperative voice ("fix foo and optimize bar"), not in any other way such
as past tense ("fixed foo and optimized bar").

Commit Messages
---------------

Please write commit messages, like mentioned for the subject above, in
imperative voice.

Commit messages should describe

-  why a change was made,
-  how it achieves its stated goal, and,
-  if applicable, other considerations such as

   -  alternatives that were considered,
   -  implications on other code,
   -  possible security implications,
   -  etc.

If you find yourself listing out a number of changes in the commit
message as a bulleted list or similar, consider splitting up the patch
into discrete changes that each do one thing. Similarly, if one of the
additional considerations is refactoring, try to shift that into a
separate patch.

Tree labels
-----------

Labeling patches with what tree the patch should go to helps maintainers
to prioritise and sort patches and avoids unnecessary emails, which
saves everyone time and speeds up patch review. Here are some tips how
to label wireless patches.

If you want to target your patch to a specific release (for example that
the patch should go -rc release not -next) you can inform the maintainer
by adding the release number inside the PATCH brackets::

   [PATCH 4.20] wifi: subsystem: fix foo

If you want to make it clear to the maintainer that the patch should NOT
go to -rc release but to -next instead you can add "-next" to PATCH
brackets::

   [PATCH -next] wifi: subsystem: fix foo

Alternatively you can specify the exact tree you are targetting by
adding the name of the git tree inside PATCH brackets::

   [PATCH wireless] wifi: mac80211: fix foo
   [PATCH wireless-next] wifi: mac80211: implement very-cool-feature
   [PATCH wireless] wifi: ath10k: fix foo
   [PATCH wireless-next] wifi: ath10k: implement awesome-feature

Sending large patches or multiple patches
-----------------------------------------

You should only send a large patch if your patch does one specific task,
or a few of them if they are easy to review. If your work consists of
multiple tasks you must split your tasks into separate patches. Each
patch must address a small set of tasks to help the maintainers with
revision. The rule of thumb here is if you read your patch and if its
not clear what the patch is doing then better break it down into
separate patches. Patches should also be run through
``scripts/checkpatch.pl``.

If you are sending multiple patches which depend on each other you can
use this format for the subjects::

   [PATCH 0/4] wifi: driver_name: introduce foo and bar
   [PATCH 1/4] wifi: driver_name: introduce get_foo_bars()
   [PATCH 2/4] wifi: driver_name: fix locking on bar_by_foo()
   [PATCH 3/4] wifi: driver_name: use foo when barring
   [PATCH 4/4] wifi: driver_name: optimize bar at init time

On the e-mail with subject, ``[PATCH 0/4] wifi: driver_name: introduce
foo and bar``, you would give a brief overview of all the changes. No
patch should be included in that e-mail, and as that e-mail will not end
up in the change logs it should not contain anything that should be
archived, only a rough overview over the purpose of the patch set, no
in-depth description which should be in the changelog for each patch.

Format of patches
-----------------

We prefer patches to be inline-text at the end of the body of the
e-mail. It's strongly recommended to use git-format-patch and
git-send-email tools to submit patches as they use the correct format
automatically. Additionally note that we prefer to apply patches with
git-am (using the -p1 diff format). A header as follows is then
acceptable::

   diff --git a/include/net/mac80211.h b/include/net/mac80211.h
   index 9b4b4a2..4832e6a 100644
   --- a/include/net/mac80211.h
   +++ b/include/net/mac80211.h

Patch tags
----------

In order to track who worked on a patch and released the source code
under the appropriate licenses used, patch tags are used to track of
provenance of patches. This also helps developers review who was in the
line of a patch work, who submitted it, and who reviewed it. This
information is available from the *git-log*. We currently use,
*Signed-off-by*, *Acked-by*, *Cc*, *Reviewed-by* and *Tested-by*.

Please note that since you are submitting patches inline, after the
*Signed-off-by:* lines, you **must** put ``---``, that is three dashes.
Example::

   ...
   Signed-off-by: Luis R. Rodriguez <mcgrof@example.com>
   ---
    include/net/ieee80211_regdomains.h |  196 ++++++++
   ...

Please also read the `official Linux SubmittingPatches
<https://www.kernel.org/doc/html/latest/process/submitting-patches.html>`__
documentation, especially the `Developer's Certificate of Origin
<https://www.kernel.org/doc/html/latest/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin>`__.
Do not submit patches unless you have read, understood and agreed to the
certificate.

New driver
----------

For submitting a new wireless driver the requirements are:

-  follow `Linux kernel coding style <https://www.kernel.org/doc/html/latest/process/coding-style.html>`__
-  use `SPDX tags <https://www.kernel.org/doc/html/latest/process/license-rules.html>`__
-  use either cfg80211 or mac80211, depending on the firmware architecture (no custom 802.11 stack in the driver)
-  have firmware images submitted for `linux-firmware <https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/>`__ with an acceptable license allowing redistribution
-  document Device Tree usage in `devicetree bindings <https://www.kernel.org/doc/html/latest/devicetree/bindings/submitting-patches.html>`__ and review them with DT maintainers
-  in the commit log/cover letter provide an overview of the driver

   -  what hardware the driver supports
   -  what features are supported (client, AP, mesh modes etc)

-  for review submit the driver as one file per patch, to make it easier for the reviewers

   -  example: https://lore.kernel.org/linux-wireless/20200623110000.31559-1-ajay.kathat@microchip.com/

-  final commit (after the review) will be one big patch

   -  for staging drivers the final patch will be just a small patch moving the driver, example: https://git.kernel.org/linus/5625f965d764

There's also a list of `preferred licenses <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/LICENSES/preferred>`__ available.

Some guidelines to speed up new driver review:

-  keep the driver small and simple, more features can be added after the driver is accepted upstream
-  use clean understandable code
-  use generic kernel frameworks instead of reinventing the wheel
-  use generic user space interfaces

   -  no driver specific user interfaces or hacks
   -  no .ini style driver configuration files

-  avoid using debugfs or nl80211 vendor interfaces

Examples of a patches
---------------------

Below are a few examples of a patches. Only the header is provided for long patches.

-  Single patch

.. code-block:: eml

   From: Michael Buesch
   To: John Linville
   Cc: linux-wireless, Bcm43xx-dev, Larry Finger
   Subject: [PATCH] wifi: b43: Remove the "radio hw enabled" message on startup.

   This message is useless. Only report state changes.

   Signed-off-by: Michael Buesch <mb@example.com>
   Cc: Larry Finger <larry.finger@example.com>

   ---

   Index: wireless-dev/drivers/net/wireless/b43/main.c
   ===================================================================
   --- wireless-dev.orig/drivers/net/wireless/b43/main.c   2007-09-20 19:39:06.000000000 +0200
   +++ wireless-dev/drivers/net/wireless/b43/main.c        2007-09-20 20:06:24.000000000 +0200
   @@ -2227,9 +2227,6 @@ static int b43_chip_init(struct b43_wlde
          if (err)
                  goto err_gpio_cleanup;
          b43_radio_turn_on(dev);
   -       dev->radio_hw_enable = b43_is_hw_radio_enabled(dev);
   -       b43dbg(dev->wl, "Radio %s by hardware\n",
   -              dev->radio_hw_enable ? "enabled" : "disabled");

          b43_write16(dev, 0x03E6, 0x0000);
          err = b43_phy_init(dev);
   @@ -3251,6 +3248,9 @@ static void setup_struct_wldev_for_init(
    {
          /* Flags */
          dev->reg124_set_0x4 = 0;
   +       /* Assume the radio is enabled. If it's not enabled, the state will
   +        * immediately get fixed on the first periodic work run. */
   +       dev->radio_hw_enable = 1;

          /* Stats */
          memset(&dev->stats, 0, sizeof(dev->stats));
   -

::

     * Multiple patches 

::

   From: Luis R. Rodriguez
   To: John Linville
   Cc: linux-wireless, Michael Wu, Johannes Berg, Daniel Drake, Larry Finger
   Subject: [PATCH 3/5] wifi: add IEEE-802.11 regualtory domain module

   This adds the regulatory domain module. It provides a way to
   allocate and construct a regulatory domain based on the current
   map. This module provides no enforcement, it just does the actual
   building of the regdomain and returns it as defined in ieee80211_regdomains.h

   This module depends on the ISO3166-1 module.

   Signed-off-by: Luis R. Rodriguez <mcgrof@example.com>

   ---
    include/net/ieee80211_regdomains.h |  196 ++++++++
    net/wireless/Kconfig               |   16 +
    net/wireless/Makefile              |    1 +
    net/wireless/reg_common.h          |  138 ++++++
    net/wireless/regdomains.c          |  751 ++++++++++++++++++++++++++++++
    net/wireless/regulatory_map.h      |  887 ++++++++++++++++++++++++++++++++++++
    6 files changed, 1989 insertions(+), 0 deletions(-)
    create mode 100644 include/net/ieee80211_regdomains.h
    create mode 100644 net/wireless/reg_common.h
    create mode 100644 net/wireless/regdomains.c
    create mode 100644 net/wireless/regulatory_map.h

   diff --git a/include/net/ieee80211_regdomains.h b/include/net/ieee80211_regdomains.h
   new file mode 100644
   index 0000000..adf4de4
   --- /dev/null
   +++ b/include/net/ieee80211_regdomains.h
   @@ -0,0 +1,196 @@
   +#ifndef _IEEE80211_REGDOMAIN_H
   +#define _IEEE80211_REGDOMAIN_H
   +/*
   ... ETC ...

Frequent problems in patch submissions
--------------------------------------

Patch version missing
~~~~~~~~~~~~~~~~~~~~~

If you send a new version of the patch or patchset you should always add
a version number. The first version does not need to be shown but
starting from second version the version number must be available::

   [PATCH] wifi: ath10k: fix DMA allocation
   [PATCH v2] wifi: ath10k: fix DMA allocation
   [PATCH v3] wifi: ath10k: fix DMA allocation
   ...
   [PATCH v11] wifi: ath10k: fix DMA allocation

You can add the version with switch ``--subject-prefix``::

   git format-patch --subject-prefix="PATCH v2"

Changelog missing
~~~~~~~~~~~~~~~~~

When sending a new version of a patch or patchset you should **always**
add a changelog so that maintainer can easily see what has changed.

If you have just one patch you can add the changelog after the ``---``
(three dashes) line.

If you have multiples patches (called a patchset) add the changelog to
the cover letter. You can create the cover letter with the switch
``--cover-letter``::

   git format-patch --subject-prefix="PATCH v2" --cover-letter

Signed-off-by missing
~~~~~~~~~~~~~~~~~~~~~

Read `Developer's Certificate of Origin
<https://www.kernel.org/doc/html/latest/process/submitting-patches.html#sign-your-work-the-developer-s-certificate-of-origin>`__.
Do not submit patches unless you have read, understood and agreed to the
certificate.

Format issues
~~~~~~~~~~~~~

Patch is somehow whitespace damaged, for example tabs converted to
spaces, extra new lines or other modifications which prevent applying
the patch without manual fixing. Or the mail is in HTML format which
most of the mailing lists even block silently.

The best way to avoid all formatting issues is to use `git send-email
<https://www.kernel.org/pub/software/scm/git/docs/git-send-email.html>`__.
See :doc:`linux-wireless git guide <git-guide>` for more information.

Fixes line is incorrect
~~~~~~~~~~~~~~~~~~~~~~~

The correct format for the commit references in Fixes line is the 12
initial digits of the SHA1_ID of the commit, followed by a space,
followed by the commit log message header line text enclosed in
parentheses and double quotes with no line breaks whatsoever. The fixes
lines must be placed just above the signed-off-by lines.

Example::

   Fixes: c742e623e941 ("mwifiex: sdio card reset enhancement")

Here's how one can configure git to provide the fixes tag in correct format::

   $ git config --global --add alias.fixes 'show -q --format=fixes'
   $ git config --global --add pretty.fixes 'Fixes: %h ("%s")'
   $ git config --global --add core.abbrev 12
   $ git fixes ba9177fcef21
   Fixes: ba9177fcef21 ("ath11k: Add basic WoW functionalities")

Commit reference is wrong
~~~~~~~~~~~~~~~~~~~~~~~~~

The correct format for the commit references in commit logs is to start
with the string "commit", followed by a space, followed 12 initial
digits of the SHA1_ID of the commit, followed by a space and followed by
the commit log message header line text enclosed in parentheses.

Example::

   commit f99a6abe59e096cc2c753e667c19f22022e3bef4
   Author: Sara Sharon <sara.sharon@intel.com>
   Date:   Sun Mar 5 18:35:02 2017 +0200

       iwlwifi: mvm: memset binding before setting values
       
       The changes in commit 9415af7f306b ("iwlwifi: mvm: support new binding
       API") assigned values that were later memset to 0.  Move the memset
       earlier.
       
       Fixes: 9415af7f306b ("iwlwifi: mvm: support new binding API")
       Signed-off-by: Sara Sharon <sara.sharon@intel.com>
       Signed-off-by: Luca Coelho <luciano.coelho@intel.com>

Commit title is wrong
~~~~~~~~~~~~~~~~~~~~~

The correct format for the commit title is name of driver, followed by a
colon, followed by a space and then followed by the actual title. Also
the title should be informative and unique, so something like "fix a
bug" is not a good title.

In 2022 we started using "wifi: " in front of all wireless patches.

For examples uou can use ``git log`` to check older commits and see what
prefix was used::

   $ git log --oneline --follow --no-merges -20 drivers/net/wireless/marvell/mwifiex/11ac.c
   277b024e5e3d mwifiex: move under marvell vendor directory
   65da33f5557f mwifiex: update Copyright to 2014
   cf831ffe4473 mwifiex: fix IE parsing issues
   d51246481c7f mwifiex: save and copy AP's VHT capability info correctly
   5f6d5983394f mwifiex: add VHT support for TDLS
   9ed230bcbab7 mwifiex: pass ieee80211_vht_cap to mwifiex_fill_vht_cap_tlv
   406d702b47a2 mwifiex: improve readability in 11ac mcsmap to maxrate conversion
   89467d8ca21b mwifiex: make 11ac mcs rate tables global and const
   7abf4129e6df mwifiex: make use of IEEE80211_VHT_MCS_NOT_SUPPORTED
   0648f3a4b0e9 mwifiex: correct bss_mode check while appending vht operation IE
   2b6254dacfe6 mwifiex: use separate AMPDU tx/rx window sizes in 11ac networks
   83c78da983d6 mwifiex: add support to configure VHT for AP mode
   a5f390562a37 mwifiex: add 802.11AC support

Too many patches
~~~~~~~~~~~~~~~~

The recommend size is 10-12 patches per patchset. More than that it gets
difficult for reviewers and maintainers. Of course there's no hard rule,
for simple patches more than that might be ok but then again for more
complex patches even 10 patches per patchset might be too much.

Resubmit the whole patchset
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Even if just one patch has changed in a patch series resubmit the whole
patchset (and remember to increase the version number), do not just
resubmit that one changed patch. The reason is that it's difficult to
apply patches in correct order when some of them are submitted
separately.

Commit log does not answer "Why?"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The commit log should *always* answer the question "Why?" and describe
the reason what motivated to implement the patch. This is the most
important part of the commit log as this helps maintainers, backports,
distros etc to make decisions if the patch is important for them or not
and to what release it should go.

The commit log needs to tell why you wrote the patch. If you fixed a bug
give a short summary of the bug (can be a long one as well, of course)
from user's point of view, and if there's a publically available bug
report include a link to that. If you are fixing a warning from a
compiler or a static checker add the warning from tool. Or if it's just
code cleanup or fixing a theoretical issue, and does not have practical
user visible changes, mention that also.

Do not top post and edit your quotes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Top posting makes following email threads hard to follow and also it
makes use of patchwork more difficult, which gets the maintainers grumpy
as you are making their work more difficult. So do not top post and
instead edit your quotes properly.

::

   A: Because it messes up the order in which people normally read text.
   Q: Why is top-posting such a bad thing?
   A: Top-posting.
   Q: What is the most annoying thing in e-mail?

   A: No.
   Q: Should I include quotations after my reply?

More info: http://www.idallen.com/topposting.html

Do not send HTML mail
~~~~~~~~~~~~~~~~~~~~~

linux-wireless mailing list drops all mail using HTML, so don't use it.

Use RFC or RFT for patches not ready
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If the patches are not yet ready to be applied by the maintainer, mark
them as RFC (Request For Comments) or RFT (Request For Test) in the
subject. This way the maintainer can easily see that the patch should
not be applied yet and saves maintainer's time.

Examples::

   [PATCH RFC] wifi: ath11k: enable power save mode always
   [PATCH RFT] wifi: ath10k: sdio: always use DMA transfers

Use Co-developed-by when multiple authors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When a patch has multiple authors you should use Co-developed-by tag:

https://www.kernel.org/doc/html/latest/process/submitting-patches.html#when-to-use-acked-by-cc-and-co-developed-by

Maximum of 7-12 patches per patchset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want your patches reviewed smoothly submit maximum of 7-12
patches per patchset. If the patches are bigger don't send more than 7
patches. But if they smaller, or trivial patches, 12 patches is ok. But
anything more than 12 patches and you will get reviewers grumpy (read:
it takes longer to get your patches reviewed and applied).

But you can submit multiple patchsets, just try to throttle it down to
avoid bufferbloat in patchwork, for example you can send a new patchset
every other day. And don't forget to document the dependencies in the
cover letter ("this patchset depends on patchset B").

More references
---------------

Here is a list of links to help you write better patches

-  `SubmittingPatches <https://www.kernel.org/doc/html/latest/process/submitting-patches.html>`__
-  https://kernelnewbies.org/FirstKernelPatch
-  `http:linux.yyz.us/patch-format.html]] \* [[https:\ www.ozlabs.org/~akpm/stuff/tpp.txt|Andrew Morton's ``The perfect patch`` <http://linux.yyz.us/patch-format.html>`__
-  `Make Bjorn's life easier (and grease the path of your patch) <http://lkml.kernel.org/r/20171026223701.GA25649@bhelgaas-glaptop.roam.corp.google.com>`__
