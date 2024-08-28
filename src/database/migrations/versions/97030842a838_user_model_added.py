"""user model added

Revision ID: 97030842a838
Revises: f372e66c8478
Create Date: 2024-08-28 14:31:09.880669

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '97030842a838'
down_revision: Union[str, None] = 'f372e66c8478'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
