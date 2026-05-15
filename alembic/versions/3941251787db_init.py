"""init

Revision ID: 3941251787db
Revises: 233bf7ea78fb
Create Date: 2026-05-14 16:02:35.217102

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3941251787db'
down_revision: Union[str, Sequence[str], None] = '233bf7ea78fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
