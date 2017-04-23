var dead_forms = {
    /**
     * After AJAX
     */
    after_ajax: function () {
        dead_forms_basic.after_ajax();
    },

    /**
     * Init
     */
    init: function () {
        dead_forms_basic.init();
    }
};

/**
 * After AJAX
 */
$(document).ajaxStop(function() {
    dead_forms.after_ajax();
});

/**
 * Document ready
 */
$(document).ready(function() {
    dead_forms.init();
});
