import time
import copy

n = int(input("N="))
l = []
f = open("randomized.txt", 'r')
for x in f:
    l.append(int(x.strip()))
l = l[0:n]


def BubbleSort(l, n):
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]


def CountSort(l):
    frecv = [0] * (max(l) + 1)
    m = []
    for i in l:
        frecv[i] = frecv[i] + 1
    k = 0
    for i in range(max(l) + 1):
        if frecv[i] > 0:
            for j in range(frecv[i]):
                m.append(i)
    l = copy.deepcopy(m)
    return l


def MergeSort(l):
    if len(l) > 1:
        mij = len(l) // 2
        S = l[:mij]
        D = l[mij:]

        MergeSort(S)
        MergeSort(D)

        i = j = k = 0
        while i < len(S) and j < len(D):
            if S[i] < D[j]:
                l[k] = S[i]
                i = i + 1
                k = k + 1
            else:
                l[k] = D[j]
                j = j + 1
                k = k + 1

        while i < len(S):
            l[k] = S[i]
            i = i + 1
            k = k + 1
        while j < len(D):
            l[k] = D[j]
            j = j + 1
            k = k + 1


def QuickSort(l):
    if len(l) < 2:
        return l

    poz = 0

    for i in range(1, len(l)):
        if l[i] <= l[0]:
            poz = poz + 1
            l[i], l[poz] = l[poz], l[i]

    l[0], l[poz] = l[poz], l[0]

    St = QuickSort(l[0: poz])
    Dr = QuickSort(l[poz + 1: len(l)])

    l = St + [l[poz]] + Dr

    return l


def LSD(l, imp):
    v = [0] * len(l)
    c = [0] * 10

    for i in range(0, len(l)):
        x = l[i] // imp
        c[x % 10] = c[x % 10] + 1

    for i in range(1, 10):
        c[i] = c[i] + c[i - 1]

    i = len(l) - 1
    while i >= 0:
        x = l[i] // imp
        v[c[x % 10] - 1] = l[i]
        c[x % 10] = c[x % 10] - 1
        i = i - 1
    for i in range(len(l)):
        l[i] = v[i]


def RadixSort(l):
    el_max = max(l)

    im = 1

    while el_max // im > 0:
        LSD(l, im)
        im = im * 10


copie = copy.deepcopy(l)
start = time.time()
BubbleSort(copie, n)
stop = time.time()
print("BubbleSort timp executie:", stop - start, 'secunde.')
if (copie == sorted(copie)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")

copie = copy.deepcopy(l)
start = time.time()
copie = CountSort(copie)
stop = time.time()
print("CountSort timp executie:", stop - start, 'secunde.')
if (copie == sorted(copie)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")

copie = copy.deepcopy(l)
start = time.time()
MergeSort(copie)
stop = time.time()
print("MergeSort timp executie:", stop - start, 'secunde.')
if (copie == sorted(copie)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")

copie = copy.deepcopy(l)
start = time.time()
copie = QuickSort(copie)
stop = time.time()
print("QuickSort timp executie:", stop - start, 'secunde.')
if (copie == sorted(copie)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")

copie = copy.deepcopy(l)
start = time.time()
RadixSort(copie)
stop = time.time()
print("RadixSort timp executie:", stop - start, 'secunde.')
if (copie == sorted(copie)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")

start = time.time()
l.sort()
stop = time.time()
print("Algoritm nativ timp executie:", stop - start, 'secunde.')
if (l == sorted(l)):
    print("Sortat corect.")
else:
    print("Sortat gresit.")
