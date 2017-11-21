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


class TestLeagueBasic(TestDB):

    # utility functions
    def insert_user(self, offset):
        salt = bcrypt.gensalt()
        new_user = User(name=str(offset), email = "{0}@{0}.com".format(offset), password = bcrypt.hashpw(str(offset) + salt, salt), salt = salt)
        self.session.add(new_user)
        self.session.commit()
        return new_user

    def test_league(self):
        now = datetime.now();
        owner = self.insert_user(0);
        new_league = League(name = "best 80's songs", owner = owner.id, principle = 1000.0, term_start = now, term_end = now + timedelta(days=30), last_updated = now)
        self.session.add(new_league)
        self.session.commit()


        owner_placement = Placement(user = owner.id, league = )
        user2 = self.insert_user(1);
        user3 = self.insert_user(1);
        user4 = self.insert_user(1);

if __name__ == "__main__":
    unittest.main()