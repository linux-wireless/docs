Maintaining stable compat-wireles releases
==========================================

This section covers the details of how stable compat-wireless releases
are made and maintained.

Recap on compat-wireless
------------------------

Wireless driver development occurs on a development tree called
:doc:`wireless-testing <../../../developers/documentation>`. The stable
kernel releases are not made from this tree though because
wireless-testing consists of patches queued up for the next kernel
release. If what was just described does not make any sense to you you
can read the :doc:`bug fix propagation documentation
<../../documentation/fix_propagation>` which covers this into much
greater detail.

We had been providing tarballs of drivers to users based on
wireless-testing but since its a development tree chances are high users
would run into issues on occasion. Using the stable kernel should then
help with that, and to help tests and get drivers to users quicker we
provide tarballs based on the latest stable RC kernel. So as soon as
2.6.33-rc1 will be released we'll provide a package with those drivers
to users and distributions.

compat-wireless branches
------------------------

compat-wireless works off the the wireless-testing git tree, as such its
master git branch is for usage with the wireless-testing git tree.
Different branches are created upon a release of a new stable RC kernel
and these new branches are then used only for updates for hunk changes
and bug fixes while the master branch continues on with the
wireless-testing tree.

We have a branch then for each stable kernel we have supported::

   mcgrof@tux ~/devel/compat-wireless-2.6 $ git branch -r
     origin/HEAD -> origin/master
     origin/linux-2.6.30.y
     origin/linux-2.6.31.y
     origin/linux-2.6.32.y
     origin/master

A new stable release - the hard way
-----------------------------------

To generate a tarball for the 2.6.32 kernel we then refer
compat-wireless to a stable kernel git tree with that code. Since
Linus's tree does not have the extra version releases of each kernel
another tree must be used for stable release purposes then. The `Unified
stable tree
<http://git.kernel.org/?p=linux/kernel/git/hpa/linux-2.6-allstable.git;a=summary>`__
is then used for this purpose. You can check out the code here::

   git://git.kernel.org/pub/scm/linux/kernel/git/hpa/linux-2.6-allstable.git

So as with the bleeding edge tree we can do::

   GIT_TREE=/home/mcgrof/linux-2.6-allstable/
   ./scripts/admin-refresh.sh

Since the goal is to make clean tarball without the git tree index stuff
a script has been added to allow you to make a release easily:

A new stable release - the easy way
-----------------------------------

::

   ./scripts/gen-stable-release.sh

This should tell you it put a tarball under /tmp/staging/ somewhere.

If you have a driver or feature you are testing you can feel free to
just stuff it into the compat/patches/ directory and upon a refresh (or
./scripts/admin-update.sh) the patch will be applied.

When do updates get made
------------------------

These are made when Luis gets a chance to run the above script and
update hpa's git tree. Betwen extra versions it becomes an easier job.
During a new rc1 release a few things needs to be synchronized to ensure
the right sha1sum is used from compat-wireless for use as the new branch
for the next stable release.
