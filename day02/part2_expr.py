import copy
import sys


class Expression:
    def __init__(self, *args):
        self.xy2term = dict()
        for term in args:
            x = term.x
            y = term.y

            if (x, y) not in self.xy2term:
                self.xy2term[(x, y)] = Term(x=x, y=y)

            self.xy2term[(x, y)] += term

        self.__rmul__ = self.__mul__
        self.__radd__ = self.__add__
        self.__repr__ = self.__str__

    def __mul__(self, other):

        if isinstance(other, int):
            other = Term(c=other)
        if isinstance(other, Term):
            other = Expression(other)

        if not isinstance(other, Expression):
            raise TypeError(
                'cannot do multiplication with {}'.format(type(other)))

        retval = Expression()

        for key1, term1 in self.xy2term.items():
            for key2, term2 in other.xy2term.items():
                term = term1 * term2

                x = term.x
                y = term.y
                c = term.c

                if c != 0:
                    if (x, y) not in retval.xy2term:
                        retval.xy2term[(x, y)] = Term(x=x, y=y)
                    retval.xy2term[(x, y)] += term

        return retval

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        retval = copy.deepcopy(self)

        if isinstance(other, int):
            other = Term(c=other)

        if isinstance(other, Term):
            if (other.x, other.y) not in retval.xy2term:
                retval.xy2term[(other.x, other.y)] = Term(x=other.x, y=other.y)
            retval.xy2term[(other.x, other.y)] += other

            if retval.xy2term[(other.x, other.y)].c == 0:
                del retval.xy2term[(other.x, other.y)]

        elif isinstance(other, Expression):
            for key in other.xy2term:
                if key not in retval.xy2term:
                    retval.xy2term[key] = Term(x=key[0], y=key[1])

                retval.xy2term[key] += other.xy2term[key]

                if retval.xy2term[key].c == 0:
                    del retval.xy2term[key]

        else:
            raise TypeError('cannot do addition with {}'.format(type(other)))

        return retval

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        if not self.xy2term:
            return 0

        return ' + '.join(map(str, self.xy2term.values()))

    def __repr__(self):
        return self.__str()

    def evaluate(self, x, y):
        total = 0
        for term in self.xy2term.values():
            total += term.evaluate(x, y)

        return total


class Term:
    def __init__(self, copy_from=None, x=0, y=0, c=0):

        if copy_from is None:
            self.x = x
            self.y = y
            self.c = c
        else:
            self.x = copy_from.x
            self.y = copy_from.y
            self.c = copy_from.c

    def __mul__(self, other):
        retval = Term(self)

        if isinstance(other, int):
            retval.c *= other
        elif isinstance(other, Term):
            retval.c *= other.c
            retval.x += other.x
            retval.y += other.y
        else:
            return NotImplemented

        return retval

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        retval = Term(self)

        if isinstance(other, int):
            if self.x == 0 and self.y == 0:
                retval.c += other
            else:
                retval = Expression(retval, Term(c=other))

        elif isinstance(other, Term):
            if self.x == other.x and self.y == other.y:
                retval.c += other.c
            else:
                retval = Expression(retval, Term(other))
        else:
            return NotImplemented

        return retval

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        if self.c == 0:
            return '0'
        elif self.x == 0 and self.y == 0:
            return str(self.c)
        elif self.x == 0 and self.y != 0:
            return '{} y^{}'.format(self.c, self.y)
        elif self.x != 0 and self.y == 0:
            return '{} x^{}'.format(self.c, self.x)
        else:
            return '{} x^{} y^{}'.format(self.c, self.x, self.y)

    def __repr__(self):
        return self.__str()

    def evaluate(self, x, y):
        return x ** self.x * y ** self.y * self.c


if __name__ == '__main__':

    mem = list(map(int, input().split(',')))

    mem[1] = Term(x=1, c=1)
    mem[2] = Term(y=1, c=1)

    for i in range(4, len(mem), 4):
        op_code = mem[i]

        if op_code == 99:
            break

        left_val = mem[mem[i + 1]]
        right_val = mem[mem[i + 2]]

        if op_code == 1:
            result = left_val + right_val
        elif op_code == 2:
            result = left_val * right_val
        else:
            # Something is wrong
            print('op_code error')
            sys.exit(1)

        mem[mem[i + 3]] = result

    final_expression = mem[0]
    print(final_expression)

    for x in range(100):
        for y in range(100):
            if final_expression.evaluate(x, y) == 19690720:

                print('Found {}, {}'.format(x, y))
                print(100 * x + y)
                sys.exit(0)
