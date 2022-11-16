from src.selector import selector
from src.mail_util import MailConfig, MailContext, send_mail
from src.config_context import ConfigContext


def main():
    config = ConfigContext()
    member_list = [1, 2, 3, 4, 5, 6]
    print(selector(member_list))


if __name__ == "__main__":
    main()
