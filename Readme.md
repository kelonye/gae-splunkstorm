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

import splunk

splunk.access_token = ''
splunk.project_id = ''

class SomeHandler(webapp.RequestHandler):

    def get(self):

        # queue job to log event to splunkstorm.

        event = {
            'event': 'visit',
            'path': '/'
        }
        deferred.defer(splunk.log, event)

```

Test
---

    $ make deps test