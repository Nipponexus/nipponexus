#!/usr/bin/env python3
"""NAMECHECK_v1: py_compile が拾えない未定義グローバル参照を実行前に検出する。"""
import sys,ast,builtins
def undefined_globals(path):
    tree=ast.parse(open(path,encoding="utf-8").read())
    top=set(dir(builtins))|{"__file__","__name__","__doc__"}
    def harvest(node,into):
        for x in ast.walk(node):
            if isinstance(x,ast.Import):
                for a in x.names: into.add((a.asname or a.name).split(".")[0])
            elif isinstance(x,ast.ImportFrom):
                for a in x.names: into.add(a.asname or a.name)
            elif isinstance(x,ast.Name) and isinstance(x.ctx,ast.Store): into.add(x.id)
            elif isinstance(x,ast.ExceptHandler) and x.name: into.add(x.name)
            elif isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef,ast.ClassDef)): into.add(x.name)
            elif isinstance(x,ast.arg): into.add(x.arg)
    harvest(tree,top)
    bad=[]
    for fn in [n for n in ast.walk(tree) if isinstance(n,(ast.FunctionDef,ast.AsyncFunctionDef))]:
        loc=set(); harvest(fn,loc)
        for x in ast.walk(fn):
            if isinstance(x,ast.Name) and isinstance(x.ctx,ast.Load) and x.id not in loc and x.id not in top:
                bad.append((fn.name,x.lineno,x.id))
    return sorted(set(bad))
if __name__=="__main__":
    rc=0
    for p in sys.argv[1:]:
        for f,l,n in undefined_globals(p):
            print("NAMECHECK %s:%d in %s(): 未定義参照 %s"%(p,l,f,n)); rc=1
        print("NAMECHECK %s: %s"%(p,"NG" if rc else "OK"))
    sys.exit(rc)
