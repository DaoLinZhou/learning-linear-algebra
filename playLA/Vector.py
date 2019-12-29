from ._global import EPSILON, is_zero
import math


class Vector:

    def __init__(self, lst):
        # 因为list是引用, 为了防止用户通过更改外面的list更改里面的值
        # 我们要对lst进行复制
        self._values = list(lst)

    @classmethod
    def zero(cls, dim):
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        """返回向量的单位向量"""
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector(self._values) / self.norm()

    def underlying_list(self):
        """返回向量的底层列表"""
        return self._values[:]

    def __getitem__(self, index):
        """取向量中的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量的长度 (维度, 有多少个元素)"""
        return len(self._values)

    def __repr__(self):
        """
        告诉系统如何显示Vector, 通常由系统调用
        通常返回的字符串应该表示该对象对应的构造方法应该写成什么样
        """
        return "Vector({})".format(self._values)

    def __str__(self):
        """
        告诉用户如何显示Vector, 通常由用户调用
        返回从用户角度里, 这个对象是什么样子
        """
        return "({})".format(", ".join(str(e) for e in self._values))

    def __add__(self, another):
        """向量加法, 返回结果向量"""
        assert isinstance(another, Vector), \
            "Error in adding. another not a Vector object"
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        # 由于已经实现__iter__, Vector就是可迭代的, 可以直接将对象传入zip中
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法, 返回结果向量"""
        assert isinstance(another, Vector), \
            "Error in subbing. another not a Vector object"
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."
        return Vector([a - b for a, b in zip(self, another)])

    def dot(self, another):
        """向量点乘, 返回结果标量"""
        assert len(self) == len(another), \
            "Error in dot product. Length of vectors must be same."
        return sum([a * b for a, b in zip(self, another)])

    def __mul__(self, k):
        """返回数量乘法的结果向量: self * k"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        """返回数量乘法的结果向量: k * self"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果向量: self / k"""
        return 1 / k * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __iter__(self):
        """返回向量的迭代器"""
        return self._values.__iter__()



