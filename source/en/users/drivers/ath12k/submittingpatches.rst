Submitting patches
==================

Send patches to the mailing lists below. Kalle Valo reviews the patches
within the next few days and, if they are ok, commits them to ath.git.

* To: ath12k@lists.infradead.org
* Cc: linux-wireless@vger.kernel.org

Preferably use :doc:`ath.git main branch <../ath10k/sources>` as the
baseline for patches. Other trees can be used as well, but then the
chances of conflicts are higher.

You can follow the state of ath12k patch review from patchwork:

https://patchwork.kernel.org/project/linux-wireless/list/?state=*&q=ath12k

More info about submitting patches:

* :doc:`../../../developers/documentation/submittingpatches`
* :doc:`../../../developers/documentation/git-guide`
* `Linux kernel submitting patches <https://www.kernel.org/doc/html/latest/process/submitting-patches.html|Linux kernel submitting patches>`__
* `How to write proper git commit messages <https://medium.com/@steveamaza/how-to-write-a-proper-git-commit-message-e028865e5791>`__

Guidelines
~~~~~~~~~~

The ath12k patch guidelines are the same as :doc:`ath10k guidelines <../ath10k/submittingpatches>`.

Hardware families
~~~~~~~~~~~~~~~~~

ath12k supports two hardware families:

- QCN9274 PCI AP devices
- WCN7850 PCI mobile devices

Just like with ath10k, all ath12k patches need to account all supported
hardware families.

Tested-on tag
~~~~~~~~~~~~~

Testing information needs to be provided using Tested-on tag. Few
Tested-on tag examples::

   Tested-on: QCN9274 hw2.0 PCI WLAN.WBE.1.0.1-00029-QCAHKSWPL_SILICONZ-1
   Tested-on: WCN7850 hw2.0 PCI WLAN.HMT.1.0-03427-QCAHMTSWPL_V1.0_V2.0_SILICONZ-1.15378.4

Patch flow
~~~~~~~~~~

The ath12k patch flow is the same as :doc:`ath10k patch flow
<../ath10k/submittingpatches>`
