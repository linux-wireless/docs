Go back --> :doc:`en/users/Drivers/ath10k <../ath10k>`

Submitting board files
----------------------

If you want to submit board files to the official board-2.bin file send a mail to `ath10k@lists.infradead.org <ath10k@lists.infradead.org>`__ with this information:

-  use subject with style of "ath10k-firmware: QCA1234 hw0.0: foo bar" (naturally replacing with real hardware name and proper title)
-  only one hardware per mail (so for example if you have files for both QCA4019 and QCA9888 send two mails)
-  description for what hardware this is
-  origin of the board file (did you create it yourself or where you downloaded)
-  ids to be used with the board file (ATH10K_BD_IE_BOARD_NAME in ath10k)
-  md5sum of each new board file to add
-  attach the actual board file (board.bin) with the exact name to be used in board-2.bin, for example bus=ahb,bmi-chip-id=0,bmi-board-id=20,variant=OM-A62.bin

Note: You should NOT submit the full board-2.bin file, just the board file/image you want to add (ie. board.bin in ath10k terms).

If everything is ok Kalle will then add the file to the official board-2.bin. As it's easy to make a mistake when adding a new board image, and every character makes a difference, please always check the commited board file carefully.

Few good examples to follow:

-  http://lists.infradead.org/pipermail/ath10k/2018-April/011179.html
-  http://lists.infradead.org/pipermail/ath10k/2018-April/011178.html
