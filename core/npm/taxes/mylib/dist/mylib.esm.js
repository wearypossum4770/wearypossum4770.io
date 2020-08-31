import React from 'react'

// see: https://github.com/storybookjs/storybook/issues/9556

var Thing = function Thing(_ref) {
    var children = _ref.children
    return React.createElement(
        'div',
        null,
        children || 'the snozzberries taste like snozzberries'
    )
}

export {Thing}
//# sourceMappingURL=mylib.esm.js.map
