from reactpy import html

from utils.server_options.server_options import ServerOptions

from .default_options import DEFAULT_OPTIONS

INDEX_CSS = {
        'rel': 'stylesheet',
        'href': '/static/css/index.css',
        'crossorigin': 'anonymous'
    }

# https://tailwindcss.com/docs/installation/play-cdn

TAILWIND_CSS = """
    tailwind.config = {
        darkMode: 'class',
        theme: {
            extend: {
                fontFamily: {
                    'sans': ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'],
                    'body': ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'system-ui', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'Noto Sans', 'sans-serif', 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', 'Noto Color Emoji'],
                    'mono': ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'Liberation Mono', 'Courier New', 'monospace']
                },
                transitionProperty: {
                    'width': 'width'
                },
                minWidth: {
                    '20': '20rem'
                },
                colors: {
                    cyan: {
                        50: '#ECFEFF',
                        100: '#CFFAFE',
                        200: '#A5F3FC',
                        300: '#67E8F9',
                        400: '#22D3EE',
                        500: '#06B6D4',
                        600: '#0891B2',
                        700: '#0E7490',
                        800: '#155E75',
                        900: '#164E63'
                    },

                    bg_gray_100: '#f3f4f6',
                    bg_gray_800: '#1f2937',
                    bg_gray_900: '#111827',
                    bg_gray_950: '#030712',

                }
            },
        },
    }
"""

TAILWIND_OPTIONS = DEFAULT_OPTIONS + ServerOptions(
    head=[

        # Use this for production
        # html.link(TAILWIND_CSS_335),

        # Use this for development
        html.script({'src': 'https://cdn.tailwindcss.com'}),

        # https://buttons.github.io/
        # html.script({'async': 'defer', 'src': 'https://buttons.github.io/buttons.js'}),
        html.script({'async': 'defer', 'src': 'static/js/buttons.js'}),

        html.script(TAILWIND_CSS),
        html.link(INDEX_CSS),
    ],
    asset_folder='',
    asset_root='static'
)
