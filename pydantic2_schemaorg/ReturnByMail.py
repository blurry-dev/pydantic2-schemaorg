from __future__ import annotations


from pydantic.v1 import Field
from pydantic2_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnByMail(ReturnMethodEnumeration):
    """Specifies that product returns must be done by mail.

    See: https://schema.org/ReturnByMail
    Model depth: 5
    """

    type_: str = Field(default="ReturnByMail", alias="@type", const=True)
