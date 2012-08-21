CKEDITOR.plugins.add('mypopup', {
    init: function(editor) {
        var command = editor.addCommand('mypopup', new CKEDITOR.dialogCommand('mypopup'));
        command.modes = {wysiwyg: 1, source: 0};
        command.canUndo = true;
        editor.ui.addButton('mypopup', {
            label : 'Создать попап',
            command : 'mypopup',
            icon: this.path + 'balloons.png'
        });
        CKEDITOR.dialog.add('mypopup', this.path + 'dialogs/mypopup.js');
        if (editor.addMenuItems) {
            editor.addMenuItem("mypopup", {
                label: 'Добавить тултип',
                command: 'mypopup',
                group: 'clipboard', 
                order: 9
            });
        }
        if (editor.contextMenu) {
            editor.contextMenu.addListener(function() {
                return {"mypopup": CKEDITOR.TRISTATE_OFF};
            });
        }
    }
});