# Generated from /Users/muchen/python_smc/DemoKernel/stupyd/compiler/stuPyd.g4 by ANTLR 4.7
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from .stuPydParser import stuPydParser
from antlr4.Token import CommonToken


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\'")
        buf.write("\u0144\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f")
        buf.write("\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\36\3\37")
        buf.write("\3\37\5\37\u00bd\n\37\3 \6 \u00c0\n \r \16 \u00c1\3!\3")
        buf.write("!\3!\5!\u00c7\n!\3!\3!\5!\u00cb\n!\3!\5!\u00ce\n!\5!\u00d0")
        buf.write("\n!\3!\3!\3\"\3\"\6\"\u00d6\n\"\r\"\16\"\u00d7\3\"\3\"")
        buf.write("\3#\3#\7#\u00de\n#\f#\16#\u00e1\13#\3$\6$\u00e4\n$\r$")
        buf.write("\16$\u00e5\3%\6%\u00e9\n%\r%\16%\u00ea\3%\3%\7%\u00ef")
        buf.write("\n%\f%\16%\u00f2\13%\3%\5%\u00f5\n%\3%\3%\6%\u00f9\n%")
        buf.write("\r%\16%\u00fa\3%\5%\u00fe\n%\3%\6%\u0101\n%\r%\16%\u0102")
        buf.write("\3%\5%\u0106\n%\3&\3&\3&\7&\u010b\n&\f&\16&\u010e\13&")
        buf.write("\3&\3&\3\'\3\'\3\'\5\'\u0115\n\'\3\'\3\'\3(\3(\3(\3(\7")
        buf.write("(\u011d\n(\f(\16(\u0120\13(\3)\3)\5)\u0124\n)\3)\6)\u0127")
        buf.write("\n)\r)\16)\u0128\3*\3*\3+\3+\3+\3+\5+\u0131\n+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\5,\u013c\n,\3-\3-\3-\3-\3-\3-\3-\2")
        buf.write("\2.\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?\2A!C\"E#G$I%K")
        buf.write("&M\'O\2Q\2S\2U\2W\2Y\2\3\2\f\4\2\13\13\"\"\5\2C\\aac|")
        buf.write("\6\2\62;C\\aac|\4\2$$^^\4\2))^^\4\2\f\f\16\17\4\2GGgg")
        buf.write("\4\2--//\5\2\62;CHch\n\2$$))^^ddhhppttvv\2\u0158\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2\7`\3\2\2\2\td\3\2\2\2\13")
        buf.write("i\3\2\2\2\rp\3\2\2\2\17u\3\2\2\2\21|\3\2\2\2\23~\3\2\2")
        buf.write("\2\25\u0080\3\2\2\2\27\u0082\3\2\2\2\31\u0084\3\2\2\2")
        buf.write("\33\u0086\3\2\2\2\35\u0088\3\2\2\2\37\u008a\3\2\2\2!\u008c")
        buf.write("\3\2\2\2#\u008e\3\2\2\2%\u0090\3\2\2\2\'\u0092\3\2\2\2")
        buf.write(")\u0094\3\2\2\2+\u0096\3\2\2\2-\u0099\3\2\2\2/\u009c\3")
        buf.write("\2\2\2\61\u009e\3\2\2\2\63\u00a3\3\2\2\2\65\u00a9\3\2")
        buf.write("\2\2\67\u00af\3\2\2\29\u00b5\3\2\2\2;\u00b7\3\2\2\2=\u00bc")
        buf.write("\3\2\2\2?\u00bf\3\2\2\2A\u00cf\3\2\2\2C\u00d5\3\2\2\2")
        buf.write("E\u00db\3\2\2\2G\u00e3\3\2\2\2I\u0105\3\2\2\2K\u0107\3")
        buf.write("\2\2\2M\u0111\3\2\2\2O\u0118\3\2\2\2Q\u0121\3\2\2\2S\u012a")
        buf.write("\3\2\2\2U\u0130\3\2\2\2W\u013b\3\2\2\2Y\u013d\3\2\2\2")
        buf.write("[\\\7=\2\2\\\4\3\2\2\2]^\7/\2\2^_\7@\2\2_\6\3\2\2\2`a")
        buf.write("\7p\2\2ab\7w\2\2bc\7o\2\2c\b\3\2\2\2de\7d\2\2ef\7q\2\2")
        buf.write("fg\7q\2\2gh\7n\2\2h\n\3\2\2\2ij\7u\2\2jk\7v\2\2kl\7t\2")
        buf.write("\2lm\7k\2\2mn\7p\2\2no\7i\2\2o\f\3\2\2\2pq\7x\2\2qr\7")
        buf.write("q\2\2rs\7k\2\2st\7f\2\2t\16\3\2\2\2uv\7u\2\2vw\7v\2\2")
        buf.write("wx\7t\2\2xy\7w\2\2yz\7e\2\2z{\7v\2\2{\20\3\2\2\2|}\7.")
        buf.write("\2\2}\22\3\2\2\2~\177\7-\2\2\177\24\3\2\2\2\u0080\u0081")
        buf.write("\7/\2\2\u0081\26\3\2\2\2\u0082\u0083\7,\2\2\u0083\30\3")
        buf.write("\2\2\2\u0084\u0085\7\61\2\2\u0085\32\3\2\2\2\u0086\u0087")
        buf.write("\7`\2\2\u0087\34\3\2\2\2\u0088\u0089\7*\2\2\u0089\36\3")
        buf.write("\2\2\2\u008a\u008b\7+\2\2\u008b \3\2\2\2\u008c\u008d\7")
        buf.write("~\2\2\u008d\"\3\2\2\2\u008e\u008f\7(\2\2\u008f$\3\2\2")
        buf.write("\2\u0090\u0091\7?\2\2\u0091&\3\2\2\2\u0092\u0093\7@\2")
        buf.write("\2\u0093(\3\2\2\2\u0094\u0095\7>\2\2\u0095*\3\2\2\2\u0096")
        buf.write("\u0097\7@\2\2\u0097\u0098\7?\2\2\u0098,\3\2\2\2\u0099")
        buf.write("\u009a\7>\2\2\u009a\u009b\7?\2\2\u009b.\3\2\2\2\u009c")
        buf.write("\u009d\7#\2\2\u009d\60\3\2\2\2\u009e\u009f\7V\2\2\u009f")
        buf.write("\u00a0\7T\2\2\u00a0\u00a1\7W\2\2\u00a1\u00a2\7G\2\2\u00a2")
        buf.write("\62\3\2\2\2\u00a3\u00a4\7H\2\2\u00a4\u00a5\7C\2\2\u00a5")
        buf.write("\u00a6\7N\2\2\u00a6\u00a7\7U\2\2\u00a7\u00a8\7G\2\2\u00a8")
        buf.write("\64\3\2\2\2\u00a9\u00aa\7r\2\2\u00aa\u00ab\7t\2\2\u00ab")
        buf.write("\u00ac\7k\2\2\u00ac\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae")
        buf.write("\66\3\2\2\2\u00af\u00b0\7y\2\2\u00b0\u00b1\7j\2\2\u00b1")
        buf.write("\u00b2\7k\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4\7g\2\2\u00b4")
        buf.write("8\3\2\2\2\u00b5\u00b6\7<\2\2\u00b6:\3\2\2\2\u00b7\u00b8")
        buf.write("\7k\2\2\u00b8\u00b9\7h\2\2\u00b9<\3\2\2\2\u00ba\u00bd")
        buf.write("\5G$\2\u00bb\u00bd\5I%\2\u00bc\u00ba\3\2\2\2\u00bc\u00bb")
        buf.write("\3\2\2\2\u00bd>\3\2\2\2\u00be\u00c0\t\2\2\2\u00bf\u00be")
        buf.write("\3\2\2\2\u00c0\u00c1\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1")
        buf.write("\u00c2\3\2\2\2\u00c2@\3\2\2\2\u00c3\u00c4\6!\2\2\u00c4")
        buf.write("\u00d0\5? \2\u00c5\u00c7\7\17\2\2\u00c6\u00c5\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8\u00cb\7")
        buf.write("\f\2\2\u00c9\u00cb\7\17\2\2\u00ca\u00c6\3\2\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\u00cd\3\2\2\2\u00cc\u00ce\5? \2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00c3\3\2\2\2\u00cf\u00ca\3\2\2\2\u00d0\u00d1\3")
        buf.write("\2\2\2\u00d1\u00d2\b!\2\2\u00d2B\3\2\2\2\u00d3\u00d6\5")
        buf.write("? \2\u00d4\u00d6\5O(\2\u00d5\u00d3\3\2\2\2\u00d5\u00d4")
        buf.write("\3\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d7")
        buf.write("\u00d8\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\b\"\3\2")
        buf.write("\u00daD\3\2\2\2\u00db\u00df\t\3\2\2\u00dc\u00de\t\4\2")
        buf.write("\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0F\3\2\2\2\u00e1\u00df")
        buf.write("\3\2\2\2\u00e2\u00e4\4\62;\2\u00e3\u00e2\3\2\2\2\u00e4")
        buf.write("\u00e5\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2")
        buf.write("\u00e6H\3\2\2\2\u00e7\u00e9\4\62;\2\u00e8\u00e7\3\2\2")
        buf.write("\2\u00e9\u00ea\3\2\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00f0\7\60\2\2\u00ed")
        buf.write("\u00ef\4\62;\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2\3\2\2\2")
        buf.write("\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f4\3")
        buf.write("\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f5\5Q)\2\u00f4\u00f3")
        buf.write("\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u0106\3\2\2\2\u00f6")
        buf.write("\u00f8\7\60\2\2\u00f7\u00f9\4\62;\2\u00f8\u00f7\3\2\2")
        buf.write("\2\u00f9\u00fa\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00fb")
        buf.write("\3\2\2\2\u00fb\u00fd\3\2\2\2\u00fc\u00fe\5Q)\2\u00fd\u00fc")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0106\3\2\2\2\u00ff")
        buf.write("\u0101\4\62;\2\u0100\u00ff\3\2\2\2\u0101\u0102\3\2\2\2")
        buf.write("\u0102\u0100\3\2\2\2\u0102\u0103\3\2\2\2\u0103\u0104\3")
        buf.write("\2\2\2\u0104\u0106\5Q)\2\u0105\u00e8\3\2\2\2\u0105\u00f6")
        buf.write("\3\2\2\2\u0105\u0100\3\2\2\2\u0106J\3\2\2\2\u0107\u010c")
        buf.write("\7$\2\2\u0108\u010b\5U+\2\u0109\u010b\n\5\2\2\u010a\u0108")
        buf.write("\3\2\2\2\u010a\u0109\3\2\2\2\u010b\u010e\3\2\2\2\u010c")
        buf.write("\u010a\3\2\2\2\u010c\u010d\3\2\2\2\u010d\u010f\3\2\2\2")
        buf.write("\u010e\u010c\3\2\2\2\u010f\u0110\7$\2\2\u0110L\3\2\2\2")
        buf.write("\u0111\u0114\7)\2\2\u0112\u0115\5U+\2\u0113\u0115\n\6")
        buf.write("\2\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2\u0115\u0116")
        buf.write("\3\2\2\2\u0116\u0117\7)\2\2\u0117N\3\2\2\2\u0118\u0119")
        buf.write("\7\61\2\2\u0119\u011a\7\61\2\2\u011a\u011e\3\2\2\2\u011b")
        buf.write("\u011d\n\7\2\2\u011c\u011b\3\2\2\2\u011d\u0120\3\2\2\2")
        buf.write("\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2\u011fP\3\2\2")
        buf.write("\2\u0120\u011e\3\2\2\2\u0121\u0123\t\b\2\2\u0122\u0124")
        buf.write("\t\t\2\2\u0123\u0122\3\2\2\2\u0123\u0124\3\2\2\2\u0124")
        buf.write("\u0126\3\2\2\2\u0125\u0127\4\62;\2\u0126\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0126\3\2\2\2\u0128\u0129\3")
        buf.write("\2\2\2\u0129R\3\2\2\2\u012a\u012b\t\n\2\2\u012bT\3\2\2")
        buf.write("\2\u012c\u012d\7^\2\2\u012d\u0131\t\13\2\2\u012e\u0131")
        buf.write("\5Y-\2\u012f\u0131\5W,\2\u0130\u012c\3\2\2\2\u0130\u012e")
        buf.write("\3\2\2\2\u0130\u012f\3\2\2\2\u0131V\3\2\2\2\u0132\u0133")
        buf.write("\7^\2\2\u0133\u0134\4\62\65\2\u0134\u0135\4\629\2\u0135")
        buf.write("\u013c\4\629\2\u0136\u0137\7^\2\2\u0137\u0138\4\629\2")
        buf.write("\u0138\u013c\4\629\2\u0139\u013a\7^\2\2\u013a\u013c\4")
        buf.write("\629\2\u013b\u0132\3\2\2\2\u013b\u0136\3\2\2\2\u013b\u0139")
        buf.write("\3\2\2\2\u013cX\3\2\2\2\u013d\u013e\7^\2\2\u013e\u013f")
        buf.write("\7w\2\2\u013f\u0140\5S*\2\u0140\u0141\5S*\2\u0141\u0142")
        buf.write("\5S*\2\u0142\u0143\5S*\2\u0143Z\3\2\2\2\34\2\u00bc\u00c1")
        buf.write("\u00c6\u00ca\u00cd\u00cf\u00d5\u00d7\u00df\u00e5\u00ea")
        buf.write("\u00f0\u00f4\u00fa\u00fd\u0102\u0105\u010a\u010c\u0114")
        buf.write("\u011e\u0123\u0128\u0130\u013b\4\3!\2\b\2\2")
        return buf.getvalue()


class stuPydLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    NUMBER = 30
    NEWLINE = 31
    BLANK = 32
    ID = 33
    INT = 34
    FLOAT = 35
    STRING = 36
    CHAR = 37

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'->'", "'num'", "'bool'", "'string'", "'void'", "'struct'", 
            "','", "'+'", "'-'", "'*'", "'/'", "'^'", "'('", "')'", "'|'", 
            "'&'", "'='", "'>'", "'<'", "'>='", "'<='", "'!'", "'TRUE'", 
            "'FALSE'", "'print'", "'while'", "':'", "'if'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "NEWLINE", "BLANK", "ID", "INT", "FLOAT", "STRING", 
            "CHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "NUMBER", "SPACES", "NEWLINE", 
                  "BLANK", "ID", "INT", "FLOAT", "STRING", "CHAR", "COMMENT", 
                  "EXPONENT", "HEX_DIGIT", "ESC_SEQ", "OCTAL_ESC", "UNICODE_ESC" ]

    grammarFileName = "stuPyd.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


        self.lastToken = None
        self.tokens = []
        self.indentStack = []

    def emit(self,t=None):
        if t == None :
            s = self._factory.create(self._tokenFactorySourcePair, self._type, self._text, self._channel, self._tokenStartCharIndex,
                                     self.getCharIndex()-1, self._tokenStartLine, self._tokenStartColumn)
            self.emitToken(s)
            # print(s)
            self.tokens.append(s)
            return s
        else:
            self.emitToken(t)
            self.tokens.append(t)
            # print(t)
            return t

    def commonToken(self,type,text):
        stop = self.getCharIndex()-1
        if len(text)==0 :
            start = stop
        else:
            start = stop - len(text)+1
        return CommonToken(self._tokenFactorySourcePair,type,self.DEFAULT_TOKEN_CHANNEL,start,stop)

    def createDedent(self):
        dedent = self.commonToken(stuPydParser.DEDENT,'')
        dedent.line = self.lastToken.line
        return dedent

    @staticmethod
    def getIndentationCount(spaces):
        count = 0
        for ch in spaces:
            if ch == '\t':
                count +=( 4 - (count%4))
            elif ch == ' ':
                count += 1
            else :
                pass
        # print(count)
        return count

    def nextToken(self):
        # Check if the end-of-file is ahead and there are still some DEDENTS expected
        if(self._input.LA(1)==Token.EOF and len(self.indentStack)!=0):
            # Remove ant trailing EOF tokens from our buffer
            i = len(self.tokens)-1
            while i>= 0 :
                if(self.tokens[i].type==Token.EOF):
                    self.tokens.pop(i)
                i-=1
            # First emit an extra line break that serves as the end of the stmt
            self.emit(self.commonToken(stuPydParser.NEWLINE,'\n'))
            # Now emit as much DEDENT tokens as needed
            while len(self.indentStack)!=0 :
                self.emit(self.createDedent())
                self.indentStack.pop()
            # put the EOF back on the token stream .
            self.emit(self.commonToken(stuPydParser.EOF,'<EOF>'))
        next = super().nextToken()
        if (next.channel == Token.DEFAULT_CHANNEL):
            # Keep track of the last token on the default channel
            self.lastToken = next
        if len(self.tokens) == 0 :
            # print(next)
            return next
        else :
            temp = self.tokens[0]
            self.tokens.pop(0)
            # print(temp)
            return temp

    def atStartOfInput(self):
        if super().getCharIndex()==0 and super().line==1 :
            # print('True')
            return True
        else:
            # print('False')
            return False


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
    	if self._actions is None:
    		actions = dict()
    		actions[31] = self.NEWLINE_action 
    		self._actions = actions
    	action = self._actions.get(ruleIndex, None)
    	if action is not None:
    		action(localctx, actionIndex)
    	else:
    		raise Exception("No registered action for:" + str(ruleIndex))

    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    newLine = self.text
                    for i in newLine :
                        if i == '\r' or i == '\n' or i == '\f':
                            pass
                        else:
                            newLine.replace(str(i),'')

                    spaces = self.text.replace('\r','')
                    spaces = self.text.replace('\n','')
                    spaces = self.text.replace('\f','')

                    next = self._input.LA(1)

                    if(next=='\r' or next == '\n' or next == '\f' or next == '<EOF>'):
                        self.skip()
                    else:
                        self.emit(self.commonToken(self.NEWLINE,newLine))
                        indent = self.getIndentationCount(spaces)
                        previous = 0
                        if len(self.indentStack) != 0 :
                            previous = self.indentStack.pop()
                            self.indentStack.append(previous)
                            # it is equal to indentStack.peek()
                        if indent==previous :
                            # skip indents of the same size as the present indent-size
                            self.skip()
                        elif indent > previous :
                            self.indentStack.append(indent)
                            self.emit(self.commonToken(stuPydParser.INDENT,spaces))
                        else:
                            # Possibly emit more than 1 DEDENT token
                            while len(self.indentStack)!=0 and self.indentStack[len(self.indentStack)-1]>indent:
                                self.emit(self.createDedent())
                                self.indentStack.pop()
               
     

    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates is None:
            preds = dict()
            preds[31] = self.NEWLINE_sempred
            self._predicates = preds
        pred = self._predicates.get(ruleIndex, None)
        if pred is not None:
            return pred(localctx, predIndex)
        else:
            raise Exception("No registered predicate for:" + str(ruleIndex))

    def NEWLINE_sempred(self, localctx:RuleContext, predIndex:int):
            if predIndex == 0:
                return self.atStartOfInput()
         


