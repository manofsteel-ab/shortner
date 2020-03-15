"""user_table_user_roles_table

Revision ID: fbebaaad0c54
Revises: aabf843e7b40
Create Date: 2020-03-15 14:44:18.318151

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fbebaaad0c54'
down_revision = 'aabf843e7b40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('updated_by', sa.Integer(), nullable=True),
    sa.Column('deleted_at', sa.DateTime(), nullable=True),
    sa.Column('role_id', sa.String(length=20), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('password', sa.String(length=100), nullable=False))
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_column('users', 'password')
    op.drop_table('user_roles')
    # ### end Alembic commands ###