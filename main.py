import configfunc
from jira import JIRA

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    config = configfunc.get_config('config.ini')
    jira_server = configfunc.get_parameter(config, 'jira', 'jira_server')
    jira_login = configfunc.get_parameter(config, 'jira', 'jira_login')
    jira_password = configfunc.get_parameter(config, 'jira', 'jira_password')
    jira_options = {'server': jira_server}
    jira = JIRA(options=jira_options, basic_auth=(jira_login, jira_password))

    # https://eax.me/python-matplotlib/

    for i in range(7):
        jqlCreated = f'created >= -{i + 1}d AND created <= -{i}d'
        jqlResolved = f'resolutiondate >= -{i + 1}d AND resolutiondate <= -{i}d'
        created = jira.search_issues(jqlCreated, 0, False).total
        resolved = jira.search_issues(jqlResolved, 0, False).total
        message = f'{i} день назад\n\U0000274C запросов создано: {created}\n\U00002705 запросов решено: {resolved}'
        print(message)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
