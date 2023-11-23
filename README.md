## reactpy-dashboard

![](https://www.admin-dashboards.com/content/images/size/w2000/2021/11/windster-tailwind-css-dashboard.jpg)

This project is a port of the Themesberg [tailwind-dashboard-windster] project to [reactpy].

    poetry install  --no-root

    uvicorn fast_app:app --host "0.0.0.0" --port 8000

    python usage.py runserver --host "0.0.0.0" --port 8000


### reactpy-router

This project uses a custom version of [reactpy-router@jonesst2608]. It's been built locally
and uploaded to pypicloud. To install it:

        poetry source add --priority=supplemental pypicloud http://debian-server:6543/simple/
        poetry config http-basic.pypicloud jonesst2608@gmail.com passme99
        
        poetry add --source pypicloud reactpy-router

### DONE/TODO

- [X] Fix composite icons
- [ ] Create a modulat forms solution
- [ ] Work out how to access client-side storage
- [ ] Stop the crazy python stack dump when the a user leaves the site.
- [ ] Figure out why my pytest tests need *@pytest.mark.anyio* but the pytest tests don't

## Testing

    playwright install

    pytest

    pytest --headed


## Links

* [reactpy-crud]


[reactpy-crud]: https://github.com/fazt/reactpy-crud
[reactpy-router@jonesst2608]: https://github.com/stevej2608/reactpy-router
[reactpy]: https://github.com/reactive-python/reactpy
[reactpy-router]: https://github.com/reactive-python/reactpy-router
[tailwind-dashboard-windster]: https://demo.themesberg.com/windster/
 

