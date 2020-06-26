class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def check(self, advantage):
        try:
            for n in advantage:
                if n == '{':
                    self.push('{')
                if n == '(':
                    self.push('(')
                if n == '[':
                    self.push('[')
                if n == '}':
                    self.items.remove('{')
                if n == ')':
                    self.items.remove('(')
                if n == ']':
                    self.items.remove('[')
            element = self.size()
            if element == 0:
                print("Сбалансировано")
            else:
                self.items.clear()
                print("Несбалансировано")
        except IndexError:
            self.items.clear()
            print("Несбалансировано")
        except ValueError:
            self.items.clear()
            print("Несбалансировано")

    def specularity(self, string):
        for item in string:
            self.items.append(item)
        run = self.size()
        if (run % 2) == 0 and run != 0:
            print('проверка на зеркальность:')
            while run != 0:
                left = self.items.pop()
                right = self.items.pop(0)
                if right == '(' and left == ')':
                    run = run - 2
                elif right == '[' and left == ']':
                    run = run - 2
                elif right == '{' and left == '}':
                    run = run - 2
                else:
                    break
            if self.size() == 0:
                print("Выполняется зеркальность")
            else:
                self.items.clear()
                print("Зеркальность не выполняется")
        else:
            self.items.clear()
            print("Зеркальность не выполняется")



test = Stack()
print('\n Проверка (((([{}])))) \n')
test.specularity('(((([{}]))))')
test.check('(((([{}]))))')

print('\n Проверка [([])((([[[]]])))]{()} \n')
test.specularity('[([])((([[[]]])))]{()}')
test.check('[([])((([[[]]])))]{()}')

print('\n Проверка {{[()]}} \n')
test.specularity('{{[()]}}')
test.check('{{[()]}}')

print('\n Проверка }{} \n')
test.specularity('}{}')
test.check('}{}')

print('\n Проверка {{[(])]}} \n')
test.specularity('{{[(])]}}')
test.check('{{[(])]}}')

print('\n Проверка [[{())}] \n')
test.specularity('[[{())}]')
test.check('[[{())}]')