"""fix add accounts monero

Revision ID: 1eb00ae6e4d7
Revises: 3319d0b73ac8
Create Date: 2024-11-03 09:31:30.909905

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1eb00ae6e4d7'
down_revision: Union[str, None] = '3319d0b73ac8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('monero_address', 'address',
               existing_type=sa.VARCHAR(length=95),
               nullable=True)
    op.alter_column('monero_address', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('monero_address', 'sub_address_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('monero_address', 'sub_address_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('monero_address', 'account_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('monero_address', 'address',
               existing_type=sa.VARCHAR(length=95),
               nullable=False)
    # ### end Alembic commands ###
