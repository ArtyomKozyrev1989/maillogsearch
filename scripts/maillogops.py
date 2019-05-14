import re
import time
import os


def find_senders_stats(file_text: list) -> dict:
    """
        | file_text is a list of strings, which were read from maillog file
        | func(list) -> dictionary
        | the function returns dictionary:
        | dictionary key is sender's emailbox
        | dictionary value is number of mails which were sent from the emailbox
    """
    if type(file_text) != list:
        raise TypeError("The variable file_text should be list")
    mailbox_pattern = '(?<=from=<).*?(?=>)'
    unique_mailbox = {}  # key is senders mailbox, value is number of mails
    for line in file_text:
        if type(line) != str:
            raise TypeError("The variable file_text should be list of strings")
        result = re.search(mailbox_pattern, line)
        if result:
            if result.group() in unique_mailbox:
                unique_mailbox[result.group()] += 1
            else:
                unique_mailbox[result.group()] = 1
    return unique_mailbox


def find_sending_stats(file_text: list) -> dict:
    """
        | file_text is a list of strings, which were read from maillog1 file
        | func(list) -> dictionary
        | the function returns dictionary:
        | dictionary key is type of operation (send mail) result
        | dictionary value is number of operations
    """
    if type(file_text) != list:
        raise TypeError("The variable file_text should be list")
    operation_result = '(?<=status=).*?(?=\s)'
    op_res_type = {}
    for line in file_text:
        if type(line) != str:
            raise TypeError("The variable file_text should be list of strings")
        result = re.search(operation_result, line)
        if result:
            if result.group() in op_res_type:
                op_res_type[result.group()] += 1
            else:
                op_res_type[result.group()] = 1
    return op_res_type


if __name__ == '__main__':
    logfile = os.getcwd() + '\\' + 'maillog'
    # нет типа файла, так как Pycharm и Windows не знает тип файла, рассматриванется как текcтовый
    if not os.path.exists(logfile):
        print("The mailog file does not exist in the working directory")
        print("Please put the file into directory and try again")
        time.sleep(5)
    else:
        file_text = []
        with open(logfile, 'r') as f:
            for line in f:
                file_text.append(line)

        senders_stats = find_senders_stats(file_text)
        op_res_type = find_sending_stats(file_text)
        print("Письма были направлены от следующих ящиков: ")
        for box, attempts in senders_stats.items():
            print("{} : {} писем".format(box, attempts))
        print("Количество попыток направить письмо по результатам отправки: ")
        for result, attempts in op_res_type.items():
            print("Тип результата {} : {} попыток".format(result.strip(","), attempts))
        time.sleep(10)
