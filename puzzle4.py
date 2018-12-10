from datetime import datetime, timedelta
from collections import defaultdict, Counter

def organize_ledger(lines):
    ledger = []
    for line in lines:
        date = datetime(int(line[1:5]), int(line[6:8]), int(line[9:11]),
                        int(line[12:14]), int(line[15:17]))
        guard = line.split()[3]
        ledger.append([date, guard])
    return sorted(ledger)

def sleep_time(ledger):
    sleep_counter = defaultdict(timedelta)
    sleep_dict = defaultdict(list)
    for entry in ledger:
        if (entry[1] != "up") and (entry[1] != "asleep"):
            guard_id = entry[1]
        elif entry[1] == "asleep":
            start_time = entry[0]
        elif entry[1] == "up":
            end_time = entry[0]
            sleep_counter[guard_id] += end_time - start_time
            sleep_dict[guard_id].append([start_time, end_time])
    return sleep_dict, sleep_counter

def most_likely_asleep(sleep_dict, guard_id=None):
    minutes_asleep = {}
    for g_id in sleep_dict.keys():
        minutes = []
        for entry in sleep_dict[g_id]:
            minutes.append([i for i in range(entry[0].minute,
                                             entry[1].minute)])
        minutes_asleep[g_id] = minutes

    if guard_id:
        cnt = Counter(i for entry in minutes_asleep[guard_id] for i in entry)
        return cnt.most_common(1)
    else:
        guard_list = {}
        for key in minutes_asleep.keys():
            cnt = Counter(i for entry in minutes_asleep[key] for i in entry)
            guard_list[key] = cnt.most_common(1)
        return guard_list

def main():
    with open("puzzle4.txt", 'r', newline='\n') as f:
        lines = f.readlines()

    ledger = organize_ledger(lines)
    sleep_dict, sleep_counter = sleep_time(ledger)
    guard = max(sleep_counter.items(), key=lambda a: a[1])
    minute = most_likely_asleep(sleep_dict, guard[0])
    print("The guard with most minutes sleep is {}. He is most usually asleep "
          "on minute {}.".format(guard[0], minute[0][0]))
    print("The first checksum is {}.".format(int(guard[0][1:]) * minute[0][0]))
    guard_list = most_likely_asleep(sleep_dict)
    minute = max(guard_list.items(), key=lambda v: v[1][0][1])
    print("The guard which is most frequently asleep on the same minute is "
          "guard {}, on minute {}.".format(minute[0], minute[1][0][1]))
    print("The second checksum is {}.".format(int(minute[0][1:]) *
                                              minute[1][0][0]))

if __name__ == "__main__":
    main()
