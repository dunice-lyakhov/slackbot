import os
import datetime

home_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + \
           '/slackbot'


def env_get_required(setting_name):
    """Get the value of an environment variable and assert that it is set."""

    setting = os.environ.get(setting_name)
    assert setting not in {None, ''}, (
        '{0} must be defined as an environment variable.'.format(setting_name)
    )
    return setting


def is_birthday(data):
    """
    Returns lines - employees who have a birthday today.

    :param data: list
    :return: list
    """
    today = datetime.datetime.now().date()

    # Delete first line because it's description of the columns.
    data.pop(0)

    # For every array in the data get date by index (4) not including year and
    # check: is today birthday or not?
    # Returns list with full names of birthday persons.
    return [f'{birthday[0]} {birthday[1]}' for birthday in data if
            datetime.datetime.strptime(birthday[4], '%d.%m.%Y').strftime(
                "%d/%m") == today.strftime("%d/%m")
            ]
