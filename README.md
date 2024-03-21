Consider the following C code:

```
void h(void) {}

void f(void) { h(); }

void g(void) { h(); }

int main() {
  f();
  g();
  return 0;
}
```

Compiling this and running it via `gdb`, one can set a breakpoint at h and inspect the traces:

```
$ cd /tmp
$ cat > foo.c
<paste code and CTRL+D>
$ gcc foo.c
$ gdb a.out
[...]
(gdb) break h
Breakpoint 1 at 0x112d
(gdb) r
Starting program: /tmp/a.out
[...]
(gdb) bt
#0  0x000055555555512d in h ()
#1  0x0000555555555139 in f ()
#2  0x0000555555555151 in main ()
(gdb) c
Continuing.

Breakpoint 1, 0x000055555555512d in h ()
(gdb) bt
#0  0x000055555555512d in h ()
#1  0x0000555555555145 in g ()
#2  0x0000555555555156 in main ()
(gdb) c
Continuing.
[Inferior 1 (process 22530) exited normally]
```

Now one can run gdb_trace_viz and build a graph out of that:

```
$ python gdb_trace_viz.py
#0  0x000055555555512d in h ()
#1  0x0000555555555139 in f ()
#2  0x0000555555555151 in main ()
BREAK
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
#0  0x000055555555512d in h ()
#1  0x0000555555555145 in g ()
#2  0x0000555555555156 in main ()
BREAK
```

The resulting graph looks like this:

![backtrace](https://github.com/smanilov/gdb-trace-viz/assets/1367673/50a3c1da-ea19-48eb-b1f5-c81c9c1ec410)

And here's the graph for long_input.txt:

```
$ cat long_input.txt | python gdb_trace_viz.py
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
Backtrace saved as DOT: backtrace.dot
Backtrace converted to PNG: backtrace.png
```

![backtrace](https://github.com/smanilov/gdb-trace-viz/assets/1367673/05169995-fa23-4bc1-bc60-99bc6081092b)

The purpose of this tool is to selectively visualize sub-graphs of the complete call-graph of an execution of a program.
