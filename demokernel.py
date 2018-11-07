import sys
from ipykernel.kernelbase import Kernel
from antlr4 import *
from stupyd.compiler.stuPydLexer import stuPydLexer
from stupyd.compiler.stuPydParser import stuPydParser
from stupyd.compiler.extendListener import extendListener
from stupyd.interpreter.stupydInterpreter import Interpreter

class DemoKernel(Kernel):
    # basic information
    implementation = 'Demo'
    implementation_version = '1.0'
    language = 'python'   # for syntax highlighting
    language_version = '0.1'
    language_info = {
        'name': 'python',
        'mimetype': 'text/python',
        'file_extension': '.py'
    }
    banner = 'Demo kernel - we can do more'

    # interpreter part
    def __init__(self, **kwargs):
        Kernel.__init__(self, **kwargs)
        self.code_obj = {}
        self.num_array = []
        self.id_array = []
        self.stack = []
        self.environmrnt = {}

        self.instruction_set = {
            0: self.LOAD_NUM,
            1: self.DECL_FAST,
            2: self.STORE_FAST,
            3: self.LOAD_FAST,
            4: self.ADD_TWO_NUMBERS,
            5: self.SUBSTRACT_TWO_NUMBERS,
            6: self.MULTIPLE_TWO_NUMBERS,
            # 7 is initially reversed for division, now use it for print
            7: self.PRINT,
            8: self.COMPARE_TWO_NUMBERS,
            9: self.JUMP,
            10: self.JUMP_IF_FALSE,
            11: self.WHILE_LOOP,
            13: self.QUIT,

            # 14 - 16 is used

            17: self.LOAD_STRING
        }

        self.false_flag = 0
        self.pc = 0
        self.quit_flag = 0

        self.silent = None

    # push a number into stack
    def LOAD_NUM(self, index):
        self.stack.append(float(self.num_array[index]))

    # push a string into a stack
    def LOAD_STRING(self, index):
        val = self.num_array[index]
        self.stack.append(self.num_array[index])

    # create a new item in enviroment using id as key
    def DECL_FAST(self, index):
        self.environmrnt[self.id_array[index]] = 0

    # pop a value from stack and set as the value of id
    def STORE_FAST(self, index):
        val = self.stack.pop()
        self.environmrnt[self.id_array[index]] = val

    # get value with id, then pop it into stack
    def LOAD_FAST(self, index):
        val = self.environmrnt[self.id_array[index]]
        self.stack.append(val)

    # pop two values from stack, push sum back
    def ADD_TWO_NUMBERS(self, useless):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        val = val2 + val1
        self.stack.append(val)

    # pop two values from stack, push difference back
    def SUBSTRACT_TWO_NUMBERS(self, useless):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        val = val2 - val1
        self.stack.append(val)

    # pop two values from stack, push product back
    def MULTIPLE_TWO_NUMBERS(self, useless):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        val = val2 * val1
        self.stack.append(val)

    # pop an item then print it
    def PRINT(self, useless):
        val = self.stack.pop()
        val = str(val)
        stream_content = {
            'name': 'stdout',
            'text': val
        }
        self.send_response(self.iopub_socket, 'stream', stream_content)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }

    # pop two items out to compare, then set flag
    def COMPARE_TWO_NUMBERS(self, case):
        val1 = self.stack.pop()
        val2 = self.stack.pop()
        if case == 0:
            if val1 <= val2:
                self.false_flag = 1
            else:
                self.false_flag = 0
        elif case == 1:
            if val1 >= val2:
                self.false_flag = 1
            else:
                self.false_flag = 0
        elif case == 2:
            if val1 == val2:
                self.false_flag = 0
            else:
                self.false_flag = 1
        else:
            pass

    # jump to target byte instruction
    def JUMP(self, target):
        self.pc = target

    # jump to target byte instruction depending on flag
    def JUMP_IF_FALSE(self, target):
        if self.false_flag == 1:
            self.pc = target

    # a flag for while_loop, doing nothing
    def WHILE_LOOP(self, useless):
        pass

    # quit the whole program, endding
    def QUIT(self, useless):
        self.quit_flag = 1


    def test_output(self, silent, content):
        if not silent:
            stream_content = {
                'name': 'stdout',
                'text': str(content) + '\n'
            }
            self.send_response(self.iopub_socket, 'stream', stream_content)

    def reset(self):
        self.code_obj = {}
        self.num_array = []
        self.id_array = []
        self.stack = []
        self.environmrnt = {}
        self.false_flag = 0
        self.pc = 0
        self.quit_flag = 0

    # 增加pc的值 返回解析后的当前指令
    def dispatch(self):
        current_ins = self.code_obj[self.pc]
        self.pc = self.pc + 2
        return current_ins

    # rewrite 'de_execute' method, which is the most important job
    def do_execute(self, code, silent, store_history=True,
                   user_expressions=None, allow_stdin=False):
        # reset
        self.reset()

        # compile code to byte instruction
        instream = InputStream(code)
        lexer = stuPydLexer(instream, None)
        token_stream = CommonTokenStream(lexer)
        parser = stuPydParser(token_stream)
        tree = parser.file_input()
        walker = ParseTreeWalker()
        listener = extendListener()
        walker.walk(listener, tree)

        self.code_obj = listener.code_obj
        self.num_array = listener.valueTable
        self.id_array = listener.varTable

        # self.test_output(silent, self.code_obj)
        # self.test_output(silent, self.num_array)

        # run code
        while self.quit_flag != 1:
            # if not silent:
            current_ins = self.dispatch()
            self.instruction_set[current_ins[0]](current_ins[1])
            # self.test_output(silent, self.instruction_set[current_ins[0]].__name__)

        return {
            'status': 'ok',
            'execution_count': self.execution_count,
            'payload': [],
            'user_expressions': {}
        }

if __name__ == '__main__':
    from ipykernel.kernelapp import IPKernelApp
    IPKernelApp.launch_instance(kernel_class=DemoKernel)