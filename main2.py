# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, word = ','):
    first = first.split(word)
    second = second.split(word)
    common = set()
    for i in range(len(first)):
        for j in range(len(second)):
            if(first[i]==second[j]):
                common.add(first[i])
    return sorted(common)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group,'|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
