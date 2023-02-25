from . import cp
import os

def readfile_progress_bar(stdscr,path: str) -> bytes:
    stdscr.clear()
    p = cp.ProgressBar(stdscr,os.path.getsize(path),message="Reading file "+path)
    data = b""
    with open(path,"rb") as f:
        lx = 0
        for line in f:
            data += line
            p.value += len(line)-2
            p.step(f"Read {len(data)} bytes")
            lx += 1
            
    #p.done()
    return data

def writefile_progress_bar(stdscr,path: str,data: bytes):
    
    p = cp.ProgressBar(stdscr,len(data)+1,message="Writing File "+path)
    p.step()
    writedata: list[bytes] = data.splitlines()
    with open(path,"wb+") as f:
        for line in writedata:
            p.value += len(line)-2
            p.step(f"Writing {len(data)} bytes")
            f.write(line)
            f.write(b"\n")
    #p.done()
"""
def copyfile_progress_bar(stdscr,src: str,dest:str) -> None:
    p = cp.ProgressBar(stdcrr)
"""