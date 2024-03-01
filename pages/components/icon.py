from typing import Callable
from reactpy import component
from reactpy.types import VdomDict
from reactpy.svg import svg, path

# pylint: disable=line-too-long

ICON = Callable[..., VdomDict]

@component
def Icon_Bars3CenterLeft():
    return svg({'id': 'toggleSidebarMobileHamburger', 'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M3 5a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1zM3 10a1 1 0 011-1h6a1 1 0 110 2H4a1 1 0 01-1-1zM3 15a1 1 0 011-1h12a1 1 0 110 2H4a1 1 0 01-1-1z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Search():
    return svg({'class_name': 'h-5 w-5 text-gray-500', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_XMark():
    return svg({'id': 'toggleSidebarMobileClose', 'class_name': 'hidden h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_RightFromLine():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M3 3a1 1 0 00-1 1v12a1 1 0 102 0V4a1 1 0 00-1-1zm10.293 9.293a1 1 0 001.414 1.414l3-3a1 1 0 000-1.414l-3-3a1 1 0 10-1.414 1.414L14.586 9H7a1 1 0 100 2h7.586l-1.293 1.293z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_User():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Bag():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M10 2a4 4 0 00-4 4v1H5a1 1 0 00-.994.89l-1 9A1 1 0 004 18h12a1 1 0 00.994-1.11l-1-9A1 1 0 0015 7h-1V6a4 4 0 00-4-4zm2 5V6a2 2 0 10-4 0v1h4zm-6 3a1 1 0 112 0 1 1 0 01-2 0zm7-1a1 1 0 100 2 1 1 0 000-2z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_SignUp():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M5 4a3 3 0 00-3 3v6a3 3 0 003 3h10a3 3 0 003-3V7a3 3 0 00-3-3H5zm-1 9v-1h5v2H5a1 1 0 01-1-1zm7 1h4a1 1 0 001-1v-1h-5v2zm0-4h5V8h-5v2zM9 8H4v2h5V8z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Dashboard():
    return svg({'class_name': 'h-6 w-6 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M2 10a8 8 0 018-8v8h8a8 8 0 11-16 0z'}),
        path({'d': 'M12 2.252A8.014 8.014 0 0117.748 8H12V2.252z'})
    )


@component
def Icon_Squares2x2Bold():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z'})
    )


@component
def Icon_Inbox():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M8.707 7.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l2-2a1 1 0 00-1.414-1.414L11 7.586V3a1 1 0 10-2 0v4.586l-.293-.293z'}),
        path({'d': 'M3 5a2 2 0 012-2h1a1 1 0 010 2H5v7h2l1 2h4l1-2h2V5h-1a1 1 0 110-2h1a2 2 0 012 2v10a2 2 0 01-2 2H5a2 2 0 01-2-2V5z'})
    )


@component
def Icon_Upgrade():
    return svg({'class_name': 'h-5 w-5 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'aria-hidden': 'true', 'focusable': 'false', 'data-prefix': 'fas', 'data-icon': 'gem', 'role': 'img', 'xmlns': 'http://www.w3.org/2000/svg', 'viewBox': '0 0 512 512'},
        path({'fill': 'currentColor', 'd': 'M378.7 32H133.3L256 182.7L378.7 32zM512 192l-107.4-141.3L289.6 192H512zM107.4 50.67L0 192h222.4L107.4 50.67zM244.3 474.9C247.3 478.2 251.6 480 256 480s8.653-1.828 11.67-5.062L510.6 224H1.365L244.3 474.9z'})
    )

@component
def Icon_Documentation():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M9 2a1 1 0 000 2h2a1 1 0 100-2H9z'}),
        path({'fill-rule': 'evenodd', 'd': 'M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 000 2h.01a1 1 0 100-2H7zm3 0a1 1 0 000 2h3a1 1 0 100-2h-3zm-3 4a1 1 0 100 2h.01a1 1 0 100-2H7zm3 0a1 1 0 100 2h3a1 1 0 100-2h-3z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Components():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M7 3a1 1 0 000 2h6a1 1 0 100-2H7zM4 7a1 1 0 011-1h10a1 1 0 110 2H5a1 1 0 01-1-1zM2 11a2 2 0 012-2h12a2 2 0 012 2v4a2 2 0 01-2 2H4a2 2 0 01-2-2v-4z'})
    )


@component
def Icon_Help():
    return svg({'class_name': 'h-6 w-6 flex-shrink-0 text-gray-500 transition duration-75 group-hover:text-gray-900', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-2 0c0 .993-.241 1.929-.668 2.754l-1.524-1.525a3.997 3.997 0 00.078-2.183l1.562-1.562C15.802 8.249 16 9.1 16 10zm-5.165 3.913l1.58 1.58A5.98 5.98 0 0110 16a5.976 5.976 0 01-2.516-.552l1.562-1.562a4.006 4.006 0 001.789.027zm-4.677-2.796a4.002 4.002 0 01-.041-2.08l-.08.08-1.53-1.533A5.98 5.98 0 004 10c0 .954.223 1.856.619 2.657l1.54-1.54zm1.088-6.45A5.974 5.974 0 0110 4c.954 0 1.856.223 2.657.619l-1.54 1.54a4.002 4.002 0 00-2.346.033L7.246 4.668zM12 10a2 2 0 11-4 0 2 2 0 014 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_UpArrow():
    return svg({'class_name': 'h-5 w-5', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M5.293 7.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 5.414V17a1 1 0 11-2 0V5.414L6.707 7.707a1 1 0 01-1.414 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_DownArrow():
    return svg({'class_name': 'h-5 w-5', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M14.707 12.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 14.586V3a1 1 0 012 0v11.586l2.293-2.293a1 1 0 011.414 0z', 'clip-rule': 'evenodd'})
    )

@component
def Icon_BackArrow():
    return svg({'class_name': '-ml-1 mr-2 h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'clip-rule': 'evenodd', 'd': 'M7.707 14.707a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l2.293 2.293a1 1 0 010 1.414z', 'fill-rule': 'evenodd'})
    )

@component
def Icon_Gear():
    return svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M11.49 3.17c-.38-1.56-2.6-1.56-2.98 0a1.532 1.532 0 01-2.286.948c-1.372-.836-2.942.734-2.106 2.106.54.886.061 2.042-.947 2.287-1.561.379-1.561 2.6 0 2.978a1.532 1.532 0 01.947 2.287c-.836 1.372.734 2.942 2.106 2.106a1.532 1.532 0 012.287.947c.379 1.561 2.6 1.561 2.978 0a1.533 1.533 0 012.287-.947c1.372.836 2.942-.734 2.106-2.106a1.533 1.533 0 01.947-2.287c1.561-.379 1.561-2.6 0-2.978a1.532 1.532 0 01-.947-2.287c.836-1.372-.734-2.942-2.106-2.106a1.532 1.532 0 01-2.287-.947zM10 13a3 3 0 100-6 3 3 0 000 6z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Bin(size:str = 'h-6 w-6'):
    return svg({'class_name': size, 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Info():
    return svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Dots():
    return svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z'})
    )


@component
def Icon_Plus():
    return svg({'class_name': '-ml-1 mr-2 h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M10 5a1 1 0 011 1v3h3a1 1 0 110 2h-3v3a1 1 0 11-2 0v-3H6a1 1 0 110-2h3V6a1 1 0 011-1z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Download():
    return svg({'class_name': '-ml-1 mr-2 h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M6 2a2 2 0 00-2 2v12a2 2 0 002 2h8a2 2 0 002-2V7.414A2 2 0 0015.414 6L12 2.586A2 2 0 0010.586 2H6zm5 6a1 1 0 10-2 0v3.586l-1.293-1.293a1 1 0 10-1.414 1.414l3 3a1 1 0 001.414 0l3-3a1 1 0 00-1.414-1.414L11 11.586V8z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Edit():
    return svg({'class_name': 'mr-2 h-5 w-5', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M17.414 2.586a2 2 0 00-2.828 0L7 10.172V13h2.828l7.586-7.586a2 2 0 000-2.828z'}),
        path({'fill-rule': 'evenodd', 'd': 'M2 6a2 2 0 012-2h4a1 1 0 010 2H4v10h10v-4a1 1 0 112 0v4a2 2 0 01-2 2H4a2 2 0 01-2-2V6z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_LeftBracket():
    return svg({'class_name': 'h-7 w-7', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_RightBracket():
    return svg({'class_name': 'h-7 w-7', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_LeftBracketSmall():
    return svg({'class_name': '-ml-1 mr-1 h-5 w-5', 'fill': ' currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_RightBracketSmall():
    return svg({'class_name': '-mr-1 ml-1 h-5 w-5', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'fill-rule': 'evenodd', 'd': 'M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Eye():
    return svg({'xmlns': 'http://www.w3.org/2000/svg', 'fill': 'none', 'viewBox': '0 0 24 24', 'strokewidth': '{1.5}', 'stroke': 'currentColor', 'class_name': 'h-6 w-6'},
        path({'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'd': 'M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z'}),
        path({'stroke-linecap': 'round', 'stroke-linejoin': 'round', 'd': 'M15 12a3 3 0 11-6 0 3 3 0 016 0z'})
    )


@component
def Icon_EyeSlash():
    return svg({'xmlns': 'http://www.w3.org/2000/svg', 'fill': 'none', 'viewBox': '0 0 24 24', 'strokewidth': '{1.5}', 'stroke': 'currentColor', 'class_name': 'h-6 w-6'},
        path({'strokelinecap': 'round', 'strokelinejoin': 'round', 'd': 'M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88'})
    )


@component
def Icon_Moon():
    return svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z'})
    )


@component
def Icon_Sun():
    return svg({'class_name': 'h-6 w-6', 'fill': 'currentColor', 'viewBox': '0 0 20 20', 'xmlns': 'http://www.w3.org/2000/svg'},
        path({'d': 'M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z', 'fill-rule': 'evenodd', 'clip-rule': 'evenodd'})
    )


@component
def Icon_Gem():
    return svg({'class_name': 'svg-inline--fa fa-gem -ml-1 mr-2 h-4 w-4', 'aria-hidden': 'true', 'focusable': 'false', 'data-prefix': 'fas', 'data-icon': 'gem', 'role': 'img', 'xmlns': 'http://www.w3.org/2000/svg', 'viewBox': '0 0 512 512'},
        path({'fill': 'currentColor', 'd': 'M378.7 32H133.3L256 182.7L378.7 32zM512 192l-107.4-141.3L289.6 192H512zM107.4 50.67L0 192h222.4L107.4 50.67zM244.3 474.9C247.3 478.2 251.6 480 256 480s8.653-1.828 11.67-5.062L510.6 224H1.365L244.3 474.9z'})
    )
