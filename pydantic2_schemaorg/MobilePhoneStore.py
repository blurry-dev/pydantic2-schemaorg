from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.Store import Store


class MobilePhoneStore(Store):
    """A store that sells mobile phones and related accessories.

    See: https://schema.org/MobilePhoneStore
    Model depth: 5
    """

    type_: str = Field(default="MobilePhoneStore", alias="@type", const=True)
