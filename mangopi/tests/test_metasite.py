from unittest import TestCase

from mangopi.metasite import MetaSite
from mangopi.site.mangafox import MangaFox
from mangopi.site.mangahere import MangaHere
from mangopi.site.mangapanda import MangaPanda
from mangopi.site.mangareader import MangaReader


class TestMetaSite(TestCase):
    SITE = MetaSite([MangaFox, MangaHere, MangaPanda, MangaReader])
    CHAPTERS = SITE.series('death note').chapters

    def test_chapter_length(self):
        self.assertEqual(len(TestMetaSite.CHAPTERS), 112)

    def test_chapter_title(self):
        chapter = TestMetaSite.CHAPTERS['42']
        self.assertEqual(chapter.title, 'Heaven')

    def test_image_existence(self):
        self.assertIsNotNone(TestMetaSite.CHAPTERS['22'].pages[2].image.url)
