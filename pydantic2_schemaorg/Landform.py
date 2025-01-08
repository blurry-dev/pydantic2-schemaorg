from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Place import Place


class Landform(Place):
    """A landform or physical feature. Landform elements include mountains, plains, lakes, rivers, seascape and
     oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous
     terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.

    See: https://schema.org/Landform
    Model depth: 3
    """

    type_: str = Field(default="Landform", alias="@type", const=True)
