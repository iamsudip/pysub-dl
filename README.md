========
pysub-dl
========

Subtitle downloader
-------------------

Actually now it only supports subscene.com to download the subtitles.

Installation
------------

To install the script do this

Option 1 : Install via pip ::

    $ sudo pip install pysub-dl

Option 2 : If you have downloaded the source ::

    $ sudo python setup.py install

Do not forget to upgrade it after a week interval I am modifying so many things very frequently ::

	$ sudo pip install pysub-dl --upgrade

How to use
----------

Use it like: pysub-dl movie [language]

[language] is optional, if language is provided you will see subtitles available for that language only or it will show you all.

For help ::

    $ pysub-dl --help

General usage ::

    $ pysub-dl iron-man english

    $ pysub-dl hitman spanish

**If you do not provide any language it will show you all the available subtitles for that movie for all languages.**

One request: **Do not use space in the movie name, Use '-'(hyphen) instead of ' '(white space).** Movie name is not case sensitive, so all you have to worry about the space only or **if you want to use special characters like ' you can use double quotes** i. e. ::

    $ pysub-dl "we're the millers"

First you should go to your movie directory then you should execute your code, it will be better cause **execution downloads the subtitle file(s) in the present working directory** but it is not mandatory.

On execution **it will show the list of subtitles available at the moment at subscene.com** for that particular movie. You have to choose one number from them.

Uncertainly **if you give wrong movie name, no problem it will show you the probable movie name and you have to choose from them**.

For windows users they should download the package manually and extract it. Run it on that directory as ::

    C:\master> python pysub-dl incredibles english

**Press [Ctrl] + c or [Ctrl] + d to exit immediately.**

For windows users it is [Ctrl] + z (I think).


Reporting Bugs
--------------

Please report bugs at github issue tracker: https://github.com/iamsudip/pysub-dl/issues

Author
------
iamsudip <iamsudip@programmer.net>

* http://github.com/iamsudip
