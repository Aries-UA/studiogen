CKEDITOR.dialog.add('mypopup', function(editor) {
    return {
        title : 'Создать подсказку',
        minWidth : 400,
        minHeight : 200,
        onOk: function() {
            var elem = editor.getSelection().getStartElement().$;
            if ($(elem).length > 0) {
                var unic_id = Math.floor(Math.random()*10000);
                var curr_id = $(elem).attr('data-id');
                if (curr_id == undefined) {
                    curr_id = 'p' + unic_id;
                }
                $(elem).attr('data-id', '#'+curr_id);
                var cls = $(elem).attr('class');
                if (cls == undefined) {
                    $(elem).attr('class', 'tp');
                }
                else {
                    if (cls != 'tp') {
                        $(elem).attr('class', cls+' tp');
                    }
                }
                var src = this.getContentElement( 'div_popup', 'img').getInputElement().getValue();
                var title = this.getContentElement( 'div_popup', 'txt').getInputElement().getValue();
                var html = '<div id="{3}" class="tooltip"><img src="{0}" /><span>{1}</span></div>';
                $(elem).after(html.replace('{0}', src).replace('{1}', title).replace('{3}', curr_id));
            }
        },
        contents: [{
            id: 'div_popup',
            label: 'First Tab',
            title: 'First Tab',
            elements: [{
                id: 'img',
                type: 'text',
                label: 'Ссылка на картинку'
            },
            {
                id: 'txt',
                type: 'text',
                label: 'Подпись'
            }]
        }]
    };
});