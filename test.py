import os
import sys
import json
import time
import datetime

LOG_FILE=str(datetime.datetime.now())+'_gdb.log'
HOST='192.168.0.11:2345'

list_tc =  [
    {"id":"TC001", "is_done":"YES", "break_point":"test.c:7", "val":"a", "expect_result":"1"},
    {"id":"TC002", "is_done":"YES", "break_point":"test.c:7", "val":"a", "expect_result":"2"},
    {"id":"TC003", "is_done":"YES", "break_point":"test.c:7", "val":"a", "expect_result":"3"}
]

cnt = 0

def setup():
    print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print ("@                                                         @")
    print ("@                            GDB                          @")
    print ("@                                                         @")
    print ("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    gdb.execute('set pagination off')
    gdb.execute('set print pretty')
    gdb.execute('target remote %s'%(HOST))
    # sleep(10)
    gdb.execute('set logging file %s'%("./logs/"+LOG_FILE))
    gdb.execute('set logging on')
    print('\nReading gdb env..\n')
    gdb.execute('show script-extension')
    gdb.execute('show sysroot')
    gdb.execute('show solib-search-path')
    print('\nSetup complete !!\n')

def add_breakpoint(func):
    gdb.execute('delete')
    gdb.execute('break %s'%(func))

def run():
    gdb.execute('continue')

def exit():
    print("=========================DONE=============================")
    gdb.execute('quit')

def handler(event):
    val = gdb.parse_and_eval (list_tc[cnt]["val"])
    if(val == (int(list_tc[cnt]["expect_result"]))):
        print('Test '+ list_tc[cnt]["id"] + ': PASS')
    else:
        print('Test '+ list_tc[cnt]["id"] + ': Fail!')

def register_handler():
    gdb.events.stop.connect(handler)

def unregister_handler():
    gdb.events.stop.disconnect(handler)

def clear_breakpoint():
    gdb.execute('d')

def run_test():
    global cnt
    for tc in list_tc:
	add_breakpoint(tc["break_point"])
        run()
	cnt=cnt+1

def main():
    setup()
    register_handler()   
    
    run_test()
    
    unregister_handler()
    exit()

main()
