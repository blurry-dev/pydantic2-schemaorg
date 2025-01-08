from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.LegalValueLevel import LegalValueLevel


class OfficialLegalValue(LegalValueLevel):
    """All the documents published by an official publisher should have at least the legal value level \"OfficialLegalValue\".
     This indicates that the document was published by an organisation with the public task of making it available
     (e.g. a consolidated version of an EU directive published by the EU Office of Publications).

    See: https://schema.org/OfficialLegalValue
    Model depth: 5
    """

    type_: str = Field(default="OfficialLegalValue", alias="@type", const=True)
