#to get event date
def get_event_date(event):
    return event.date


def current_users(events):
    #sort the event base on date
    events.sort(key=get_event_date)

    #dict to store machine name and users' name
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.user in machines[event.machine] and event.type == "logout":
            machines[event.machine].remove(event.user)
    return machines


#printing function
def generate_report(machines):
    for machine, users in machines.items():

        #ensure machine have users in list
        if len(users) > 0:

            #formating the output machine and users
            user_list = ", ".join(users)
            print("{}:{}".format(machine,user_list))


class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user



events = [
    Event('2020-01-21 12:45:56','logout','myworkstation.local','jordan'),
    # Event('2020-01-22 12:53:42','logout','webserver.local','jordan'),
    # Event('2020-01-21 18:53:21','login','webserver.local','lane'),
    # Event('2020-01-22 10:25:34','logout','myworkstation.local','jordan'),
    # Event('2020-01-21 08:20:01','login','webserver.local','jordan'),
    # Event('2020-01-23 11:24:35','logout','mailserver.local','chris')
]


users = current_users(events)
print("THIS IS USER : \n {}\n".format(users))

#generate report
generate_report(users)