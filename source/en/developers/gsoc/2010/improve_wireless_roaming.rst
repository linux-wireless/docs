:doc:`Go back to Linux wireless GSoC 2010 page <../2010>`

\*\* /!\\ Other people have worked on roaming, this may not be a good SoC topic unless you have a good idea that you want to pursue.*\*

Improve wireless roaming
------------------------

Roaming support currently exists within wpa_supplicant, but there are no triggers to assist roaming within mac80211. This can be improved by providing triggers for scanning and sending the results to userspace. The triggers can be based on signal level but also can be based on location change and knowledge of previous AP locations based on historical seeds through the usage of `GeoClue <http://www.freedesktop.org/wiki/Software/GeoClue>`__. We will ideally always want to roam to the closets and strongest AP seamlessly

2010 details
------------

Mentors
~~~~~~~

-  Johannes Berg

Interested students
~~~~~~~~~~~~~~~~~~~

::

     * Sign up here 
