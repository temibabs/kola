from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class Model(SQLModel):

    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now, nullable=True)
