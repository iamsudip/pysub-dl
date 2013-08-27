========
pysub-dl
========

Subtitle downloader
-------------------

Actually now it only supports subscene.com to download the subtitles.

I know there is many work to do. It is an early release but works well.

Installation
------------

Now it is a stable release so if you want to install it in your system you can do it else try it in a virtual environment. To install it in yur system it requires su access.

To install the script do this

Option 1 : Install via pip ::

    $ sudo pip install pysub-dl

Option 2 : If you have downloaded the source ::

    $ sudo python setup.py install

Do not forget to upgrade it after a week interval I am modifying so many things very frequently ::

	$ sudo pip install pysub-dl --upgrade

How to use
----------

Use it like: pysub-dl [moviename] [language]

For help ::

    $ pysub-dl --help

General usage ::

    $ pysub-dl iron-man english

    $ pysub-dl hitman spanish

One request: **Do not use space in the movie name, Use '-'(hyphen) instead of ' '(white space).** Movie name is not case sensitive, so all you have to worry about the space only.

First you should go to your movie directory then you should execute your code, it will be better cause **execution creates the subtitle zip in the present working directory** but it is not mandatory.

On execution **it will show the list of subtitles available at the moment at subscene.com** for that particular movie. You have to choose one number from them.

Uncertainly **if you give wrong movie name, no problem it will show you the probable movie name and you have to choose from them**.

For windows users they should download the package manually and extract it. Run it on that directory as ::

    C:\master> python pysub-dl incredibles english

**Press [Ctrl] + c or [Ctrl] + d to exit immediately.**

Reporting Bugs
--------------

Please report bugs at github issue tracker: https://github.com/iamsudip/pysub-dl/issues

Author
------
iamsudip <iamsudip@programmer.net>

* http://github.com/iamsudip
