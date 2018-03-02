# File: bear.py
# Author: Simon Chu
# Date: 3/5/2017
# Purpose: to print the bear with texts under the bear

from graphics import *

def main():

    # generate the window
    winWidth = 500
    winHeight = 500

    win = GraphWin("Bear", winWidth, winHeight)
    win.setBackground("white")

    # create upperpart
    upperPart = Polygon(Point(192,238), 
    Point(191,211), 
    Point(192,206), 
    Point(192,204), 
    Point(192,202), 
    Point(191,200), 
    Point(184,198), 
    Point(179,196), 
    Point(176,194), 
    Point(172,192), 
    Point(169,188), 
    Point(168,185), 
    Point(168,177), 
    Point(168,172), 
    Point(169,170), 
    Point(170,167), 
    Point(174,163), 
    Point(178,158), 
    Point(182,155), 
    Point(186,152), 
    Point(187,152), 
    Point(189,152), 
    Point(193,152), 
    Point(197,153), 
    Point(200,155), 
    Point(203,156), 
    Point(206,159), 
    Point(210,162), 
    Point(215,158), 
    Point(219,156), 
    Point(219,156), 
    Point(219,153), 
    Point(224,152), 
    Point(228,151), 
    Point(232,151), 
    Point(236,151), 
    Point(238,150), 
    Point(240,149), 
    Point(241,149), 
    Point(243,151), 
    Point(247,149), 
    Point(250,149), 
    Point(250,150), 
    Point(254,149), 
    Point(258,149), 
    Point(264,148), 
    Point(273,148), 
    Point(276,151), 
    Point(285,151), 
    Point(292,153), 
    Point(294,156), 
    Point(299,162), 
    Point(300,163), 
    Point(305,159), 
    Point(309,158), 
    Point(320,155), 
    Point(327,155), 
    Point(336,155), 
    Point(341,160), 
    Point(345,166), 
    Point(348,171), 
    Point(348,176), 
    Point(348,181), 
    Point(345,186), 
    Point(342,191), 
    Point(338,195), 
    Point(332,197), 
    Point(326,199), 
    Point(324,200), 
    Point(326,205), 
    Point(325,208), 
    Point(325,210), 
    Point(322,214), 
    Point(322,214), 
    Point(311,249))
    upperPart.setFill("#CF8114")
    upperPart.draw(win)
    
    # create eyes, the white parts in the eyes and the ears
    eye1 = Circle(Point(222,179), 8)
    eye1.setFill("#09000D")
    eye1.draw(win)
    
    eye2 = Circle(Point(288,177), 8)
    eye2.setFill("#09000D")
    eye2.draw(win)
    
    eye1White = Circle(Point(224,177), 3)
    eye1White.setFill("#FFFFFC")
    eye1White.draw(win)
    
    eye2White = Circle(Point(291,175), 3)
    eye2White.setFill("#FFFFFC")
    eye2White.draw(win)

    # create mouth and nose
    mouth = Polygon(Point(219,251), 
    Point(222,211), 
    Point(222,209), 
    Point(223,206), 
    Point(224,202), 
    Point(226,199), 
    Point(227,197), 
    Point(228,196), 
    Point(231,192), 
    Point(234,192), 
    Point(235,191), 
    Point(238,190), 
    Point(242,187), 
    Point(247,186), 
    Point(254,186), 
    Point(259,186), 
    Point(263,186), 
    Point(271,187), 
    Point(277,189), 
    Point(281,191), 
    Point(285,193), 
    Point(287,195), 
    Point(289,197), 
    Point(290,199), 
    Point(293,202), 
    Point(293,203), 
    Point(293,207), 
    Point(294,210), 
    Point(293,235))
    mouth.setFill("#FECB7D")
    mouth.draw(win)

    mouthLeft = Polygon(Point(226,223), 
    Point(230,214), 
    Point(229,211), 
    Point(230,208), 
    Point(232,205), 
    Point(229,204), 
    Point(232,203), 
    Point(234,203), 
    Point(236,203), 
    Point(237,203), 
    Point(237,204), 
    Point(234,205), 
    Point(234,206), 
    Point(234,208), 
    Point(233,210), 
    Point(232,218))
    mouthLeft.setFill("#000009")
    mouthLeft.draw(win)

    mouthMid = Polygon(Point(256,217), 
    Point(258,218), 
    Point(258,220), 
    Point(258,222), 
    Point(258,225), 
    Point(258,230), 
    Point(258,233), 
    Point(254,233), 
    Point(254,227), 
    Point(254,225), 
    Point(255,220), 
    Point(257,218))
    mouthMid.setFill("#000009")
    mouthMid.draw(win)

    mouthRight = Polygon(Point(283,207), 
    Point(282,206), 
    Point(277,206), 
    Point(278,204), 
    Point(280,204), 
    Point(283,204), 
    Point(285,204), 
    Point(288,204), 
    Point(290,204), 
    Point(289,204), 
    Point(287,206), 
    Point(287,207), 
    Point(287,210), 
    Point(287,212), 
    Point(287,213), 
    Point(287,220), 
    Point(283,219), 
    Point(283,213), 
    Point(284,211), 
    Point(283,208), 
    Point(282,206))
    mouthRight.setFill("#000009")
    mouthRight.draw(win)
    
    nose = Oval(Point(247,200), Point(267,185))
    nose.setFill("#673807")
    nose.draw(win)

    ear1shadow = Polygon(Point(181,173), 
    Point(184,176), 
    Point(188,184), 
    Point(189,188), 
    Point(191,192), 
    Point(197,188), 
    Point(199,183), 
    Point(200,178), 
    Point(201,175), 
    Point(201,170), 
    Point(198,167), 
    Point(193,165), 
    Point(190,164), 
    Point(187,164), 
    Point(185,164), 
    Point(182,167), 
    Point(181,169), 
    Point(180,172))
    ear1shadow.setFill("#AF6A05")
    ear1shadow.setOutline("#AF6A05")
    ear1shadow.draw(win)

    ear2shadow = Polygon(Point(336,168), 
    Point(338,165), 
    Point(336,165), 
    Point(334,165), 
    Point(329,164), 
    Point(325,165), 
    Point(321,167), 
    Point(319,171), 
    Point(318,175), 
    Point(317,182), 
    Point(318,185), 
    Point(319,189), 
    Point(321,191), 
    Point(324,194), 
    Point(325,193), 
    Point(327,190), 
    Point(329,188), 
    Point(332,186), 
    Point(334,182), 
    Point(335,181), 
    Point(336,177), 
    Point(336,173), 
    Point(336,172), 
    Point(336,169))
    ear2shadow.setFill("#AF6A05")
    ear2shadow.setOutline("#AF6A05")
    ear2shadow.draw(win)

    ear1 = Polygon(Point(185,164), 
    Point(188,164), 
    Point(191,164), 
    Point(193,164), 
    Point(196,166), 
    Point(198,168), 
    Point(199,170), 
    Point(201,174), 
    Point(201,177), 
    Point(201,181), 
    Point(199,184), 
    Point(197,187), 
    Point(196,188), 
    Point(194,190), 
    Point(194,191), 
    Point(196,189), 
    Point(198,187), 
    Point(199,185), 
    Point(201,183), 
    Point(202,182), 
    Point(202,179), 
    Point(203,179), 
    Point(203,177), 
    Point(205,175), 
    Point(203,175), 
    Point(203,172), 
    Point(203,171), 
    Point(201,170), 
    Point(200,168), 
    Point(199,166), 
    Point(197,164), 
    Point(192,163), 
    Point(190,163), 
    Point(187,163), 
    Point(185,164))
    ear1.setFill("#090000")
    ear1.draw(win)
    
    ear2 = Polygon(Point(328,163), 
    Point(327,163), 
    Point(325,163), 
    Point(322,164), 
    Point(321,166), 
    Point(320,168), 
    Point(317,172), 
    Point(317,176), 
    Point(317,180), 
    Point(317,186), 
    Point(319,190), 
    Point(319,191), 
    Point(319,188), 
    Point(317,186), 
    Point(317,182), 
    Point(317,178), 
    Point(318,175), 
    Point(319,172), 
    Point(321,170), 
    Point(323,168), 
    Point(328,166), 
    Point(330,164), 
    Point(327,164))
    ear2.setFill("#090000")
    ear2.draw(win)

    # create two feet of the bear
    footLeft = Polygon(Point(218,292), 
    Point(205,294), 
    Point(195,302), 
    Point(191,304), 
    Point(189,305), 
    Point(187,306), 
    Point(193,315), 
    Point(187,307), 
    Point(184,303), 
    Point(180,301), 
    Point(174,299), 
    Point(170,299), 
    Point(163,299), 
    Point(161,300), 
    Point(157,304), 
    Point(156,306), 
    Point(154,308), 
    Point(153,311), 
    Point(151,315), 
    Point(151,318), 
    Point(151,321), 
    Point(151,326), 
    Point(151,329), 
    Point(152,332), 
    Point(153,337), 
    Point(153,340), 
    Point(155,343), 
    Point(156,345), 
    Point(160,349), 
    Point(164,351), 
    Point(170,353), 
    Point(175,353), 
    Point(179,353), 
    Point(182,353), 
    Point(191,352), 
    Point(196,351), 
    Point(201,350), 
    Point(207,349), 
    Point(215,348), 
    Point(221,347), 
    Point(238,342), 
    Point(248,341), 
    Point(262,338))
    footLeft.setFill("#DD940A")
    footLeft.draw(win)

    footRight = Polygon(Point(308,301), 
    Point(311,302), 
    Point(314,304), 
    Point(315,307), 
    Point(311,314), 
    Point(309,317), 
    Point(314,311), 
    Point(316,307), 
    Point(321,303), 
    Point(323,301), 
    Point(328,299), 
    Point(331,298), 
    Point(335,298), 
    Point(338,298), 
    Point(340,299), 
    Point(347,303), 
    Point(350,305), 
    Point(351,311), 
    Point(352,319), 
    Point(352,323), 
    Point(351,327), 
    Point(350,332), 
    Point(348,333), 
    Point(347,336), 
    Point(346,338), 
    Point(344,341), 
    Point(342,342), 
    Point(339,344), 
    Point(335,347), 
    Point(333,349), 
    Point(330,351), 
    Point(327,352), 
    Point(325,353), 
    Point(322,353), 
    Point(321,353), 
    Point(320,353), 
    Point(319,353), 
    Point(317,353), 
    Point(315,351), 
    Point(311,350), 
    Point(300,348), 
    Point(294,347), 
    Point(288,344), 
    Point(285,344), 
    Point(280,343), 
    Point(278,342), 
    Point(276,342), 
    Point(273,342), 
    Point(267,341), 
    Point(266,340))
    footRight.setFill("#DD940A")
    footRight.draw(win)

    # create the shadow on the feet
    footLeftShadow = Polygon(Point(152,312), 
    Point(155,310), 
    Point(158,309), 
    Point(163,308), 
    Point(167,309), 
    Point(170,312), 
    Point(172,317), 
    Point(172,320), 
    Point(173,325), 
    Point(173,329), 
    Point(173,333), 
    Point(174,337), 
    Point(175,339), 
    Point(177,342), 
    Point(180,343), 
    Point(191,346), 
    Point(196,346), 
    Point(202,346), 
    Point(210,346), 
    Point(223,344), 
    Point(229,343), 
    Point(218,346), 
    Point(187,351), 
    Point(176,354), 
    Point(168,353), 
    Point(165,353), 
    Point(160,350), 
    Point(156,345), 
    Point(153,343), 
    Point(151,338), 
    Point(151,334), 
    Point(150,331), 
    Point(150,326), 
    Point(151,323), 
    Point(151,319), 
    Point(151,314), 
    Point(153,311), 
    Point(155,309))
    footLeftShadow.setFill("#B1700B")
    footLeftShadow.setOutline("#B1700B")
    footLeftShadow.draw(win)

    footRightShadow = Polygon(Point(271,341), 
    Point(277,341), 
    Point(281,341), 
    Point(284,340), 
    Point(288,340), 
    Point(293,341), 
    Point(303,342), 
    Point(307,342), 
    Point(312,342), 
    Point(320,343), 
    Point(321,336), 
    Point(321,331), 
    Point(325,325), 
    Point(327,321), 
    Point(331,317), 
    Point(335,313), 
    Point(339,312), 
    Point(343,312), 
    Point(345,312), 
    Point(347,314), 
    Point(348,317), 
    Point(348,321), 
    Point(349,324), 
    Point(349,327), 
    Point(348,329), 
    Point(347,330), 
    Point(347,332), 
    Point(345,335), 
    Point(343,338), 
    Point(341,341), 
    Point(340,342), 
    Point(338,343), 
    Point(337,345), 
    Point(329,348), 
    Point(324,351), 
    Point(320,351), 
    Point(317,351))
    footRightShadow.setFill("#B1700B")
    footRightShadow.setOutline("#B1700B")
    footRightShadow.draw(win)

    # create the lines and arcs on the feet
    line1 = Line(Point(157,320), Point(165,321))
    line1.draw(win)

    line2 = Line(Point(157,326), Point(162,326))
    line2.draw(win)

    line3 = Line(Point(159,331), Point(164,331))
    line3.draw(win)

    line4 = Line(Point(159,336), Point(165,336))
    line4.draw(win)

    line5 = Line(Point(163,342), Point(168,341))
    line5.draw(win)

    line6 = Line(Point(336,321), Point(344,321))
    line6.draw(win)

    line7 = Line(Point(334,326), Point(342,326))
    line7.draw(win)

    line8 = Line(Point(334,332), Point(339,332))
    line8.draw(win)

    line9 = Line(Point(329,337), Point(336,337))
    line9.draw(win)

    line10 = Line(Point(327,341), Point(333,342))
    line10.draw(win)

    arc1 = Polygon(Point(159,317), 
    Point(160,316), 
    Point(160,320), 
    Point(163,336), 
    Point(164,340), 
    Point(166,345), 
    Point(168,345), 
    Point(168,345), 
    Point(167,344), 
    Point(166,342), 
    Point(166,339), 
    Point(164,337), 
    Point(163,332), 
    Point(162,327), 
    Point(162,324), 
    Point(161,320), 
    Point(161,319), 
    Point(160,317))
    arc1.setFill("#351A01")
    arc1.draw(win)

    arc2 = Polygon(Point(340,318), 
    Point(337,327), 
    Point(332,336), 
    Point(330,339), 
    Point(327,343), 
    Point(327,345), 
    Point(331,341), 
    Point(332,337), 
    Point(335,335), 
    Point(337,332), 
    Point(340,324), 
    Point(341,321), 
    Point(342,318))
    arc2.setFill("#351A01")
    arc2.draw(win)

    # create heart
    heart = Polygon(Point(257,351), 
    Point(248,346), 
    Point(243,342), 
    Point(240,338), 
    Point(229,332), 
    Point(216,322), 
    Point(212,317), 
    Point(207,313), 
    Point(202,308), 
    Point(195,301), 
    Point(190,297), 
    Point(185,290), 
    Point(180,283), 
    Point(180,280), 
    Point(171,243), 
    Point(171,239), 
    Point(171,238), 
    Point(171,235), 
    Point(172,233), 
    Point(172,231), 
    Point(174,229), 
    Point(177,225), 
    Point(178,223), 
    Point(179,222), 
    Point(182,219), 
    Point(185,218), 
    Point(186,216), 
    Point(188,214), 
    Point(190,214), 
    Point(193,214), 
    Point(196,212), 
    Point(199,212), 
    Point(204,211), 
    Point(208,211), 
    Point(213,210), 
    Point(218,210), 
    Point(223,210), 
    Point(228,212), 
    Point(235,215), 
    Point(242,218), 
    Point(246,220), 
    Point(253,226), 
    Point(255,228), 
    Point(256,229), 
    Point(261,225), 
    Point(264,224), 
    Point(268,222), 
    Point(273,220), 
    Point(279,217), 
    Point(284,215), 
    Point(292,213), 
    Point(299,212), 
    Point(303,212), 
    Point(309,212), 
    Point(313,213), 
    Point(317,214), 
    Point(322,217), 
    Point(324,219), 
    Point(326,220), 
    Point(328,224), 
    Point(332,228), 
    Point(332,231), 
    Point(332,236), 
    Point(333,241), 
    Point(331,243), 
    Point(321,282), 
    Point(317,290), 
    Point(315,293), 
    Point(312,297), 
    Point(310,301), 
    Point(307,303), 
    Point(304,305), 
    Point(300,310), 
    Point(299,312), 
    Point(296,315), 
    Point(291,320), 
    Point(288,323), 
    Point(284,327), 
    Point(281,330), 
    Point(278,332), 
    Point(274,335), 
    Point(271,339), 
    Point(266,343), 
    Point(264,345), 
    Point(258,350), 
    Point(258,351))
    heart.setFill("#F6000E")
    heart.draw(win)

    # create the 3D effect on the heart
    effect1 = Polygon(Point(179,236), 
    Point(183,233), 
    Point(186,230), 
    Point(189,228), 
    Point(192,227), 
    Point(199,225), 
    Point(203,225), 
    Point(208,225), 
    Point(214,223), 
    Point(219,222), 
    Point(220,221), 
    Point(220,218), 
    Point(213,218), 
    Point(210,218), 
    Point(208,218), 
    Point(207,218), 
    Point(203,218), 
    Point(200,218), 
    Point(197,220), 
    Point(194,220), 
    Point(191,221), 
    Point(191,221), 
    Point(190,222), 
    Point(188,224), 
    Point(187,225), 
    Point(186,226), 
    Point(184,228), 
    Point(183,229), 
    Point(182,231), 
    Point(178,235))
    effect1.setFill("#E7FFFF")
    effect1.setOutline("#E7FFFF")
    effect1.draw(win)

    effect2 = Polygon(Point(267,233), 
    Point(274,230), 
    Point(280,228), 
    Point(286,226), 
    Point(292,226), 
    Point(296,226), 
    Point(302,225), 
    Point(305,225), 
    Point(309,225), 
    Point(311,225), 
    Point(312,224), 
    Point(313,223), 
    Point(313,221), 
    Point(308,220), 
    Point(306,219), 
    Point(300,219), 
    Point(296,219), 
    Point(291,220), 
    Point(283,220), 
    Point(281,221), 
    Point(280,223), 
    Point(275,225), 
    Point(273,227), 
    Point(270,229))
    effect2.setFill("#E7FFFF")
    effect2.setOutline("#E7FFFF")
    effect2.draw(win)

    # create texts on the heart
    B = Polygon(Point(213,255), 
    Point(212,253), 
    Point(211,247), 
    Point(213,244), 
    Point(216,241), 
    Point(220,239), 
    Point(224,238), 
    Point(227,238), 
    Point(228,240), 
    Point(229,241), 
    Point(224,243), 
    Point(222,246), 
    Point(222,249), 
    Point(219,252), 
    Point(218,256), 
    Point(211,261), 
    Point(209,261), 
    Point(208,259), 
    Point(206,261), 
    Point(207,262), 
    Point(212,263), 
    Point(215,263), 
    Point(217,262), 
    Point(218,260), 
    Point(219,256), 
    Point(221,254), 
    Point(223,250), 
    Point(224,247), 
    Point(225,245), 
    Point(228,243), 
    Point(229,242), 
    Point(229,242), 
    Point(230,242), 
    Point(230,245), 
    Point(229,246), 
    Point(227,248), 
    Point(224,251), 
    Point(225,251), 
    Point(228,253), 
    Point(228,255), 
    Point(227,257), 
    Point(226,259), 
    Point(225,260), 
    Point(223,261), 
    Point(223,261), 
    Point(223,259), 
    Point(220,258), 
    Point(220,262), 
    Point(223,262), 
    Point(226,262), 
    Point(229,262), 
    Point(231,259), 
    Point(231,256), 
    Point(231,254), 
    Point(230,253), 
    Point(230,251), 
    Point(228,251), 
    Point(228,251), 
    Point(230,249), 
    Point(232,246), 
    Point(232,243), 
    Point(231,241), 
    Point(229,238), 
    Point(233,237), 
    Point(231,237), 
    Point(229,238), 
    Point(226,237), 
    Point(221,237), 
    Point(217,237), 
    Point(213,240), 
    Point(211,242), 
    Point(209,245), 
    Point(208,249), 
    Point(208,251), 
    Point(209,254), 
    Point(212,255), 
    Point(216,255))
    B.setFill("#E7FFFF")
    B.setOutline("#E7FFFF")
    B.draw(win)

    e = Polygon(Point(236,257), 
    Point(239,257), 
    Point(243,254), 
    Point(243,251), 
    Point(241,249), 
    Point(237,251), 
    Point(235,255), 
    Point(233,260), 
    Point(236,262), 
    Point(239,263), 
    Point(242,262), 
    Point(245,259), 
    Point(248,256), 
    Point(248,255), 
    Point(246,255), 
    Point(244,259), 
    Point(242,260), 
    Point(238,261), 
    Point(237,260), 
    Point(237,258), 
    Point(237,256), 
    Point(237,256), 
    Point(240,254), 
    Point(241,252), 
    Point(241,251), 
    Point(240,251), 
    Point(238,253), 
    Point(237,255), 
    Point(236,256))
    e.setFill("#E7FFFF")
    e.setOutline("#E7FFFF")
    e.draw(win)

    my = Polygon(Point(250,257), 
    Point(251,257), 
    Point(250,260), 
    Point(252,261), 
    Point(260,258), 
    Point(277,236), 
    Point(271,247), 
    Point(273,250), 
    Point(275,248), 
    Point(277,243), 
    Point(281,240), 
    Point(284,238), 
    Point(289,237), 
    Point(290,237), 
    Point(285,239), 
    Point(284,242), 
    Point(283,244), 
    Point(281,247), 
    Point(280,249), 
    Point(279,252), 
    Point(278,254), 
    Point(276,257), 
    Point(275,260), 
    Point(273,262), 
    Point(275,261), 
    Point(277,260), 
    Point(279,259), 
    Point(281,257), 
    Point(282,255), 
    Point(284,251), 
    Point(285,249), 
    Point(286,250), 
    Point(285,253), 
    Point(284,255), 
    Point(283,258), 
    Point(282,260), 
    Point(283,260), 
    Point(283,262), 
    Point(286,262), 
    Point(286,260), 
    Point(289,256), 
    Point(289,254), 
    Point(291,251), 
    Point(293,250), 
    Point(293,252), 
    Point(293,253), 
    Point(291,254), 
    Point(291,257), 
    Point(289,260), 
    Point(296,257), 
    Point(291,262), 
    Point(289,264), 
    Point(285,268), 
    Point(283,269), 
    Point(282,269), 
    Point(282,269), 
    Point(278,274), 
    Point(272,274), 
    Point(271,272), 
    Point(270,268), 
    Point(274,266), 
    Point(273,267), 
    Point(272,268), 
    Point(272,270), 
    Point(274,271), 
    Point(275,272), 
    Point(278,271), 
    Point(281,271), 
    Point(283,268), 
    Point(285,265), 
    Point(285,263), 
    Point(288,260), 
    Point(285,263), 
    Point(280,263), 
    Point(281,260), 
    Point(277,261), 
    Point(274,263), 
    Point(270,264), 
    Point(269,263), 
    Point(272,261), 
    Point(274,259), 
    Point(274,256), 
    Point(276,252), 
    Point(277,250), 
    Point(278,248), 
    Point(280,245), 
    Point(281,243), 
    Point(276,249), 
    Point(274,252), 
    Point(273,254), 
    Point(272,256), 
    Point(269,259), 
    Point(268,261), 
    Point(266,262), 
    Point(264,263), 
    Point(263,261), 
    Point(264,258), 
    Point(266,255), 
    Point(268,251), 
    Point(269,247), 
    Point(271,244), 
    Point(264,252), 
    Point(263,254), 
    Point(261,256), 
    Point(258,259), 
    Point(255,261), 
    Point(251,262), 
    Point(248,261), 
    Point(248,259), 
    Point(250,257))
    my.setFill("#E7FFFF")
    my.setOutline("#E7FFFF")
    my.draw(win)

    V = Polygon(Point(205,282), 
    Point(198,284), 
    Point(198,281), 
    Point(199,277), 
    Point(202,276), 
    Point(206,274), 
    Point(210,273), 
    Point(212,272), 
    Point(213,272), 
    Point(210,276), 
    Point(209,278), 
    Point(208,281), 
    Point(207,284), 
    Point(207,287), 
    Point(207,289), 
    Point(206,291), 
    Point(206,293), 
    Point(205,294), 
    Point(208,293), 
    Point(210,291), 
    Point(212,289), 
    Point(214,288), 
    Point(215,286), 
    Point(217,283), 
    Point(217,282), 
    Point(220,280), 
    Point(220,277), 
    Point(220,275), 
    Point(219,273), 
    Point(220,272), 
    Point(222,272), 
    Point(222,272), 
    Point(222,274), 
    Point(222,275), 
    Point(222,276), 
    Point(221,277), 
    Point(220,278), 
    Point(220,278), 
    Point(220,280), 
    Point(219,282), 
    Point(218,283), 
    Point(216,287), 
    Point(214,288), 
    Point(214,289), 
    Point(213,291), 
    Point(212,292), 
    Point(210,293), 
    Point(208,295), 
    Point(207,296), 
    Point(207,297), 
    Point(206,297), 
    Point(204,300), 
    Point(204,300), 
    Point(202,297), 
    Point(204,295), 
    Point(204,292), 
    Point(204,291), 
    Point(205,288), 
    Point(205,286), 
    Point(206,283), 
    Point(207,280), 
    Point(208,278), 
    Point(209,276), 
    Point(209,275), 
    Point(205,276), 
    Point(203,277), 
    Point(202,279), 
    Point(201,281), 
    Point(204,283), 
    Point(205,282), 
    Point(205,282), 
    Point(203,284), 
    Point(201,285))
    V.setFill("#E7FFFF")
    V.setOutline("#E7FFFF")
    V.draw(win)
    
    a = Polygon(Point(230,284), 
    Point(227,283), 
    Point(222,285), 
    Point(220,285), 
    Point(217,288), 
    Point(216,292), 
    Point(216,294), 
    Point(217,296), 
    Point(221,297), 
    Point(222,297), 
    Point(223,295), 
    Point(219,295), 
    Point(220,290), 
    Point(222,287), 
    Point(223,285), 
    Point(224,285), 
    Point(226,286), 
    Point(225,288), 
    Point(224,291), 
    Point(223,292), 
    Point(222,295), 
    Point(223,296), 
    Point(225,297), 
    Point(226,297), 
    Point(228,296), 
    Point(231,294), 
    Point(227,295), 
    Point(226,295), 
    Point(226,293), 
    Point(227,290), 
    Point(229,288), 
    Point(230,286), 
    Point(228,284))
    a.setFill("#E7FFFF")
    a.setOutline("#E7FFFF")
    a.draw(win)

    l = Polygon(Point(242,272), 
    Point(239,274), 
    Point(238,279), 
    Point(236,283), 
    Point(234,286), 
    Point(231,291), 
    Point(231,297), 
    Point(236,296), 
    Point(233,295), 
    Point(241,276), 
    Point(242,272), 
    Point(242,270))
    l.setFill("#E7FFFF")
    l.setOutline("#E7FFFF")
    l.draw(win)

    e2 = Polygon(Point(243,292), 
    Point(245,292), 
    Point(247,290), 
    Point(250,288), 
    Point(249,285), 
    Point(245,284), 
    Point(242,285), 
    Point(240,290), 
    Point(238,292), 
    Point(240,297), 
    Point(244,298), 
    Point(247,297), 
    Point(248,296), 
    Point(245,296), 
    Point(243,295), 
    Point(243,295), 
    Point(242,293), 
    Point(242,291), 
    Point(243,290), 
    Point(244,288), 
    Point(245,286), 
    Point(247,286), 
    Point(247,288), 
    Point(245,289), 
    Point(243,291))
    e2.setFill("#E7FFFF")
    e2.setOutline("#E7FFFF")
    e2.draw(win)

    n = Polygon(Point(248,296), 
    Point(254,284), 
    Point(256,283), 
    Point(256,285), 
    Point(258,285), 
    Point(261,284), 
    Point(261,286), 
    Point(260,290), 
    Point(260,295), 
    Point(264,293), 
    Point(261,298), 
    Point(259,297), 
    Point(257,294), 
    Point(258,291), 
    Point(259,288), 
    Point(259,286), 
    Point(255,288), 
    Point(254,290), 
    Point(253,292), 
    Point(252,295), 
    Point(252,297), 
    Point(250,297), 
    Point(250,295), 
    Point(251,292), 
    Point(252,287))
    n.setFill("#E7FFFF")
    n.setOutline("#E7FFFF")
    n.draw(win)

    t = Polygon(Point(267,286), 
    Point(266,290), 
    Point(264,294), 
    Point(264,296), 
    Point(269,297), 
    Point(270,294), 
    Point(266,295), 
    Point(266,293), 
    Point(267,290), 
    Point(269,284), 
    Point(274,284), 
    Point(271,284), 
    Point(272,281), 
    Point(270,280), 
    Point(268,285), 
    Point(265,284), 
    Point(267,285))
    t.setFill("#E7FFFF")
    t.setOutline("#E7FFFF")
    t.draw(win)

    i1 = Polygon(Point(281,280), 
    Point(282,279), 
    Point(281,277), 
    Point(280,277), 
    Point(279,278), 
    Point(280,279))
    i1.setFill("#E7FFFF")
    i1.setOutline("#E7FFFF")
    i1.draw(win)

    i2 = Polygon(Point(276,284), 
    Point(272,293), 
    Point(272,296), 
    Point(276,295), 
    Point(278,294), 
    Point(275,295), 
    Point(276,293), 
    Point(277,290), 
    Point(278,288), 
    Point(278,286), 
    Point(278,285), 
    Point(276,285), 
    Point(275,287))
    i2.setFill("#E7FFFF")
    i2.setOutline("#E7FFFF")
    i2.draw(win)

    n2 = Polygon(Point(277,296), 
    Point(279,294), 
    Point(280,291), 
    Point(281,288), 
    Point(282,285), 
    Point(284,284), 
    Point(286,284), 
    Point(284,287), 
    Point(288,284), 
    Point(290,284), 
    Point(290,289), 
    Point(288,293), 
    Point(288,295), 
    Point(292,295), 
    Point(292,297), 
    Point(288,298), 
    Point(287,295), 
    Point(288,289), 
    Point(288,287), 
    Point(286,286), 
    Point(284,291), 
    Point(282,295), 
    Point(280,297), 
    Point(278,297), 
    Point(283,286), 
    Point(284,285))
    n2.setFill("#E7FFFF")
    n2.setOutline("#E7FFFF")
    n2.draw(win)

    e3 = Polygon(Point(296,293), 
    Point(300,292), 
    Point(304,287), 
    Point(302,284), 
    Point(298,284), 
    Point(295,287), 
    Point(292,293), 
    Point(294,298), 
    Point(298,299), 
    Point(303,297), 
    Point(306,294), 
    Point(308,290), 
    Point(308,288), 
    Point(305,292), 
    Point(301,295), 
    Point(298,296), 
    Point(297,294), 
    Point(297,291), 
    Point(297,289), 
    Point(298,286), 
    Point(300,285), 
    Point(301,285), 
    Point(301,288), 
    Point(299,289), 
    Point(297,290))
    e3.setFill("#E7FFFF")
    e3.setOutline("#E7FFFF")
    e3.draw(win)

    # create the hands of the bear
    handLeft = Polygon(Point(164,250), 
    Point(166,247), 
    Point(171,246), 
    Point(174,245), 
    Point(181,246), 
    Point(185,251), 
    Point(190,258), 
    Point(190,261), 
    Point(187,264), 
    Point(181,266), 
    Point(184,266), 
    Point(186,267), 
    Point(187,270), 
    Point(186,273), 
    Point(184,276), 
    Point(179,279), 
    Point(176,279), 
    Point(170,275), 
    Point(167,272), 
    Point(164,266), 
    Point(162,261), 
    Point(161,257), 
    Point(162,253), 
    Point(162,251), 
    Point(164,248), 
    Point(166,246), 
    Point(171,245))
    handLeft.setFill("#DD930D")
    handLeft.draw(win)

    handRight = Polygon(Point(323,265), 
    Point(320,264), 
    Point(319,259), 
    Point(319,255), 
    Point(324,249), 
    Point(332,247), 
    Point(340,246), 
    Point(342,249), 
    Point(343,256), 
    Point(344,265), 
    Point(342,268), 
    Point(339,273), 
    Point(338,276), 
    Point(333,279), 
    Point(329,281), 
    Point(325,281), 
    Point(321,280), 
    Point(319,279), 
    Point(318,275), 
    Point(317,270), 
    Point(318,266), 
    Point(320,265), 
    Point(322,265))
    handRight.setFill("#DD930D")
    handRight.draw(win)

    # create text underneath the bear
    name = Text(Point(winWidth / 2, 400), "Simon Chu")
    name.setFill("red")
    name.setFace("times roman")
    name.draw(win)
    
    likes = Text(Point(winWidth / 2, 415), "likes")
    likes.setFill("red")
    likes.setFace("times roman")
    likes.draw(win)
    
    course = Text(Point(winWidth / 2, 430), "CS 125")
    course.setFill("red")
    course.setFace("times roman")
    course.draw(win)

    win.getMouse()

    win.close()


main()