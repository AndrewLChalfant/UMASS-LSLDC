#CURRENTLY NOT FUNCTIONING
#CURRENTLY NOT FUNCTIONING
#CURRENTLY NOT FUNCTIONING
#CURRENTLY NOT FUNCTIONING

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, COLOUser, timestamp):
        return (
            six.text_type(COLOUser.pk) + six.text_type(COLOUser.time)
            )

account_activation_token = AccountActivationTokenGenerator()