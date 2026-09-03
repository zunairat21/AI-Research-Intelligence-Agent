from pydantic import BaseModel, Field

class ArticleIntelligence(BaseModel):
        summary : str = Field(min_length=1)
        key_points : list[str] = Field(min_length=1)
        why_it_matters :str = Field(min_length=1)
