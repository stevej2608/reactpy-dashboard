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
- [ ] Add table CRUD operations (inc multi-record delete)
- [ ] Work out how to access client-side storage
- [ ] Stop the crazy python stack dump when the a user leaves the site.
- [ ] Figure out why my pytest tests need *@pytest.mark.anyio* but the ReactPy pytest tests don't

## Testing

    playwright install

    pytest

    pytest --headed


## Tailwind CSS

During development [tailwindcss play] is used. Tailwind play generates CSS rules
on the fly. They are accumulated, as pages are visited,  into a custom 
style tag. This process a fast and seamless. 

You can, if neccecery, create a static CSS file containing all the 
accumulated rules. To do this you need to copy the content of the tailwind play 
style tag from a live browser session and dump it to file. 

Chrome debug tools are used to dump the style tag to the file:

        ./static/css/tailwind-3.3.5.css

## Links

* [reactpy-crud]


[tailwindcss play]: https://tailwindcss.com/docs/installation/play-cdn
[reactpy-crud]: https://github.com/fazt/reactpy-crud
[reactpy-router@jonesst2608]: https://github.com/stevej2608/reactpy-router
[reactpy]: https://github.com/reactive-python/reactpy
[reactpy-router]: https://github.com/reactive-python/reactpy-router
[tailwind-dashboard-windster]: https://demo.themesberg.com/windster/
 

