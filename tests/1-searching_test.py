#!/usr/bin/env python3
# let's sign into meetup!

import logging

from selenium.webdriver.common.keys import Keys


def test_wikipedia_search(py):
    # visit the a search engine website
    py.visit("https://bing.com/")

    # fill in a search for wikipedia
    py.get("input[type='search']").type('wikipedia', Keys.ENTER)

    py.get("a[href='https://www.wikipedia.org/']").click()

    py.get("input[type='search']").type('quality ass')
    py.wait(use_py=True).sleep(1)
    py.get("input[type='search']").type(Keys.DOWN, Keys.ENTER)

    py.contains('Software testing').click()

    url = py.url()

    logging.info(f'url: {url}')

    assert 'Software_tesdting' in url
