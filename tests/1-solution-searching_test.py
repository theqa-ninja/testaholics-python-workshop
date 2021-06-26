#!/usr/bin/env python3
# let's search wikipedia!

import logging

from selenium.webdriver.common.keys import Keys


# run this test with the command `python -m pytest tests/1-solution-searching_test.py`
def test_wikipedia_search(py):
    # visit the a search engine website
    py.visit("https://bing.com/")

    # fill in a search for wikipedia
    py.get("input[type='search']").type('wikipedia', Keys.ENTER)

    # locate wikipedia in the search links and click it
    py.get("a[href='https://www.wikipedia.org/']").click()

    # do a search for "quality as"
    py.get("input[type='search']").type('quality as')

    py.wait(use_py=True).sleep(1)

    # verify autocomplete appears and select "quality assurance"
    py.get("input[type='search']").type(Keys.DOWN, Keys.ENTER)

    # let's confirm if the page contains a "Software Testing" link and click it
    py.contains('Software testing').click()

    py.screenshot('software_page.png')

    url = py.url()

    logging.info(f'url: {url}')

    # verify the url you're on contains software_testing
    assert 'Software_testing' in url
