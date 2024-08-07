try:
    s = "abcd" * 2**62
    # TODO 2**30 if size_t is 32-bit
except OverflowError:
    pass
except MemoryError:
    pass

try:
    s = [1, 2] * 2**62
    # TODO 2**30 if size_t is 32-bit
except OverflowError:
    pass
except MemoryError:
    pass
