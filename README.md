# Snorkel Zoo
![snorkel-logo](https://www.snorkel.org/doks-theme/assets/images/layout/Snorkel.png)

The Snorkel Zoo is a collection of utilities for writing labeling functions, transformation functions, and slicing functions, as seen in the [core Snorkel library](https://github.com/snorkel-team/snorkel). We’ve demonstrated the efficacy of _templates_ or _declarative operators_ across a range of use cases in prior work ([Ratner et. al 2019](https://arxiv.org/abs/1711.10160)). In this reposiotry, we aim to provide a shared resource for different _builders_, _generators_, and _primitives_ that are effective in both research and production contexts. More importantly, we’re excited to crowdsource ideas from the community!

## Structure
The repository is divided into subfolders for builders, generators, and primitives.

### Templates
For a single problem, It’s helpful to have a shared interface for building a specific type of labeling function. For instance, the [Intro Tutorial](https://www.snorkel.org/use-cases/01-spam-tutorial) features a number of keyword labeling functions using a shared template:

```python
def make_keyword_lf(keywords, label=SPAM):
    return LabelingFunction(
        name=f"keyword_{keywords[0]}",
        f=keyword_lookup,
        resources=dict(keywords=keywords, label=label),
    )


"""Spam comments talk about 'my channel', 'my video', etc."""
keyword_my = make_keyword_lf(keywords=["my"])

"""Spam comments ask users to subscribe to their channels."""
keyword_subscribe = make_keyword_lf(keywords=["subscribe"])

"""Spam comments post links to other channels."""
keyword_link = make_keyword_lf(keywords=["http"])

"""Spam comments make requests rather than commenting."""
keyword_please = make_keyword_lf(keywords=["please", "plz"])

"""Ham comments actually talk about the video's content."""
keyword_song = make_keyword_lf(keywords=["song"], label=HAM)
```

### Generators
Labeling functions may be generated using programmatic methods. We’ve explored this in a number of settings — from automatically-generated labeling functions ([Varma et. al 2019](http://www.vldb.org/pvldb/vol12/p223-varma.pdf)) to natural language interfaces for parsing labeling functions ([Hancock et. al 2018](https://arxiv.org/pdf/1805.03818.pdf)).

### Primitives
For certain use cases, it's helpful to generate primitives, or basic features, over the underlying data for Snorkel operators to access. This is especially important for non-textual data modalities, as we’ve shown in work across medical imaging ([Fries et. al, 2019](https://www.nature.com/articles/s41467-019-11012-3))  and computer vision ([Chen et. al 2019](https://arxiv.org/abs/1904.11622)).

## Contributing
Coming soon!
