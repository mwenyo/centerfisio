// Using jquery.inputmask: https://github.com/RobinHerbots/jquery.inputmask
// For 8 digit phone fields, the mask is like this: (99) 9999-9999
// For 9 digit phone fields the mask is like this: (99) 99999-9999
function setupPhoneMaskOnField(selector) {
    var inputElement = $(selector)

    setCorrectPhoneMask(inputElement);
    inputElement.on('input, keyup', function () {
        setCorrectPhoneMask(inputElement);
    });
}

function setCorrectPhoneMask(element) {
    if (element.inputmask('unmaskedvalue').length > 10) {
        element.inputmask('remove');
        element.inputmask('(99) 9999[9]-9999')
    } else {
        element.inputmask('remove');
        element.inputmask({ mask: '(99) 9999-9999[9]', greedy: false })
    }
}