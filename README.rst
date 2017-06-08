Basicapp
--------

Always best to install using mkvirtualenv.


You'll likely clone at the command line using git clone <project_url>.

When cloning finishes, cd into the project root directory `basicapp' and do the following:
    `python setup.py install`
    `pip install -r requirements.txt`

After this, you should be able to cd one more level down to `basicapp/basicapp` and execute one of the command line utils below.


Available command line utils:
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




