from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from getpass import getpass
from datetime import datetime, timedelta
import bcrypt
import unittest
 
from config import Config
from declarative import Base, User, League, Investment, Placement

class TestDB(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        TestDB.ENGINE = create_engine(Config.TEST_ENGINE)

    def setUp(self):
        Base.metadata.drop_all(TestDB.ENGINE)
        Base.metadata.create_all(TestDB.ENGINE)
        DBSession = sessionmaker(bind=TestDB.ENGINE)
        self.session = DBSession()


class TestUserBasic(TestDB):

    @classmethod
    def setUpClass(cls):
        super(TestUserBasic, cls).setUpClass()
        TestUserBasic.PASSWORD = "the hands of a government man"

    # utility functions
    def insert_user(self):
        salt = bcrypt.gensalt()
        new_user = User(name='born_under_punches', email = "remain_in_light@talking_heads.com", password = bcrypt.hashpw(TestUserBasic.PASSWORD + salt, salt), salt = salt)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    # test functions
    def test_double_insert(self):
        self.insert_user();
        self.assertRaises(IntegrityError, self.insert_user)

    def test_password(self):
        supplied = self.insert_user();
        queried = self.session.query(User).first()
        self.assertEqual(supplied, queried)
        self.assertNotEqual(queried.password, TestUserBasic.PASSWORD)
        salt_str = queried.salt.encode('utf-8')
        self.assertEqual(queried.password, bcrypt.hashpw(TestUserBasic.PASSWORD + salt_str, salt_str))

if __name__ == "__main__":
    unittest.main()