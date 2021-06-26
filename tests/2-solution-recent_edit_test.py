#!/usr/bin/env python3
# let's confirm the most recent pages were modified today

import datetime
from datetime import timedelta


# run this test with the command `python -m pytest tests/2-solution-recent_edit_test.py`
def test_wikipedia_recent_edit(py):
    # visit wikipedia
    py.visit("https://en.wikipedia.org/wiki/Main_Page")

    # click on the "Recent changes" link
    py.getx('//a[text()="Recent changes"]').click()

    # find the number of results on the page that don't start with "User" and go to the third one
    py.findx('//li//a[@class="mw-changeslist-title" and not(contains(text(), "User"))]')[3].click()

    # click "View History"
    py.getx('//a[contains(@title, "Past revisions")]').click()

    # Locate the 2 most recent edits
    edit1 = py.getx('//li//span[text()="cur" and not(@href)]/../..//a[@class="mw-changeslist-date"]').text()

    edit2 = py.getx('//li//a[text()="cur" and (@href)]/../../..//a[@class="mw-changeslist-date"]').text()

    py.screenshot("revision_page.png")

    date1 = datetime.datetime.strptime(edit1, '%H:%M, %d %B %Y')

    date2 = datetime.datetime.strptime(edit2, '%H:%M, %d %B %Y')

    # verify that the top date is most recent than the next row's date
    assert date1 > date2

    # verify that the "cur" was editted today (remember wikipedia users UTC time)
    assert date1 > datetime.datetime.today() - timedelta(days=1)