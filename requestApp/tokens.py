#CREATE UNIQUE TOKENS TO ALLOW SECURE INDIVIDUAL EMAIL CONFIRMATION
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

#USES RESET TOKEN SYSTEM - ALWAYS UNIQUE
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, COLOUser, timestamp):
        return (
            six.text_type(COLOUser.pk) + six.text_type(COLOUser.time)
            )

account_activation_token = AccountActivationTokenGenerator()