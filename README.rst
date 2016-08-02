Basicapp
--------

##  HOW-TO URL:  http://python-packaging.readthedocs.io/en/latest/index.html


Always best to install using mkvirtualenv.

Then 'pip install -r requirements.txt' and, finally, 'pip setup.py install'.

After this, you can do the following....

2 command line utils available:
    >>> a) icelandic-beer
    >>> b) german-joke

Unit tests run by either of the following ways:
    >>> a) nosetests
    >>> b) pip setup.py test

To use (with caution), simply do::

    >>> import basicapp
    >>> print basicapp.beer()
        <p>Má ég vinsamlegast fá bjór?</p>

    >>> print basicapp.joke()
        Wenn ist das Nunstück git und Slotermeyer? Ja! ... Beiherhund das Oder die Flipperwaldt gersput.

    >>> print basicapp.reading()
        <p>Ég er að lesa.</p>


    >>> from basicapp import german
    >>> print german.joke()
        Wenn ist das Nunstück git und Slotermeyer? Ja! ... Beiherhund das Oder die Flipperwaldt gersput.


    >>> from basicapp import icelandic
    >>> print icelandic.beer()
        <p>Má ég vinsamlegast fá bjór?</p>
    >>> print icelandic.reading()
        <p>Ég er að lesa.</p>




