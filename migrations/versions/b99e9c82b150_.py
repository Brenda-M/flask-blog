"""empty message

Revision ID: b99e9c82b150
Revises: 7fbaaaf3a5a2
Create Date: 2020-05-09 19:39:57.378935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99e9c82b150'
down_revision = '7fbaaaf3a5a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.add_column('blogposts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('blogposts_users_id_fkey', 'blogposts', type_='foreignkey')
    op.create_foreign_key(None, 'blogposts', 'users', ['user_id'], ['id'])
    op.drop_column('blogposts', 'users_id')
    op.drop_constraint('users_role_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'role_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_role_id_fkey', 'users', 'roles', ['role_id'], ['id'])
    op.add_column('blogposts', sa.Column('users_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'blogposts', type_='foreignkey')
    op.create_foreign_key('blogposts_users_id_fkey', 'blogposts', 'users', ['users_id'], ['id'])
    op.drop_column('blogposts', 'user_id')
    op.create_table('roles',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='roles_pkey')
    )
    # ### end Alembic commands ###
