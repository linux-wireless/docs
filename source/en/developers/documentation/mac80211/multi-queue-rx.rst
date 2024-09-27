= mac80211 multi-queue RX design (considerations) =

:!::!::!: **NOTE: This text is written as though the feature already existed, but that's not true; this is just intended to help make it into proper documentation later.**

In order to support new hardware that has RSS (Receive Side Scaling, i.e. L3 hashing to steer packets to different CPUs with MSI-X or similar) mac80211 supports multi-queue RX.
