from reactpy import component, html


@component
def AppMain():
    return html.div(
    html.div({'class_name': 'container'},
        html.div({'class_name': 'row'},
            html.div({'class_name': 'col-md-12'},
                html.div({'class_name': 'error-template'},
                    html.h1("Oops!"),
                    html.h2("404 Not Found"),
                    html.div({'class_name': 'error-details'}, "Sorry, an error has occured, Requested page not found!"),
                    html.div({'class_name': 'error-actions'},
                        html.a({'href': 'http://www.jquery2dotnet.com', 'class_name': 'btn btn-primary btn-lg'},
                            html.span({'class_name': 'glyphicon glyphicon-home'}),
                            "Take Me Home"
                        ),
                        html.a({'href': 'http://www.jquery2dotnet.com', 'class_name': 'btn btn-default btn-lg'},
                            html.span({'class_name': 'glyphicon glyphicon-envelope'}),
                            "Contact Support"
                        )
                    )
                )
            )
        )
    )
)
