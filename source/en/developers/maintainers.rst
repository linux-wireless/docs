maintainer list
===============

``cfg80211`` and ``mac80211`` maintainer is Johannes Berg.

``wireless drivers`` maintainer is Kalle Valo.

`wireless-testing
<https://git.kernel.org/cgit/linux/kernel/git/wireless/wireless-testing.git/>`__
tree maintainer is Bob Copeland.

See `the official maintainers file
<https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/tree/MAINTAINERS>`__
for details.

Wireless tree maintainer guidelines
-----------------------------------

Here are guidelines how to maintain common wireless trees as a team.
This is for the maintainers, NOT for users.

Tree locations
^^^^^^^^^^^^^^

Clone::

   git clone git@gitolite.kernel.org:pub/scm/linux/kernel/git/wireless/wireless
   git clone git@gitolite.kernel.org:pub/scm/linux/kernel/git/wireless/wireless-next

Web:

-  https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless.git/
-  https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless-next.git/

Apply for a kernel.org account:

https://korg.docs.kernel.org/accounts.html

Kernel.org group "wlan" gives access to
pub/scm/linux/kernel/git/wireless/, ask Kalle to submit a request to
helpdesk@kernel.org.

The branch in each tree is called 'main', instead of the legacy name 'master'.

Patchwork
^^^^^^^^^

https://patchwork.kernel.org/project/linux-wireless/list/

After the patch has been committed to the tree change the state to
Accepted and assign the patch to you. The patchwork bot (once enabled)
should be able to do this automatically, but if it's not working this
needs to be done manually.

Patchwork does automatic assignment of patches based on filepaths.
Johannes has rights to edit the filter. But do note that patchwork is
buggy in this regard and does not always automatically assign patches,
especially pull requests are problematic. Here's a direct link to
unassigned patches:

https://patchwork.kernel.org/project/linux-wireless/list/?series=&submitter=&state=&q=&archive=&delegate=Nobody

Admin rights are needed to be able to modify patches in patchwork. Ask
Kalle to submit a request to helpdesk@kernel.org.

Baseline
^^^^^^^^

This means there should be no extra commits pulled in from other trees
(including net/net-next) when merging to net and net-next trees
respectively.

Current vs next
^^^^^^^^^^^^^^^

wireless tree is the "current" tree for -rc releases, and only takes
fixes. All new features must go to wireless-drivers-next.

No rebasing
^^^^^^^^^^^

Due to downstream trees (eg. iwlwifi, ath, mt76) wireless and
wireless-next must not be rebased.

Pull requests
^^^^^^^^^^^^^

Ideally 2-3 pull requests are sent in a cycle, to avoid having too large
pull requests. Anyone from the maintainer team can write and send the
pull request, but preferably with coordination from others.

TODO: how to coordinate writing of pull request? Some shared file somewhere which everyone can edit?

It's a good idea to let the commits be in the tree for at least two
business days to wait for any build problem reports, this is especially
important when adding new drivers or otherwise bigger changes.

The pull request must use a signed tag and must be created with 'git request-pull' command. Example tag names:

-  wireless-2021-11-10
-  wireless-next-2021-11-10

The signed tag should contain a paragraph or two of description what the
pull requests have and then possible followed by a list of major changes
or new features.

Example::

   Here's another pull request for net-next - including the
   eth_hw_addr_set() and related changes, but also quite a
   few other things:

   cfg80211/mac80211

    * the applicable eth_hw_addr_set() and const hw_addr changes
    * various code cleanups/refactorings
    * stack usage reductions across the wireless stack
    * some unstructured find_ie() -> structured find_element()
      changes

   rtw88

   * support adaptivity for ETSI/JP DFS region
   * 8821c: support RFE type4 wifi NIC

   brcmfmac

   * DMI nvram filename quirk for Cyberbook T116 tablet

   ath9k

   * load calibration data and pci init values via nvmem subsystem

The email containing the pull request should look like::

   From:   Johannes Berg <johannes@sipsolutions.net>
   Subject: pull-request: wireless-next 2021-11-10
   To:     netdev@vger.kernel.org
   Cc:     linux-wireless@vger.kernel.org

   Hi,

   Here's a pull request for net-next, see the tag description below for
   more information.

   Please pull and let us know if there's any problem.

   Thanks,
   Johannes


   The following changes since commit 428168f9951710854d8d1abf6ca03a8bdab0ccc5:

   ....

Fast forwarding
^^^^^^^^^^^^^^^

Both wireless and wireless-next should be fast forwarded after a pull
request to net and net-next, respectively. This is to get the latest
code from upstream trees and avoid extra merges.

Merge window
^^^^^^^^^^^^

During merge window wireless-next should be closed, meaning no new
features are allowed. Important fixes can go to wireless-drivers, but in
general it is easier if the trees are closed during the merge window.
The maintainers also have a few weeks to relax, hopefully ;)

Link tag
^^^^^^^^

Every commit should a Link tag pointing to the mail containing the
patch. This is to track the commits history easier.

Example::

       ath11k: Use memset_startat() for clearing queue descriptors
       
       In preparation for FORTIFY_SOURCE performing compile-time and run-time
       field bounds checking for memset(), avoid intentionally writing across
       neighboring fields.
       
       Use memset_startat() so memset() doesn't get confused about writing
       beyond the destination member that is intended to be the starting point
       of zeroing through the end of the struct. Additionally split up a later
       field-spanning memset() so that memset() can reason about the size.
       
       Signed-off-by: Kees Cook <keescook@chromium.org>
       Signed-off-by: Kalle Valo <kvalo@codeaurora.org>
       Link: https://lore.kernel.org/r/20211118202416.1286046-1-keescook@chromium.org

With pwcli that's possible to automatically add using msgid-tag option::

   msgid-tag = Link: https://lore.kernel.org/r/%s

And b4 looks to have --add-link option for this.

Checking patch fields
^^^^^^^^^^^^^^^^^^^^^

Stephen Rothwell's check_commits or similar must be used to make sure
From, Signed-off-by, Fixes tags and 'commit 123456789012' references are
in correct format.

TODO: link to the script and example usage
