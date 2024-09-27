Go back --> :doc:`ath10k <../ath10k>`

ath10k sources
--------------

*ath10k* development happens in the ath/ath.git tree on kernel.org:

https://git.kernel.org/cgit/linux/kernel/git/ath/ath.git/

To clone the tree:

::

   git clone git://git.kernel.org/pub/scm/linux/kernel/git/ath/ath.git

ath10k driver is located in directory drivers/net/wireless/ath/ath10k.

If you just want to browse the source code with your web browser this links always points to latest version of ath10k:

https://git.kernel.org/cgit/linux/kernel/git/ath/ath.git/tree/drivers/net/wireless/ath/ath10k

Git branches
------------

ath.git contains multiple branches:

-  **main:** The default branch selected when cloning the tree. Everyone working on any ath drivers (ath11k, ath10k, ath9k, ath6kl, wcn36xx, wil6210 etc) should use this branch as the baseline for patches and when testing submitted patches. Follows Bob Copeland's `wireless-testing tree <https://git.kernel.org/pub/scm/linux/kernel/git/wireless/wireless-testing.git/>`__, which contains `the latest -rc release <https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/>`__ from Linus Torvalds and latest wireless trees. On top of that latest ath patches are merged from `ath-next <https://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git/log/?h=ath-next>`__ and `ath-current <https://git.kernel.org/pub/scm/linux/kernel/git/kvalo/ath.git/log/?h=ath-current>`__ branches. Also latest `mhi-next <https://git.kernel.org/pub/scm/linux/kernel/git/mani/mhi.git/log/?h=mhi-next>`__ is merged. The branch is rebased every time it's updated. Due to unclean history bisect will not work, better to use ath-next (or ath-current) for bisecting.
-  **ath-next:** Based on wireless-next tree and will be periodically merged to wireless-next and scheduled for the next release under works (not for the current -rc releases). ath patches are commited to this branch first and then merged to the main branch. For bisect runs it's better to use this branch instead of the main branch. All patches adding new features or low priority fixes go to this branch.
-  **ath-current:** Based on wireless tree and will be periodically merged to wireless tree and scheduled for the current release under works (for the upcoming -rc release). Only critical fixes.
-  **pending:** Used for building and runtime testing patches under review. Is rebased almost daily and hence commit ids are NOT stable. Use this only if you know what you are doing.
-  **main-pending:** The pending branch merged on top of the main branch, for easier testing of the pending patches. Same rules apply as with the pending branch.

See also :doc:`submitting ath10k patches <submittingpatches>` for more information about the patch flow.
