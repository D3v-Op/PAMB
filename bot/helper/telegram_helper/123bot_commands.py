class _BotCommands:
    def __init__(self):
        self.StartCommand = 'start'
        self.MirrorCommand = 'load'
        self.UnzipMirrorCommand = 'unzload'
        self.TarMirrorCommand = 'tarload'
        self.CancelMirror = 'cancel'
        self.CancelAllCommand = 'cancelall'
        self.ListCommand = 'list'
        self.SpeedCommand = 'speedtest'
        self.StatusCommand = 'status'
        self.AuthorizeCommand = 'auth'
        self.UnAuthorizeCommand = 'dauth'
        self.PingCommand = 'ping'
        self.RestartCommand = 'reboot'
        self.StatsCommand = 'usage'
        self.HelpCommand = 'help'
        self.LogCommand = 'log'
        self.CloneCommand = 'clone'
        self.WatchCommand = 'watch'
        self.TarWatchCommand = 'tarwatch'
        self.deleteCommand = 'del'

BotCommands = _BotCommands()
