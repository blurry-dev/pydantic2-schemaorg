from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Enumeration import Enumeration


class MeasurementTypeEnumeration(Enumeration):
    """Enumeration of common measurement types (or dimensions), for example \"chest\" for a person, \"inseam\"
     for pants, \"gauge\" for screws, or \"wheel\" for bicycles.

    See: https://schema.org/MeasurementTypeEnumeration
    Model depth: 4
    """

    type_: str = Field(default="MeasurementTypeEnumeration", alias="@type", const=True)
