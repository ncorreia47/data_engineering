def colors_ansi(color_name):

    colors = {
        'black': '\033[30m', 
        'red': '\033[31m', 
        'green': '\033[32m', 
        'yellow': '\033[33m',
        'blue': '\033[34m', 
        'magenta': '\033[35m', 
        'cyan': '\033[36m', 
        'white': '\033[37m',
        'gray': '\033[90m', 
        'light_red': '\033[91m', 
        'light_green': '\033[92m',
        'light_yellow': '\033[93m', 
        'light_blue': '\033[94m', 
        'light_magenta': '\033[95m',
        'light_cyan': '\033[96m', 
        'light_white': '\033[97m'
    }

    return colors[color_name] if color_name in colors else colors['light_white'] 
    