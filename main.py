from src.selector import selector
from src.mail_util import MailConfig, MailContext, send_mail
from src.config_context import ConfigContext
import json


def main():
    config = ConfigContext().config
    # load member list
    with open("resource/member_list.json", "r") as f:
        member_list: dict = json.load(f)["member_list"]
        print(member_list)
    # Render result list
    member_target_pair_list = selector(list(member_list.keys()))
    print(member_target_pair_list)
    mail_config = MailConfig(
        mail_from=config["mail"]["from"],
        password=config["mail"]["password"],
        host=config["mail"]["host"],
        port=config["mail"]["port"],
    )
    print(mail_config)
    for mail_pair in member_target_pair_list:
        # Base on result list to rander the result
        mail = prepare_mail()
        # send email
        # send_mail(mail, config)


def prepare_mail() -> MailContext:
    mail_context = MailContext(to="", content="", subject="")
    return mail_context


if __name__ == "__main__":
    main()
