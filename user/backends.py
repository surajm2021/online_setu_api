from django.contrib.auth import login

from .models import User
import logging


def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
        if user.is_active:
            return user
        return None
    except User.DoesNotExist:
        logging.getLogger("error_logger").error("user with %(user_id)d not found")
        return None


class MyAuthBackend(object):
    def authenticate(self, username, password):
        print(username)
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
            else:
                return None
        except User.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None
