# gdb

Automate with gdb

- GDB Server:
```
gdbserver <host>:<port> test $(pidof test)
```
- GDB Client:
``` 
  gdb -x test.py
```
