Administration of releases
==========================

This page is for admins of release for compat-wireless.

compat-wireless bleeding edge releases
--------------------------------------

These are automated and cronjob'd on wireless.kernel.org. If any patch
fails the tarball won't be generated.

backups of compat-wireless releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

These are wget'd at Orbit every day. They are kept on repository2 server
on the path::

   /export/kernel/compat-wireless-2.6

The cronjob is at::

   /etc/cron.daily/get-compat-wireless

Stable releases
---------------

Stable compat-wireless releases are maintained in repository2 at Orbit.
The path is::

   /export/kernel/compat-wireless-2.6-stable/

Stable compat-wireless releases are not automated. They are manually
built from the stable kernel tree and tested once. Once tested the
tarball is dumped into the directory above.

Making new releases
~~~~~~~~~~~~~~~~~~~

hpa's linux-2.6-allstable.git tree is used as a base for the stable
kernel releases. We checkout the current stable kernel target branch and
then modify the GIT_TREE environment variable to point to this local
directory for compat-wireless. The git tree is::

   git://git.kernel.org/pub/scm/linux/kernel/git/hpa/linux-2.6-allstable.git

This tree has a remote branch for every stable kernel release cycle. The
master branch always keeps track of the latest stable kernel. To check
out the latest stable 2.6.29.y kernel release you can do this for
example::

   git checkout -b linux-2.6.29.y origin/linux-2.6.29.y

If you want to track the latest stable just use the default master.

compat-wireless has branches for each stable kernel release as well.
These branches are created at the close of the next stable kernel
release cycle.

Once the stable kernel tree is cloned and we have it at the appropriate
stable kernel release we run::

   cd compat-wireless-2.6
   git checkout -b linux-2.6.30.y remotes/origin/linux-2.6.30.y
   export GIT_TREE=/home/mcgrof/linux-2.6-allstable/
   ./scripts/admin-update.sh
