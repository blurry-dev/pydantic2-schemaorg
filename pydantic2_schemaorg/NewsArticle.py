from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.Article import Article


class NewsArticle(Article):
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials
     for understanding the news. A more detailed overview of [schema.org News markup](/docs/news.html) is also
     available.

    See: https://schema.org/NewsArticle
    Model depth: 4
    """

    type_: str = Field(default="NewsArticle", alias="@type", const=True)
    printColumn: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The number of the column in which the NewsArticle appears in the print edition.",
    )
    printSection: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="If this NewsArticle appears in print, this field indicates the print section in which the article appeared.",
    )
    dateline: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included in news articles that describes where and when the story was written or filed though the date is often omitted. Sometimes only a placename is provided. Structured representations of dateline-related information can also be expressed more explicitly using [[locationCreated]] (which represents where a work was created, e.g. where a news report was written). For location depicted or described in the content, use [[contentLocation]]. Dateline summaries are oriented more towards human readers than towards automated processing, and can vary substantially. Some examples: "BEIRUT, Lebanon, June 2.", "Paris, France", "December 19, 2017 11:43AM Reporting from Washington", "Beijing/Moscow", "QUEZON CITY, Philippines".',
    )
    printEdition: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The edition of the print product in which the NewsArticle appears.",
    )
    printPage: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
