
from system_hotkey import SystemHotkey


class HotKey(SystemHotkey):
    '''
    description: HotKey class
    param {*} self
    param {*} name: hotkey name
    param {*} hotkey: hotkey tuple. e.g. ('control','alt','c')
    param {*} callback_fun: callback function
    return {*}
    '''    
    def __init__(self,name,hotkey,callback_fun):
        super(HotKey,self).__init__()
        self.name = name
        self.hotkey = hotkey
        self.callback_fun = callback_fun
        self.register(self.hotkey,callback=lambda x:self.callback_fun(self.name))
    
    def modify_hotkey(self,hotkey):
        self.unregister(self.hotkey)
        self.hotkey = hotkey
        self.register(self.hotkey,callback=lambda x:self.callback_fun(self.name))
    
    def hotkey_unregister(self):
        self.unregister(self.hotkey)
        
    def hotkey_register(self):
        self.register(self.hotkey,callback=lambda x:self.callback_fun(self.name))

class HotkeysMgr(object):
    def __init__(self,sigkeyhot):
        # Signal
        self.sigkeyhot = sigkeyhot
        # HotKey init
        self.hotkeylist = [HotKey("clipboard_img_process",('control','alt','c'),self.sendkeyevent),
                       HotKey("folder_img_process",('control','alt','f'),self.sendkeyevent),
                       HotKey("capture_hotkey",('alt','q'),self.sendkeyevent)]
        
        
    def set_hotkey(self,hotkey_name,hotkey):
        for hotkey_item in self.hotkeylist:
            if hotkey_item.name == hotkey_name:
                hotkey_item.modify_hotkey(hotkey)
                break
    
    def sendkeyevent(self,signal_str):
        self.sigkeyhot.emit(signal_str)
    
    def unregister_all(self):
        for hotkey_item in self.hotkeylist:
            hotkey_item.hotkey_unregister()

    def register_all(self):
        for hotkey_item in self.hotkeylist:
            hotkey_item.hotkey_register()
        
