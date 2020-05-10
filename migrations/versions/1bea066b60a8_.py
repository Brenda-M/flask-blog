"""empty message

Revision ID: 1bea066b60a8
Revises: b99e9c82b150
Create Date: 2020-05-09 19:47:21.956402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1bea066b60a8'
down_revision = 'b99e9c82b150'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogposts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('blogposts_users_id_fkey', 'blogposts', type_='foreignkey')
    op.create_foreign_key(None, 'blogposts', 'users', ['user_id'], ['id'])
    op.drop_column('blogposts', 'users_id')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('blogposts', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogposts', type_='foreignkey')
    op.create_foreign_key('blogposts_users_id_fkey', 'blogposts', 'users', ['users_id'], ['id'])
    op.drop_column('blogposts', 'user_id')
    # ### end Alembic commands ###