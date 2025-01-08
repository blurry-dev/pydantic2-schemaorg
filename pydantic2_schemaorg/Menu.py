from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.CreativeWork import CreativeWork


class Menu(CreativeWork):
    """A structured representation of food or drink items available from a FoodEstablishment.

    See: https://schema.org/Menu
    Model depth: 3
    """

    type_: str = Field(default="Menu", alias="@type", const=True)
    hasMenuItem: Optional[Union[List[Union["MenuItem", str]], "MenuItem", str]] = Field(
        default=None,
        description="A food or drink item contained in a menu or menu section.",
    )
    hasMenuSection: Optional[
        Union[List[Union["MenuSection", str]], "MenuSection", str]
    ] = Field(
        default=None,
        description="A subgrouping of the menu (by dishes, course, serving time period, etc.).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.MenuItem import MenuItem
    from pydantic2_schemaorg.MenuSection import MenuSection
