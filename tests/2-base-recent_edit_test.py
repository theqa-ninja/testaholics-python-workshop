#!/usr/bin/env python3
# let's confirm the most recent pages were modified today

from selenium.webdriver.common.keys import Keys


# run this test with the command `python -m pytest tests/2-base-recent_edit_test.py`
def test_wikipedia_recent_edit(py):
    # visit wikipedia

    # click on the "Recent changes" link

    # click the 5th item on the page

    # click "View History"

    # Locate the 2 most recent edits

    # verify that the "cur" is most recent than the "prev" one

    # verify that the "cur" was editted today (remember wikipedia users UTC time)
