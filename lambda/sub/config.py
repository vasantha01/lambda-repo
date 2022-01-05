from configparser import ConfigParser


def config(filename='database.ini',section='redshift'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section for redshift
    db = {}
    if parser.has_section(section):
        rsparams = parser.items(section)
        for param in rsparams:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db