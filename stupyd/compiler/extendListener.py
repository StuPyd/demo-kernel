from .stuPydLexer import stuPydLexer
from .stuPydParser import stuPydParser
from .stuPydListener import stuPydListener
from .stupydInterpreter import Interpreter

class extendListener(stuPydListener):
     # listener members
    def __init__(self):
        # Variable Table relative
        self.varTable = []
        self.k = 0 ;
        self.tempVarLoc=-1
        # Value Table relative
        self.valueTable=[]
        self.locValueTable = 0
        # code_obj and relative， added by muchensun
        self.code_obj = {}
        self.code_index = 0
        self.current_instruction = []
        self.boolReslut = False
        self.whileStack = []

    # added by muchensun
    def add_to_code_obj(self, code, attr):
        self.current_instruction = [code, attr]
        self.code_obj[self.code_index] = self.current_instruction
        self.code_index = self.code_index + 2

    # added by muchensun
    def print_relatives(self):
        print("constants: ", self.valueTable)  # print relative attributes
        print("variables: ", self.varTable)
        print("code object:")
        for key, value in self.code_obj.items():
            print('\t{key}: {value}'.format(key=key, value=value))
        print('\n')

    def findVarTable(self,s):
        i=0
        for temps in self.varTable:
            if temps == s :
                return i
            i=i+1
        return -1

    def getNewValueLocation(self):
        rt = self.locValueTable
        self.locValueTable = self.locValueTable + 1
        return rt

    def findLocationOfValueTable(self,v):
        i = 0;
        for str in self.valueTable :
            if self.valueTable[i] == v :
                return i
            i=i+1
        # str is a float although i named it str
        tempLoc = self.getNewValueLocation()
        #self.valueTable.append(v)
        self.valueTable.append(v)
        return tempLoc

    def exitTarget(self, ctx:stuPydParser.TargetContext):
        sInTarget = ctx.ID().getText()
        tl = self.findVarTable(sInTarget)
        if(tl==-1):
            i = self.k
            #self.varTable[i]=sInTarget
            self.varTable.append(sInTarget)
            # print('FAST_DECL\t%d'%self.k)
            self.add_to_code_obj(1, self.k)
            self.k=self.k + 1
        else:
            # print('Error.\n')
            pass

    def exitFnum(self, ctx: stuPydParser.FnumContext):
        s=ctx.getText()
        tl=self.findLocationOfValueTable(s)
        # print('LOAT_CONST\t%d'%tl)
        self.add_to_code_obj(0, tl)

    # added by muchensun
    def exitFString(self, ctx: stuPydParser.FStringContext):
        text = ctx.getText()
        new_text = text[1:len(text)-1]
        new_text = str(new_text)
        new_text = new_text.encode().decode('unicode_escape')
        tl = self.findLocationOfValueTable(new_text)
        # print('LOAT_STRING\t%d'%tl)
        self.add_to_code_obj(17, tl)

    def exitFprmy(self, ctx:stuPydParser.FprmyContext):
        # print('LOAD_FAST\t%d'%self.tempVarLoc)
        self.add_to_code_obj(3, self.tempVarLoc)

    def exitUfac(self, ctx:stuPydParser.UfacContext):
        pass

    def exitTunary(self, ctx:stuPydParser.TunaryContext):
        pass

    def exitEterm(self, ctx:stuPydParser.EtermContext):
        pass

    def exitEadd(self, ctx:stuPydParser.EaddContext):
        # print('ADD_TWO_NUMBERS()')
        self.add_to_code_obj(4, -1)

    def exitEsub(self, ctx: stuPydParser.EsubContext):
        # print('SUB_TWO_NUMBERS()')
        self.add_to_code_obj(5, -1)

    def exitGvExp(self, ctx: stuPydParser.GvExpContext):
        gvVarName = ctx.prmy().getText()
        varLoc = self.findVarTable(gvVarName)
        # print('STORE_FAST\t%d'%varLoc)
        self.add_to_code_obj(2, varLoc)

    # EDIT ON 2018-8-14

    def exitGvBool(self, ctx:stuPydParser.GvBoolContext):
        gvVarName = ctx.prmy().getText()
        varLoc = self.findVarTable(gvVarName)
        # print('STORE_FAST\t%d'%varLoc)
        self.add_to_code_obj(2, varLoc)

    def exitPrmy(self, ctx: stuPydParser.PrmyContext):
        IDname = ctx.ID().getText()
        self.tempVarLoc = self.findVarTable(IDname)

    def exitTmul(self, ctx: stuPydParser.TmulContext):
        # print('MUL_TWO_NUMBERS()')
        self.add_to_code_obj(6, -1)

    # added by muchen
    # old version.
    # def exitOutput(self, ctx:stuPydParser.OutputContext):
    #
    #     IDname = ctx.ID().getText()
    #     IDLoc = self.findVarTable(IDname)
    #     # print('LOAD_FAST\t%d'%IDLoc)
    #     # print('print')
    #     self.add_to_code_obj(3, IDLoc)
    #     self.add_to_code_obj(7, -1)
    #
    # def exitDirect_print(self, ctx:stuPydParser.Direct_printContext):
    #     self.add_to_code_obj(7, -1)
    # def exitCall_print(self, ctx:stuPydParser.Call_printContext):
    #     self.add_to_code_obj(7, -1)
    def exitOutput(self, ctx:stuPydParser.OutputContext):
        self.add_to_code_obj(7, -1)

    # added by muchen
    def exitSimple_stmt(self, ctx:stuPydParser.Simple_stmtContext):
        pass

    def exitFile_input(self, ctx:stuPydParser.File_inputContext):
        self.add_to_code_obj(13, -1)  # add QUIT instruction

        # self.print_relatives()

        # stupyd = Interpreter(self.code_obj, self.valueTable, self.varTable)
        # stupyd.run_code()
        # stupyd.print_running_env()

    def exitBtrue(self, ctx:stuPydParser.BtrueContext):
        # print("LOAD_BOOL\t1")
        self.add_to_code_obj(16,1)

    def exitBfalse(self, ctx:stuPydParser.BfalseContext):
        # print("LOAD_BOOL\t0")
        self.add_to_code_obj(16, 0)

    def exitRnot(self, ctx:stuPydParser.RnotContext):
        # print("NO\t")
        pass

    def exitRbig(self, ctx:stuPydParser.RbigContext):
        # print("COMPARE_TWO_NUMBERS\t1")
        self.add_to_code_obj(8, 1)

    def exitRsml(self, ctx:stuPydParser.RsmlContext):
        # print("COMPARE_TWO_NUMBERS\t0")
        self.add_to_code_obj(8, 0)

    def exitRbe(self, ctx:stuPydParser.RbeContext):
        # print("COMPARE_TWO_NUMBERS\t4")
        self.add_to_code_obj(8, 4)

    def exitRse(self, ctx:stuPydParser.RseContext):
        # print("COMPARE_TWO_NUMBERS\t3")
        self.add_to_code_obj(8, 3)

    def exitEeql(self, ctx:stuPydParser.EeqlContext):
        # print("COMPARE_TWO_NUMBERS\t2")
        self.add_to_code_obj(8, 2)

    def exitJand(self, ctx:stuPydParser.JandContext):
        # print("AND\t")
        self.add_to_code_obj(13,-1)

    def exitBor(self, ctx:stuPydParser.BorContext):
        # print("OR\t")
        self.add_to_code_obj(14, -1)

    def exitRprmy(self, ctx:stuPydParser.RprmyContext):
        # print('LOAD_FAST\t%d' % self.tempVarLoc)
        self.add_to_code_obj(3, self.tempVarLoc)

    def enterWhile_stmt(self, ctx:stuPydParser.While_stmtContext):
        # print("WHILE_LOOP()")
        self.add_to_code_obj(11,-1)
        self.whileStack.append(self.code_index - 2)

    def exitWhile_judge(self, ctx:stuPydParser.While_judgeContext):
        # I store in the code_obj but without parameters .
        # Then put location into whileStack . so that I can change it when "while_stmt"ends .
        # print("JUMP_IF_FALSE\t//parameters behind the nearest JUMP")
        self.add_to_code_obj(10,-1)
        self.whileStack.append(self.code_index-2)

    def exitWhile_stmt(self, ctx:stuPydParser.While_stmtContext):
        JIFLoc = self.whileStack.pop()
        whileLoc = self.whileStack.pop()
        # print("JUMP\t%d\t%d"%(whileLoc,self.code_index+2))
        JIFtarget = self.code_index
        self.add_to_code_obj(9,whileLoc)
        self.code_obj[JIFLoc] = (10,self.code_index)
        # print(JIFLoc,'\t',self.code_obj[JIFLoc])

    def enterSuite(self, ctx:stuPydParser.SuiteContext):
        # print('INDENT')
        pass

    def exitSuite(self, ctx:stuPydParser.SuiteContext):
        # print('DEDENT')
        pass
