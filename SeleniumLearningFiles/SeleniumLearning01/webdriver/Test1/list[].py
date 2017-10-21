def foo(bar=[]):
    bar.append("abc")
    return bar

print(foo())
print(foo())
print("========修改后正确的范式===============")

def ff(bar=None):
    if bar is None:
        bar=[]
    bar.append("def")
    return bar
print(ff())
print(ff())