# Unitrade Troubleshooting

Use this when the user shows an error, failed login, failed order, empty data, or connection problem.

## First Checks

1. Confirm `unitrade` is installed and imported.
2. Confirm `api = Unitrade()` was executed before using `api`.
3. Confirm `api.on_error` is registered before login.
4. Confirm the login URL starts with `http://` or `https://`.
5. Confirm certificate path points to the `.pfx` file visible from the script's working directory.
6. Confirm `login_response.ok` and `api.login_status_flag` before any component call.
7. Confirm account-bound operations use an account returned by `api.get_accounts()`.
8. Check maintenance windows if the error says not connected or if login/order/query fails unexpectedly.

## Login Failures

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `No module named 'unitrade'` | Package not installed | `pip install unitrade` |
| `name 'api' is not defined` | API object not initialized | Run import and `api = Unitrade()` |
| URL must start with `http://` or `https://` | Bad login URL | Use full URL |
| `Connection reset by peer` | Network/server unreachable | Check network, VPN/firewall, server URL |
| `查無資料` | Login account not found | Login account may need branch code plus trading account |
| `輸入資料錯誤` | Password or login fields wrong | Recheck account/password |
| Certificate cannot be found | `.pfx` path or working directory wrong | Use absolute path or place file next to script |
| Certificate info incorrect | Certificate does not match account | Use the certificate for that login account |
| Already logged in | Session already active | Call `api.logout()` before re-login |

## Order Failures

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `不允許操作` | Not logged in or component not connected | Check `api.login_status_flag` and connection events |
| `該帳號不允許操作` | Wrong account format or account not enabled | Use one of `api.get_accounts()`; trading account is usually 7 digits in order examples |
| `尚未連線` | Network, maintenance, or component not connected | Check server status and maintenance windows |
| Certificate invalid/expired | Certificate mismatch or expired | Renew or use correct `.pfx` |

## SDK Error Codes

| Code | Meaning |
| --- | --- |
| `MSG000` | Buy/sell side error. Use `B` or `S`. |
| `MSG001` | Order condition error. Use `R`, `F`, or `I`. |
| `MSG002` | Order type or related flag error. |
| `MSG003` | Day-trade flag error. Use `Y` or `N`. |
| `MSG004` | Format error. |
| `MSG005` | Required field missing. |
| `MSG007` | Order count limit exceeded. |
| `MSG008` | Invalid order number. |
| `MSG009` | Numeric value must be greater than 0. |
| `MSG010` | Single-order quantity limit exceeded. |
| `MSG011` | Call/Put error. Futures use blank or `F`; options use `C` or `P`. |
| `MSG012` | Strike price must be numeric. |
| `MSG013` | Price type error. Use `M`, `L`, `3`, or `4` where supported. |
| `MSG014` | Open/close flag error. Use the values documented for the target market. |
| `MSG015` | Day-trade code error. Use `Y` or `N`. |
| `MSG016` | Not connected. Check network or API connection status. |

## Maintenance Windows

Times are Taiwan time, GMT+8.

| Service | Window |
| --- | --- |
| Login service | Daily 05:30-05:50 |
| Domestic futures trading | Weekdays 07:00-07:27; weekend from Saturday 07:00 to Monday 07:27 |
| Domestic futures quote | Weekdays 07:00-07:20; weekend from Saturday 07:00 to Monday 07:20 |
| Domestic futures account | Daily 06:00-07:30 |
| Foreign futures trading | Weekdays 05:30-05:50; weekend from Saturday 05:30 to Monday 05:50 |
| Foreign futures account | Daily 05:30-05:50 |

Foreign futures maintenance table is summer time. Add one hour in winter time.

## Time Format

API time strings use `HHmmssfff`:

- `HH`: hour in 24-hour format.
- `mm`: minute.
- `ss`: second.
- `fff`: millisecond.

Example: `153901370` means 15:39:01.370 Taiwan time.

## Debug Snippets

Check login and account:

```python
print("login flag:", api.login_status_flag)
print("accounts:", api.get_accounts())
```

Check component server list:

```python
for name in ["dquote", "dtrade", "ftrade", "daccount", "faccount"]:
    component = getattr(api, name)
    print(name, component.get_current_server())
```

Handle spelling differences:

```python
def set_server(component, server_name):
    if hasattr(component, "set_sever_by_name"):
        return component.set_sever_by_name(server_name)
    return component.set_server_by_name(server_name)
```
