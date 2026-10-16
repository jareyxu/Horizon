# Horizon VPS operations

The VPS runs `horizon.timer` daily at **07:00 Asia/Shanghai**. The server itself
can keep UTC. The `horizon` account owns `/opt/horizon/app` (main checkout),
`/opt/horizon/pages` (gh-pages checkout), and `/opt/horizon/state`.

Credentials live in `/etc/horizon/horizon.env`, owned by root with mode 600:
`SILICONFLOW_API_KEY` and `RAPIDAPI_KEY`. Never commit this file. A dedicated
repository deploy key provides Git access. GitHub API calls can run without a
token, subject to the unauthenticated rate limit.

Run these commands as root:

```sh
systemctl list-timers horizon.timer
systemctl start horizon.service
journalctl -u horizon.service -n 100 --no-pager
systemctl show horizon.service -p Result -p ActiveState
```

The runner locks concurrent runs and skips a date already successfully pushed.
Failures retry once after five minutes, with a one-hour timeout per attempt.
Public source failures may be tolerated by the application; inspect the log
for missing sources even when the service succeeds. Journal retention follows
the server's existing journald policy.

Update code by running the service: it pulls main with `--ff-only` and syncs
locked dependencies. If service/timer definitions change, install them from
`deploy/` into `/etc/systemd/system/`, then run `systemctl daemon-reload`.

To stop server scheduling:

```sh
systemctl disable --now horizon.timer
```

For disaster recovery, manually dispatch `Daily Horizon Summary` in GitHub
Actions. Reintroduce its schedule only after disabling the VPS timer to avoid
duplicate daily runs. Existing reports remain on gh-pages.
