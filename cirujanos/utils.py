import pdb


def debugger(func):
    def debugger_wrapper(*args, **kwargs):
        pdb.set_trace()
        func(*args, **kwargs)
    return debugger_wrapper
