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

         #Ask AIs
        self.m_textWaAI.SetValue(str(hidari+migi+10))
        self.m_textSaAI.SetValue(str(hidari-migi+10))
        self.m_textSekiAI.SetValue(str(hidari * migi+10))       

        #Ask PC 
        self.m_textWaPC.SetValue(str(hidari+migi))
        self.m_textSaPC.SetValue(str(hidari-migi))
        self.m_textSekiPC.SetValue(str(hidari * migi))
    

    

app = wx.App( False )
frame = Mainframe( None )
frame.Show( True )
app.MainLoop()