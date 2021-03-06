"""empty message

Revision ID: 519bf64cd1ea
Revises: 
Create Date: 2019-05-15 13:09:32.387546

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '519bf64cd1ea'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('repos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gitid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('chats', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('repos')
    # ### end Alembic commands ###
