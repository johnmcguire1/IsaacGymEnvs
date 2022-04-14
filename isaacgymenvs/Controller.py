import os
import threading
import time
import torch
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from os.path import exists

status = "go"

def instanceOne():
    os.system('python train.py task=Ant headless=True rl_device=cuda:0 sim_device=cuda:0')


def instanceTwo():
    os.system('python train.py task=Ant headless=True rl_device=cuda:1 sim_device=cuda:1')

def instanceThree():
    os.system('python train.py task=Ant headless=True rl_device=cuda:2 sim_device=cuda:2')

def instanceFour():
    os.system('python train.py task=Ant headless=True rl_device=cuda:3 sim_device=cuda:3')

def combineNN(path1, path2):
    if exists(path1) and exists(path2):
        nn0 = torch.load(path1)
        nn1 = torch.load(path2)
    
        for key in nn1['model'].keys():

            nn0['model'][key] = (nn0['model'][key] + nn1['model'][key]) / 2
            nn1['model'][key] = (nn0['model'][key] + nn1['model'][key]) / 2
        
        status = "saving models"
        torch.save(nn0, path1)
        torch.save(nn1, path2)
        time.sleep(2)
        status = "go"

def on_created(event):
    print("CREATED")

def on_modified_nn0(event):
    if status == "go":
        print("FILE MODIFIED IN RUNS/CARTPOLE/NN0!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        combineNN("runs/Cartpole/nn0/Cartpole.pth", "runs/Cartpole/nn1/Cartpole.pth")
    else:
        print(status)

def on_modified_nn1(event):
    if status == "go":
        print("FILE MODIFIED IN RUNS/CARTPOLE/NN1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        combineNN("runs/Cartpole/nn0/Cartpole.pth", "runs/Cartpole/nn1/Cartpole.pth")
    else:
        print(status)

def watchFoldernn0():
    time.sleep(5)
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    #my_event_handler.on_created = on_created
    #my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified_nn0
    #my_event_handler.on_moved = on_moved_nn0

    path = "runs/Humanoid/nn0/"
    nn0_observer = Observer()
    nn0_observer.schedule(my_event_handler, path)

    nn0_observer.start()
    count = 0
    while count < 50000:
        time.sleep(0.1)
        count += 1
    nn0_observer.stop()
    nn0_observer.join()

def watchFoldernn1():
    time.sleep(5)
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    #my_event_handler.on_created = on_created
    #my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified_nn1
    #my_event_handler.on_moved = on_moved_nn1

    path = "runs/Humanoid/nn1/"
    nn1_observer = Observer()
    nn1_observer.schedule(my_event_handler, path)

    nn1_observer.start()
    count = 0
    while count < 50000:
        time.sleep(0.1)
        count += 1
    nn1_observer.stop()
    nn1_observer.join()

thread1 = threading.Thread(target=instanceOne)
thread2 = threading.Thread(target=instanceTwo)
thread3 = threading.Thread(target=instanceThree)
thread4 = threading.Thread(target=instanceFour)



#thread3.start()
#thread4.start()
#thread4.start()
thread3.start()
thread2.start()
thread1.start()
