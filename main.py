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
        mail_from=config["mail"]["mail_from"],
        password=config["mail"]["password"],
        host=config["mail"]["host"],
        port=config["mail"]["port"],
    )
    print(mail_config)
    for mail_pair in member_target_pair_list:
        # Base on result list to rander the result
        mail = prepare_mail(mail_pair, member_list)
        # send email
        send_mail(mail, config=mail_config)


def prepare_mail(mail_pair, member_list) -> MailContext:
    member = mail_pair[0]
    target = mail_pair[1]
    
    # Rander mail body
    subject = "2022 Christmas Exchange Gift - UAT"
    content = f"Hello {member},Your target is {target}"
    
    mail_context = MailContext(to=member_list[member], content=content,subject=subject)
    return mail_context


if __name__ == "__main__":
    main()
