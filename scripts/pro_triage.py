# -*- coding: utf-8 -*-
"""pro_triage: Proの『確認不可』をフィールド条件付きで仕分ける(還元V)。
由緒/固有史の細部は従来どおり降格(過剰否定11例の実績)。
権威属性(主催/共催/後援/問い合わせ/正式名称/指定名称)に触れるものは
DeepSeekが定型を流し込む領域のため『必須一次照合』へ格上げする。"""
import re
AUTH_KEYS = ['主催','共催','後援','主管','問い合わせ','問合せ','連絡先','正式名称','指定名称','運営主体','事務局']
def triage(items):
    """items=Proの確認不可テキストのリスト。戻り値 (escalate, downgrade)"""
    esc, dwn = [], []
    for t in items:
        (esc if any(k in t for k in AUTH_KEYS) else dwn).append(t)
    return esc, dwn
def field_of(t):
    for k in AUTH_KEYS:
        if k in t: return 'authority'
    return 'lore'
