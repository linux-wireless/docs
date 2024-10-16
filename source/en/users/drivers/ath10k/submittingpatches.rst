Submitting patches
==================

Send patches to the mailing lists below. Kalle Valo reviews the patches
within the next few days and, if they are ok, commits them to ath.git.

* To: ath10k@lists.infradead.org
* Cc: linux-wireless@vger.kernel.org

Preferably use :doc:`ath.git main branch <sources>` as the baseline for
patches. Other trees can be used as well, but then the chances of
conflicts are higher.

It's important that linux-wireless is CCed on the patches, otherwise it
won't be in patchwork and the maintainer won't see it. You can follow
the state of ath10k patch review from patchwork:

* https://patchwork.kernel.org/project/linux-wireless/list/?state=*&q=ath10k

More info about submitting patches:

* :doc:`linux-wireless submitting patches instructions <../../../developers/documentation/submittingpatches>`
* :doc:`linux-wireless git guide <../../../developers/documentation/git-guide>`
* `Linux kernel submitting patches <https://www.kernel.org/doc/html/latest/process/submitting-patches.html>`__
* `How to write proper git commit messages <https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791>`__
* `Ingo Molnar's points about commit logs <https://lkml.kernel.org/r/20150314075357.GA8319@gmail.com>`__

Guidelines
~~~~~~~~~~

Guidelines for patches are:

- MUST follow `Documentation/SubmittingPatches <https://www.kernel.org/doc/html/latest/process/submitting-patches.html>`__
- MUST follow :doc:`ath10k coding style <codingstyle>`
- MUST be compiler and sparse warning free.
- `git send-email <https://www.kernel.org/pub/software/scm/git/docs/git-send-email.html>`__ SHOULD be used to submit the patch to avoid any formatting issues.
- Patchsets SHOULD contain no more than 12 patches and include a cover letter.
- Commit log MUST `answer the question "Why?" <#answer_to_why>`__.
- Commit log MUST not be empty.
- Commit log MUST have `Tested-on tags <#tested-on_tag>`__.
- SHOULD use `Reported-by: and Tested-by: tags
  <https://www.kernel.org/doc/html/latest/process/submitting-patches.html#using-reported-by-tested-by-reviewed-by-suggested-by-and-fixes>`__
  if others have reported the issue.
- SHOULD use `Fixes: tag
  <https://www.kernel.org/doc/html/latest/process/submitting-patches.html#describe-changes>`__
  if it fixes a regression caused by known commit.
- SHOULD be *mostly* checkpatch clean (though not all patchworks
  warnings make sense), it's RECOMMENDED to test patches with
  :doc:`ath10k-check <codingstyle>` as that will disable the useless
  warnings.

The terminology is from http://www.ietf.org/rfc/rfc2119.txt

Answer to "Why?"
~~~~~~~~~~~~~~~~

The commit log needs to describe the motivation behind the bug, in other
words provide the background information why the patch is needed and why
is it needed the way it is.

- How does it change the functionality from user's point of view?
- Does it fix a bug? If it does, please describe the bug (doesn't
  necessarily need to be long). Also if there's a public bug report add
  a link to the bug report or email describing the issue.
- If a problem has been found during code review and doesn't fix a known
  issue, mention that in the commit log this is a theoretical fix.

Ingo Molnar has written `a nice description
<https://lkml.kernel.org/r/20150314075357.GA8319@gmail.com>`__ about
what maintainers are looking from a commit log, read that to understand
more about commit logs.

Hardware families
~~~~~~~~~~~~~~~~~

ath10k supports multiple hardware families:

- QCA988X PCI Wave 1 AP devices
- QCA9884 PCI Wave 2 AP devices
- QCA4019 part of IPQ4019 AP SoC
- QCA6174 PCI mobile devices
- QCA6174 SDIO mobile devices

For each of these families have their own firmware branch with different
interfaces and possibly different functionality. So then writing a patch
for ath10k it's not enough to think about just one family and instead
all families need to be taken into account. Otherwise risk of
regressions on other families increases significantly.

To speed up patch acceptance the commit log should explain what families
are affected and what families are not, and why. If that is not done
that task will be left for the driver mantainer to do and that will slow
down the review significantly.

Tested-on tag
~~~~~~~~~~~~~

As there are so many different hardware families, to make it clear on
what hardware and firmware the patch is tested on please use the
Tested-on tag. It's similar as Fixes tag, just informing the testing
information. The format is::

   Tested-on: <hwname> <hwversion> <bus> <fwversion>

Add this information after the commit log text, but before the s-o-b
lines, and adding an empty line between Tested-on and s-o-b tags. There
can be (and is very much preferred!) to have multiple Tested-on tags,
each tag for every hardware tested.

Few examples::

   Tested-on: WCN3990 hw1.0 SNOC WLAN.HL.3.1-01040-QCAHLSWMTPLZ-1
   Tested-on: QCA6174 hw3.2 SDIO WLAN.RMH.4.4.1-00029
   Tested-on: QCA6174 hw3.2 PCI WLAN.RM.4.4.1-00110-QCARMSWP-1
   Tested-on: QCA9888 hw2.0 PCI 10.4-3.10-00047

Tested-on tag should be in every patch, as non-trivial patches should
not be submitted without testing. For trivial patches it's ok to skip
Tested-on tag but then it should say "Compile tested only".

Patch flow
~~~~~~~~~~

The ath10k patch flow is this:

* Patch gets posted to the mailing lists. 
* Kalle applies ASAP (usually can take 1-3 business days) the patch to
  pending and main-pending branches for build testing. 
* Kalle waits minimum of two business days for patch being under review
  (unless the patch is urgent). 
* If no comments or warnings, Kalle applies the patch either to
  ath-current branch (for critical fixes) or to ath-next branch (new
  features, low priority fixes) and sends a "Thanks, applied" reply. 
* Kalle merges ath-next and ath-current to main branch immediately after
  the patch is applied. 
* Kalle merges ath-next into wireless-drivers-next tree and ath-current
  to wireless-drivers tree roughly every 2-3 weeks.
* David Miller merges wireless-drivers-next into net-next tree and
  wireless-drivers to net tree every two weeks or so.
* Linus Torvalds merges net every week and net-next during
  `the merge window <https://www.kernel.org/doc/html/latest/process/2.Process.html>`__
  into linux.git .

As a rough estimate it takes 2-4 months for a patch to propagate from
ath-next to an official Linux release.

To clarify the meaning with ath-current and ath-next let's take a
concrete example: let's say that the latest release from Linux is
v4.9-rc2. If a patch is applied to ath-current it will most like be in
v4.9-rc4 or v4.9-rc5 (usually it takes a minimum of one week to get to
Linus' tree, sometimes more). But if the patch is applied to ath-next
the first release it will be in is v4.10-rc1.

See also :doc:`ath10k sources and branches <sources>`.
