from __future__ import annotations
from typing import TYPE_CHECKING

from typing import List, Optional, Union
from pydantic.v1 import AnyUrl


from pydantic.v1 import Field
from pydantic2_schemaorg.Episode import Episode


class TVEpisode(Episode):
    """A TV episode which can be part of a series or season.

    See: https://schema.org/TVEpisode
    Model depth: 4
    """

    type_: str = Field(default="TVEpisode", alias="@type", const=True)
    countryOfOrigin: Optional[Union[List[Union["Country", str]], "Country", str]] = (
        Field(
            default=None,
            description="The country of origin of something, including products as well as creative works such as movie and TV content. In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable. In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.",
        )
    )
    partOfTVSeries: Optional[Union[List[Union["TVSeries", str]], "TVSeries", str]] = (
        Field(
            default=None,
            description="The TV series to which this episode or season belongs.",
        )
    )
    titleEIDR: Optional[
        Union[List[Union[AnyUrl, "URL", str, "Text"]], AnyUrl, "URL", str, "Text"]
    ] = Field(
        default=None,
        description='An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television. For example, the motion picture known as "Ghostbusters" has a titleEIDR of "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]]. Since schema.org types like [[Movie]], [[TVEpisode]], [[TVSeason]], and [[TVSeries]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.',
    )
    subtitleLanguage: Optional[
        Union[List[Union[str, "Text", "Language"]], str, "Text", "Language"]
    ] = Field(
        default=None,
        description="Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).",
    )


if TYPE_CHECKING:
    from pydantic2_schemaorg.Country import Country
    from pydantic2_schemaorg.TVSeries import TVSeries
    from pydantic2_schemaorg.URL import URL
    from pydantic2_schemaorg.Text import Text
    from pydantic2_schemaorg.Language import Language
