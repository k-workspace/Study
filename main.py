#! env python
# -*- coding: utf-8 -*-


import wx
import AI_calc_GUI

class Mainframe( AI_calc_GUI.MyFrame1 ):
    def __init__( self, parent ):
        AI_calc_GUI.MyFrame1.__init__( self, parent )

    def CalcButtonPush( self, event ):
        hidari = int(self.m_textHidari.GetValue())
        migi   = int(self.m_textMigi.GetValue())

         #Ask AI
        wa , sa , seki = ask_AI(hidari,migi)
        self.m_textWaAI.SetValue(str(wa))
        self.m_textSaAI.SetValue(str(sa))
        self.m_textSekiAI.SetValue(str(seki))       

        #Ask PC 
        wa , sa , seki = ask_PC(hidari,migi)
        self.m_textWaPC.SetValue(str(wa))
        self.m_textSaPC.SetValue(str(sa))
        self.m_textSekiPC.SetValue(str(seki))
    
def ask_PC( hidari , migi ):
        return (hidari+migi) , (hidari - migi) , (hidari*migi)

def ask_AI( hidari , migi ):
        return (hidari+migi+110) , (hidari - migi+110) , (hidari*migi+110)
    

app = wx.App( False )
frame = Mainframe( None )
frame.Show( True )
app.MainLoop()