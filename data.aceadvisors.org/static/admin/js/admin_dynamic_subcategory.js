(function ($) {
    $(document).ready(function () {
        var categoryField = $('#id_Category');
        var subcategoryField = $('#id_SubCategory');

        function updateSubcategories() {
            var categoryId = categoryField.val();
            $.ajax({
                url: "/get_subcategories/",
                data: {
                    'category_id': categoryId
                },
                dataType: 'json',
                success: function (data) {
                    subcategoryField.empty();
                    $.each(data, function (index, subcategory) {
                        subcategoryField.append(
                            $("<option></option>")
                                .attr("value", subcategory.id)
                                .text(subcategory.name)
                        );
                    });
                }
            });
        }

        categoryField.change(function () {
            updateSubcategories();
        });

        // Trigger initial update on page load
        updateSubcategories();
    });
})(django.jQuery);
