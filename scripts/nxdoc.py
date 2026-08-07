# -*- coding: utf-8 -*-
"""文書追記は insert_once だけを使う。冪等性の鍵はブロック全文でなく短い一意キー。"""
import os, shutil, datetime
def has_key(path, key):
    return open(path,encoding='utf-8').read().count(key)
def insert_once(path, key, block, anchor=None, backup=True):
    src=open(path,encoding='utf-8').read()
    if key in src:
        return {'skipped':True,'reason':'key exists','count':src.count(key)}
    if backup:
        bk=os.path.join(os.path.dirname(os.path.abspath(__file__)),'_backup'); os.makedirs(bk,exist_ok=True)
        shutil.copy2(path, os.path.join(bk, os.path.basename(path)+'.'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S')))
    if not block.endswith('\n'): block+='\n'
    if anchor is None:
        new=src+('\n' if not src.endswith('\n') else '')+block
    else:
        if src.count(anchor)!=1:
            raise ValueError('anchor count=%d (must be 1): %r'%(src.count(anchor),anchor[:40]))
        new=src.replace(anchor, block+'\n'+anchor, 1)
    open(path,'w',encoding='utf-8').write(new)
    chk=open(path,encoding='utf-8').read()
    if chk.count(key)!=1: raise AssertionError('key count=%d after insert'%chk.count(key))
    for ln in src.split('\n'):
        if ln.strip() and ln not in chk: raise AssertionError('original line lost: %r'%ln[:40])
    return {'inserted':len(block),'key_count':1,'bytes':len(chk)}
