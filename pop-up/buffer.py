#
# copyright © 2022 Giuseppe Fanuli
#
# This file is part of pop-up.
#
# See README.txt for more information 
#

import win32event
import mmap
import os
import struct

class BufferRead(object):
    def __init__(self):
        """
        This class is able to read data form the Windows Debugger
        """
        self.buffer_ready = win32event.CreateEvent (None, 0, 0,"DBWIN_BUFFER_READY")
        self.data_ready = win32event.CreateEvent (None, 0, 0, "DBWIN_DATA_READY")
        self.buffer = mmap.mmap (0, 32, "DBWIN_BUFFER", mmap.ACCESS_WRITE)

    def readBuffer(self):
        """
        Return the string read form the Windows Debugger.\n
        In case of no data is retrieved, an empty string is returned.
        """
        out = os.popen("tasklist|findstr lghub_agent.exe").read() # Save the Logitech(c) Agent process id to filter informations
        win32event.SetEvent (self.buffer_ready)
        
        if win32event.WaitForSingleObject (self.data_ready, win32event.INFINITE) == win32event.WAIT_OBJECT_0:
            self.buffer.seek (0)
            
            # The first DWORD is the process id which generated the output
            process_id, = struct.unpack ("L", self.buffer.read (4))
            
            if f"{process_id}" in out:
                # consider only the information printed by the Logitech(c) Agent
                data = self.buffer.read (32).decode("utf-8")
                if "\0" in data:
                    self.buffer.flush()
                    return data[:data.index ("\0")]
                else:
                    return data 
        
        self.buffer.flush()
        return ""