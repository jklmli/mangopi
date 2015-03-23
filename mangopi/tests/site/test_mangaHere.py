from unittest import TestCase

from mangopi.site.mangahere import MangaHere


class TestMangaHere(TestCase):
    SERIES = MangaHere.series('gantz')
    CHAPTERS = SERIES.chapters

    def test_chapter_count(self):
        self.assertEqual(len(TestMangaHere.SERIES.chapters), 377)

    def test_chapter_title(self):
        self.assertEqual(TestMangaHere.CHAPTERS[-2].title, 'Lightning Counterstrike')

    def test_chapter_pages(self):
        self.assertEqual(len(TestMangaHere.CHAPTERS[0].pages), 43)

    def test_for_image_url(self):
        url = TestMangaHere.CHAPTERS[0].pages[0].image.url
        self.assertTrue(len(url) > 0)
        self.assertEqual(url[:7], 'http://')

    def test_for_equal_image_url(self):
        url0 = TestMangaHere.CHAPTERS[0].pages[0].image.url
        url1 = TestMangaHere.CHAPTERS[0].pages[1].image.url
        self.assertNotEqual(first = url0, second = url1)
