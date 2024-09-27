Talked about on the second wireless summit, it might be a good thing to have a "wireless linux" certification. There should be different levels for this and the details need to be worked out.

Why do we want to certify? (by David Christian Berg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Let me start with a short story. Some months ago I walked in to a small computer store at my university town and asked for a WLAN card for my PCMCIA slot that would work under my Linux setup. They couldn't help me. It took them two weeks to figure out, that the very expensive Netgear card I'm using now should be suitable. And it took recompiling my kernel to make it work.

As you can tell, I'm a user. I didn't want to invest the time, browsing the internet, figuring out myself, what cards might be suited for my system. I just wanted to enjoy the comfort of WLAN with my old Linux laptop.

| So what should the goal of a certification be? Making it easier for Linux users to find the right WLAN card for themselves!
| Only if this is the aim, users and manufacturers will adopt a system of certification. As soon as some manufacturers got their cards certified (maybe the kick of for the process will have to be a certification without the manufacturers asking for it) users will prefer these cards because it makes it easier for them to choose. The certification implies extra information that they otherwise would time-consumingly have to search for. With a growing community of Linux users more and more people will want to have a wireless card that is compatible with they system. Manufacturers hence have an incentive to have their cards certified as "easily working with Linux".

A proposal for the Certifications (by David Christian Berg)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After having some thoughts on this and with respect to the thoughts outlined in "Why do we want to certify" I came to the conclusion that it must be clear to home users, what product they shall buy. Still I am aware of the discussion, how much of the driver sources must be open. To satisfy both aspects while laying the focus on the home user market ("I don't care, as long as it works.") I suggest the following different seals.

Best Choice
^^^^^^^^^^^

.. list-table::

   - 

      - |best-choice.png|
      - This seal certifies, that the product not only is easy to set up for a normal user, but also meets the standards concerning the availability of the source code of drivers and firmware.

Home User
^^^^^^^^^

.. list-table::

   - 

      - |home-user.png|
      - Products carrying this seal are easy to set up, but don't have open drivers or firmware. Many manufacturers will only want to reach this seal, but from the users point of view, this doesn't matter that much. If we don't give this option, we can just forget the whole idea.

Geek User
^^^^^^^^^

.. list-table::

   - 

      - |geek-user.png|
      - Geeks are the target group of products identified with this seal. While drivers and firmware are open, they are not easy to install. So you will need to be a geek or have one as family or friends :)

certification level considerations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  availability of driver
-   \* binary only
-   \* partial source
-   \* full source
-   \* partial open source
-   \* full open source
-   \* for binary drivers, platforms are important
-   possibly work with `WINLAB/Orbit <http://www.orbit-lab.org/>`__ and have certified hardware installed there
-   card/chipset combination is certified to avoid un-renamed cards with different chipset
-   ...

alternatives
~~~~~~~~~~~~

Why not simply provide \*one\* sticker/logo which means the vendor's driver is now in Linus' tree and that the vendor supports it.

So we would need only one:

.. image:: in-linux-green.png
   :alt: in-linux-green.png

.. |best-choice.png| image:: best-choice.png
.. |home-user.png| image:: home-user.png
.. |geek-user.png| image:: geek-user.png
