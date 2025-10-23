import argparse
import json
from datetime import datetime
fil = "tasks.json"
def load():
    with open(fil, "r") as f:
        return json.load(f)
def save(tasks):
    with open(fil, "w") as f:
        json.dump(tasks,f)
def findt(tasks,id):
    for t in tasks:
        if(t["id"]==id):
            return t
def findid(tasks):
    if(not tasks):
        return 1
    return max(t["id"] for t in tasks)+1
def add(desc):
    tasks=load()
    id = findid(tasks)
    tmp={"id":id,
         "desc":desc,
         "status":"todo",
         "created_at":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    tasks.append(tmp)
    save(tasks)
    print("Task",id,"added successfully")
def update(id,desc):
    tasks=load()
    t=findt(tasks,id)
    if(t==None):
        print("Task",id,"not found")
        return
    t["desc"]=desc
    save(tasks)
    print("Task",id,"updated successfully")
def delete(id):
    tasks=load()
    t=findt(tasks,id)
    if(t==None):
        print("Task",id,"not found")
        return
    tasks.remove(t)
    save(tasks)
    print("Task",id,"deleted successfully")
def mark(id,status):
    tasks=load()
    t=findt(tasks,id)
    if(t==None):
        print("Task",id,"not found")
        return
    t["status"]=status
    save(tasks)
    print("Task",id,"marked as",status)
def list(status):
    tasks=load()
    for t in tasks:
        if(t["status"]==status):
            print(t)

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    parser_add = subparsers.add_parser("add")
    parser_add.add_argument("desc")

    parser_update = subparsers.add_parser("update")
    parser_update.add_argument("id",type=int)
    parser_update.add_argument("desc")

    parser_delete = subparsers.add_parser("delete")
    parser_delete.add_argument("id",type=int)

    parser_mark = subparsers.add_parser("mark")
    parser_mark.add_argument("id",type=int)
    
    parser_mark.add_argument("status")

    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("status")

    args = parser.parse_args()
    if args.command=="add":
        add(args.desc)
    elif args.command=="update":
        update(args.id,args.desc)
    elif args.command=="delete":
        delete(args.id)
    elif args.command=="mark":
        mark(args.id,args.status)
    elif args.command=="list":
        list(args.status)

if __name__ == "__main__":
    main()