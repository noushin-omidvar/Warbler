"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_message_model.py


from app import app
import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError
from models import db, User, Message, Follows


app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgresql:///warbler-test'))


class UserModelTestCase(TestCase):
    """Test model for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        db.drop_all()
        db.create_all()
        User.query.delete()
        Message.query.delete()
        Follows.query.delete()

        self.client = app.test_client()

        self.u = User(
            email="test@test.com",
            username="testuser",
            password="HASHED_PASSWORD"
        )

        db.session.add(self.u)
        db.session.commit()

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.remove()
        db.drop_all()

    def test_message_model(self):
        """Does basic model work?"""

        msg = Message(text="Message1", user_id=1)

        db.session.add(msg)
        db.session.commit()

        # User should have 1 messages
        self.assertEqual(len(self.u.messages), 1)
        self.assertEqual(Message.query.count(), 1)
