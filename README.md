## reactpy-dashboard

![](https://www.admin-dashboards.com/content/images/size/w2000/2021/11/windster-tailwind-css-dashboard.jpg)

This project is a port of the Themesberg [tailwind-dashboard-windster] project to [reactpy].

    poetry install  --no-root

    uvicorn fast_app:app --port 8000

    python usage.py runserver --port 8000

### DONE/TODO

- [X] Tailwind CSS
- [X] Fix composite icons
- [X] Create a modular forms solution
- [X] Add table pagination
- [X] Add table search
- [X] Add gitHub Stars Button
- [ ] Work out how to access client-side storage
- [ ] Stop the crazy python stack dump when the a user leaves the site.
- [ ] Figure out why my pytest tests need *@pytest.mark.anyio* but the ReactPy pytest tests don't

## Testing

    playwright install

    pytest

    pytest --headed


## reactpy_table

* [use_reactpy_table](tmp/table/examples/react/pagination/src/main.tsx#L110)
        [useReactTable](tmp/table/packages/react-table/src/index.tsx#L57)


## Tailwind CSS

During development [tailwindcss play] is used. 

To get a static css file containing all the CSS active rules, you need to copy
the tailwind play generated style tag from a live browser session and 
dump it into a file. See *static\css\tailwind-3.3.5.css*. This file will 
contain the accumulated CSS rules for every page visited.

## Links

* [reactpy-crud]


[tailwindcss play]: https://tailwindcss.com/docs/installation/play-cdn
[reactpy-crud]: https://github.com/fazt/reactpy-crud
[reactpy-router@jonesst2608]: https://github.com/stevej2608/reactpy-router
[reactpy]: https://github.com/reactive-python/reactpy
[reactpy-router]: https://github.com/reactive-python/reactpy-router
[tailwind-dashboard-windster]: https://demo.themesberg.com/windster/
 

