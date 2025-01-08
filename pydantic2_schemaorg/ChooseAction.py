from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.AssessAction import AssessAction


class ChooseAction(AssessAction):
    """The act of expressing a preference from a set of options or a large or unbounded set of choices/options.

    See: https://schema.org/ChooseAction
    Model depth: 4
    """

    type_: str = Field(default="ChooseAction", alias="@type", const=True)
    actionOption: Optional[
        Union[List[Union[str, "Text", "Thing"]], str, "Text", "Thing"]
    ] = Field(
        default=None,
        description="A sub property of object. The options subject to this action.",
    )
    option: Optional[Union[List[Union[str, "Text", "Thing"]], str, "Text", "Thing"]] = (
        Field(
            default=None,
            description="A sub property of object. The options subject to this action.",
        )
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Thing import Thing
