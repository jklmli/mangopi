from unittest import TestCase

from mangopi.site.mangafox import MangaFox


class TestMangaFox(TestCase):
    SERIES = MangaFox.series('gantz')
    CHAPTERS = SERIES.chapters

    def test_chapter_count(self):
        self.assertEqual(len(TestMangaFox.CHAPTERS), 386)

    def test_chapter_title(self):
        self.assertEqual(TestMangaFox.CHAPTERS[-2].title, 'Lightning Counterstrike')

    def test_chapter_pages(self):
        self.assertEqual(len(TestMangaFox.CHAPTERS[0].pages), 43)

    def test_for_image_url(self):
        url = TestMangaFox.CHAPTERS[0].pages[0].image.url
        self.assertTrue(len(url) > 0)
        self.assertEqual(url[:7], 'http://')

    def test_for_equal_image_url(self):
        url0 = TestMangaFox.CHAPTERS[0].pages[0].image.url
        url1 = TestMangaFox.CHAPTERS[0].pages[1].image.url
        self.assertNotEqual(first = url0, second = url1)
