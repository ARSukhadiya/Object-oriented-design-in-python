from abc import ABC, abstractmethod

class LegacyPaymentGateway:
    def process_credit_card_payment(self, credit_card_number: str, expiration_date: str, cvv: str, amount: float) -> bool:
        print("Simulates processing a credit card payment")
        return True
    
class  PayPalPaymentGateway(ABC):
    @abstractmethod
    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        pass

class PaymentAdapter(PayPalPaymentGateway):
    def __init__(self, obj: LegacyPaymentGateway) -> None:
        self.__obj = obj

    def process_paypal_payment(self, email_address: str, amount: float) -> bool:
        credit_card_number = self.get_credit_card_number(email_address)
        cvv = self.get_cvv(email_address)
        expiration_date = self.expiration_date(email_address)
        return self.__obj.process_credit_card_payment(credit_card_number, expiration_date, cvv, amount)

    def get_credit_card_number(self, email_address):
        return "5200-4235-7361-1071"

    def get_cvv(self, email_address):
        return "077"

    def expiration_date(self, email_address):
        return "01-07-2029"


class PaymentFactory:
    @staticmethod
    def get_payment_gateway() -> PayPalPaymentGateway:
        return PaymentAdapter(LegacyPaymentGateway())

    
def main():
    gateway = PaymentFactory.get_payment_gateway()
    print(gateway.process_paypal_payment("peterine@yahoo.com", 3000))


if __name__ == "__main__":
    main()
