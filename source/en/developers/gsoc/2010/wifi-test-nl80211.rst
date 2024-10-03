Extending wifi-test with nl80211 support
========================================

:doc:`wifi-test <../../testing/wifi-test>` is an open project aimed at
assisting automation of testing using scripts for Linux 802.11 drivers.
This project currently uses the old :doc:`wireless-extensions
<../../documentation/wireless-extensions>` which are now deprecated. We
have moved to a much better 802.11 configuration and userspace <-->
kernel communication API with :doc:`cfg80211
<../../documentation/cfg80211>` and :doc:`nl80211
<../../documentation/nl80211>`. The goal of this project is to add an
initial basic C framework to help test specific tasks on 802.11 drivers.

Last year we had a similar project but it was really ambitious and aimed
at creating both the test framework and to enable :doc:`automation of
testing using an 802.11 testbed <../2009/automation_of_testing>`. That
project failed to gain traction and not a single line of code was
published even though the project was accepted and we had three
extremely qualified students apply for the project. This year we lighten
the load with small focus and aim at only building a very simple nl80211
test framework. The effort is expected to enable the community to
further extend this and use it for more advanced tests.

2010 mentors and students
-------------------------

2010 mentors
~~~~~~~~~~~~

-  Luis R. Rodriguez

2010 interested students
~~~~~~~~~~~~~~~~~~~~~~~~

* Sign up here 

Student requirements
--------------------

* Good knowledge of C 
* Familiarity with 802.11 basics 
* Comfortable with git or willing to learn it 
* Feels perfectly comfortable in engaging with the community on a public mailing list 
* Experience working with the community on any open projects is a plus 

What you should start with
--------------------------

After reading the :doc:`cfg80211 <../../documentation/cfg80211>` and
:doc:`nl80211 <../../documentation/nl80211>`, and :doc:`iw
<../../../users/documentation/iw>` documentation, check out iw code from
git:

::

   http://git.sipsolutions.net/iw.git

Then glance over the *event.c* file. That is the key to our entry into
enabling testing. The kernel sends out events upon specific errors or
task completions, or asynchronous events of different types. Read over
all known events and read then the documentation about them on the
*nl80211.h* file. This file is the header upstream on the Linux kernel.
It gets synchronized to userspace.

The iw package ships its own *nl80211.h* file to allow further commands
to be compilable and available on older kernels. When a user upgrades to
a newer kernel the idea is that userspace will know about the new
commands already.

A simple test case would be to use iw to trigger an action, and prior to
that write some simple C code to register for nl80211 events and see if
that command you issued through iw completed. An example would be if
association completed to an AP.

This itself would be a good first step. We will build on this and build
more complicated tests cases. Your ideas are welcomed for both writing
new events upstream in the kernel, and for also coming up with new tests
cases.

Resources
---------

You can read all the documentation on the links below.

* :doc:`../../documentation/cfg80211`
* :doc:`../../documentation/nl80211`
* :doc:`../../../users/documentation/iw`
* :doc:`../../testing/wifi-test`
* :doc:`../../documentation/git-guide`
