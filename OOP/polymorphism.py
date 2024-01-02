# Polymorphism in Object-Oriented Python
# Polymorphism is the principle that allows
# classes derived from the same superclass
# to have methods with the same signature
# but different behaviors.
# Method signature = Same name and number
# of parameters (return is not part of the signature)
# Opinion + principles that matter:
# Method signature: same name, parameters, and return
# SOLID
# Liskov Substitution Principle
# Objects of a superclass should be replaceable
# with objects of a subclass without affecting the application.
# Method Overloading 🐍 = ❌
# Method Overriding 🐍 = ✅
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool:...


class EmailNotification(Notification):
    def send(self) -> bool:
        print('E-mail: sending - ', self.message)
        return True


class SMSNotification(Notification):
    def send(self) -> bool:
        print('SMS: sending - ', self.message)
        return True


def notifying(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('Notification sent.')
    else:
        print('Notification not sent.')

email_notification = EmailNotification('Testing e-mail.')
notifying(email_notification)

sms_notification = SMSNotification('Testing SMS.')
notifying(sms_notification)