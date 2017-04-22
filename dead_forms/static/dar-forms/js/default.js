var dar_forms = {
    /**
     * After AJAX
     */
    after_ajax: function () {
        dar_forms_basic.after_ajax();
    },

    /**
     * Init
     */
    init: function () {
        dar_forms_basic.init();
    }
};

/**
 * After AJAX
 */
$(document).ajaxStop(function() {
    dar_forms.after_ajax();
});

/**
 * Document ready
 */
$(document).ready(function() {
    dar_forms.init();
});
