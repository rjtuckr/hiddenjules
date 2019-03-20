from configparser import ConfigParser

def read_db_config(filename='DbConfig.ini', section='mysqlcharsheet'):
    """
    Read database configuration from file
    :param filename: name of the config file
    :param section: name of the section in the config file
    :return: a dictionary of parameters
    """

    parser = ConfigParser()
    parser.read(filename)

    db = {} # dictionary
    if parser.has_section(section):
        items = parser.items(section) # reads back as an array
        for item in items:
            db[item[0]] = item[1] # populates dictionary with values from array

    else:
        raise Exception('{0} section is not found in {1} file'.format(section, filename))

    return db