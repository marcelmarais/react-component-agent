from typing import List
from data.shadcn_ui_docs import SHAD_CN_UI_COMPONENTS
from pydantic.v1 import BaseModel, Field


class GetDocumentationDataModel(BaseModel):
    component_names: List[str] = Field(
        min_items=1,
        example=SHAD_CN_UI_COMPONENTS,
        description=f"A list of components to retrieve SHADCN UI documentation for. Must be a combination of {SHAD_CN_UI_COMPONENTS}"
    )
