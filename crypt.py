#!/usr/bin/python
# -*- coding: cp1252 -*-
import easygui
"""
__version__ = "$Revision: 1.3 $"
__date__ = "$Date: 2004/04/14 02:38:47 $"
"""

from PythonCard import model

class MyBackground(model.Background):

    def on_initialize(self, event):
        # if you have any initialization
        # including sizer setup, do it here
        pass
    def on_Verschlsseln_mouseClick(self, event):
        import ver
        ver.do(self.components.path.text ,self.components.dictionarypy.text)
    def on_Entschlsseln_mouseClick(self, event):
        if self.components.passwort.text == "4":
            self.components.Gauge1.value=100
        else:
            import ent
            ent.do(self.components.path.text ,self.components.dictionarypy.text)
    def on_neuesDict_mouseClick(self,event):
        import dict
        if easygui.buttonbox("Dies wird alle im moment Verschlüsselten dateinen unbrauchbar machen!\nSicher?","",("Ja","Nein"))=="Ja":
            dict.create()
    def on_browse_mouseClick(self, event):
        self.components.path.text=easygui.fileopenbox()
    

if __name__ == '__main__':
    app = model.Application(MyBackground)
    app.MainLoop()
