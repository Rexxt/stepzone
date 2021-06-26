# 21 key concept
def modeInit():
    lanes = 21
    special = 0
    keys = [config.keybinds[range(4,21)]]
    return [lanes, special, keys]

def configFile():
    for k in range(4,21):
        config.add("keybindings", k)
