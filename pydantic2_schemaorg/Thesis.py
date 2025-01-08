from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Thesis(CreativeWork):
    """A thesis or dissertation document submitted in support of candidature for an academic degree or professional
     qualification.

    See: https://schema.org/Thesis
    Model depth: 3
    """

    type_: str = Field(default="Thesis", alias="@type", const=True)
    inSupportOf: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="Qualification, candidature, degree, application that Thesis supports.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
