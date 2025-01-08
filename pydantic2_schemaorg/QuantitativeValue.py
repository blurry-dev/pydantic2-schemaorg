from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl, StrictBool, StrictInt, StrictFloat


from pydantic.v1 import Field
from pydantic2_schemaorg.StructuredValue import StructuredValue


class QuantitativeValue(StructuredValue):
    """A point value or interval for product characteristics and other purposes.

    See: https://schema.org/QuantitativeValue
    Model depth: 4
    """

    type_: str = Field(default="QuantitativeValue", alias="@type", const=True)
    valueReference: Optional[
        Union[
            List[
                Union[
                    str,
                    "Text",
                    "QualitativeValue",
                    "PropertyValue",
                    "Enumeration",
                    "QuantitativeValue",
                    "DefinedTerm",
                    "StructuredValue",
                    "MeasurementTypeEnumeration",
                ]
            ],
            str,
            "Text",
            "QualitativeValue",
            "PropertyValue",
            "Enumeration",
            "QuantitativeValue",
            "DefinedTerm",
            "StructuredValue",
            "MeasurementTypeEnumeration",
        ]
    ] = Field(
        default=None,
        description="A secondary value that provides additional information on the original value, e.g. a reference temperature or a type of measurement.",
    )
    unitCode: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description="The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.",
    )
    maxValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The upper value of some characteristic or property.",
    )
    value: Optional[
        Union[
            List[
                Union[
                    StrictInt,
                    StrictFloat,
                    "Number",
                    StrictBool,
                    "Boolean",
                    str,
                    "Text",
                    "StructuredValue",
                ]
            ],
            StrictInt,
            StrictFloat,
            "Number",
            StrictBool,
            "Boolean",
            str,
            "Text",
            "StructuredValue",
        ]
    ] = Field(
        default=None,
        description="The value of a [[QuantitativeValue]] (including [[Observation]]) or property value node. * For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'. * For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'. * Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols. * Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.",
    )
    minValue: Optional[
        Union[
            List[Union[StrictInt, StrictFloat, "Number", str]],
            StrictInt,
            StrictFloat,
            "Number",
            str,
        ]
    ] = Field(
        default=None,
        description="The lower value of some characteristic or property.",
    )
    unitText: Optional[Union[List[Union[str, "Text"]], str, "Text"]] = Field(
        default=None,
        description="A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for <a href='unitCode'>unitCode</a>.",
    )
    additionalProperty: Optional[
        Union[List[Union["PropertyValue", str]], "PropertyValue", str]
    ] = Field(
        default=None,
        description="A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.QualitativeValue import QualitativeValue
    from pydantic2_schemaorg.PropertyValue import PropertyValue
    from pydantic2_schemaorg.Enumeration import Enumeration
    from pydantic2_schemaorg.DefinedTerm import DefinedTerm
    from pydantic2_schemaorg.StructuredValue import StructuredValue
    from pydantic2_schemaorg.MeasurementTypeEnumeration import (
        MeasurementTypeEnumeration,
    )
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Number import Number
    from pydantic2_schemaorg.Boolean import Boolean
