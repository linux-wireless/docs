Developer process
=================

This section documents the development process for 802.11 and the trees
used.

Patch review process
--------------------

Patches for the 802.11 subsystem must be sent to the relevant
maintainer(s) according to the MAINTAINERS file, which of course
includes the :doc:`linux-wireless mailing list <mailinglists>`. For
details of the patch format review the :doc:`patch submission guide for
802.11 <documentation/submittingpatches>` and our :doc:`git guide
<documentation/git-guide>`. Once posted the patches will go through a
review process by the community. Anyone can post comments regarding your
patch, you should try to be responsive and address any questions asked.

Your e-mails and replies to e-mails should use `bottom posting style for
replies <http://en.wikipedia.org/wiki/Posting_style#Bottom-posting>`__.
HTML e-mails are rejected by the :doc:`linux-wireless <mailinglists>`
mailing list so be sure to use plain text.

The review process completes once no one has posted concerns, questions
or comments, or explicitly has ACKed the patch. The maintainers will
usually merge the patch the week the review process completes.

Maintainer chain
----------------

802.11 development follows the usual Linux kernel development style and
currently has co-maintenance between Kalle Valo and Johannes Berg for
the wireless/wireless-next trees, with the responsibilities roughly
split between drivers and stack respectively. There are other
maintainers (listed in MAINTAINERS) who don't directly commit to the
tree but are responsible for certain drivers.
