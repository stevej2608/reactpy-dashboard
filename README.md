## reactpy-dashboard

![](https://www.admin-dashboards.com/content/images/size/w2000/2021/11/windster-tailwind-css-dashboard.jpg)

This project is a port of the Themesberg [tailwind-dashboard-windster] project to [reactpy].


    poetry install  --no-root

    uvicorn fast_app:app --host "0.0.0.0" --port 8000

    python usage.py runserver --host "0.0.0.0" --port 8000

## Testing

    playwright install

    pytest

    pytest --headed


[reactpy]: https://github.com/reactive-python/reactpy
[reactpy-router]: https://github.com/reactive-python/reactpy-router
[tailwind-dashboard-windster]: https://demo.themesberg.com/windster/
 

