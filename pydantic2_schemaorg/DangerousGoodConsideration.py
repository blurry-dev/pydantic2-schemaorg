from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.AdultOrientedEnumeration import AdultOrientedEnumeration


class DangerousGoodConsideration(AdultOrientedEnumeration):
    """The item is dangerous and requires careful handling and/or special training of the user. See also the [UN Model
     Classification](https://unece.org/DAM/trans/danger/publi/unrec/rev17/English/02EREv17_Part2.pdf)
     defining the 9 classes of dangerous goods such as explosives, gases, flammables, and more.

    See: https://schema.org/DangerousGoodConsideration
    Model depth: 5
    """

    type_: str = Field(default="DangerousGoodConsideration", alias="@type", const=True)
