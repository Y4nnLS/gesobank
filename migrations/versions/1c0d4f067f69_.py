"""empty message

Revision ID: 1c0d4f067f69
Revises: 
Create Date: 2024-05-07 16:13:38.998140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1c0d4f067f69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('card',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cardName', sa.String(), nullable=False),
    sa.Column('number', sa.String(), nullable=False),
    sa.Column('cvc', sa.String(), nullable=False),
    sa.Column('validity', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('userHash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('userHash', sa.String(), nullable=False),
    sa.Column('passwordHash', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('cpf', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('balance', sa.String(), nullable=True),
    sa.Column('publickey', sa.Text(), nullable=True),
    sa.Column('privatekey', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('userHash')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('card')
    # ### end Alembic commands ###
