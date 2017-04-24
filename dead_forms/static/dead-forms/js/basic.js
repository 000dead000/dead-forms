var dead_forms_basic = {
    /**
     * Change hint text
     */
    change_hint_text: function(element, text) {
        var hint = element.next().next();

        if (!hint.hasClass("dead-form-control-hint")) {
            hint.addClass("dead-form-control-hint");
        }

        hint.html(text);
    },

    /**
     * Chosen select
     */
    chosen_select: function () {
        var _this = this;

        $(".chosen-select").chosen({
            disable_search_threshold: 10,
            no_results_text: "No hay resultados para esta búsqueda",
            placeholder_text_multiple: "Selecciona algunos de los elementos"
        }).change(function () {
            if ($(this).hasClass("chosen-select-hint-text")) {
                var element = $(this);
                var value = element.val();
                var text = "";
                var hint = element.next().next();

                if (value != "")
                    text = element.find("option:selected").text();

                _this.change_hint_text(element, text);
            }
        });
    },

    /**
     * Bootstrap file style
     */
    bs_file: function () {
        $(".bs-file").filestyle({
            input: false,
            buttonText: "&nbsp;Seleccionar archivo",
            buttonName: "btn-primary",
            iconName: "glyphicon glyphicon-inbox"
        });
    },

    /**
     * Dual listbox
     */
    dual_listbox: function () {
        $(".dual-listbox").bootstrapDualListbox({
            filterTextClear: "Mostrar todos",
            filterPlaceHolder: "Filtrar",
            moveAllLabel: "Seleccionar todos",
            removeAllLabel: "Deseleccionar todos",
            infoText: "Mostrando todos {0}",
            infoTextFiltered: '<span class="label label-warning">Filtrado</span> {0} de {1}',
            infoTextEmpty: "Lista vacía"
        });
    },

    /**
     * Toggle checkbox
     */
    toggle_checkbox: function () {
        $(".toggle-checkbox").bootstrapToggle({
            on: "Si",
            off: "No",
            onstyle: "success",
            offstyle: "danger"
        });
    },

    /**
     * After AJAX
     */
    after_ajax: function () {
        this.chosen_select();
        this.bs_file();
        this.dual_listbox();
        this.toggle_checkbox();
    },

    /**
     * Init
     */
    init: function () {
        this.chosen_select();
        this.bs_file();
        this.dual_listbox();
        this.toggle_checkbox();
    }
};