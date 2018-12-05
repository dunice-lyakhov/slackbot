from slackclient import SlackClient

from core.settings import SLACK_CLIENT_ID


class SlackBirthdayHelper(object):
    def __init__(self):
        self.slack_client = SlackClient(SLACK_CLIENT_ID)

    def slack_connect(self):
        return self.slack_client.rtm_connect()

    def slack_read_rtm(self):
        return self.slack_client.rtm_read()

    def write_to_slack(self, channel, message):
        return self.slack_client.api_call("chat.postMessage", channel=channel,
                                          text=message, as_user=True)
