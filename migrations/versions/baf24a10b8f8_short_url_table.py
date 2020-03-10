"""short-url-table

Revision ID: baf24a10b8f8
Revises: 750ffd3104d7
Create Date: 2020-03-10 20:32:48.791704

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'baf24a10b8f8'
down_revision = '750ffd3104d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('urls',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('createdAt', sa.DateTime(), nullable=False),
    sa.Column('createdBy', sa.Integer(), nullable=True),
    sa.Column('updatedAt', sa.DateTime(), nullable=False),
    sa.Column('updatedBy', sa.Integer(), nullable=True),
    sa.Column('deletedAt', sa.DateTime(), nullable=True),
    sa.Column('deleteToken', sa.String(length=100), nullable=False),
    sa.Column('longUrl', sa.Text(), nullable=False),
    sa.Column('shortUrl', sa.String(length=200), nullable=False),
    sa.Column('expiresAt', sa.DateTime(), nullable=False),
    sa.Column('hitCount', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('urls')
    # ### end Alembic commands ###
