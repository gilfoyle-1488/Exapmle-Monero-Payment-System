"""Fix address out to to

Revision ID: 65bd411ae4fa
Revises: 2dd40202a8ba
Create Date: 2024-11-07 03:23:19.927660

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65bd411ae4fa'
down_revision: Union[str, None] = '2dd40202a8ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monero_withdraw_transaction', sa.Column('address_to', sa.String(length=95), nullable=False))
    op.drop_column('monero_withdraw_transaction', 'address_out')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monero_withdraw_transaction', sa.Column('address_out', sa.VARCHAR(length=95), autoincrement=False, nullable=False))
    op.drop_column('monero_withdraw_transaction', 'address_to')
    # ### end Alembic commands ###