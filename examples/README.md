# Minimal Django Example

This example project has a `/hello/` endpoint and the code modifier UI. It is
intended for local development and does not include production security
settings.

## Run the Example

From this directory, create and activate a virtual environment and install
Django:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install "Django>=5.2"
```

Start the server from the `examples` directory. The `PYTHONPATH` entry makes
the package source in the repository root importable:

```bash
PYTHONPATH=.. python manage.py runserver 127.0.0.1:8000 --noreload
```

Open the sample endpoint to see the original response:

[http://127.0.0.1:8000/hello/](http://127.0.0.1:8000/hello/)

Open the code modifier to edit the `hello` view:

[http://127.0.0.1:8000/code_modifier/code_mod/](http://127.0.0.1:8000/code_modifier/code_mod/)

Select `example_app` and `hello`, then submit a replacement function body,
for example:

```python
def replacement(request):
    from django.http import JsonResponse
    return JsonResponse({"message": "Hello after the change!"})
```

Reload `/hello/` to see the updated response. The runserver command uses
`--noreload`; the view update happens in the running process.
