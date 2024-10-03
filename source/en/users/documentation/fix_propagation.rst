When will your kernel issue be fixed ?
======================================

Understanding how bugs actually get fixed and fixes get propagated
through the kernel is important to understanding when and how your
specific issue may be fixed upstream. It should also help you as a user
understand why using bleeding edge can tend to help accelerate the pace
for a bug fix.

Getting fixes in to wireless-testing first
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cfg80211, mac80211, or wireless driver bugs will **always** be fixed
**first** on the :doc:`wireless-testing git
<../../developers/documentation>` tree. Once a bug is fixed there it
will be determined by the developer and community whether the fix is
also required for older stable kernel releases, if it is it will undergo
the process described below.

Getting fixes in to stable kernel releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a patch submitted for inclusion into :doc:`wireless-testing
<../../developers/documentation>` is a stable fix candidate the patch
will be annotated as such prior to submission with a note towards the
bottom of the patch commit log for stable::

   Cc: stable@vger.kernel.org

Once the patch gets merged onto John's tree, John Linville (wireless
maintainer) will determine whether or not the patch also fixes an issue
on Linus' tree; and if so it gets submitted to David Miller (networking
maintainer) so that David can then propagate the fix to Linus. Once the
patch gets merged onto Linus' tree an e-mail will be sent to
`stable@vger.kernel.org </mailto/stable@vger.kernel.org>`__ and the
patch will be either directly queued or ported for review on the
`stable-review mailing list
<http://linux.kernel.org/mailman/listinfo/stable-review>`__. If no
objections are raised the patch then gets merged onto the respective
stable kernels.

Getting the fix in your Linux distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Linux distributions which make official tagged release stick to a series
of stable kernels for each release. This is contrary to *rolling
distributions* which always just keep on the latest and greatest all the
time. Distributions like Ubuntu, Debian, RHEL, Fedora are not *rolling
distributions*, distributions like Gentoo and Arch are rolling
distributions. Non-rolling distributions usually stick to supporting
only one kernel per tagged release. The kernel they pick for use on a
release is based on the date of the targeted release. Updates to the
kernel will be made on a Linux distribution once a new stable kernel
release with a newer *extraversion* is released. The *extraversion* is
the last number in a 4 series number release, so in 2.6.31.2 the
*extraversion* would be 2.

When a fix cannot be propagated to stable releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Not all fixes will be propagated to stable releases of the Linux kernel.
It is better to understand what fixes **will** be merged onto stable
kernel releases than to consider which fixes will not. Fixes which will
be accepted for stable kernel releases will vary but a general rule of
thumb is:

- Kernel oops
- Security flaws
- Memory leaks
- Regressions (issues introduced into newer kernels which did not exist
  in older kernel releases)
- Critical fixes What fits into a *Critical fix* category are left to
  the judgment of the subsystem maintainer. Unfortunately for users the
  reality of this model is some minor fixes which can help a user out on
  a stable kernel will not be merged into new stable kernel release, but
  this is also why new kernels are always encouraged, and also why we
  have come up with :doc:`bleeding edge compat-wireless releases
  <../download>` and :doc:`stable compat-wireless releases
  <../download/stable>`.
