"""User model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


from app import app
import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, Follows


app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///warbler-test'))


class UserModelTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.remove()
        db.drop_all()

    def test_user_model(self):
        """Does basic model work?"""

        u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no messages & no followers
        self.assertEqual(len(u.messages), 0)
        self.assertEqual(len(u.followers), 0)

        self.assertEqual(User.query.count(), 1)

        # User repr method shoud work as expected
        self.assertEqual(repr(u), "<User #1: testuser, test@test.com>")

    def test_is_following(self):

        u1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )

        u3 = User(
            email="test3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)

        db.session.commit()
        # create a new Follows instance
        follow = Follows(
            user_being_followed_id=u2.id,
            user_following_id=u1.id
        )

        db.session.add(follow)
        db.session.commit()

        # is_following successfully detect when user1 is following user2
        self.assertTrue(u1.is_following(u2))

        # is_following successfully detect when user1 is not following user3
        self.assertFalse(u1.is_following(u3))

    def test_is_followed(self):

        u1 = User(
            email="test1@test.com",
            username="testuser1",
            password="HASHED_PASSWORD"
        )

        u2 = User(
            email="test2@test.com",
            username="testuser2",
            password="HASHED_PASSWORD"
        )

        u3 = User(
            email="test3@test.com",
            username="testuser3",
            password="HASHED_PASSWORD"
        )

        db.session.add(u1)
        db.session.add(u2)
        db.session.add(u3)

        db.session.commit()

        follow = Follows(
            user_being_followed_id=u1.id,
            user_following_id=u2.id
        )

        db.session.add(follow)
        db.session.commit()

        # is_followed_by successfully detect when user1 is followed by user2
        self.assertTrue(u1.is_followed_by(u2))

        # is_followed_by successfully detect when user1 is not followed by user3
        self.assertFalse(u1.is_followed_by(u3))

    def test_user_create(self):
        """Test user sign up"""

        # Create a user with a unique email
        User.signup('testuser1', 'test1@test.com', 'password', None)
        db.session.commit()

        # Try to create a new user with the same email
        user = User.signup('testuser2', 'test1@test.com', 'password', None)
        with self.assertRaises(IntegrityError):
            db.session.commit()

        # Make sure the user was not created
        self.assertIsNone(user.id)
        db.session.rollback()
    #    User.create fail to create a new user with non-nullable field

        # Try to create a user with blank email
        user = User.signup(
            email=None,
            username="testuser3",
            password="password",
            image_url=None
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

         # Make sure the user was not created
        self.assertIsNone(user.id)
        db.session.rollback()

        # Try to create a user with a blank username
        user = User.signup(
            email="test4@test.com",
            username=None,
            password="password",
            image_url=None
        )
        with self.assertRaises(IntegrityError):
            db.session.commit()

         # Make sure the user was not created
        self.assertIsNone(user.id)
        db.session.rollback()

        # Try to create a user with a blank password
        with self.assertRaises(ValueError):
            user = User.signup(
                email="test5@test.com",
                username="user5",
                password=None,
                image_url=None
            )


def test_user_authenticate(self):
    """Test the user authentication"""
    # Create a user with a unique email
    User.signup('testuser1', 'test1@test.com', 'password', None)
    db.session.commit()

    # User.authenticate successfully return a user when given
    # a valid username and password
    self.assertTrue(User.authenticate('testuser1', 'password'))

    # User.authenticate fail to return a user when the username is invalid
    self.assertFalse(User.authenticate('notauser', 'password'))

    # User.authenticate fail to return a user when the password is invalid
    self.assertFalse(User.authenticate('testuser1', 'WrongPassword'))
