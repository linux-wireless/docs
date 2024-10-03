Git guide for Linux wireless users and developers
=================================================

This is a quick git-guide for Linux users and developers with emphasis
on Linux wireless.

Git trees in use for wireless patches integration
-------------------------------------------------

The wireless maintainers use different git trees depending on the patches target. Contributors are expected to base their work on the relevant tree:

- `wireless-next <https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless-next.git>`__
  must be used for patches bringing new features, either for
  mac80211/cfg80211 or device drivers. The patches from this tree will
  eventually land in Linus' tree during each merge window.
- some devices family have their own git tree which should then be
  preferred over wireless-next, that's for example the case for `ath
  <https://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git>`__ or
  `iwlwifi <https://git.kernel.org/pub/scm/linux/kernel/git/iwlwifi/iwlwifi-next.git>`__
- urgent patches/fixes must target the `wireless <https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless.git>`__
  tree. Those fixes will be sent for "-rc" releases and/or to stable
  kernels
- for some specific cases, the `wireless-testing tree <https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless-testing.git>`__
  can be used. wireless and wireless-next are frequently merged into it
  to run automated tests
- device firmwares are handled separately and should target
  `linux-firmware <https://gitlab.com/kernel-firmware/linux-firmware>`__

Cloning a development tree
--------------------------

First, clone the relevant tree, for example wireless-next.git tree::

   git clone git://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless-next.git
   cd wireless-next

If you need to work on multiple trees, you can either clone needed repositories at different paths, or use a multi-remote repository::

   git remote add ath https://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git
   git fetch ath

Get the latest updates
----------------------

You will want to update your local git repository to match what
maintainers has last committed. You can do this as follows::

   git pull origin master

Review the changes last registered
----------------------------------

::

   git log

To review changes made to wireless drivers
------------------------------------------

::

   git log -p drivers/net/wireless/

To review changes made to mac80211
----------------------------------

::

   git log -p net/mac80211/

You get the idea.

Hacking on Linux wireless
-------------------------

If you'd like to hack on Linux wireless you can create own branch based
on the one you are using. This is so you don't screw your current branch
up::

   git checkout -b my-fix-for-foo
   # hack hack hack
   # To get a diff of your work:
   git diff > my_changes.diff
   # Or if you just want to read them:
   git diff
   # To revert to the original state of the branch:
   git checkout -f
   # If instead you want to commit
   git commit -a

Check available branches
------------------------

Suppose you have created a few branches, and just are not sure what you
have anymore::

   # To view local branches
   git branch -l
   # To view all remote branches
   git branch -r

Reviewing changes between commmits
----------------------------------

Suppose you want to get the log and diff between two commits::

   # get the SHA of two commits
   git log
   # Then get the diff of them, by showing the logs in between
   git log -p d8a285c8f83f728be2d056e6d4b0909972789d51..9202ec15da36ca060722c363575e0e390d85fb71
   # Since SHAs are pretty unique you can just give it a short version
   # and it will try to match what is right:
   git log -p d8a28..9202e

Merging git branches
--------------------

Say you have two local branches, and I want to merge them. If you're on
local branch *my-latest* and I want to merge with local branch
*my-fix-for-foo*, you would do::

   git pull . my-fix-for-foo

Checkout code as it was from specific commit
--------------------------------------------

Suppose you want to checkout what the codebase looked like at a specific
commit SHA. You can do this with branches::

   # Long form:
   git checkout -b view-commit-foo d8a285c8f83f728be2d056e6d4b0909972789d51
   # Or short form:
   git checkout -b view-commit-foo d8a28

Delete branches
---------------

If you are fed up with a branch delete it. You must not be on that
branch so go into another one::

   git checkout master
   git branch -D old-branch

No need to download more kernel tarballs
----------------------------------------

You can simply make your current directory look like a specific tag
blessed by Linus (or Linville)::

   git checkout -b v2.6.27-rc7 v2.6.27-rc7

Generate patches
----------------
Say you have 3 commits and you want to send the patches now::

   git format-patch --cover-letter -o some-dir d8a285c8f83f728be2d056e6d4b0909972789d51..9202ec15da36ca060722c363575e0e390d85fb71
   # this is equivalent to, this is the short form
   git format-patch --cover-letter -n -o some-dir d8a28..9202e

Where d8a28 was the last commit before you started hacking and 9202e is
the current head, meaning the commit ID of your latest commit.

Generating patches for renames
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you are going to rename files you can add "-M" to the arguments to
git-format-patch, this way the patches don't generate useless endless
removals and adds for a simple rename.

Fixing patches after review
---------------------------

This section tells you how to deal with fixing patches with git after
you have sent them out for review or in case you realize you need to go
back in history and edit/fix something.

Fixing a patch or commit message
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To fix a patch or commit message you have committed you can simply do::

   # Edit the file you forgot to add a fix for, and then
   # tell git (-a option) all the files you have edited
   # should go into the commit, but that you want it to apply
   # to the last commit and you also want to review/edit the
   # commit message
   git commit -a --amend

If you want to ignore all changes you have pending don't use the "-a" option.

Fixing a series of patches
~~~~~~~~~~~~~~~~~~~~~~~~~~

When you a large set of patches and you are not the maintainer chances
are pretty high you'll get feedback and you'll need to respin them. A
nice trick to avoid having to use quilt/stgit/etc is to use git to edit
the patch back in history and continue then. You can do this with git's
rebase::

   git rebase -i commit-id-foo

This will let you select which patches you want to edit, once done with
editing you will have to add the file you fixed::

   git add drivers/net/wireless/foo/bar.c

And then amend the commit::

   git commit --amend

You can skip the 'git add' part by just using 'git commit -a --amend'
but keep in mind this will add into the commit \*all\* changes in your
current diff (git diff).

If you didn't have to remove a commit, let the rebase continue::

   git rebase --continue

Keep in mind you will have to edit the patches to deal with conflicts if
any were found. To deal with them simply edit the files its complaining
about, git add them, and do 'git rebase --continue' once done. The
conflicts are marked with a set of "<<<<" in the sections. It'll have
part from the original file and the part from the new file. You get to
mangle with these to figure out what is the right code.

Annotating new revision
^^^^^^^^^^^^^^^^^^^^^^^

If developers raise issues with your patch you are expected to follow up
with another iteration of your patch or series of patches. In your new
iteration of patches you should specify that these patches are part of a
new iteration. You can do this by specifying the iteration number on the
subject. For example, for a second iteration you would use::

   [PATCH v2]

You can specify this with git by using an argument to git format-patch::

   --subject-prefix="PATCH v2"

Removing a commit from a series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to *remove* a commit you can do this trick::

   git rebase -i commit-id-foo
   git checkout commit-id-before-change
   git rebase --continue

Adding a new commit to the series
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to add a new commit to the series simply add the commit
using the usual commit procedures. Once you are done continue with the
rebase.

Sending patches
---------------

Read git-send-email man page. But here is a quick summary for those who
just want to get it to work. Keep in mind git send-email is a perl
script and is usually shipped separately from git core.

You can install your favorite mailer, you can directly contact to your
SMTP server or alternivately to use ssmtp.

To set your name and email in git::

   git config --global user.name "Ed Example"
   git config --global user.email "ed@example.com"

Using SMTP server directly
~~~~~~~~~~~~~~~~~~~~~~~~~~

Set SMTP settings to git::

   git config --global sendemail.smtpencryption tls
   git config --global sendemail.smtpserver mail.example.com
   git config --global sendemail.smtpuser ed@example.com
   git config --global sendemail.smtpserverport 587
   git config --global sendemail.smtppass myverysecretpassword

Setting up ssmtp (optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Below is an example config that works with an exchange server, in
``etc/ssmtp/ssmtp.conf``::

   root=hacker@company.com
   mailhub=smtp.company.com
   hostname=smtp.company.com
   FromLineOverride=YES

   UseSTARTTLS=YES
   AuthUser=hacker
   AuthPass=my-uber-secret-password

Here is an example ``/etc/ssmtp/revaliases``::

   user:hacker@company.com:smtp.company.com
   hacker:hacker@company.com:smtp.company.com

user can be the username (``whoami``) on the system.

Sending e-mails
~~~~~~~~~~~~~~~

Once you have your mailer setup and patches in a directory, review them
so they are correct. Once all done send them out using::

   git send-email --to linux-wireless@vger.kernel.org --cc maintainer-of-driver@example.com some-dir/

Where some-dir is where you stashed your patches. Keep in mind that if
you are submitting a series it helps to send an introductory PATCH [0/n]
as well, where n is the number of patches you want to send. You can add
this to the git-send-email queue easily using ``--cover-letter`` when
generating patches using git-format-patch. Be sure to edit the patch
0000-foo then. git-send-email will pick it up when you specify the
directory :)
