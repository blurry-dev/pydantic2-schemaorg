from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.Intangible import Intangible


class BroadcastFrequencySpecification(Intangible):
    """The frequency in MHz and the modulation used for a particular BroadcastService.

    See: https://schema.org/BroadcastFrequencySpecification
    Model depth: 3
    """

    type_: str = Field(
        default="BroadcastFrequencySpecification", alias="@type", const=True
    )
    broadcastSignalModulation: Optional[
        Union[
            List[Union[str, "Text", "QualitativeValue"]],
            str,
            "Text",
            "QualitativeValue",
        ]
    ] = Field(
        default=None,
        description="The modulation (e.g. FM, AM, etc) used by a particular broadcast service.",
    )
    broadcastSubChannel: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="The subchannel used for the broadcast.",
    )
    broadcastFrequencyValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", "QuantitativeValue", str]],
            StrictInt,
            StrictFloat,
            "Number",
            "QuantitativeValue",
            str,
        ]
    ] = Field(
        default=None,
        description="The frequency in MHz for a particular broadcast.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.QualitativeValue import QualitativeValue
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.QuantitativeValue import QuantitativeValue
