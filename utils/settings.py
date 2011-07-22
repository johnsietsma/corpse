def read_host_settings():
    host = None
    settings = {}
    try:
        import socket
        hostname = '_'.join(socket.gethostname().split('.')[-2:])
        host = __import__("settings_%s" % hostname)
        
        for setting in dir(host):
            if setting == setting.upper():
                settings[setting] = getattr(host, setting)
    
    except ImportError, e:
        import sys
        sys.stderr.write('Unable to read settings_%s.py\n' % hostname)
        sys.exit(1)
        
    return settings
