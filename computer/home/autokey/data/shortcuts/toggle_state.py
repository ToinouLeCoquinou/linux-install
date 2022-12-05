# Enter script code
print("0-state:", store.get_global_value("state"))

output = ""
if store.get_global_value("state") == 1:
    store.set_global_value("state", 0)
    output = system.exec_command("polybar-msg action autokey hook 1", getOutput=True)
elif store.get_global_value("state") == 0:
    store.set_global_value("state", 1)
    output = system.exec_command("polybar-msg action autokey hook 0", getOutput=True)

print(output)
print("1-state:", store.get_global_value("state"))
