
========
pysub-dl
========

Movie subtitle downloader

Actually now it only supports subscene.com to download the subtitles.

I know there is many work to do. It is first release so you can understand.

Installation
------------

Now it is a stable release so if you want to install it in your system you can do it else try it in a virtual environment.

To install the script do this

::

    $ python setup.py install

or

::

    $ pip install pysub-dl

How to use
----------

Use it like: pysub-dl [moviename] [language]

For help

::

    $ pysub-dl -h

General usage

::

    $ pysub-dl iron-man english

    $ pysub-dl hitman english

One request: Do not use space in the movie name, Use '-'(hyphen) instead of ' '(white space). Movie name is not case sensitive, so all you have to worry about the space only.
