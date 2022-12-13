#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/4 14:54
# @Author  : Feiyang Yu
# @Email   : yufeiyang01.stu.cdut.edu.cn
# @File    : Sort
# @Software: PyCharm
import math
import random
import time


def record_runtime(f):
    def decorator_func(*args, **kwargs):  # 函数默认无返回值
        t0 = time.perf_counter()
        f(*args, **kwargs)
        t1 = time.perf_counter()
        exec_t = t1 - t0
        print(f'Cost time: {exec_t}')

    return decorator_func


def gen_rand_arr(n: int):
    # 传入所需列表长度 返回[0, N)打乱后的正整数序列
    assert n > 1, "生成序列长度应大于1."
    arr = list(range(n))
    random.shuffle(arr)
    return arr


class Sort:
    def __init__(self, array=None):
        assert array is not None, "请传入排序序列."
        self.arr = array
        self.N = len(array)

    @record_runtime
    def bubble_sort(self):
        for i in range(self.N - 1):
            for j in range(self.N - 1 - i):
                # j: 交换变量
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    @record_runtime
    def select_sort(self):
        for i in range(self.N - 1):
            # 每次选出最小的元素
            min_e, min_idx = self.arr[i], i
            for j in range(i, self.N):
                if self.arr[j] < min_e:
                    min_e = self.arr[j]
                    min_idx = j
            self.arr[min_idx], self.arr[i] = self.arr[i], self.arr[min_idx]  # 交换最小元素

    @record_runtime
    def insert_sort(self):
        if self.N <= 1:
            pass
        else:
            for i in range(1, self.N):
                tmp = self.arr[i]
                # 查找
                j = i - 1
                while j >= 0:
                    if self.arr[j] > tmp:
                        self.arr[j + 1] = self.arr[j]
                    else:
                        break
                    j -= 1
                self.arr[j + 1] = tmp

    @record_runtime
    def shell_sort(self):
        gap = self.N
        while gap > 1:
            gap //= 2
            for i in range(self.N - gap):
                end = i
                x = self.arr[end + gap]
                while end >= 0:
                    if self.arr[end] > x:
                        self.arr[end + gap] = self.arr[end]
                        end -= gap
                    else:
                        break
                self.arr[end + gap] = x

    @record_runtime
    def merge_sort(self):
        # 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列；
        # 设定两个指针，最初位置分别为两个已经排序序列的起始位置；
        # 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置；
        # 重复步骤 3
        # 直到某一指针达到序列尾；
        # 将另一序列剩下的所有元素直接复制到合并序列尾。
        self.__mergeSort(self.arr)

    def __mergeSort(self, arr: list):
        # Refer: https://www.runoob.com/w3cnote/merge-sort.html
        if len(arr) < 2:
            return arr
        middle = math.floor(len(arr) / 2)  # 折半序列
        left, right = arr[0:middle], arr[middle:]
        return self.__merge(self.__mergeSort(left), self.__mergeSort(right))

    @staticmethod
    def __merge(left, right):
        # Refer: https://www.runoob.com/w3cnote/merge-sort.html
        result = []
        while left and right:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        while left:  # 直接把左边剩下的元素加进去
            result.append(left.pop(0))
        while right:  # 直接把右边剩下的元素加进去
            result.append(right.pop(0))
        return result

    @record_runtime
    def fast_sort(self):
        # 重写方法 避免给定参数
        self.__fast_sort(0, self.N - 1)

    def __fast_sort(self, low: int, high: int):
        # 快速排序
        if low < high:  # 每次递归后要检查一次 否则循环不及时跳出
            mid = self.__part(low, high)
            self.__fast_sort(low, mid - 1)
            self.__fast_sort(mid + 1, high)

    def __part(self, low, high):
        pivot = self.arr[low]  # 选定基准
        # 双指针移动
        i, j = low, high
        while i < j:
            # 子情况的讨论要加上i < j否则循环不及时跳出，会i>j
            while i < j and self.arr[j] > pivot:
                j -= 1
            self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
            if i < j:  # 每次交换后要检查一次 否则循环不及时跳出
                i += 1
            while i < j and self.arr[i] < pivot:
                i += 1
            self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
            if i < j:  # 每次交换后要检查一次 否则循环不及时跳出
                j -= 1
        return i


s = Sort(gen_rand_arr(22))
# s.fast_sort()
# s.bubble_sort()
# s.select_sort()
# s.insert_sort()
# s.merge_sort()
print(s.arr)
