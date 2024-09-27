Go back --> :doc:`en/users/Drivers/ath11k <../ath11k>`

Reporting ath11k bugs
---------------------

ath11k bug reports can be filed to `bugzilla.kernel.org <https://bugzilla.kernel.org/enter_bug.cgi?product=Drivers>`__. Use these catagories:

-  Product: Drivers
-  Component: network-wireless
-  Summary: start with string "ath11k:"

Before filing see also the list of `open <https://bugzilla.kernel.org/buglist.cgi?bug_status=NEW&bug_status=ASSIGNED&bug_status=REOPENED&list_id=1082403&query_format=advanced&short_desc=ath11k&short_desc_type=allwordssubstr>`__ and `closed <https://bugzilla.kernel.org/buglist.cgi?bug_status=RESOLVED&bug_status=VERIFIED&bug_status=REJECTED&bug_status=DEFERRED&bug_status=NEEDINFO&bug_status=CLOSED&list_id=1111073&query_format=advanced&short_desc=ath11k&short_desc_type=allwordssubstr>`__ ath11k bugs.

To make it easier for the developers to help, include in the bug report at least this information:

-  Exact kernel version. Is it a distro kernel or have you compiled it yourself? Any extra patches?
-  Linux distribution version.
-  Host device information, for example if it's a laptop make and model, architecture, CPU etc.
-  BIOS version.
-  How many times have you seen the bug and how many times did you try to reproduce it? For example, the test failed 3 times out of 5 total times tested.
-  Output from: uname -a
-  Output from: lspci -mnn
-  Output from: find /lib/firmware/ath11k/ -type f \| xargs md5sum
-  Output from: dmesg \| grep ath11k

*Always open a new bug*, do not report your issue as a comment to an existing bug. Even if the symptoms are the same (eg. "kernel freeze" or "firmware crash"), the actual bugs causing the issue might be very different. It's better that the developers do the analysis, and if it's really the same bug the developers will mark the report as duplicate. If people report their issues to an existing bug reports, it will become a mess for the developers to maintain them.

https://bugzilla.kernel.org is only for `upstream kernel.org releases <https://www.kernel.org/>`__. As distros (Ubuntu, Fedora etc) can modify ath11k on their own, and it's difficult to track what has changed, report bugs seen on distro kernels to the distro bug trackers.

Bugzilla is not a support forum, it is a tool to collect and track actual bugs. All questions, comments and support requests should be sent to :doc:`the mailing list <mailinglist>`.

Patches are not submitted via bugzilla, see :doc:`Submitting patches <submittingpatches>`.
