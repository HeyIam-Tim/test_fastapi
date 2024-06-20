import pytest
from sqlalchemy import insert, select

from src.auth.models import role
from .conftest import client, async_session_maker


async def test_add_role():
    async with async_session_maker() as session:
        stmt = insert(role).values(id=1, name='Admin', permissions=None)
        await session.execute(stmt)
        await session.commit()

        query = select(role)
        result = await session.execute(query)
        assert result.all() == [(1, 'Admin', None)], 'No Role'


def test_register():
    response = client.post(
        url='/auth/register',
        json={
            "email": "string@gmail.com",
            "password": "string_user",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "role_id": 1,
            "username": "string_username",
        },
    )

    assert response.status_code == 201
