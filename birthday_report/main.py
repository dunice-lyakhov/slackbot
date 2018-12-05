from apscheduler.schedulers.background import BackgroundScheduler

from birthday_report import app
from birthday_report.bot import SlackBirthdayHelper
from birthday_report.google_sheets import get_sheet_data
from core.utils import is_birthday
from core.settings import HOURS, MINUTES, CHANNEL_NAME


@app.route('/')
def endpoint():
    birthday_persons = main()
    return birthday_persons


def main():
    """
    Main function for slack bot.

    :return:
    """

    # Get birthdays from google sheet
    data_from_sheets = get_sheet_data()

    # List of all birthdays
    birthday_persons = is_birthday(data_from_sheets)

    bot = SlackBirthdayHelper()

    # For each worker who has birthday today write message in special channel
    # in the slack.
    if not birthday_persons:
        bot.write_to_slack(channel=CHANNEL_NAME,
                           message=f'Именинников сегодня нет.')
        return "Ok!"

    for worker in birthday_persons:
        bot.write_to_slack(channel=CHANNEL_NAME,
                           message=f'У {worker} сегодня день рождения!'
                                   f' Не забудьте ее поздравить.')

    return str(birthday_persons)


sched = BackgroundScheduler()
sched.add_job(main, 'cron', hour=HOURS, minute=MINUTES)
sched.start()

if __name__ == '__main__':
    app.run(debug=False)
