
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '12424A11741F115318FE86A7FFB4A9A9'
    
_lr_action_items = {'LSQBRACKET':([0,1,2,6,7,8,9,11,12,13,14,15,16,17,18,19,],[1,1,-7,1,-5,-8,-6,-10,-14,1,-9,-12,1,-11,-15,-13,]),'LPAREN':([0,1,2,6,7,8,9,11,12,13,14,15,16,17,18,19,],[6,6,-7,6,-5,-8,-6,-10,-14,6,-9,-12,6,-11,-15,-13,]),'STRING':([0,1,2,6,7,8,9,11,12,13,14,15,16,17,18,19,],[2,2,-7,2,-5,-8,-6,-10,-14,2,-9,-12,2,-11,-15,-13,]),'$end':([0,2,3,4,5,7,8,9,10,12,15,18,19,],[-4,-7,-1,-2,-3,-5,-8,-6,0,-14,-12,-15,-13,]),'NUMBER':([0,1,2,6,7,8,9,11,12,13,14,15,16,17,18,19,],[8,8,-7,8,-5,-8,-6,-10,-14,8,-9,-12,8,-11,-15,-13,]),'RPAREN':([2,6,7,8,9,11,12,14,15,16,17,18,19,],[-7,15,-5,-8,-6,-10,-14,-9,-12,19,-11,-15,-13,]),'RSQBRACKET':([1,2,7,8,9,11,12,13,14,15,17,18,19,],[12,-7,-5,-8,-6,-10,-14,18,-9,-12,-11,-15,-13,]),'SYMBOL':([0,1,2,6,7,8,9,11,12,13,14,15,16,17,18,19,],[7,7,-7,7,-5,-8,-6,-10,-14,7,-9,-12,7,-11,-15,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'exprs':([1,6,],[13,16,]),'atom':([0,1,6,13,16,],[3,11,11,17,17,]),'symbol':([0,1,6,13,16,],[9,9,9,9,9,]),'empty':([0,],[4,]),'toplevel':([0,],[10,]),'list':([0,1,6,13,16,],[5,14,14,14,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> toplevel","S'",1,None,None,None),
  ('toplevel -> atom','toplevel',1,'p_toplevel','parser.py',7),
  ('toplevel -> empty','toplevel',1,'p_toplevel','parser.py',8),
  ('toplevel -> list','toplevel',1,'p_toplevel','parser.py',9),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',14),
  ('symbol -> SYMBOL','symbol',1,'p_symbol','parser.py',19),
  ('atom -> symbol','atom',1,'p_atom','parser.py',29),
  ('atom -> STRING','atom',1,'p_atom','parser.py',30),
  ('atom -> NUMBER','atom',1,'p_atom','parser.py',31),
  ('atom -> list','atom',1,'p_atom','parser.py',32),
  ('exprs -> atom','exprs',1,'p_exprs_1','parser.py',37),
  ('exprs -> exprs atom','exprs',2,'p_exprs_2','parser.py',44),
  ('list -> LPAREN RPAREN','list',2,'p_list_0','parser.py',51),
  ('list -> LPAREN exprs RPAREN','list',3,'p_list_1','parser.py',56),
  ('list -> LSQBRACKET RSQBRACKET','list',2,'p_list_2','parser.py',61),
  ('list -> LSQBRACKET exprs RSQBRACKET','list',3,'p_list_3','parser.py',66),
]
