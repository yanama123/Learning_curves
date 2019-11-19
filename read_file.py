import re
import logging


logging.basicConfig(level=logging.INFO)


def read_and_parse_data(data):
    logging.info('The data is going to read and parse here: ')
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
        logging.info('The data parsed and converted to list : {}'.format(final_data))
    except Exception as e:
        logging.error('Error occurred during file parse: {}'.format(e))

    return final_data
