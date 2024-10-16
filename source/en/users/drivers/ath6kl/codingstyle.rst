ath6kl Coding Style
===================

Status/error variables
~~~~~~~~~~~~~~~~~~~~~~

Use a variable named "ret" to store return values or status codes. Also
propagate the error code to upper levels.

Example:

.. code-block:: c

   int ret;

   ret = request_firmware(&fw_entry, filename, ar->dev);
   if (ret)
           return ret;

Name context variables either "ar" or "ar\_<hifname>". Use
ath6kl\_<hifname>_priv() to get access to hif specific context.

Examples:

.. code-block:: c

   struct ath6kl *ar = ptr;
   struct ath6kl_sdio *ar_sdio = ath6kl_sdio_priv(ar);

For consistency always use the main context (struct ath6kl \*ar) as
function parameter, don't use hif specific context.

Error path
~~~~~~~~~~

Use goto labels err\_<action> for handing error path, with <action>
giving a clear idea what the label does.

Example:

.. code-block:: c

   ret = ath6kl_hif_power_on(ar);
   if (ret)
           return ret;

   ret = ath6kl_configure_target(ar);
   if (ret)
           goto err_power_off;

   ret = ath6kl_init_upload(ar);
   if (ret)
           goto err_cleanup_target;

   return 0;

   err_cleanup_scatter:
           ath6kl_cleanup_target(ar);
   err_power_off:
           ath6kl_hif_power_off(ar);
   return ret;

Locking
~~~~~~~

Always document what spinlock/mutex/rcu actually protects. Locks should
always protect data, not code flow.

Naming
~~~~~~

Name of symbols and functions follow style
<drivername>\_<filename>\_<symbolname>.

Example:

.. code-block:: c

   int ath6kl_init_hw(struct ath6kl *ar)

For each component use function names create/destroy for allocating and
freeing something, init/cleanup for initialising variables and cleaning
up them afterwards and start/stop to temporarily pause something.

Example:

.. code-block:: c

   int ath6kl_cfg80211_create(struct ath6kl *ar)
   int ath6kl_cfg80211_start(struct ath6kl *ar)
   void ath6kl_cfg80211_stop(struct ath6kl *ar)
   void ath6kl_cfg80211_destory(struct ath6kl *ar)

Things NOT to do
~~~~~~~~~~~~~~~~

Don't use void pointers.

Don't use typedef.

Linux style
~~~~~~~~~~~

Follow `Linux Coding Style
<http://git.kernel.org/?p=linux/kernel/git/torvalds/linux.git;a=blob;f=Documentation/CodingStyle;hb=HEAD>`__.
