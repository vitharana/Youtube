import time

def counter(reset = False):
    if reset:
        counter.count = 0
        return counter.count

    if not hasattr(counter, "count"):
        counter.count = 0
        print("Runs only once")
    counter.count += 1
    return counter.count

while True:
    if counter() <= 100:
        print(counter.count)
    else:
        counter(reset=True)

    time.sleep(0.1)












