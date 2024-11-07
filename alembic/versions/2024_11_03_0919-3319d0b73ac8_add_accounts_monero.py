"""add accounts monero

Revision ID: 3319d0b73ac8
Revises: 1fcdcacb1299
Create Date: 2024-11-03 09:19:08.726844

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3319d0b73ac8'
down_revision: Union[str, None] = '1fcdcacb1299'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('monero_address', sa.Column('account_id', sa.Integer(), nullable=False))
    op.add_column('monero_address', sa.Column('sub_address_id', sa.Integer(), nullable=False))
    op.alter_column('monero_address', 'address',
               existing_type=sa.VARCHAR(length=100),
               type_=sa.String(length=95),
               existing_nullable=False)
    op.create_unique_constraint(None, 'monero_address', ['account_id'])
    op.add_column('monero_deposit_transaction', sa.Column('account_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'monero_deposit_transaction', ['account_id'])
    op.add_column('monero_withdraw_transaction', sa.Column('account_id', sa.Integer(), nullable=False))
    op.create_unique_constraint(None, 'monero_withdraw_transaction', ['account_id'])
    op.add_column('users', sa.Column('monero_account_id', sa.Integer(), nullable=False))
    op.add_column('users', sa.Column('monero_zero_address', sa.String(length=95), nullable=True))
    op.drop_index('ix_users_tg_chat_id', table_name='users')
    op.create_unique_constraint(None, 'users', ['tg_chat_id'])
    op.create_unique_constraint(None, 'users', ['monero_account_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_constraint(None, 'users', type_='unique')
    op.create_index('ix_users_tg_chat_id', 'users', ['tg_chat_id'], unique=True)
    op.drop_column('users', 'monero_zero_address')
    op.drop_column('users', 'monero_account_id')
    op.drop_constraint(None, 'monero_withdraw_transaction', type_='unique')
    op.drop_column('monero_withdraw_transaction', 'account_id')
    op.drop_constraint(None, 'monero_deposit_transaction', type_='unique')
    op.drop_column('monero_deposit_transaction', 'account_id')
    op.drop_constraint(None, 'monero_address', type_='unique')
    op.alter_column('monero_address', 'address',
               existing_type=sa.String(length=95),
               type_=sa.VARCHAR(length=100),
               existing_nullable=False)
    op.drop_column('monero_address', 'sub_address_id')
    op.drop_column('monero_address', 'account_id')
    # ### end Alembic commands ###