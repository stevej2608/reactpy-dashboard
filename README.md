## reactpy-dashboard

![](https://www.admin-dashboards.com/content/images/size/w2000/2021/11/windster-tailwind-css-dashboard.jpg)

This project is a port of the Themesberg [tailwind-dashboard-windster] project to [reactpy].

    poetry install  --no-root

    uvicorn fast_app:app --port 8000

    python usage.py runserver --port 8000


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


## reactpy_table

* [use_reactpy_table](tmp/table/examples/react/pagination/src/main.tsx#L110)
        [useReactTable](tmp/table/packages/react-table/src/index.tsx#L57)


## Tailwind CSS

During development use [tailwindcss play]. 

To get a static css file containing all the CSS rules you need to copy
the tailwind ;play generated style tag from a live browser session and 
dump it into a file. see *static\css\tailwind-3.3.5.css*. This file will 
contain the accumulated CSS rules for every page visited.


## Links

* [reactpy-crud]


[tailwindcss play]: https://tailwindcss.com/docs/installation/play-cdn
[reactpy-crud]: https://github.com/fazt/reactpy-crud
[reactpy-router@jonesst2608]: https://github.com/stevej2608/reactpy-router
[reactpy]: https://github.com/reactive-python/reactpy
[reactpy-router]: https://github.com/reactive-python/reactpy-router
[tailwind-dashboard-windster]: https://demo.themesberg.com/windster/
 

