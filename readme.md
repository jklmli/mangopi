# mangopi

[![Build Status](https://travis-ci.org/jiaweihli/mangopi.png)](https://travis-ci.org/jiaweihli/mangopi)
[![Coverage Status](https://coveralls.io/repos/jiaweihli/mangopi/badge.png?branch=master)](https://coveralls.io/r/jiaweihli/mangopi?branch=master)

mangopi aims to be an easy-to-use, easy-to-extend manga api.  Adding a new site should be as simple
as filling in a few regexes - everything else is taken care of.

## Installation

Run `pip install mangopi`, or clone the repo and run `python setup.py install`.

## Layout

`helper` contains some shared, non-application-specific code.  (Or it will, after the Util class
is removed.)

`site` contains the library logic to retrieve data from the websites.  The hierarchy:

    MangaSite
      - Noez
        - MangaFox
        - MangaHere
      - Aftv
        - MangaPanda
        - MangaReader

Noez and Aftv appear to be the parent companies of the sites that exist under them.

## Usage

Q: What's the image url for the first page of the first chapter of 'Toriko'?

    >>> from mangopi.site.mangafox import MangaFox
    >>> MangaFox.series('toriko').chapters[0].pages[0].image.url
    'http://z.mfcdn.net/store/manga/3660/01-001.0/compressed/toriko_v01_c01_01.jpg'

Alternatively, use MetaSite, which allows aggregation of multiple sites (there are some performance
issues related to error correction that are being worked out however):

    >>> from mangopi.metasite import MetaSite
    >>> search = MetaSite([MangaFox, MangaHere, MangaPanda, MangaReader])
    >>> from mangopi.site.mangafox import MangaFox
    >>> from mangopi.site.mangahere import MangaHere
    >>> from mangopi.site.mangapanda import MangaPanda
    >>> from mangopi.site.mangareader import MangaReader
    >>> search.series('death note').chapters['22'].pages[0].image.url
    'http://i39.mangapanda.com/death-note/22/death-note-1678383.jpg'

Take a look at the `mangopi.tests` module for further examples.

## Version Support

Support is maintained on Python 2.7.  Support for 3.2 and 3.3 is pending a pull request in a
dependency.

## Testing

Run `python setup.py test` or `nosetests`.
