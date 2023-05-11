
from ._base import BodyComponent


__all__ = ['MjAccordionElement']

from ..helpers import conditionalTag


class MjAccordionElement(BodyComponent):
    component_name = 'mj-accordion-element'

    @classmethod
    def allowed_attrs(cls):
        return {
            'background-color'  : 'color',
            'border'            : 'string',
            'font-family'       : 'string',
            'icon-align'        : 'enum(top,middle,bottom)',
            'icon-width'        : 'unit(px,%)',
            'icon-height'       : 'unit(px,%)',
            'icon-wrapped-url'  : 'string',
            'icon-wrapped-alt'  : 'string',
            'icon-unwrapped-url': 'string',
            'icon-unwrapped-alt': 'string',
            'icon-position'     : 'enum(left,right)',
        }

    @classmethod
    def default_attrs(cls):
        return {
            'title': {
                'img': {
                    'width' : '32px',
                    'height': '32px',
                },
            },
        }

    # js: getStyles()
    def get_styles(self):
        return {
            'td'   : {
                'padding'         : '0px',
                'background-color': self.getAttribute('background-color'),
            },
            'label': {
                'font-size'  : '13px',
                'font-family': self.getAttribute('font-family'),
            },
            'input': {
                'display': 'none',
            },
        }

    def handleMissingChildren(self):
        from . import MjAccordionText
        from . import MjAccordionTitle

        children = self.props['children']
        children_attrs = {
            'border'            : self.getAttribute('border'),
            'icon-align'        : self.getAttribute('icon-align'),
            'icon-width'        : self.getAttribute('icon-width'),
            'icon-height'       : self.getAttribute('icon-height'),
            'icon-position'     : self.getAttribute('icon-position'),
            'icon-wrapped-url'  : self.getAttribute('icon-wrapped-url'),
            'icon-wrapped-alt'  : self.getAttribute('icon-wrapped-alt'),
            'icon-unwrapped-url': self.getAttribute('icon-unwrapped-url'),
            'icon-unwrapped-alt': self.getAttribute('icon-unwrapped-alt'),
        }
        has_title = False
        has_text = False

        result = []

        for child in children:
            if child['tagName'] == 'mj-accordion-title':
                has_title = True
            if child['tagName'] == 'mj-accordion-text':
                has_text = True

            if has_title and has_text:
                break

        if not has_title:
            result.append(
                MjAccordionTitle(attributes=children_attrs, context=self.getChildContext()).render()
            )

        result.append(self.renderChildren(children, attributes=children_attrs))

        if not has_text:
            result.append(
                MjAccordionText(attributes=children_attrs, context=self.getChildContext()).render()
            )

        return '\n'.join(result)



    def render(self):
        label_attrs = self.html_attrs(
            class_='mj-accordion-element',
            style='label',
        )
        checkbox = f'''
            <input
                {self.html_attrs(
                    class_='mj-accordion-checkbox',
                    type='checkbox',
                    style='input',
                )}
            />
        '''
        return f'''
            <tr {self.html_attrs(class_=self.getAttribute('css-class', missing_ok=True))}>
                <td {self.html_attrs(style='td')}>
                    <label {label_attrs}>
                        {conditionalTag(checkbox, True)}
                        <div>
                            {self.handleMissingChildren()}
                        </div>
                    </label>
                </td>
            </tr>
        '''

