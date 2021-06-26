#!/usr/bin/env python3
# let's confirm the most recent pages were modified today

import datetime


# run this test with the command `python -m pytest tests/2-base-recent_edit_test.py`
def test_wikipedia_recent_edit(py):
    # visit wikipedia

    # click on the "Recent changes" link

    # find the number of results on the page that don't start with "User" and go to the third one

    # click "View History"

    # Locate the 2 most recent edits

    # verify that the top date is most recent than the next row's date

    # verify that the "cur" was editted today (remember wikipedia users UTC time)