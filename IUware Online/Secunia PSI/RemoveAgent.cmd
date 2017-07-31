@echo off
Echo Attempting to stop agent service
SC stop "Secunia CSI Agent">null
Echo Attempting to remove agent service
SC delete "Secunia CSI Agent">null
Echo Waiting for 60 seconds for remove operation to complete...
Timeout /T 60>null
