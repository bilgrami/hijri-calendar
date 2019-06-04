    c = get_config()

    # Notebook server config below
    # Kernel config
    c.IPKernelApp.pylab = 'inline'  # if you want plotting support always

    # Notebook config: ip address and port
    c.NotebookApp.ip = '0.0.0.0'
    c.NotebookApp.port = 8888

    # disables the browser
    c.NotebookApp.open_browser = False