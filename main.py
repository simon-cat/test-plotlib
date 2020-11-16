import configfunc
from jira import JIRA

import matplotlib as mpl
import matplotlib.pyplot as plt

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

    created_arr = []
    resolved_arr = []

    for i in range(7):
        jqlCreated = f'created >= -{i + 1}d AND created <= -{i}d'
        jqlResolved = f'resolutiondate >= -{i + 1}d AND resolutiondate <= -{i}d'
        created = jira.search_issues(jqlCreated, 0, False).total
        resolved = jira.search_issues(jqlResolved, 0, False).total
        created_arr.append(created)
        resolved_arr.append(resolved)
        # message = f'{i} день назад\n\U0000274C запросов создано: {created}\n\U00002705 запросов решено: {resolved}'
        # print(message)

    print(created_arr)
    print(resolved_arr)

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.axis([0, 7, 0, 100])

    plt.title('Sine & Cosine')
    plt.xlabel('x')
    plt.ylabel('F(x)')

    xs = [0, 1, 2, 3, 4, 5, 6]

    plt.plot(xs, created_arr, color='blue', linestyle='solid',
             label='sin(x)')
    plt.plot(xs, resolved_arr, color='red', linestyle='dashed',
             label='cos(x)')

    plt.legend(loc='upper right')
    fig.savefig('trigan.png')
    print('сохранил1')

    # data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'waste_disposal',
    #               'atm', 'bench', 'parking', 'restaurant',
    #               'place_of_worship']
    # data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
    #                5092, 3629]

    # fig2 = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    #
    # plt.title('OpenStreetMap Point Types')
    #
    # ax = plt.axes()
    # ax.yaxis.grid(True, zorder=1)
    #
    # # xs = range(len(data_names))
    #
    # plt.bar(xs, created_arr,
    #         width=0.2, color='red', alpha=0.7, label='created',
    #         zorder=2)
    # plt.bar(xs, resolved_arr,
    #         width=0.2, color='blue', alpha=0.7, label='resolved',
    #         zorder=2)
    # # plt.xticks(xs, data_names)
    #
    # fig2.autofmt_xdate(rotation=25)
    #
    # plt.legend(loc='upper right')
    # fig2.savefig('bars.png')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
