# Tb blog Refresher

`selenium` == `4.5.0`
`ChromeDriver` == `107.0.5304.62`

To use bot, set `driverLocation` with a driver file location.
Detailed information about Chrome Driver is in [here](https://sites.google.com/chromium.org/driver/)

## Removing all Reblogs

First, change `mail`, `password` and `blogName` in rb_remover.py file.
If you want to use UltraSurf to access Tumblr, change `vpn` value with `True`

```batch
python3 rb_remover.py
```

## Removing all likes

First, change `mail` and `password` in like_remover.py file.
If you want to use UltraSurf to access Tumblr, change `vpn` value with `True`

```batch
python3 like_remover.py
```
