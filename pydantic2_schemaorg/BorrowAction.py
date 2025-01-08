from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union


from pydantic.v1 import Field
from pydantic2_schemaorg.TransferAction import TransferAction


class BorrowAction(TransferAction):
    """The act of obtaining an object under an agreement to return it at a later date. Reciprocal of LendAction. Related
     actions: * [[LendAction]]: Reciprocal of BorrowAction.

    See: https://schema.org/BorrowAction
    Model depth: 4
    """

    type_: str = Field(default="BorrowAction", alias="@type", const=True)
    lender: Optional[
        Union[List[Union["Person", "Organization", str]], "Person", "Organization", str]
    ] = Field(
        default=None,
        description="A sub property of participant. The person that lends the object being borrowed.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Person import Person
    from pydantic2_schemaorg.Organization import Organization
