Formatting Syntax
=================

`DokuWiki <https://www.dokuwiki.org/DokuWiki>`__ supports some simple markup language, which tries to make the datafiles to be as readable as possible. This page contains all possible syntax you may use when editing the pages. Simply have a look at the source of this page by pressing "Edit this page". If you want to try something, just use the `playground </playground/playground>`__ page. The simpler markup is easily accessible via `quickbuttons <https://www.dokuwiki.org/toolbar>`__, too.

Basic Text Formatting
---------------------

DokuWiki supports **bold**, *italic*, *underlined* and ``monospaced`` texts. Of course you can **``combine``** all these.

::

   DokuWiki supports **bold**, //italic//, __underlined__ and ''monospaced'' texts.
   Of course you can **__//''combine''//__** all these.

You can use :sub:`subscript` and :sup:`superscript`, too.

::

   You can use <sub>subscript</sub> and <sup>superscript</sup>, too.

You can mark something as [STRIKEOUT:deleted] as well.

::

   You can mark something as <del>deleted</del> as well.

**Paragraphs** are created from blank lines. If you want to **force a newline** without a paragraph, you can use two backslashes followed by a whitespace or the end of line.

| This is some text with some linebreaks
| Note that the two backslashes are only recognized at the end of a line
| or followed by
| a whitespace \\\\this happens without it.

::

   This is some text with some linebreaks\\ Note that the
   two backslashes are only recognized at the end of a line\\
   or followed by\\ a whitespace \\this happens without it.

You should use forced newlines only if really needed.

Links
-----

DokuWiki supports multiple ways of creating links.

External
~~~~~~~~

External links are recognized automagically: http://www.google.com or simply www.google.com - You can set the link text as well: `This Link points to google <http://www.google.com>`__. Email addresses like this one: andi@splitbrain.org are recognized, too.

::

   DokuWiki supports multiple ways of creating links. External links are recognized
   automagically: http://www.google.com or simply www.google.com - You can set
   link text as well: [[http://www.google.com|This Link points to google]]. Email
   addresses like this one: <andi@splitbrain.org> are recognized, too.

Internal
~~~~~~~~

Internal links are created by using square brackets. You can either just give a `pagename <pagename>`__ or use an additional `link text <pagename>`__.

::

   Internal links are created by using square brackets. You can either just give
   a [[pagename]] or use an additional [[pagename|link text]].

`Wiki pagenames <https://www.dokuwiki.org/pagename>`__ are converted to lowercase automatically, special characters are not allowed.

You can use `namespaces </some/namespaces>`__ by using a colon in the pagename.

::

   You can use [[some:namespaces]] by using a colon in the pagename.

For details about namespaces see `namespaces <https://www.dokuwiki.org/namespaces>`__.

Linking to a specific section is possible, too. Just add the section name behind a hash character as known from HTML. This links to `this Section <syntax#internal>`__.

::

   This links to [[syntax#internal|this Section]].

Notes:

-  Links to `existing pages <syntax>`__ are shown in a different style from `nonexisting <nonexisting>`__ ones.
-  DokuWiki does not use `CamelCase <https://en.wikipedia.org/wiki/CamelCase>`__ to automatically create links by default, but this behavior can be enabled in the `config <https://www.dokuwiki.org/config>`__ file. Hint: If DokuWiki is a link, then it's enabled.
-  When a section's heading is changed, its bookmark changes, too. So don't rely on section linking too much.

Interwiki
~~~~~~~~~

DokuWiki supports `Interwiki <https://www.dokuwiki.org/Interwiki>`__ links. These are quick links to other Wikis. For example this is a link to Wikipedia's page about Wikis: `Wiki <https://en.wikipedia.org/wiki/Wiki>`__.

::

   DokuWiki supports [[doku>Interwiki]] links. These are quick links to other Wikis.
   For example this is a link to Wikipedia's page about Wikis: [[wp>Wiki]].

Windows Shares
~~~~~~~~~~~~~~

Windows shares like `this <\\server\share>`__ are recognized, too. Please note that these only make sense in a homogeneous user group like a corporate `Intranet <https://en.wikipedia.org/wiki/Intranet>`__.

::

   Windows Shares like [[\\server\share|this]] are recognized, too.

Notes:

-  For security reasons direct browsing of windows shares only works in Microsoft Internet Explorer per default (and only in the "local zone").
-  For Mozilla and Firefox it can be enabled through different workaround mentioned in the `Mozilla Knowledge Base <http://kb.mozillazine.org/Links_to_local_pages_do_not_work>`__. However, there will still be a JavaScript warning about trying to open a Windows Share. To remove this warning (for all users), put the following line in ``conf/userscript.js``:

::

   LANG.nosmblinks = '';

Image Links
~~~~~~~~~~~

You can also use an image to link to another internal or external page by combining the syntax for links and `images <#images_and_other_files>`__ (see below) like this:

::

   [[http://www.php.net|{{wiki:dokuwiki-128.png}}]]

|dokuwiki-128.png|

Please note: The image formatting is the only formatting syntax accepted in link names.

The whole `image <#images_and_other_files>`__ and `link <#links>`__ syntax is supported (including image resizing, internal and external images and URLs and interwiki links).

Footnotes
---------

You can add footnotes  [1]_ by using double parentheses.

::

   You can add footnotes ((This is a footnote)) by using double parentheses.

Sectioning
----------

You can use up to five different levels of headlines to structure your content. If you have more than three headlines, a table of contents is generated automatically -- this can be disabled by including the string ``~~NOTOC~~`` in the document.

Headline Level 3
~~~~~~~~~~~~~~~~

Headline Level 4
^^^^^^^^^^^^^^^^

Headline Level 5
''''''''''''''''

::

   ==== Headline Level 3 ====
   === Headline Level 4 ===
   == Headline Level 5 ==

By using four or more dashes, you can make a horizontal line:

--------------

Media Files
-----------

You can include external and internal `images, videos and audio files <https://www.dokuwiki.org/images>`__ with curly brackets. Optionally you can specify the size of them.

Real size: |image1|

Resize to given width: |image2|

Resize to given width and height [2]_: |image3|

Resized external image: |http://de3.php.net/images/php.gif|

::

   Real size:                        {{wiki:dokuwiki-128.png}}
   Resize to given width:            {{wiki:dokuwiki-128.png?50}}
   Resize to given width and height: {{wiki:dokuwiki-128.png?200x50}}
   Resized external image:           {{http://de3.php.net/images/php.gif?200x50}}

By using left or right whitespaces you can choose the alignment.

.. image:: /wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: right

.. image:: /wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: left

.. image:: /wiki/dokuwiki-128.png
   :alt: dokuwiki-128.png
   :align: center

::

   {{ wiki:dokuwiki-128.png}}
   {{wiki:dokuwiki-128.png }}
   {{ wiki:dokuwiki-128.png }}

Of course, you can add a title (displayed as a tooltip by most browsers), too.

.. image:: /wiki/dokuwiki-128.png
   :alt: This is the caption
   :align: center

::

   {{ wiki:dokuwiki-128.png |This is the caption}}

For linking an image to another page see `#Image Links <#Image Links>`__ above.

Supported Media Formats
~~~~~~~~~~~~~~~~~~~~~~~

DokuWiki can embed the following media formats directly.

.. list-table::

   - 

      - Image
      - ``gif``, ``jpg``, ``png``
   - 

      - Video
      - ``webm``, ``ogv``, ``mp4``
   - 

      - Audio
      - ``ogg``, ``mp3``, ``wav``
   - 

      - Flash
      - ``swf``

If you specify a filename that is not a supported media format, then it will be displayed as a link instead.

Fallback Formats
~~~~~~~~~~~~~~~~

Unfortunately not all browsers understand all video and audio formats. To mitigate the problem, you can upload your file in different formats for maximum browser compatibility.

For example consider this embedded mp4 video:

::

   {{video.mp4|A funny video}}

When you upload a ``video.webm`` and ``video.ogv`` next to the referenced ``video.mp4``, DokuWiki will automatically add them as alternatives so that one of the three files is understood by your browser.

Additionally DokuWiki supports a "poster" image which will be shown before the video has started. That image needs to have the same filename as the video and be either a jpg or png file. In the example above a ``video.jpg`` file would work.

Lists
-----

Dokuwiki supports ordered and unordered lists. To create a list item, indent your text by two spaces and use a ``*`` for unordered lists or a ``-`` for ordered ones.

-  This is a list
-  The second item

   -  You may have different levels

-  Another item

#. The same list but ordered
#. Another item

   #. Just use indention for deeper levels

#. That's it

::

     * This is a list
     * The second item
       * You may have different levels
     * Another item

     - The same list but ordered
     - Another item
       - Just use indention for deeper levels
     - That's it

Also take a look at the `FAQ on list items <https://www.dokuwiki.org/faq:lists>`__.

Text Conversions
----------------

DokuWiki can convert certain pre-defined characters or strings into images or other text or HTML.

The text to image conversion is mainly done for smileys. And the text to HTML conversion is used for typography replacements, but can be configured to use other HTML as well.

Text to Image Conversions
~~~~~~~~~~~~~~~~~~~~~~~~~

DokuWiki converts commonly used `emoticon <https://en.wikipedia.org/wiki/emoticon>`__\ s to their graphical equivalents. Those `Smileys <https://www.dokuwiki.org/Smileys>`__ and other images can be configured and extended. Here is an overview of Smileys included in DokuWiki:

-  8-) %% 8-) %%
-  8-O %% 8-O %%
-  :-( %% :-( %%
-  :-) %% :-) %%
-  =) %% =) %%
-  :-/ %% :-/ %%
-  :-\\ %% :-\\ %%
-  :-? %% :-? %%
-  :-D %% :-D %%
-  :-P %% :-P %%
-  :-O %% :-O %%
-  :-X %% :-X %%
-  :-\| %% :-\| %%
-  ;-) %% ;-) %%
-  ^\_^ %% ^\_^ %%
-  :?: %% :?: %%
-  :!: %% :!: %%
-  LOL %% LOL %%
-  FIXME %% FIXME %%
-  DELETEME %% DELETEME %%

Text to HTML Conversions
~~~~~~~~~~~~~~~~~~~~~~~~

Typography: `DokuWiki <DokuWiki>`__ can convert simple text characters to their typographically correct entities. Here is an example of recognized characters.

-> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r) "He thought 'It's a man's world'..."

::

   -> <- <-> => <= <=> >> << -- --- 640x480 (c) (tm) (r)
   "He thought 'It's a man's world'..."

The same can be done to produce any kind of HTML, it just needs to be added to the `pattern file <https://www.dokuwiki.org/entities>`__.

There are three exceptions which do not come from that pattern file: multiplication entity (640x480), 'single' and "double quotes". They can be turned off through a `config option <https://www.dokuwiki.org/config:typography>`__.

Quoting
-------

Some times you want to mark some text to show it's a reply or comment. You can use the following syntax:

::

   I think we should do it

   > No we shouldn't

   >> Well, I say we should

   > Really?

   >> Yes!

   >>> Then lets do it!

I think we should do it

   No we shouldn't

..

      Well, I say we should

   Really?

..

      Yes!

         Then lets do it!

Tables
------

DokuWiki supports a simple syntax to create tables.

.. list-table::
   :header-rows: 1

   - 

      - Heading 1
      - Heading 2
      - Heading 3
   - 

      - Row 1 Col 1
      - Row 1 Col 2
      - Row 1 Col 3
   - 

      - Row 2 Col 1
      - some colspan (note the double pipe)
      - 
   - 

      - Row 3 Col 1
      - Row 3 Col 2
      - Row 3 Col 3

Table rows have to start and end with a ``|`` for normal rows or a ``^`` for headers.

::

   ^ Heading 1      ^ Heading 2       ^ Heading 3          ^
   | Row 1 Col 1    | Row 1 Col 2     | Row 1 Col 3        |
   | Row 2 Col 1    | some colspan (note the double pipe) ||
   | Row 3 Col 1    | Row 3 Col 2     | Row 3 Col 3        |

To connect cells horizontally, just make the next cell completely empty as shown above. Be sure to have always the same amount of cell separators!

Vertical tableheaders are possible, too.

.. list-table::

   - 

      - 
      - Heading 1
      - Heading 2
   - 

      - Heading 3
      - Row 1 Col 2
      - Row 1 Col 3
   - 

      - Heading 4
      - no colspan this time
      - 
   - 

      - Heading 5
      - Row 2 Col 2
      - Row 2 Col 3

As you can see, it's the cell separator before a cell which decides about the formatting:

::

   |              ^ Heading 1            ^ Heading 2          ^
   ^ Heading 3    | Row 1 Col 2          | Row 1 Col 3        |
   ^ Heading 4    | no colspan this time |                    |
   ^ Heading 5    | Row 2 Col 2          | Row 2 Col 3        |

You can have rowspans (vertically connected cells) by adding ``:::`` into the cells below the one to which they should connect.

.. list-table::
   :header-rows: 1

   - 

      - Heading 1
      - Heading 2
      - Heading 3
   - 

      - Row 1 Col 1
      - this cell spans vertically
      - Row 1 Col 3
   - 

      - Row 2 Col 1
      - :::
      - Row 2 Col 3
   - 

      - Row 3 Col 1
      - :::
      - Row 2 Col 3

Apart from the rowspan syntax those cells should not contain anything else.

::

   ^ Heading 1      ^ Heading 2                  ^ Heading 3          ^
   | Row 1 Col 1    | this cell spans vertically | Row 1 Col 3        |
   | Row 2 Col 1    | :::                        | Row 2 Col 3        |
   | Row 3 Col 1    | :::                        | Row 2 Col 3        |

You can align the table contents, too. Just add at least two whitespaces at the opposite end of your text: Add two spaces on the left to align right, two spaces on the right to align left and two spaces at least at both ends for centered text.

.. list-table::
   :header-rows: 1

   - 

      - Table with alignment
      - 
      - 
   - 

      - right
      - center
      - left
   - 

      - left
      - right
      - center
   - 

      - xxxxxxxxxxxx
      - xxxxxxxxxxxx
      - xxxxxxxxxxxx

This is how it looks in the source:

::

   ^           Table with alignment           ^^^
   |         right|    center    |left          |
   |left          |         right|    center    |
   | xxxxxxxxxxxx | xxxxxxxxxxxx | xxxxxxxxxxxx |

Note: Vertical alignment is not supported.

No Formatting
-------------

If you need to display text exactly like it is typed (without any formatting), enclose the area either with ``<nowiki>`` tags or even simpler, with double percent signs ``%%``.

This is some text which contains addresses like this: http://www.splitbrain.org and \**formatting*\*, but nothing is done with it. The same is true for //\__this\_\_ text// with a smiley ;-).

::

   <nowiki>
   This is some text which contains addresses like this: http://www.splitbrain.org and **formatting**, but nothing is done with it.
   </nowiki>
   The same is true for %%//__this__ text// with a smiley ;-)%%.

Code Blocks
-----------

You can include code blocks into your documents by either indenting them by at least two spaces (like used for the previous examples) or by using the tags ``<code>`` or ``<file>``.

::

   This is text is indented by two spaces.

::

   This is preformatted code all spaces are preserved: like              <-this

::

   This is pretty much the same, but you could use it to show that you quoted a file.

Those blocks were created by this source:

::

     This is text is indented by two spaces.

::

   <code>
   This is preformatted code all spaces are preserved: like              <-this
   </code>

::

   <file>
   This is pretty much the same, but you could use it to show that you quoted a file.
   </file>

Syntax Highlighting
~~~~~~~~~~~~~~~~~~~

`DokuWiki </wiki/DokuWiki>`__ can highlight sourcecode, which makes it easier to read. It uses the `GeSHi <http://qbnz.com/highlighter/>`__ Generic Syntax Highlighter -- so any language supported by GeSHi is supported. The syntax uses the same code and file blocks described in the previous section, but this time the name of the language syntax to be highlighted is included inside the tag, e.g. ``<code java>`` or ``<file java>``.

.. code:: java

   /**
    * The HelloWorldApp class implements an application that
    * simply displays "Hello World!" to the standard output.
    */
   class HelloWorldApp {
       public static void main(String[] args) {
           System.out.println("Hello World!"); //Display the string.
       }
   }

The following language strings are currently recognized: *4cs, 6502acme, 6502kickass, 6502tasm, 68000devpac, abap, actionscript-french, actionscript, actionscript3, ada, algol68, apache, applescript, asm, asp, autoconf, autohotkey, autoit, avisynth, awk, bascomavr, bash, basic4gl, bf, bibtex, blitzbasic, bnf, boo, c, c_loadrunner, c_mac, caddcl, cadlisp, cfdg, cfm, chaiscript, cil, clojure, cmake, cobol, coffeescript, cpp, cpp-qt, csharp, css, cuesheet, d, dcs, delphi, diff, div, dos, dot, e, epc, ecmascript, eiffel, email, erlang, euphoria, f1, falcon, fo, fortran, freebasic, fsharp, gambas, genero, genie, gdb, glsl, gml, gnuplot, go, groovy, gettext, gwbasic, haskell, hicest, hq9plus, html, html5, icon, idl, ini, inno, intercal, io, j, java5, java, javascript, jquery, kixtart, klonec, klonecpp, latex, lb, lisp, llvm, locobasic, logtalk, lolcode, lotusformulas, lotusscript, lscript, lsl2, lua, m68k, magiksf, make, mapbasic, matlab, mirc, modula2, modula3, mmix, mpasm, mxml, mysql, newlisp, nsis, oberon2, objc, objeck, ocaml-brief, ocaml, oobas, oracle8, oracle11, oxygene, oz, pascal, pcre, perl, perl6, per, pf, php-brief, php, pike, pic16, pixelbender, pli, plsql, postgresql, povray, powerbuilder, powershell, proftpd, progress, prolog, properties, providex, purebasic, pycon, python, q, qbasic, rails, rebol, reg, robots, rpmspec, rsplus, ruby, sas, scala, scheme, scilab, sdlbasic, smalltalk, smarty, sql, systemverilog, tcl, teraterm, text, thinbasic, tsql, typoscript, unicon, uscript, vala, vbnet, vb, verilog, vhdl, vim, visualfoxpro, visualprolog, whitespace, winbatch, whois, xbasic, xml, xorg_conf, xpp, yaml, z80, zxbasic*

Downloadable Code Blocks
~~~~~~~~~~~~~~~~~~~~~~~~

When you use the ``<code>`` or ``<file>`` syntax as above, you might want to make the shown code available for download as well. You can do this by specifying a file name after language code like this:

::

   <file php myexample.php>
   <?php echo "hello world!"; ?>
   </file>

.. code:: php

   <?php echo "hello world!"; ?>

If you don't want any highlighting but want a downloadable file, specify a dash (``-``) as the language code: ``<code - myfile.foo>``.

Embedding HTML and PHP
----------------------

You can embed raw HTML or PHP code into your documents by using the ``<html>`` or ``<php>`` tags. (Use uppercase tags if you need to enclose block level elements.)

HTML example:

::

   <html>
   This is some <span style="color:red;font-size:150%;">inline HTML</span>
   </html>
   <HTML>
   <p style="border:2px dashed red;">And this is some block HTML</p>
   </HTML>

.. raw:: html

   <p style="border:2px dashed red;">And this is some block HTML</p>

PHP example:

::

   <php>
   echo 'The PHP version: ';
   echo phpversion();
   echo ' (generated inline HTML)';
   </php>
   <PHP>
   echo '<table class="inline"><tr><td>The same, but inside a block level element:</td>';
   echo '<td>'.phpversion().'</td>';
   echo '</tr></table>';
   </PHP>

.. raw:: html

   <?php echo '<table class="inline"><tr><td>The same, but inside a block level element:</td>';
   echo '<td>'.phpversion().'</td>';
   echo '</tr></table>';
    ?>

**Please Note**: HTML and PHP embedding is disabled by default in the configuration. If disabled, the code is displayed instead of executed.

RSS/ATOM Feed Aggregation
-------------------------

`DokuWiki <DokuWiki>`__ can integrate data from external XML feeds. For parsing the XML feeds, `SimplePie <http://simplepie.org/>`__ is used. All formats understood by SimplePie can be used in DokuWiki as well. You can influence the rendering by multiple additional space separated parameters:

.. list-table::
   :header-rows: 1

   - 

      - Parameter
      - Description
   - 

      - any number
      - will be used as maximum number items to show, defaults to 8
   - 

      - reverse
      - display the last items in the feed first
   - 

      - author
      - show item authors names
   - 

      - date
      - show item dates
   - 

      - description
      - show the item description. If `HTML <https://www.dokuwiki.org/config:htmlok>`__ is disabled all tags will be stripped
   - 

      - *n*\ [dhm]
      - refresh period, where d=days, h=hours, m=minutes. (e.g. 12h = 12 hours).

The refresh period defaults to 4 hours. Any value below 10 minutes will be treated as 10 minutes. `DokuWiki </wiki/DokuWiki>`__ will generally try to supply a cached version of a page, obviously this is inappropriate when the page contains dynamic external content. The parameter tells `DokuWiki </wiki/DokuWiki>`__ to re-render the page if it is more than *refresh period* since the page was last rendered.

**Example:**

::

   {{rss>http://slashdot.org/index.rss 5 author date 1h }}

.. image:: /rss>http///slashdot.org/index.rss 5 author date 1h
   :alt: //slashdot.org/index.rss 5 author date 1h
   :align: left

Control Macros
--------------

Some syntax influences how DokuWiki renders a page without creating any output it self. The following control macros are availble:

.. list-table::
   :header-rows: 1

   - 

      - Macro
      - Description
   - 

      - ~~NOTOC~~
      - If this macro is found on the page, no table of contents will be created
   - 

      - ~~NOCACHE~~
      - DokuWiki caches all output by default. Sometimes this might not be wanted (eg. when the <php> syntax above is used), adding this macro will force DokuWiki to rerender a page on every call

Syntax Plugins
--------------

DokuWiki's syntax can be extended by `Plugins <https://www.dokuwiki.org/plugins>`__. How the installed plugins are used is described on their appropriate description pages. The following syntax plugins are available in this particular DokuWiki installation:

~~\ INFO:syntaxplugins\ ~~

.. [1]
   This is a footnote

.. [2]
   when the aspect ratio of the given width and height doesn't match that of the image, it will be cropped to the new ratio before resizing

.. |dokuwiki-128.png| image:: /wiki/dokuwiki-128.png
   :target: http://www.php.net
.. |image1| image:: /wiki/dokuwiki-128.png
.. |image2| image:: /wiki/dokuwiki-128.png
   :width: 50px
.. |image3| image:: /wiki/dokuwiki-128.png
   :width: 200px
   :height: 50px
.. |http://de3.php.net/images/php.gif| image:: http://de3.php.net/images/php.gif
   :width: 200px
   :height: 50px
