"""
Using a fake robot as the receiver of messages.
"""

# TODO: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# TODO: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.


def main():
    import tkinter
    from tkinter import ttk
    import mqtt_remote_method_calls as com
    import time
    root=tkinter.Tk()
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")
    frame1=ttk.Frame(root,padding=10)
    frame1.grid()


    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)

    go_forward_button=ttk.Button(frame1,text='Forward')
    go_forward_button.grid()
    go_forward_button['command']=(lambda: blyat(entry_box,mqtt_client,entry_box2,entry_box3))

    frame2=ttk.Frame(root,padding=10)
    frame2.grid()

    entry_box=ttk.Entry(frame1)
    entry_box.grid()

    entry_box2=ttk.Entry(frame2)
    entry_box2.grid()

    entry_box3=ttk.Entry(frame1)
    entry_box3.grid()


    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    root.mainloop()

def blyat(entry_box,mqtt_client,entry_box2,entry_box3):
    entry_box3=entry_box3.get()
    entry_box=entry_box.get()
    entry_box2=entry_box2.get()

    s=entry_box
    mqtt_client.send_message('forwardprint', [s,entry_box2,entry_box3])




# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()