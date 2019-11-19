import re
import logging


logging.basicConfig(level=logging.INFO)


def read_and_parse_data(data):
    logging.info('{} data is going to read and parse'.format(data))
    final_data = []
    try:
        for line in data:
            lines = line.rstrip('\n')
            line_group = []
            if re.match("(.*)config(.*)", lines):
                temp = lines.split('INFO:')
                temp_date = temp[0].lstrip(' ')
                temp_config = temp[1].lstrip(' ')
                config_data = list(temp_config.split(" "))
                temp_config = list(temp_config)
                for config in config_data:
                    config.strip(' ')
                    config_split = config.split(":")[1]
                    line_group.append(config_split)

                line_group.append(temp[0])
                final_data.append(line_group)
                logging.info('data parsed and converted to list : {}'.format(final_data))
    except Exception as e:
        logging.error('Error occured during file parse: {}'.format(e))

    return final_data

# pattern = r'.(.*AM) [a-zA-Z]+: cofigID:([0-9]+) configName:"([a-zA-Z]+)" configStatus:([a-zA-Z]+)'
# pat = re.compile(pattern)
# with open('a.log') as f:
#     for line in f.readline():
#         match = pat.match(line)
#         if match:
#             print("matching object is found")
#             print("Date is : {}".format(match.group(1)))
