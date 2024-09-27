Go back --> :doc:`en/users/Drivers/ath11k <../ath11k>`

Submitting patches
------------------

Send patches to the mailing lists below. Kalle Valo reviews the patches within the next few days and, if they are ok, commits them to ath.git.

::

       * To: [[ath11k@lists.infradead.org]] 
       * Cc: [[linux-wireless@vger.kernel.org]] 

Preferably use :doc:`ath.git main branch <../ath10k/sources>` as the baseline for patches. Other trees can be used as well, but then the chances of conflicts are higher.

You can follow the state of ath11k patch review from patchwork:

https://patchwork.kernel.org/project/linux-wireless/list/?state=*&q=ath11k

More info about submitting patches:

::

         * [[en/developers/Documentation/SubmittingPatches|linux-wireless submitting patches instructions]] 
         * [[en/developers/Documentation/git-guide|linux-wireless git guide]]
         * [[https://www.kernel.org/doc/html/latest/process/submitting-patches.html|Linux kernel submitting patches]]
         * [[https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791|How to write proper git commit messages]]

Guidelines
~~~~~~~~~~

The ath11k patch guidelines are the same as :doc:`ath10k guidelines <../ath10k/submittingpatches>`.

Hardware families
~~~~~~~~~~~~~~~~~

ath11k supports two hardware families:

-  IPQ8074 SoC AP devices
-  QCA6390 PCI mobile devices

Just like with ath10k, all ath11k patches need to account all supported hardware families.

Tested-on tag
~~~~~~~~~~~~~

Testing information needs to be provided using Tested-on tag. Few Tested-on tag examples:

::

   Tested-on: IPQ8074 hw2.0 AHB WLAN.HK.2.1.0.1-00410-QCAHKSWPL_SILICONZ-2
   Tested-on: IPQ6018 hw1.0 AHB WLAN.HK.2.1.0.1-01161-QCAHKSWPL_SILICONZ-1
   Tested-on: QCA6390 hw2.0 PCI WLAN.HST.1.0.1-01230-QCAHSTSWPLZ_V2_TO_X86-1

Patch flow
~~~~~~~~~~

The ath11k patch flow is the same as :doc:`ath10k patch flow <../ath10k/submittingpatches>`
