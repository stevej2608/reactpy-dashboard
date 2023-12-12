from reactpy import component, html

# https://buttons.github.io/

@component
def GitHubButton(props, children):
    return html.div({'class_name': '-mb-1'},
        html.a({
            'class_name': 'github-button', 
            'href': 'https://github.com/themesberg/windster-tailwind-css-dashboard', 
            'data-color-scheme': 'no-preference: dark; light: light; dark: light;', 
            'data-icon': 'octicon-star', 
            'data-size': 'large', 
            'data-show-count': 'true', 
            'aria-label': 'Star themesberg/windster-tailwind-css-dashboard on GitHub'}, "Star"
        )
    )
