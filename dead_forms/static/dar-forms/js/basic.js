var dar_forms_basic = {
    /**
     * Chosen select
     */
    chosen_select: function () {
        $(".chosen-select").chosen({
            disable_search_threshold: 10,
            no_results_text: "No hay resultados para esta búsqueda"
        });
    },

    /**
     * Bootstrap file style
     */
    // bs_file: function () {
    //     $(".bs-file").filestyle({
    //         input: false,
    //         buttonText: "&nbsp;Seleccionar archivo",
    //         buttonName: "btn-primary",
    //         iconName: "glyphicon glyphicon-inbox"
    //     });
    // },

    /**
     * Dual listbox
     */
    // dual_listbox: function () {
    //     $(".dual-listbox").bootstrapDualListbox({
    //         filterTextClear: "Mostrar todos",
    //         filterPlaceHolder: "Filtrar",
    //         moveAllLabel: "Seleccionar todos",
    //         removeAllLabel: "Deseleccionar todos",
    //         infoText: "Mostrando todos {0}",
    //         infoTextFiltered: '<span class="label label-warning">Filtrado</span> {0} de {1}',
    //         infoTextEmpty: "Lista vacía"
    //     });
    // },

    /**
     * Toggle checkbox
     */
    // toggle_checkbox: function () {
    //     $(".toggle-checkbox").bootstrapToggle({
    //         on: "Si",
    //         off: "No",
    //         onstyle: "success",
    //         offstyle: "danger"
    //     });
    // },

    /**
     * Display maxlength
     */
    // display_maxlength: function () {
    //     $('.display-maxlength').maxlength({
    //         alwaysShow: true,
    //         placement: 'right'
    //     });
    // },

    /**
     * After AJAX
     */
    after_ajax: function () {
        this.chosen_select();
        // this.bs_file();
        // this.dual_listbox();
        // this.toggle_checkbox();
    },

    /**
     * Init
     */
    init: function () {
        this.chosen_select();
        // this.bs_file();
        // this.dual_listbox();
        // this.toggle_checkbox();
        // this.display_maxlength();
    }
};