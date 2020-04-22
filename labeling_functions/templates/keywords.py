from typing import List
from snorkel.labeling import LabelingFunction

ABSTAIN = -1

def make_keyword_lf(keywords: List[str], label: str, field: str = "text"):
    def keyword_lookup(x, keywords, label):
        if any(word in x[field].lower() for word in keywords):
            return label
        return ABSTAIN

    return LabelingFunction(
        name=f"keyword_{keywords[0]}",
        f=keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )


"""Youtube Comment Spam Classification"""
# Spam comments talk about 'my channel', 'my video', etc.
keyword_my = make_keyword_lf(keywords=["my"], label="SPAM")
# Spam comments ask users to subscribe to their channels.
keyword_subscribe = make_keyword_lf(keywords=["subscribe"], label="SPAM")
# Spam comments post links to other channels.
keyword_link = make_keyword_lf(keywords=["http"], label="SPAM")
# Spam comments make requests rather than commenting.
keyword_please = make_keyword_lf(keywords=["please", "plz"], label="SPAM")
# Ham comments actually talk about the video's content.
keyword_song = make_keyword_lf(keywords=["song"], label="HAM")