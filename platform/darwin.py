from AppKit import NSWorkspace

def get_active_window_title():
    return NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
