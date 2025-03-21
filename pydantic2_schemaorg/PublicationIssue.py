from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class PublicationIssue(CreativeWork):
    """A part of a successively published publication such as a periodical or publication volume, often numbered,
     usually containing a grouping of works such as articles. See also [blog post](http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html).

    See: https://schema.org/PublicationIssue
    Model depth: 3
    """

    type_: str = Field(default="PublicationIssue", alias="@type", const=True)
    pageStart: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description='The page on which the work starts; for example "135" or "xiii".',
    )
    issueNumber: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description='Identifies the issue of publication; for example, "iii" or "2".',
    )
    pagination: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description='Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".',
    )
    pageEnd: Optional[
        Union[List[Union[int, "Integer", str, "Text"]], int, "Integer", str, "Text"]
    ] = Field(
        default=None,
        description='The page on which the work ends; for example "138" or "xvi".',
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Integer import Integer
    from pydantic2_schemaorg.Text import Text
