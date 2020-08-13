const password_field = 'dnn_ctr2863_Login_Login_EuclidCVCustom_txtPassword'
const username_field = 'dnn_ctr2863_Login_Login_EuclidCVCustom_txtUsername'
const password = '3P2ZKmx'
const username = 'AAA51433'

console.save = function (data, filename) {
    if (!data) {
        console.error('Console.save: No data')
        return
    }

    if (!filename) filename = 'story.json'

    if (typeof data === 'object') {
        data = JSON.stringify(data, undefined, 4)
    }

    var blob = new Blob([data], {
            type: 'text/json',
        }),
        e = document.createEvent('MouseEvents'),
        a = document.createElement('a')

    a.download = filename
    a.href = window.URL.createObjectURL(blob)
    a.dataset.downloadurl = ['text/json', a.download, a.href].join(':')
    e.initMouseEvent(
        'click',
        true,
        false,
        window,
        0,
        0,
        0,
        0,
        0,
        false,
        false,
        false,
        false,
        0,
        null
    )
    a.dispatchEvent(e)
}
