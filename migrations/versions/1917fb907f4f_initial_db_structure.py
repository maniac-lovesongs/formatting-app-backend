"""initial db structure

Revision ID: 1917fb907f4f
Revises: 
Create Date: 2024-01-16 06:46:05.413526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1917fb907f4f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('insta_char',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('value', sa.String(length=1), nullable=False),
    sa.Column('symbol', sa.Unicode(length=10), nullable=False),
    sa.Column('style_font_pair_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['style_font_pair_id'], ['style_font_pair.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('insta_char')
    # ### end Alembic commands ###
