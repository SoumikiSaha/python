# Your code here
import unittest

class NotLoggedInException(Exception):
    pass

class TestCacheDecorator(unittest.TestCase):

    def setUp(self):
        self.cache = CacheDecorator()

    def test_set_and_get_value(self):
        self.cache.set('key1', 'value1')
        self.assertEqual(self.cache.get('key1'), 'value1')

    def test_get_nonexistent_key(self):
        self.assertIsNone(self.cache.get('key2'))

    def test_overwrite_value(self):
        self.cache.set('key1', 'value1')
        self.cache.set('key1', 'value2')
        self.assertEqual(self.cache.get('key1'), 'value2')

    def test_cache_invalidation(self):
        self.cache.set('key1', 'value1')
        self.cache.invalidate('key1')
        self.assertIsNone(self.cache.get('key1'))

    def test_cache_size_limit(self):
        for i in range(5):
            self.cache.set(f'key{i}', f'value{i}')
        self.cache.set('key5', 'value5')
        self.assertIsNone(self.cache.get('key0'))  # Assuming a size limit of 5 items
        self.assertEqual(self.cache.get('key5'), 'value5')

# task 4
class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap

# task 5

class LoginMetaClass(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value):
                dct[key] = cls.login_required(value)
        return super(LoginMetaClass, cls).__new__(cls, name, bases, dct)
    
    @staticmethod
    def login_required(func):
        def wrapper(self, *args, **kwargs):
            if not getattr(self, 'logged_in', False):
                raise NotLoggedInException("User must be logged in to call this method.")
            return func(self, *args, **kwargs)
        return wrapper


class AccessWebsite(metaclass=LoginMetaClass):
    logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True

    def access_website(self):
        return "Success"
    

