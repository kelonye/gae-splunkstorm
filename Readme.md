Install
---

copy `lib/__init__.py` to your project, ideally, as `splunk.py`.

Use
---

Add `deferred` to your app.yaml `builtins:`

```yaml
builtins:
- deferred: on
```
Use logger

```python

from splunk import Log

YOUR_SPLUNK_ACCESS_TOKEN = '--'
YOUR_SPLUNK_PROJECT_ID = '--'

syslogger = Log(SPLUNK_ACCESS_TOKEN, SPLUNK_PROJECT_ID).send

class SomeHandler(webapp.RequestHandler):

    def get(self):

        # queue job to log event to splunkstorm.

        log = {
            'event': 'visit',
            'path': '/'
        }
        deferred.defer(syslogger, log)

```

Test
---

    $ make deps test