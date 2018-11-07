class Interpreter:
    def __init__(self, code_obj, num_array, id_array):
        self.code_obj = code_obj
        self.num_array = num_array
        self.id_array = id_array
        self.stack = []
        self.environmrnt = {}

        self.instruction_set = {
            0: self.LOAD_CONST,
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
            13: self.QUIT
        }

        self.false_flag = 0
        self.pc = 0
        self.quit_flag = 0

    def readfile(self, code_obj):
        pass

    def print_running_env(self):
        print("running environment:")
        for key, value in self.environmrnt.items():
            print('\t{key}: {value}'.format(key=key, value=value))
        print('\n')

    # push a number into stack
    def LOAD_CONST(self, index):
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
        val = val1 + val2
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
        val = val1 * val2
        self.stack.append(val)

    def PRINT(self, useless):
        val = self.stack.pop()
        print(val)

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

    def JUMP(self, target):
        self.pc = target

    def JUMP_IF_FALSE(self, target):
        if self.false_flag == 1:
            self.pc = target

    def WHILE_LOOP(self, useless):
        pass

    def QUIT(self, useless):
        self.quit_flag = 1

    # 增加pc的值 返回解析后的当前指令
    def dispatch(self):
        current_ins = self.code_obj[self.pc]
        self.pc = self.pc + 2
        return current_ins

    def run_code(self):
        while self.quit_flag != 1:
            current_ins = self.dispatch()
            self.instruction_set[current_ins[0]](current_ins[1])


# demo = Interpreter(code_obj, num_array, id_array)
# demo.run_code()