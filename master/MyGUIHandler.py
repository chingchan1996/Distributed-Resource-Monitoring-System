from Monitor import GuiThread


class MyGUIHandler(object):
    """description of class"""
    def __init__( self, _ec, _msgCenter, _db, _lm ):
        self.__ec = _ec 
        self.__msgCenter = _msgCenter
        self.__db = _db 
        self.__localMachine = _lm
        self.__GUI = GuiThread( self.__ec, self.__msgCenter, self.__db, self.__localMachine )
        self.__GUI.start()
    # end

    def restart(self):
        if self.__GUI.is_alive():
            pass
        else: 
            self.__GUI = GuiThread( self.__ec, self.__msgCenter, self.__db, self.__localMachine )
            self.__GUI.start()
    # end of restart()

    def isAlive(self):
        return self.__GUI.is_alive()
    # end of isAlive()

