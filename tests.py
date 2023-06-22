import unittest
from datetime import datetime, timedelta

from app import create_app, db
from app.models import User, Post
from config import Config


class TestConfig(Config):
    """
    Конфигурация сервера для тестирования
    """
    TESTING = True

    # Путь к локальной БД sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite://'


class UserModelCase(unittest.TestCase):
    """
    Класс для тестирования сценарий пользователя
    """
    def setUp(self):
        """
        Подготовка к тестированию
        :return:
        """
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        """
        После тестирования
        :return:
        """
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        """
        Тест хеширования пароля
        :return:
        """
        with self.app.app_context():
            user = User()
            user.set_password('cat')
            self.assertFalse(user.check_password('dog'))
            self.assertTrue(user.check_password('cat'))

    def test_avatar(self):
        """
        Тест генерации аватарки
        :return:
        """
        with self.app.app_context():
            user = User(username='john', email='john@example.com')
            self.assertEqual(user.avatar(128), ('https://www.gravatar.com/avatar/'
                                                'd4c74594d841139328695756648b6bd6'
                                                '?d=identicon&s=128'))

    def test_follow(self):
        """
        Тестирование подписки
        Cценарии:
        1. Создать двух пользователей
        2. Пользователь1 подписывается на Пользователь2
        3. Пользователь1 отписывается от Пользователь2
        :return:
        """
        with self.app.app_context():
            u1 = User(username='john', email='john@example.com')
            u2 = User(username='susan', email='susan@example.com')
            db.session.add(u1)
            db.session.add(u2)
            db.session.commit()
            self.assertEqual(u1.followed.all(), [])
            self.assertEqual(u1.followers.all(), [])

            u1.follow(u2)
            db.session.commit()
            self.assertTrue(u1.is_following(u2))
            self.assertEqual(u1.followed.count(), 1)
            self.assertEqual(u1.followed.first().username, 'susan')
            self.assertEqual(u2.followers.count(), 1)
            self.assertEqual(u2.followers.first().username, 'john')

            u1.unfollow(u2)
            db.session.commit()
            self.assertFalse(u1.is_following(u2))
            self.assertEqual(u1.followed.count(), 0)
            self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        """
        Тестирование публикаций
        Сценарии:
        1. Создать пользователей
        2. Создать посты
        3. Подписаться на пользователей
        3. Проверить публикации (свои + публикации тех, на кого подписан)
        :return:
        """
        with self.app.app_context():

            u1 = User(username='john', email='john@example.com')
            u2 = User(username='susan', email='susan@example.com')
            u3 = User(username='mary', email='mary@example.com')
            u4 = User(username='david', email='david@example.com')
            db.session.add_all([u1, u2, u3, u4])

            now = datetime.utcnow()
            p1 = Post(body="post from john", author=u1,
                      timestamp=now + timedelta(seconds=1))
            p2 = Post(body="post from susan", author=u2,
                      timestamp=now + timedelta(seconds=4))
            p3 = Post(body="post from mary", author=u3,
                      timestamp=now + timedelta(seconds=3))
            p4 = Post(body="post from david", author=u4,
                      timestamp=now + timedelta(seconds=2))
            db.session.add_all([p1, p2, p3, p4])
            db.session.commit()

            u1.follow(u2)
            u1.follow(u4)
            u2.follow(u3)
            u3.follow(u4)
            db.session.commit()

            f1 = u1.followed_posts().all()  # u1 подписан на u2, u4 (посты  p1, p2 ,p4)
            f2 = u2.followed_posts().all()  # u2 подписан на u3 (посты p1, p3)
            f3 = u3.followed_posts().all()  # u3 подписан на u4 (посты p3, p4)
            f4 = u4.followed_posts().all()  # u4 нет подписок (пост p4)
            self.assertEqual(f1, [p2, p4, p1])
            self.assertEqual(f2, [p2, p3])
            self.assertEqual(f3, [p3, p4])
            self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity - уровень детализации
