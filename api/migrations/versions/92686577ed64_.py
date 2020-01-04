"""empty message

Revision ID: 92686577ed64
Revises: 
Create Date: 2020-01-04 18:49:16.114826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92686577ed64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###