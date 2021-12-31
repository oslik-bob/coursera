# =============================================================================
# import sys
# def lest(numb):
#     result=''
#     for i in range(1,(numb+1)):
#         result+=(f"{' '*(numb-i)}{'#'*i}"+('\n' if i<numb else ''))
#     return result
# 
# print(lest(int(sys.argv[1]))) if sys.argv[1].isdigit() else None 
# 
# 
# =============================================================================
# =============================================================================
# import sys
# 
# num_steps = int(sys.argv[1])
# 
# for i in range(num_steps):
#     print(i)
#     print(" " * (num_steps - i - 1), "#" * (i + 1), sep="")
# =============================================================================
# =============================================================================
# import sys 
# def cor (a,b,c,D,dub):
#     if dub:
#         x1=(-b+(D**0.5))/(2*a)
#         x2=(-b-(D**0.5))/(2*a)
#         
#         return f'{int(x1)}\n{int(x2)}'
#     else:
#         x1=(-b+(D**0.5))/(2*a)
#         return int(x1)
#     
# a = int(sys.argv[1]) 
# b = int(sys.argv[2]) 
# c = int(sys.argv[3])
# D=(b**2)-(4*a*c)
# if D>0:
#     print(cor(a,b,c,D,True))
# elif D==0:
#     print(cor(a,b,c,D,False))
# else:
#     print("Корней нет")
#     
# =============================================================================
# =============================================================================
# def files(filename):
#     def logger (fun):
#         def wrap(inner):
#             result='ответ из логгера '+str(fun(inner))
#             
#             print(filename,str(result),sep=r" >> ")
#             print(type(result))
#             print(result)
#             return (result)
#         return wrap
#     return logger
# 
# @files('logger')
# def summary(num_list):
#     return sum(num_list)
# 
# print(f'summary: {summary([1,2,3,5,6])}')
# =============================================================================

# =============================================================================
# def generate(a,b):
#     c=a
#     while c<b:
#         print (c)
#         yield c
#         c+=1
#         print('новая итерация псоле {}'.format(str(c-1)))
# generate(1,5)
# 
# =============================================================================
# =============================================================================
# def akkum():
#     total=0
#     while True:
#         value=yield total
#         print(f'Получил {value}')
#         if not value: break
#         total+=1
# =============================================================================
# =============================================================================
# import sys
# import os
# import tempfile
# =============================================================================
# =============================================================================
# 
# storage_path = os.path.join(tempfile.gettempdir(),'storage.data')
# if "--val" in sys.argv and '--key' in sys.argv:
#     print('key', type(sys.argv))
# =============================================================================
# =============================================================================
# s=['--key', 'dsafas', '--val']
# storage_path = os.path.join(tempfile.gettempdir(),'storage.data')
# def logger(filename):
#     def decorator(func):
#         def wrapped(**kwargs):
#             result = func(key,val)
#             with open(filename, 'a') as f:
#                 f.write(str(result))
#             return result
#         return wrapped
#     return decorator
# 
# 
# #@logger(storage_path)
# 
# def keys(func):
#     def wrapped(**kwargs):
#         
#         return "key" + func(kwargs[0])
#     return wrapped
# 
# 
# def values(func):
#     def wrapped(**kwargs):
#         return 'val' + func(kwargs[1]) 
#     return wrapped
# 
# 
# @keys
# @values
# def summator(s):
#     if "--val" in s and '--key' in s:
#         try:
#             key=s[s.index('--key')+1]
#         except :
#             key='None'
#         try:
#             val=s[s.index('--val')+1]
#         except:
#             val='None'
#         return (key, val) 
# print(summator(s))
# 
# 
# def get_data():
#   return {
#     'data': 42
#   }
#   
# get_data()  
# =============================================================================
# =============================================================================
# import argparse
# import os
# import tempfile
# import json
# 
# 
# 
# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# 
# def logger(filename):
#     def decorator(func):
#         def wrapped(*args):
#             #result
#             with open(filename, 'w') as f:
#                 json.dump(*args, f)
#                 #f.write("".join(func(*args)))
#                 result=None
#                 return result
#         return wrapped
#     return decorator
# 
# 
# @logger(storage_path)
# def insert_data(save):
#     return save
# 
# 
# #s=['--key', 'd', '--val', 'gggggggggg']
# s=argparse.ArgumentParser(description='storage test')
# s.add_argument('--key',dest='key', type=str, help='Key storage')
# s.add_argument('--val',dest='val',type=str, help='Value data')
# args=s.parse_args()
# print(args.key)
# print(args.val)
# if args.key and args.val:
#     dick=dict(zip((args.key,),(args.val,)))
#     try:    
#         with open(storage_path, 'r') as f:
#             lines = dict(json.load(f))
#             print (lines, type(lines))
#             if args.key in lines.keys():
#                 lines.update(zip((args.key,),([lines[args.key],args.val],)))
#                 print (lines,'sdfad')
#             else: lines=dict(zip((args.key,),(args.val,)))
#         insert_data(lines)
#     except:
#         insert_data(dick)
#         #insert_data(('{0} {1}\n'.format(args.key, args.val),))
# elif args.key and args.val is None:
#     
#     try:
#             
#         with open(storage_path, 'r') as f:
#             
#             line = f.readlines()
#             for li in line:
#                 if args.key == li.split(' ')[0]:
#                     print(', '.join(li.split(' ')[1:]))
#     except: None
# 
# =============================================================================
# =============================================================================
# import sys
# import os
# import tempfile
# 
# 
# 
# storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# 
# def logger(filename):
#     def decorator(func):
#         def wrapped(*args):
#             #result
#             with open(filename, 'w') as f:
#                 f.write("".join(func(*args)))
#                 result=None
#                 return result
#         return wrapped
#     return decorator
# 
# 
# @logger(storage_path)
# def insert_data(save):
#     print(save)
#     return save
# 
# 
# #s=['--key', 'd', '--val', 'gggggggggg']
# s=sys.argv[1:]
# if '--key' in s and '--val' in s:
#     key=s[s.index('--key')+1]
#     try:
#         val=s[s.index('--val')+1]
#     except:
#         val=None
#     if val is not None:
#         try:    
#             with open(storage_path, 'r') as f:
#                 lines = f.readlines()
#                 for k, li in enumerate(lines):
#                     if key == li.split(' ')[0]:
#   #                      print('chenge')
#                         lines[k]=('{0} {1}\n'.format(li.rstrip("\n"), val))
#                         break
#                 else:
#  #                   print('ADD',val)
#                     lines.append('{0} {1}\n'.format(key, val))
#             insert_data(lines)
#         except:            
# #            print('{0} {1}\n'.format(key, val))
#             insert_data(('{0} {1}\n'.format(key, val),))
#                    # f.write(line.replace(line, '{} {}\n'.format(line.rstrip("\n"), val)))
#         #insert_data(key, val)
# elif '--key' in s and '--val' not in s:
#     key=s[s.index('--key')+1]
#     with open(storage_path, 'r') as f:
#         
#         line = f.readlines()
#         for li in line:
#             if key == li.split(' ')[0]:
#                  print(', '.join(li.split(' ')[1:]))
# =============================================================================
# =============================================================================
# import json
# import functools
# 
# def to_json(func):
#     @functools.wraps(func)
#     def wrapped (*args, **kwargs):
# # =============================================================================
# #         if len(args) > 0:
# #             return json.dumps(args)
# #         elif len(kwargs) >0:
# #             return json.dumps(kwargs)
# #         else:
# # =============================================================================
#         if isinstance(func(*args, **kwargs), set):
#             return json.dumps({'{0}'.format(list(func(*args, **kwargs)))})
#         else: return json.dumps(func(*args, **kwargs))
# # =============================================================================
# #         elif isinstance(func(), str):
# #             return json.dumps(func())
# #         elif isinstance(func(), float):
# #             return json.dumps(func())
# #         elif isinstance(func(), list):
# #             return json.dumps(func())
# #         elif 
# # =============================================================================
#              
#     return wrapped
#     
# # =============================================================================
# # @to_json
# # def get_data():
# #     return 5*'5'
# # 
# # print(get_data())
# # 
# # =============================================================================
# 
# =============================================================================
