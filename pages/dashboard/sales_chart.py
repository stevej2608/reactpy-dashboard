from reactpy import component
from reactpy_apexcharts import ApexChart

SALES_CHART = {
    "chart": {
        "fontFamily": "Inter, sans-serif",
        "foreColor": "#6B7280",
        "toolbar": {"show": False},
    },
    "fill": {
        "type": "solid",
        "opacity": 0.3,
    },
    "dataLabels": {"enabled": False},
    "tooltip": {
        "style": {
            "fontSize": "14px",
            "fontFamily": "Inter, sans-serif",
        },
    },
    "grid": {
        "show": False,
    },
    "xaxis": {
        "categories": ["01 Feb", "02 Feb", "03 Feb", "04 Feb", "05 Feb", "06 Feb", "07 Feb"],
        "labels": {
            "style": {
                "colors": ["#6B7280"],
                "fontSize": "14px",
                "fontWeight": 500,
            },
        },
        "axisBorder": {
            "color": "#F3F4F6",
        },
        "axisTicks": {
            "color": "#F3F4F6",
        },
    },
    "yaxis": {
        "labels": {
            "style": {
                "colors": ["#6B7280"],
                "fontSize": "14px",
                "fontWeight": 500,
            },
            'formatter': "${value}"
        },
    },
    "responsive": [{"breakpoint": 1024, "options": {"xaxis": {"labels": {"show": False}}}}],
}

@component
def SalesChart():
    series = {"name": "Revenue", "data": [6356, 6218, 6156, 6526, 6356, 6256, 6056], "color": "#0694a2"}
    chart = ApexChart(options=SALES_CHART, series=[series], chart_type='area', height=420)
    return chart
