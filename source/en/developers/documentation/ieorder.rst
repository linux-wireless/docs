This table (compiled by Jouni) documents in which order IEs are added to association and reassociation request frames, and where they originate in the Linux implementation.

.. list-table::

   - 

      - **Kernel/User**
      - **order
         (assoc req)**
      - **order
         (reassoc req)**
      - **IE number**
      - **name [amendment]**
   - 

      - K
      - 3
      - 4
      - 0
      - SSID
   - 

      - K
      - 4
      - 5
      - 1
      - Supp Rates
   - 

      - K
      - 5
      - 6
      - 50
      - Ext Supp Rates
   - 

      - K
      - 6
      - 7
      - 33
      - Power Capab
   - 

      - K
      - 7
      - 8
      - 36
      - Supp Chan
   - 

      - U
      - 8
      - 9
      - 48
      - RSN
   - 

      - K
      - 9
      - 10
      - 46
      - QoS Capab
   - 

      - K
      - 10
      - 11
      - 70
      - RRM Enabled Capab [11k]
   - 

      - U
      - 11
      - 12
      - 54
      - mobility domain [11r]
   - 

      - U
      - -
      - 13
      - 55
      - ftie [11r]
   - 

      - U
      - -
      - 14
      - 57
      - ric(multiple IEs; can include vendor IEs) [11r]
   - 

      - K
      - 12
      - 15
      - 59
      - supp reg classes [11y]
   - 

      - K
      - 13
      - 16
      - 45
      - HT Capab [11n]
   - 

      - K
      - 14
      - 17
      - 72
      - 20/40 BSS Coex [11n]
   - 

      - K
      - 15
      - 18
      - 127
      - Extended Capab [11n]
   - 

      - K
      - 16
      - 19
      - ?
      - QoS Traffic Capab [11v]
   - 

      - K
      - 17
      - 20
      - ?
      - TIM Broadcast Req [11v]
   - 

      - K+U
      - last
      - last
      - 221
      - vendor-specific
