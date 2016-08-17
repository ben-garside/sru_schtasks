# sru_schtasks
SRU package for Windows Scheduled Tasks. Requires `schtasks_shim` 

## Query
> http[s]://[host]/schtasks/query

Provides functionality to query Scheduled Tasks

### get_all
Returns all Scheduled tasks on machine.


    {
        "action": "get_all"
    }

### get_by_name
Returns a Scheduled Task based on the name provided, use the parial flag to do a partial match.

    {
        "action": "end_by_name",
        "action_params": {
            "name": "\\Microsoft\\Windows\\WindowsBackup\\ConfigNotification"
        }
    }

### get_by_status
Returns all Scheduled Tasks that have the state provided in the request.

    {
        "action": "get_by_status",
        "action_params": {
            "status": "ready"
        }
    }

## Control
> http[s]://[host]/schtasks/control

Provides functionality to control Scheduled Tasks

### run_by_name
Runs the Scheduled Task with provided name.

    {
        "action": "run_by_name",
        "action_params": {
            "name": "\\Microsoft\\Windows\\WindowsBackup\\ConfigNotification"
        }
    }

### end_by_name
Ends the Scheduled Task with provided name.

    {
        "action": "end_by_name",
        "action_params": {
            "name": "\\Microsoft\\Windows\\WindowsBackup\\ConfigNotification"
        }
    }

## Edit
> http[s]://[host]/schtasks/Edit

Provides functionality to create, remove and edit Scheduled Tasks

TODO :) 