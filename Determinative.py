from pypresence import Presence
import time

rpc = Presence("1131127607719628830")
rpc.connect()
while 1:
    rpc.update(
        state="Questioning existence",
        details="Fighting with void",
        large_image="penguin-1",
    )
    time.sleep(1)
