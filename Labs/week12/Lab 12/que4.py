from abc import ABC, abstractmethod


class LegacyNotificationSystem:
    def send_sms_notification(self, phoneNumber: str, message: str) -> None:
        print("Simulates sending an SMS notification")

class NewNotificationSystem(ABC):
    @abstractmethod
    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        pass

    @abstractmethod
    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        pass

    @abstractmethod
    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        pass


class NotificationAdapter(NewNotificationSystem):
    def __init__(self, obj: LegacyNotificationSystem) -> None:
        self.__obj = obj

    def send_email_notification(self, emailAddress: str, subject: str, body: str) -> None:
        print("\nEmail-address:", emailAddress)
        print("Subject:", subject)
        print("Body:", body)
        print("Sending Mail...\n")

    def sendPushNotification(self, deviceToken: str, title: str, message: str) -> None:
        phone_no = self.get_phone_number(deviceToken)
        self.__obj.send_sms_notification(phone_no, message = title + ' | ' + message)

    def send_social_media_update(self, social_media_platform: str, postContent: str) -> None:
        print("\nSocial media platform:", social_media_platform)
        print("Post-content:", postContent)
        print("Sending Media update...")
    
    def get_phone_number(self, deviceToken) -> str:
        return "+1 XXX XXX-XXXX"


class NotificationFactory:
    @staticmethod
    def get_notification_system() -> NewNotificationSystem:
        return NotificationAdapter(LegacyNotificationSystem())
    

def main():
    notif_system = NotificationFactory.get_notification_system()
    notif_system.send_email_notification("perterine@yahoo.com", "Recharge", "Hello ____, your recharge has been done successfully!")
    notif_system.sendPushNotification("21a54e93v60n7y", "Recharge-Done", "Hello ____, your recharge has been done successfully!")
    notif_system.send_social_media_update("Facebook", "Hello ____, your recharge has been done successfully!")


if __name__ == "__main__":
    main()
